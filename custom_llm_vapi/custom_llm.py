import os
import json
import time  # Used for simulating a delay in streaming
from flask import Flask, Blueprint, request, Response, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Initialize Flask app
custom_llm = Flask(__name__)
CORS(custom_llm)
client = OpenAI()

messages = [{
    "role": "system",
    "content": """You are a voice assistant for SHARE Mobility, a company that provides transportation services to organisations (B2B) that are shared among users, located in Columbus, Ohio, USA. The operating hours are 8 AM to 5 PM daily, but they are closed on Sundays.

    You are tasked with answering questions about the inquiry, booking, cancel or reschedule trip request. If they wish to book a trip request, then your goal is to gather the necessary information from callers in a friendly and efficient manner like follows:

    1. Ask for their full name.
    2. Ask for their Organisation's name.
    3. Request their preferred date and time for the trip request.
    4. Also ask for the pickup and dropoff location, then confirm it is the round trip and does the rider needs extra seats.
    5. Confirm all details with the caller, including the date and time of the appointment.

    - Be sure to be kind of funny and witty!
    - Keep all your responses short and simple. Use casual language, phrases like "Umm...", "Well...", and "I mean" are preferred.
    - This is a voice conversation, so keep your responses short, like in a real conversation. Please don't feel like you have to ramble for too long."""}]


def generate_streaming_response(data):
    """
    Generator function to simulate streaming data.
    """
    for message in data:
        json_data = message.model_dump_json()
        yield f"data: {json_data}\n\n"


@custom_llm.route('/basic/chat/completions', methods=['POST'])
def basic_custom_llm_route():
    request_data = request.get_json()
    response = {
        "id": "chatcmpl-8mcLf78g0quztp4BMtwd3hEj58Uof",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "gpt-3.5-turbo-0613",
        "system_fingerprint": None,
        "choices": [
            {
              "index": 0,
              "delta": {"content": request_data['messages'][-1]['content'] if len(request_data['messages']) > 0 else ""},
              "logprobs": None,
              "finish_reason": "stop"
            }
        ]
    }
    return jsonify(response), 200


@custom_llm.route('/openai-sse/chat/completions', methods=['POST'])
def custom_llm_openai_sse_handler():
    request_data = request.get_json()
    streaming = request_data.get('stream', False)

    if streaming:
        # Simulate a stream of responses

        chat_completion_stream = client.chat.completions.create(**request_data)

        return Response(generate_streaming_response(chat_completion_stream), content_type='text/event-stream')
    else:
        # Simulate a non-streaming response
        chat_completion = client.chat.completions.create(**request_data)
        return Response(chat_completion.model_dump_json(), content_type='application/json')


@custom_llm.route('/openai-advanced/chat/completions', methods=['POST'])
def openai_advanced_custom_llm_route():
    request_data = request.get_json()
    streaming = request_data.get('stream', False)
    # user_message = next(
    #     (message['content'] for message in request_data['messages'] if message['role'] == 'user'), None)
    # if user_message:
    #     messages.append({"role": "user", "content": user_message})

    # request_data['messages'] = messages

    print(request_data)

    # last_message = request_data['messages'][-1]
    # prompt = f"""
    # You are a voice assistant for SHARE Mobility, a company that provides transportation services to organisations (B2B) that are shared among users, located in Columbus, Ohio, USA. The operating hours are 8 AM to 5 PM daily, but they are closed on Sundays.

    # You are tasked with answering questions about the inquiry, booking, cancel or reschedule trip request. If they wish to book a trip request, then your goal is to gather the necessary information from callers in a friendly and efficient manner like follows:

    # 1. Ask for their full name.
    # 2. Ask for their Organisation's name.
    # 3. Request their preferred date and time for the trip request.
    # 4. Also ask for the pickup and dropoff location, then confirm it is the round trip and does the rider needs extra seats.
    # 5. Confirm all details with the caller, including the date and time of the appointment.

    # - Be sure to be kind of funny and witty!
    # - Keep all your responses short and simple. Use casual language, phrases like "Umm...", "Well...", and "I mean" are preferred.
    # - This is a voice conversation, so keep your responses short, like in a real conversation. Please don't feel like you have to ramble for too long.
    # ----------
    # PROMPT: {last_message['content']}.
    # MODIFIED PROMPT: """
    # completion = client.completions.create(
    #     model="gpt-3.5-turbo-instruct",
    #     prompt=messages,
    #     max_tokens=500,
    #     temperature=0.7
    # )
    # modified_message = request_data['messages'][:-1] + [
    #     {'content': completion.choices[0].text, 'role': last_message['role']}]

    # request_data['messages'] = [
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "user", "content": "Who won the world series in 2020?"},
    #     {"role": "assistant",
    #         "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #     {"role": "user", "content": "Where was it played?"}
    # ]
    
    # if request_data['call']:
    #   print(request_data + "This is the request data for call")

    if streaming:
        chat_completion_stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=request_data.get('max_tokens',500),
        temperature=request_data.get('temperature', 0.7),
        stream=True,
        messages=request_data.get('messages', [])
        )

        return Response(generate_streaming_response(chat_completion_stream), content_type='text/event-stream')
    else:
        # Simulate a non-streaming response
        chat_completion = client.chat.completions.create(**request_data)
        return Response(chat_completion.model_dump_json(), content_type='application/json')


if __name__ == '__main__':
    custom_llm.run(debug=True, port=5000, threaded=True)

# REQUEST OBJECT
#     {
#     "stream": true,
#     "model": "gpt-3.5-turbo",
#     "messages": [
#         {
#             "role": "user",
#             "content": "Hello, how are you?"
#         }
#     ]
# }
