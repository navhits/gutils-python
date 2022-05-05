import os
from typing import Optional

class Secret:
    """
    This class checks and imports the environment variables and raises exception if they are not set.
    """
    def __init__(self, environment_variable: str, required: bool, default_value: Optional[str] = None) -> None:
        self.environment_variable = environment_variable
        self.required = required
        self.value = os.getenv(environment_variable)
        if not self.value and default_value:
            self.value = default_value
        if self.required and not self.value:
            raise Exception(f"'{environment_variable}' environment variable is not set. Please set it before execution.")


OAUTH_CREDS_DIR = "gutils/creds/google/oauth"
GOOGLE_OAUTH_CLIENT_ID = Secret(environment_variable="GOOGLE_OAUTH_CLIENT_ID", required=False).value
GOOGLE_OAUTH_CLIENT_SECRET = Secret(environment_variable="GOOGLE_OAUTH_CLIENT_SECRET", required=False).value
GOOGLE_OAUTH_ACCESS_TOKEN = Secret(environment_variable="GOOGLE_OAUTH_ACCESS_TOKEN", required=False).value
GCP_PROJECT_ID = Secret(environment_variable="GCP_PROJECT_ID", required=False).value
GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID = Secret(environment_variable="GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID", required=False).value
GCP_SERVICE_ACCOUNT_PRIVATE_KEY = Secret(environment_variable="GCP_SERVICE_ACCOUNT_PRIVATE_KEY", required=False).value
GCP_SERVICE_ACCOUNT_CLIENT_EMAIL = Secret(environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_EMAIL", required=False).value
GCP_SERVICE_ACCOUNT_CLIENT_ID = Secret(environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_ID", required=False).value
GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL = Secret(environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL", required=False).value
