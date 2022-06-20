# G-Utils Python [![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

G-Utils abstracts and presents reusable components of workspace resource based APIs. Currently supports Sheets, and Drive API methods.

## Installation

```bash
# Actiate virtual environment
python3 -m venv venv
. venv/bin/activate

# Install the package
pip3 install git+ssh://git@github.com/navhits/gutils-python.git
```

## Development

```bash
# Install poetry
curl -sSL https://install.python-poetry.org | python -

# Clone the repo
git clone https://github.com/navhits/gutils-python.git && cd gutils-python

# Actiate virtual environment
python3 -m venv venv
. venv/bin/activate

# Install dependencies from lock file
poetry install
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
from gutils.creds.google.oauth.credentials import get_secret

# Google Sheets
scopes = ['https://www.googleapis.com/auth/spreadsheets']

sheets = Sheets(scopes = scopes, client_config = get_secret(), login_type="OAUTH2")
sheets.initialize()

# Google Drive
scopes = ['https://www.googleapis.com/auth/drive']

drive = Drive(scopes = scopes, client_config = get_secret(), login_type="OAUTH2")
drive.initialize()
```

### Using Oauth Authorization token directly

If you set these additional environment variables if you have them, to skip the oauth flow

```bash
export GCP_OAUTH_AUTH_TOKEN=dummy-token
export GCP_OAUTH_REFRESH_TOKEN=dummy-refresh-token
```

### Revoking an Oauth permission

```python
sheets.revoke_oauth_permission()

drive.revoke_oauth_permission()
```

Note: revoke_oauth_permission() will not have effect if environment variables `GCP_OAUTH_AUTH_TOKEN` and `GCP_OAUTH_REFRESH_TOKEN` are set.

### Service Account Login

```python
from gutils.services.sheets import Sheets
from gutils.services.drive import Drive
from gutils.creds.google.service_account.credentials import get_secret

# Google Sheets
scopes = ['https://www.googleapis.com/auth/spreadsheets']

sheets = Sheets(scopes = scopes, client_config = get_secret(), login_type="SERVICE_ACCOUNT")
sheets.initialize()

# Google Drive
scopes = ['https://www.googleapis.com/auth/drive']

drive = Drive(scopes = scopes, client_config = get_secret(), login_type="SERVICE_ACCOUNT")
drive.initialize()
```
