########################
# Library imports
########################

from openai import OpenAI
import requests
import json
from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS


@app.route("/")
def home():
    print("Home route accessed")
    return "Hello, Flask!"

@app.route('/api/endpoint', methods=['POST'])
def process_data():

    data = request.get_json()
    recipe_name = data.get('recipeName')

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
                "content": recipe_name
            }
        ]
    }

    response = requests.post(chatURL, json = chatData, headers = chatHeader)
    modelResponse = response.json()['choices'][0]['message']['content']


    if response.status_code == 200:
        print("Request was successful!")
        print(response.json())
    else:
        print("Failed to send the request. Status code:", response.status_code, response.json())
    
    return jsonify({"message": modelResponse})


if __name__ == '__main__':
    app.run()