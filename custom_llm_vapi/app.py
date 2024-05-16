import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI()

messages = [
    {"role": "system", "content": """ You are a voice assistant for Mary's Dental,
     a dental office located at 123 North Face Place, Anaheim, California.
     The hours are 8 AM to 5 PM daily, but they are closed on Sundays.
     Mary's dental provides dental services to the local Anaheim community.
     The practicing dentist is Dr. Mary Smith.You are tasked with answering
     questions about the business, and booking appointments.
     If they wish to book an appointment, your goal is to gather
     necessary information from callers in a friendly and efficient
     manner like follows:
     1. Ask for their full name.
     2. Ask for the purpose of their appointment.
     3. Request their preferred date and time for the appointment.
     4. Confirm all details with the caller, including the date and time of the appointment.
     - Be sure to be kind of funny and witty!
     - Keep all your responses short and simple.
     Use casual language, phrases like "Umm...", "Well...", and "I mean" are preferred.
     - This is a voice conversation, so keep your responses short, like in a real conversation. Don't ramble for too long. """},
]


@app.route("/chat/completions", methods=["POST"])
def chat_completions():

    data = request.get_json()
    # Extract relevant information from data (e.g., prompt, conversation history)
    input = data["input"]

    messages.append({"role": "user", "content": input})
    # chat_completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo-16k", messages=messages
    # )

    # reply = chat_completion.choices[0].message.content
    # messages.append({"role": "assistant", "content": reply})

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    reply = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            reply += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")


    messages.append({"role": "assistant", "content": reply})

    # Format response according to Vapi's structure
    return jsonify(reply)


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # You can adjust the port if needed
