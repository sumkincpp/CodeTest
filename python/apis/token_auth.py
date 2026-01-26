from logging import Logger

import requests
from requests.auth import AuthBase
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session, OAuth2

def get_auth(token_url, client_id, client_secret):
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
    auth: AuthBase = OAuth2(client_id=client_id, client=client, token=token)
    
    return auth


auth = get_auth()
response = requests.post(application_url, json=data, auth=auth)
