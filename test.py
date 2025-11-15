import requests
from urllib.parse import quote_plus

# Настройки клиента
CLIENT_ID = '<your_client_id>'
CLIENT_SECRET = '<your_client_secret>'
REDIRECT_URI = 'https://example.com/callback'
SCOPE = 'read write'
AUTHORIZATION_URL = f'https://stepik.org/oauth2/authorize/?client_id={quote_plus(CLIENT_ID)}&response_type=code&redirect_uri={quote_plus(REDIRECT_URI)}&scope={quote_plus(SCOPE)}'

def get_access_token(code):
    token_url = 'https://stepik.org/api/oauth2/token/'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(token_url, data=data)
    return response.json().get('access_token')
