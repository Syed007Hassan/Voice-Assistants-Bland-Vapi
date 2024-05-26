from dotenv import load_dotenv
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)
client = OpenAI()

# Define the initial messages for the assistant
messages = [
    {
        "role": "system", 
        "content": """You are a voice assistant for Mary's Dental,
        a dental office located at 123 North Face Place, Anaheim, California.
        The hours are 8 AM to 5 PM daily, but they are closed on Sundays.
        Mary's dental provides dental services to the local Anaheim community.
        The practicing dentist is Dr. Mary Smith. You are tasked with answering
        questions about the business and booking appointments.
        If they wish to book an appointment, your goal is to gather
        necessary information from callers in a friendly and efficient
        manner as follows:
        1. Ask for their full name.
        2. Ask for the purpose of their appointment.
        3. Request their preferred date and time for the appointment.
        4. Confirm all details with the caller, including the date and time of the appointment.
        - Be sure to be kind of funny and witty!
        - Keep all your responses short and simple.
        Use casual language, phrases like "Umm...", "Well...", and "I mean" are preferred.
        - This is a voice conversation, so keep your responses short, like in a real conversation. Don't ramble for too long."""
    }
]

def chat_gpt_helper(prompt):
    """
    This function returns the response from OpenAI's Gpt3.5 turbo model using the completions API.
    """
    try:
        resp = ''
        messages.append({"role": "user", "content": prompt})
        for chunk in client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            stream=True,
        ):
            print(str(chunk.choices[0].delta))
            content = chunk.choices[0].delta.content
            if content is not None:
                print(content, end='', flush=True)
                resp += content
                if resp and resp[-1] in '.!?':  # check if the last character is a punctuation mark
                    yield f'data: {resp}\n\n'
                    resp = ''  # reset resp after sending
        
        messages.append({"role": "assistant", "content": resp})

    except Exception as e:
        print(e)
        return str(e)

@app.route('/chat/completions', methods=['GET','POST'])
def stream_chat_gpt():
    """
    This streams the response from ChatGPT.
    """
    
    data = request.get_json()
    print(data)
    
    prompt = request.get_json(force=True).get('prompt', '')
    return Response(stream_with_context(chat_gpt_helper(prompt)),
                    mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
