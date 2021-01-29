import requests
from requests.exceptions import HTTPError

url_valid = 'https://api.github.com'
url_invalid = 'https://api.github.com/invalid'

for url in [url_valid, url_invalid]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'http error: {http_err}')
    except Exception as other_err:
        print(f'error: {other_err}')
    else:
        print('success')
