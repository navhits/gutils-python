"""
Service account configuration for Google APIs.
"""
import typing

# pylint: disable=import-error
from gutils.creds import Secret

class ServiceAccountCreds:
    def __init__(self, project_id: str = None, private_key_id: str = None, 
                private_key: str = None, client_email: str = None, 
                client_id: str = None, client_x509_cert_url: str = None) -> None:

        self.project_id = project_id if project_id else Secret(
            environment_variable="GCP_PROJECT_ID", required=True)
        
        self.private_key_id = private_key_id if private_key_id else Secret(
            environment_variable="GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID", required=True)
        
        self.private_key = private_key if private_key else Secret(
            environment_variable="GCP_SERVICE_ACCOUNT_PRIVATE_KEY", required=True)
        
        self.client_email = client_email if client_email else Secret(
            environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_EMAIL", required=True)
        
        self.client_id = client_id if client_id else Secret(
            environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_ID", required=True)   

        self.type = "service_account"
        self.auth_uri = "https://accounts.google.com/o/oauth2/auth"
        self.token_uri = "https://oauth2.googleapis.com/token"
        self.auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
        self.redirect_uris = ["http://localhost"]

        self.client_x509_cert_url = client_x509_cert_url if client_x509_cert_url else Secret(
            environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL", required=True)

    def _is_mandatory_keys_set(self) -> bool:
        return True if self.project_id and self.private_key_id and self.private_key and \
            self.client_email and self.client_id and self.client_x509_cert_url else False

    def _build_secret(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def get_secret(self) -> typing.Union[dict, None]:
        return self._build_secret() if self._is_mandatory_keys_set() else None