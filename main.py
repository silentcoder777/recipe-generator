########################
# Library imports
########################

from openai import OpenAI
import requests
from config import OPENAI_API_KEY


###############
# Variables
##############
chatModel = "gpt-4o-mini"
testChatMessage = "Hello. who are you?"

# URL
chatURL = "https://api.openai.com/v1/chat/completions"

# Headers
chatHeader = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
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