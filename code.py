from gtts import gTTS
import os
import requests

text = "Im Kenneth, Im aslesel API and Im here to help you."
tts = gTTS(text)
tts.save("output.mp3")
file_path = "output.mp3"

# endPoint = 'https://api.mnotify.com/api/voice/quick'
# apiKey = 'fyKaR5gxMc3BNZyg5t3Q2K3Mi'

# # Open the file in binary mode
# file = {'file': open("output.mp3", 'rb')}
# data = {
#     'campaign': 'First Voice Campaign',
#     'recipient[]': ['0242002367'],
#     'is_schedule': False,
# }

# url = endPoint + '?key=' + apiKey

# response = requests.post(url, files=file, data=data)
# try:
#     response_data = response.json()
#     if response_data['status'] == 'success':
#         print(response_data['message'])
#     else:
#         print("Failed to send file. Error:", response_data['message'])
# except ValueError:
#     print("Invalid JSON response from the API.")


url = 'https://sms.arkesel.com/api/v2/sms/voice/send'
headers = {
    'api-key': 'OkZTNThRVEpQVTVac1FacWE='
}

data = {
    'recipients[]': ['233545865156', '233242002367']
}

files = {
    'voice_file': open("output.mp3", 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 200:
    print(response.json())
else:
    print(response.text)
