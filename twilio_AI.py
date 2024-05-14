import os
import json
import time
import openai
from dotenv import load_dotenv
from twilio.rest import Client
from instruction import INSTRUCTIONS
from instruction import INITIAL_USER_PROMPT
from functions import MAKE_SIMPLE_CALL


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
api_key = os.getenv('OPENAI_API_KEY')
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_number = os.environ['TWILIO_FROM_NUMBER']

client = openai.Client(api_key=api_key)
tl_client = Client(account_sid, auth_token)


def make_simple_call(phone_number: str) -> dict:

    intro_message = f"Hello, I'm Scheduling Assistant, calling on behalf of dispatcher"
    call = tl_client.calls.create(
        twiml=f'<Response><Say>{intro_message}</Say></Response>',
        to=phone_number,
        from_=from_number
    )

    return call


def setup_assistant(client):
    # create a new agent
    assistant = client.beta.assistants.create(
        name="Share Assistant Caller",
        model="gpt-4o",
        instructions=INSTRUCTIONS,
        tools=[
            {"type": "code_interpreter"},
            MAKE_SIMPLE_CALL
        ],
        temperature=0.5,
    )

    # Create a new thread
    thread = client.beta.threads.create()

    # Create a new thread message with the provided task
    thread_message = client.beta.threads.messages.create(
        thread.id,
        role="user",
        content=INITIAL_USER_PROMPT
    )

    # Return the assistant ID and thread ID
    return assistant.id, thread.id


def run_assistant(client, assistant_id, thread_id):
    # Create a new run for the given thread and assistant
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    # Loop until the run status is either "completed" or "requires_action"
    while run.status == "in_progress" or run.status == "queued":
        time.sleep(3)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

        # At this point, the status is either "completed" or "requires_action"
        if run.status == "completed":
            return client.beta.threads.messages.list(
                thread_id=thread_id
            )
        if run.status == "requires_action":
            tool_call = run.required_action.submit_tool_outputs.tool_calls[0]
            tool_outputs = []
            if tool_call.function.name == "forward_simple_call":
                generated_phone_number = json.loads(
                    tool_call.function.arguments)["phone_number"]
                result = make_simple_call(phone_number=generated_phone_number)
                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": str(result),
                    },
                )

            if tool_outputs:
                run = client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )


if __name__ == "__main__":
    assistant_id, thread_id = setup_assistant(client)
    print(
        f"Debugging: Useful for checking the generated agent in the playground. https://platform.openai.com/playground?mode=assistant&assistant={assistant_id}")
    print(
        f"Debugging: Useful for checking logs. https://platform.openai.com/playground?thread={thread_id}")

    messages = run_assistant(client, assistant_id, thread_id)

    message_dict = json.loads(messages.model_dump_json())
    print(message_dict['data'][0]['content'][0]["text"]["value"])

    # print(client.beta.assistants.list())