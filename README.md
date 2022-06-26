# G-Utils Python [![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

G-Utils abstracts and presents reusable components of workspace resource based APIs. Currently supports Sheets, and Drive API methods.

## Installation

```bash
# Actiate virtual environment
python3 -m venv venv
. venv/bin/activate

# Install the package
# Note: Use till commit hash `ff58e1d4da3c203790779f53f9ec884e7388298d` as its stable to use for now.

pip3 install git+https://github.com/navhits/gutils-python.git@ff58e1d4da3c203790779f53f9ec884e7388298d
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
from gutils.services.api_client import GoogleApiClient
from gutils.services.enums import LoginType
from gutils.creds.google.oauth import Oauth2Creds

# Sample scopes
scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

config = Oauth2Creds(
    client_id = "dummy-client-id"
    client_secret = "dummy-client-secret"
    project_id = "dummy-project-id"
)

# If environment variables are set,
config = Oauth2Creds()

client = GoogleApiClient(scopes=scopes, config=config, login_type=LoginType.OAUTH2)
client.initialize()

# Example to create a Google Sheets Client instance
service = client.create_service("sheets", "v4")
```

### Using Oauth Authorization token directly

If you set these additional environment variables if you have them, to skip the oauth flow

```bash
export GCP_OAUTH_AUTH_TOKEN=dummy-token # Optional
export GCP_OAUTH_REFRESH_TOKEN=dummy-refresh-token
```

Alternatively this can be programatically done. Example code below.

```python
from gutils.services.api_client import GoogleApiClient
from gutils.services.enums import LoginType
from gutils.creds.google.oauth import Oauth2Token


token = Oauth2Token(
    client_id = "dummy-client-id"
    client_secret = "dummy-client-secret"
    token = "dummy-auth-token" # Optional
    refresh_token = "dummy-refresh-token"
)

# If environment variables are set,
token = Oauth2Token()

scopes = ['https://www.googleapis.com/auth/spreadsheets'] # Note: The scopes authorised to this token will only work.
                                                          # If new scope needs to be added, use `client.add_scope()` which will trigger a new oauth flow and it will require 
                                                          # `gutils.creds.google.oauth.Oauth2Creds` to be set.

client = GoogleApiClient(scopes=scopes, config=config, login_type=LoginType.OAUTH2)
client.set_authz_token(token)
client.initialize()

# Example to create a Google Sheets Client instance
service = client.create_service("sheets", "v4")

```

### Revoking an Oauth permission

```python
client.revoke_oauth_permission()
```

### Service Account Login

```python
from gutils.services.api_client import GoogleApiClient
from gutils.services.enums import LoginType
from gutils.creds.google.service_account import ServiceAccountCreds

scopes = ['https://www.googleapis.com/auth/spreadsheets']

config =  ServiceAccountCreds(
    project_id = "dummy=project-id", 
    private_key_id = "dummy-private-key-id", 
    private_key = "dummy-private-key-id", 
    client_email = "dummy-client_email", 
    client_id = "dummy_service_account_client_id",
    client_x509_cert_url = "dummy-cert-url"
)

# If environment variables are set,
config = ServiceAccountCreds()

client = GoogleApiClient(scopes=scopes, config=config, LoginType.SERVICE_ACCOUNT)
client.initialize()

# Example to create a Google Sheets Client instance
service = client.create_service("sheets", "v4")
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

If you want to add a new service, you can add it to the `services` directory and follow this directory structure.

```bash
.
├── ...
└── gutils
    ├── ...
    └── services
        ├── ...
        ├── services.json # This needs to be modified if a new API client is added to the services
        ├── drive
        │   └── ...
        ├── sheets
        │   └── ...
        └── <new_service>
            ├── __init__.py
            ├── <new_service>.py
            └── <other_modules>.py
```
