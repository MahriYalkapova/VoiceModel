import requests
import json

url = "https://arpeggi.io/api/kits/v1/voice-models"

api_token = 'TSESMmZW.-Jb_8n6RnEzHPgiaGsw5gWFU'

headers = {
    'Authorization' : f'Bearer {api_token}'
}

params = {
    'order' : 'asc',
    'page' : 1,
    'perPage' : 10,
    'myModels' : "true"
}

response = requests.get(url=url, headers=headers, params=params)

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print("Something happened and there was an issue")

    