import requests
import os

url = "https://arpeggi.io/api/kits/v1/voice-models"

api_token = 'YIWvJDug.QiyScScD6HWh3AoHVS5S6dti'

headers = {
    'Authorization' : f'Bearer {api_token}'
}

params = {
    'order': 'asc',
    'page': 1,
    'perPage': 10,
    'myModels' : "true"
}

response = requests.get(url=url, headers=headers, params=params)

if response.status_code == 200:
    # print(json.dumps(response.json(), indent=4))
    voice_name = [{voice["title"] : voice["id"]}  for voice in response.json()["data"]]
    # print(voice_name)
else:
    print("Something happened and there was an issue")
    
for item in voice_name:
    try:
        print(f'ID: {item["Male Gospel Pop + Female Doo-Wop Pop"]}')
        voice_id = item["Male Gospel Pop + Female Doo-Wop Pop"]
    except:
        pass
    # print(item)
    
url_conversion = "https://arpeggi.io/api/kits/v1/voice-conversions"

data = {
    'voiceModelId' : voice_id,
    'conversionStrength' : 0.5,
    'modelVolumeMix' : 0.5,
    'pitchShift' : 0
}

file = {
    'soundFile' : ("song.wav", open("song.wav", "rb"))
}

response = requests.post(url=url_conversion, headers=headers, params=data, files=file)

# Do conversion
if response.status_code == 200:
    conversion_data = response.json()
    job_id = conversion_data["id"]
    print(f"Job ID: {job_id}")
else:
    print(response.status_code)
    

url_get_conversion = f"https://arpeggi.io/api/kits/v1/voice-conversions/{job_id}"
response = requests.get(url=url_get_conversion, headers=headers)

if response.status_code == 200:
    job_data = response.json()
    print(job_data)
else:
    print(response.status_code)  

output_file_url = job_data['outputFileUrl']
if output_file_url:
    response = requests.get(output_file_url)
    if response.status_code == 200:
        filename = "converted_file.wav"
        save_path = os.path.join(os.getcwd(), filename)
        
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File saved as {save_path}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
else:
    print("No outputFileUrl found in the API response.")
