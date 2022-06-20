"""
This module contains the necessay methods for services that require auth to access them.
"""
import os
import pickle
import json

from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as OauthCredentials
from google.oauth2.service_account import Credentials as ServiceCredentials
from httplib2 import Credentials

from gutils.creds import OAUTH_CREDS_DIR
from gutils.creds.google import oauth
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from gutils.services.enums import *


class GoogleApiClient:
    """
    Abstracted Google API client that implements Oauth2 and Service Account authentication
    """
    def __init__(self, scopes: list, login_type: LoginType,
                 client_config: dict = None, token_file: str='token.json.pickle') -> None:
        # Client config must be provided if authentication is being done for the first time
        # Login type is provided so that inherited classes and other helper methods can \
            # initialize the client accordingly
        self.config = client_config
        self.scopes = scopes
        self.credentials, self.service = None, None
        self.token_file = token_file
        if login_type in list(LoginType.__members__):
            self.login_type = login_type
        else:
            raise ValueError(f"{login_type} is not a valid Login type")

    def _get_authz_token(self) -> bool:
        """
        Checks if the authorization token is available.
        """
        token = oauth.credentials.get_token()
        if token.get("token") and token.get("refresh_token"):
            return token
        oauth_dir = OAUTH_CREDS_DIR
        if os.path.exists(f"{oauth_dir}/{self.token_file}"):
            try:
                with open(f"{oauth_dir}/{self.token_file}", "rb") as pickled_file:
                    token = json.loads(pickle.load(pickled_file))
                return token
            except (Exception, EOFError):
                os.remove(f"{oauth_dir}/{self.token_file}")
                return None
        return None

    def _set_authz_token(self, token: dict) -> None:
        """
        Sets the authorization token.
        """
        oauth_dir = OAUTH_CREDS_DIR
        with open(f"{oauth_dir}/{self.token_file}", "wb") as pickled_file:
            pickled_file.write(pickle.dumps(token))

    def oauth2_login(self, trigger_new_flow: bool=False) -> Credentials:
        """
        Authenticates the user using Oauth2 and saves the credentials to a pickle file.
        """
        credentials = None
        
        if trigger_new_flow:
            self.revoke_oauth_permission()

        token = self._get_authz_token()
        if token:
            credentials = OauthCredentials.from_authorized_user_info(token, self.scopes)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                if not self.config:
                    raise ValueError("Missing client config for Oauth2 login")
                flow = InstalledAppFlow.from_client_config(self.config, scopes = self.scopes)
                credentials = flow.run_local_server(port=0)

            self._set_authz_token(credentials.to_json())

        self.credentials = credentials
        return credentials

    def service_account_auth(self) -> Credentials:
        """
        Authenticates the user using Service Account and returns the credentials.
        """
        credentials = None
        if not self.config:
            raise ValueError("Missing client config for service account")
        try:
            credentials = ServiceCredentials.from_service_account_info(self.config,
                                                                       scopes = self.scopes)
        except OSError as exception:
            raise OSError from exception

        self.credentials = credentials
        return credentials

    def set_service(self, service_name: str, version: str) -> None:
        """
        Creates a Google API service Resource object that has necessary methods
        to interact with the services.
        """
        self.service = discovery.build(service_name, version, credentials=self.credentials,
                                       cache_discovery=False)

    def add_scopes(self, scopes: list, reauth: bool = True) -> None:
        """
        Adds a new scope to the list of scopes.
        """
        if not isinstance(scopes, list):
            raise TypeError(f"Scopes must be provided as list. {type(scopes)} was provided.")
        if scopes:
            for scope in scopes:
                if scope not in self.scopes:
                    self.scopes.append(scope)
            if not reauth:
                return
            if self.login_type == LoginType.OAUTH2:
                self.oauth2_login(trigger_new_flow=True)
            elif self.login_type == LoginType.SERVICE_ACCOUNT:
                self.service_account_auth()

    def remove_scopes(self, scopes: list, reauth: bool = True) -> None:
        """
        Removes the given scopes from the set scopes.
        """
        if not isinstance(scopes, list):
            raise TypeError(f"Scopes must be provided as list. {type(scopes)} was provided.")
        if scopes:
            for scope in scopes:
                if scope in self.scopes:
                    self.scopes.remove(scope)
            if not reauth:
                return
            if self.login_type == LoginType.OAUTH2:
                self.oauth2_login(trigger_new_flow=True)
            elif self.login_type == LoginType.SERVICE_ACCOUNT:
                self.service_account_auth()

    def revoke_oauth_permission(self) -> None: # pylint: disable=no-self-use
        """
        Revokes the Oauth permission by removing the access token file.
        """
        oauth_dir = OAUTH_CREDS_DIR
        for content in os.scandir(oauth_dir):
            if content.is_file() and content.name.endswith(".pickle"):
                os.remove(f"{oauth_dir}/{content.name}")

    def initialize(self):
        """
        Initializes the Google API client.
        """
        if self.login_type == LoginType.OAUTH2:
            self.oauth2_login()
        elif self.login_type == LoginType.SERVICE_ACCOUNT:
            self.service_account_auth()
        self.set_service(self.resource_name, self.version) # pylint: disable=no-member
