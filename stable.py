import os
import requests
import config


api_host = 'https://makersuite.google.com/app/apikey'
url = f"{api_host}/v1/engines/list"
api_key = config.api_key



response = requests.get(url, headers={
    "Authorization": f"Bearer {api_key}"
})

if response.status_code == 200:
    payload = response.json()
    print(payload)



