"""
Oauth configuration file for Google APIs.
"""
import json
import os
import pickle
import tempfile
import typing

# pylint: disable=import-error
from gutils.creds import Secret


class Oauth2Creds:
    def __init__(self, client_id: str = None, client_secret: str = None, project_id: str = None) -> None:
        self.client_id = client_id if client_id else Secret(
                environment_variable="GCP_OAUTH_CLIENT_ID", required=True)
        self.client_secret = client_secret if client_secret else Secret(
                environment_variable="GCP_OAUTH_CLIENT_SECRET", required=True)
        self.project_id = project_id if project_id else Secret(
                environment_variable="GCP_PROJECT_ID", required=True)
        self.auth_uri = "https://accounts.google.com/o/oauth2/auth"
        self.token_uri = "https://oauth2.googleapis.com/token"
        self.auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
        self.redirect_uris = ["http://localhost"]

    def _is_mandatory_keys_set(self) -> bool:
        return True if self.client_id and self.client_secret and self.project_id else False

    def _build_secret(self) -> dict:
        installed = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return {"installed": installed}

    def get_secret(self) -> typing.Union[dict, None]:
        return self._build_secret() if self._is_mandatory_keys_set() else None


class Oauth2Token:
    _temp_dir = os.path.join(tempfile.gettempdir())
    _oauth_cred_dir = os.path.join(_temp_dir, "gutils/creds/google/oauth")
    def __init__(self, client_id: str = None, client_secret: str = None,
                 token: str = None, refresh_token: str = None, token_file: str = "token.json.pickle") -> None:
        self.client_id = client_id if client_id else Secret(environment_variable="GCP_OAUTH_CLIENT_ID", required=False)
        self.client_secret = client_secret if client_secret else Secret(environment_variable="GCP_OAUTH_CLIENT_SECRET", required=False)
        self.token = token if token else Secret(environment_variable="GCP_OAUTH_AUTH_TOKEN", required=False)
        self.refresh_token = refresh_token if refresh_token else Secret(environment_variable="GCP_OAUTH_REFRESH_TOKEN", required=False)
        self._token_file = token_file

    def _build_token(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def _is_mandatory_keys_set(self) -> bool:
        return True if self.client_id and self.client_secret and self.refresh_token else False
            
    def get_token(self) -> typing.Union[dict, None]:
        if os.path.exists(f"{self._oauth_cred_dir}/{self._token_file}"):
            try:
                with open(f"{self._oauth_cred_dir}/{self._token_file}", "rb") as pickled_file:
                    token = json.loads(pickle.load(pickled_file))
                if token.get("client_id") == self.client_id:
                    return token
            except (Exception, EOFError):
                os.remove(f"{self._oauth_cred_dir}/{self._token_file}")
                pass
        self.set_token() if self._is_mandatory_keys_set() else None
        return self._build_token() if self._is_mandatory_keys_set() else None

    def set_token(self) -> typing.Union[dict, None]:
        if self._is_mandatory_keys_set():
            if os.path.exists(f"{self._oauth_cred_dir}/{self._token_file}"):
                try:
                    with open(f"{self._oauth_cred_dir}/{self._token_file}", "wb") as pickled_file:
                        pickled_file.write(pickle.dumps(self._build_token()))
                    return self._build_token()
                except (Exception, EOFError):
                    os.remove(f"{self._oauth_cred_dir}/{self._token_file}")
                    pass
        return None

    @classmethod
    def remove_tokens(cls) -> None:
        """
        Removes all tokens stored
        """
        [os.remove(f"{cls._oauth_cred_dir}/{content.name}")
         for content in os.scandir(cls._oauth_cred_dir)
         if content.is_file() and content.name.endswith(".pickle")]
