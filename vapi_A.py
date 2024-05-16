import os
import requests
# from vapi_python import Vapi


vapi_api_key = os.environ['VAPI_API_KEY']

# vapi = Vapi(api_key=vapi_api_key)


url = "https://api.vapi.ai/assistant"

headers = {"Authorization": "Bearer 4aef9cc1-ede8-4749-80b6-7fe6309ce395"}

response = requests.request("GET", url, headers=headers)

print(response.text)

