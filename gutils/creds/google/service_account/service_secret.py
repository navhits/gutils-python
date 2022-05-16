"""
Service account configuration for Google APIs.
"""
# pylint: disable=import-error
from gutils.creds import (GCP_PROJECT_ID, GCP_SERVICE_ACCOUNT_CLIENT_ID,
                      GCP_SERVICE_ACCOUNT_CLIENT_EMAIL, GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID,
                      GCP_SERVICE_ACCOUNT_PRIVATE_KEY, GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL)

secret ={
  "type": "service_account",
  "project_id": GCP_PROJECT_ID,
  "private_key_id": GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID,
  "private_key": GCP_SERVICE_ACCOUNT_PRIVATE_KEY,
  "client_email": GCP_SERVICE_ACCOUNT_CLIENT_EMAIL,
  "client_id": GCP_SERVICE_ACCOUNT_CLIENT_ID,
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL
}
