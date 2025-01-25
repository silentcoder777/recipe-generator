########################
# Library imports
########################

from openai import OpenAI
import requests
import json

#Read config file
# Open the config.json file
with open('config.json', 'r') as f:
    config = json.load(f)

###############
# Variables
##############
chatModel = "gpt-4o-mini"
testChatMessage = "Hello. who are you?"
openAIKey = config['OPENAI_API_KEY']

# URL
chatURL = "https://api.openai.com/v1/chat/completions"

# Headers
chatHeader = {
    'Authorization': f'Bearer {openAIKey}',
    'Content-Type': 'application/json'
}


chatData = {
    'model': chatModel,
    'messages':  [
        {
            "role": "user",
            "content": testChatMessage
        }
    ]
}

response = requests.post(chatURL, json = chatData, headers = chatHeader)


if response.status_code == 200:
    print("Request was successful!")
    print(response.json())
else:
    print("Failed to send the request. Status code:", response.status_code, response.json())