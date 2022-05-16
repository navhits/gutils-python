# pylint: disable=import-error
from gutils.creds import GCP_OAUTH_CLIENT_ID, GCP_OAUTH_CLIENT_SECRET, GCP_PROJECT_ID

# Template for client config that can be used to initiate a new Oauth2 flow.

secret = {
    "installed": {
        "client_id": GCP_OAUTH_CLIENT_ID,
        "project_id": GCP_PROJECT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": GCP_OAUTH_CLIENT_SECRET,
        "redirect_uris": [
            "http://localhost"
        ]
    }
}
