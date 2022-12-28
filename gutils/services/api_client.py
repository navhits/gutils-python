"""
This module contains the necessay methods for services that require auth to access them.
"""
import json
import typing
from importlib import import_module
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as OauthCredentials
from google.oauth2.service_account import Credentials as ServiceCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery
from httplib2 import Credentials

from gutils.creds.google.oauth import Oauth2Creds, Oauth2Token
from gutils.creds.google.service_account import ServiceAccountCreds
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from gutils.services.enums import *


class GoogleApiClient:
    """
    Abstracted Google API client that implements Oauth2 and Service Account authentication
    """
    oauth_revoked: bool = False
    
    def __init__(self, scopes: list = None, config: typing.Union[Oauth2Creds, ServiceAccountCreds] = None,
                 token: Oauth2Token = None, login_type: LoginType = LoginType.OAUTH2) -> None:

        self.token = None
        self.config = None
        self.scopes = scopes
        self.credentials = None
        if login_type in list(LoginType.__members__):
            self.login_type = login_type
        else:
            raise ValueError(f"{login_type} is not a valid Login type")
        
        if token:
            self.token = token.get_token()
            login_type = LoginType.OAUTH2        
        if config:
            self.config = config.get_secret()

    def _get_client_config(self) -> typing.Union[dict, None]:
        """
        Checks and returns client config if available.
        """
        return self.config if self.config else Oauth2Creds().get_secret()

    def set_client_config(self, client_id: str, client_secret: str, project_id: str) -> None:
        """
        Sets a given client configuration
        """
        creds = Oauth2Creds(client_id, client_secret, project_id)
        self.config = creds.get_secret()
        
    def _get_authz_token(self) -> typing.Union[dict, None]:
        """
        Checks and returns authorization token if available.
        """
        return self.token if self.token else Oauth2Token().get_token()

    def set_authz_token(self, client_id: str, client_secret: str,
                        refresh_token: str, token: str = None, **kwargs) -> None:
        """
        Sets the authorization token.
        """
        token = Oauth2Token(client_id, client_secret, token, refresh_token)
        self.token = token.set_token()

    def oauth2_login(self, trigger_new_flow: bool=False) -> Credentials:
        """
        Authenticates the user using Oauth2 and saves the credentials to a pickle file.
        """
        credentials = None
        token = None

        if trigger_new_flow:
            self.revoke_oauth_permissions()
            self.oauth_revoked = True
        if not self.oauth_revoked:
            token = self._get_authz_token()
        if token:
            credentials = OauthCredentials.from_authorized_user_info(token, self.scopes)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                if not self.config:
                    raise ValueError("""Missing client config for Oauth2 login. Please check if the following is set.
                                     > `client_id`, `client_secret`, `refresh_token`""")
                flow = InstalledAppFlow.from_client_config(self.config, scopes = self.scopes)
                credentials = flow.run_local_server(port=0)

            creds = json.loads(credentials.to_json())

            self.set_authz_token(**creds)

        self.credentials = credentials
        self.oauth_revoked = False
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
            
    def create_service(self, service_name: str, version: str) -> typing.Union[object, None]:
        """
        Creates and returns a Google API service Resource object that has necessary methods
        to interact with the services.
        """
        service = discovery.build(service_name, version, credentials=self.credentials,
                                       cache_discovery=False)
        if service:
            with open(Path(__file__).parent.absolute().joinpath("services.json"), mode="r") as json_doc:
                services = json.load(json_doc)
            for name, attributes in services.get("service").items():
                if name == service_name.lower() and attributes.get("version") == version:
                    path = f"{services.get('entrypoint')}.{attributes.get('module')}.{attributes.get('version')}.{attributes.get('module')}"
                    module = import_module(path)
                    client = getattr(module, f"{attributes.get('class')}")
                    return client(service=service)
        return None            

    def return_service(self, service_name: str, version: str) -> typing.Union[object, None]:
        service = discovery.build(service_name, version, credentials=self.credentials,
                                       cache_discovery=False)
        return service if service else None
    
    def add_scopes(self, scopes: list) -> None:
        """
        Adds a new scope to the list of scopes.
        When a scope is added a new login flow is initiated.
        """
        if not isinstance(scopes, list):
            raise TypeError(f"Scopes must be provided as list. {type(scopes)} was provided.")
        if scopes:
            for scope in scopes:
                if scope not in self.scopes:
                    self.scopes.append(scope)
            if self.login_type == LoginType.OAUTH2:
                self.oauth2_login(trigger_new_flow=True)
            elif self.login_type == LoginType.SERVICE_ACCOUNT:
                self.service_account_auth()

    def remove_scopes(self, scopes: list, reauth: bool = True) -> None:
        """
        Removes the given scopes from the set scopes.
        When a scope is removed a new login flow is initiated.
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

    def revoke_oauth_permissions(self) -> None: # pylint: disable=no-self-use
        """
        Revokes the Oauth permission by removing the access token file.
        """
        Oauth2Token.remove_tokens()
        self.oauth_revoked = True

    def initialize(self):
        """
        Initializes the Google API client.
        """
        if self.login_type == LoginType.OAUTH2:
            self.oauth2_login()
        elif self.login_type == LoginType.SERVICE_ACCOUNT:
            self.service_account_auth()
