# G-Utils Python

G-Utils abstracts and presents reusable components of workspace resource based APIs. Currently supports Sheets, and Drive API methods.

`Note: This pacakge is WIP and currently cannot be installed via pip. The repo must be cloned and used as is with the provided instructions.`

## Geting started

### Clone the repo and install dependencies

```bash
git clone https://github.com/navhits/gutils-python.git && cd gutils-python
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

### Evironment variables

Set the following environment variables with respective values.

```bash
# If using Oauth2 login
export GCP_OAUTH_CLIENT_ID=dummy-client.apps.googleusercontent.com
export GCP_OAUTH_CLIENT_SECRET=dummy-secret
export GCP_PROJECT_ID=dummy-project

# If using service account
export GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID=dummy-key-id
export GCP_SERVICE_ACCOUNT_PRIVATE_KEY=dummy-key
export GCP_SERVICE_ACCOUNT_CLIENT_EMAIL=dummy-email
export GCP_SERVICE_ACCOUNT_CLIENT_ID=dummy-client-id
export GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL=dummy-cert-url
```

## Auth

### Oauth2 login

```python
from gutils.services.sheets import Sheets
from gutils.services.drive import Drive
from gutils.creds.google.oauth.client_secret import secret

scopes = ['https://www.googleapis.com/auth/spreadsheets']

sheets = Sheets(scopes = scopes, client_config = secret, login_type="OAUTH2")
sheets.initialize()

drive = Drive(scopes = scopes, client_config = secret, login_type="OAUTH2")
drive.initialize()
```

### Revoking an Oauth permission

```python
sheets.revoke_oauth_permission()
drive.revoke_oauth_permission()
```

### Service Account Login

```python
from gutils.services.sheets import Sheets
from gutils.services.drive import Drive
from gutils.creds.google.service_account.service_secret import secret

scopes = ['https://www.googleapis.com/auth/spreadsheets']

sheets = Sheets(scopes = scopes, client_config = secret, login_type="SERVICE_ACCOUNT")
sheets.initialize()

sheets = Sheets(scopes = scopes, client_config = secret, login_type="SERVICE_ACCOUNT")
sheets.initialize()
```
