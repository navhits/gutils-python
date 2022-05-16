import os
from typing import Optional

# pylint: disable=line-too-long
# pylint: disable=invalid-name
def Secret(environment_variable: str,
        required: bool, default_value: Optional[str] = None) -> None:
    """
    This class checks and imports the environment variables and raises exception if they are not set.
    """
    value = os.getenv(environment_variable)
    if not value and default_value:
        value = default_value
    if required and not value:
        raise Exception(f"'{environment_variable}' environment variable is not set. Please set it before execution.")
    return value


OAUTH_CREDS_DIR = "gutils/creds/google/oauth"
GOOGLE_OAUTH_CLIENT_ID = Secret(environment_variable="GOOGLE_OAUTH_CLIENT_ID", required=False)
GOOGLE_OAUTH_CLIENT_SECRET = Secret(environment_variable="GOOGLE_OAUTH_CLIENT_SECRET", required=False)
GOOGLE_OAUTH_ACCESS_TOKEN = Secret(environment_variable="GOOGLE_OAUTH_ACCESS_TOKEN", required=False)
GCP_PROJECT_ID = Secret(environment_variable="GCP_PROJECT_ID", required=False)
GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID = Secret(environment_variable="GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID", required=False)
GCP_SERVICE_ACCOUNT_PRIVATE_KEY = Secret(environment_variable="GCP_SERVICE_ACCOUNT_PRIVATE_KEY", required=False)
GCP_SERVICE_ACCOUNT_CLIENT_EMAIL = Secret(environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_EMAIL", required=False)
GCP_SERVICE_ACCOUNT_CLIENT_ID = Secret(environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_ID", required=False)
GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL = Secret(environment_variable="GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL", required=False)
