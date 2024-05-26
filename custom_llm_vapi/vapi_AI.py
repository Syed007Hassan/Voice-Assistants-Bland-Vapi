import os
import requests
from dotenv import load_dotenv
# from vapi_python import Vapi

load_dotenv()

vapi_api_key = os.environ['VAPI_API_KEY']

# vapi = Vapi(api_key=vapi_api_key)


url = "https://api.vapi.ai/assistant"

getPhoneUrl = "https://api.vapi.ai/phone-number"


headers = {"Authorization": "Bearer 4aef9cc1-ede8-4749-80b6-7fe6309ce395"}

response = requests.request("GET", getPhoneUrl, headers=headers)

print(response.text)

# Setting up an endpoint that would be the Server where we would receive the response from the Vapi API
# Creating a new assistant with the Vapi API
# Import twilio number via the Vapi API
# create an openai assistant
# create an inbound call with the assistant
# create a new thread
