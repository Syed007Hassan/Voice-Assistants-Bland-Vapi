import os
from typing import *
import json
import time
import subprocess
from dotenv import load_dotenv
import requests
import openai
from instruction import INSTRUCTIONS
from instruction import INITIAL_USER_PROMPT
from functions import SEND_SIMPLE_CALL

load_dotenv()


api_key = os.getenv('OPENAI_API_KEY')
client = openai.Client(api_key=api_key)


def execute_python_code(s: str) -> str:
    with NamedTemporaryFile(suffix='.py', delete=False) as temp_file:
        temp_file_name = temp_file.name
        temp_file.write(s.encode('utf-8'))
        temp_file.flush()
    try:
        result = subprocess.run(
            ['python', temp_file_name],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
    finally:
        import os
        os.remove(temp_file_name)


def make_simple_call(phone_number: str, task: str) -> dict:
    url = "https://api.bland.ai/v1/calls"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'sk-vepvnqju3xd7tk9rs70j8e4dkxq0d2xr4lsdareaknnmwljqyom81wvm2d22qps769'
    }
    data = {
        "phone_number": phone_number,
        "task": task
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


def setup_assistant(client):
    # create a new agent
    assistant = client.beta.assistants.create(
        name="Share Assistant Caller",
        instructions=INSTRUCTIONS,
        tools=[
            {"type": "code_interpreter"},
            SEND_SIMPLE_CALL
        ],
        model="gpt-4-turbo",
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
            if tool_call.function.name == "send_simple_call":
                generated_phone_number = json.loads(
                    tool_call.function.arguments)["phone_number"]
                generated_task = json.loads(
                    tool_call.function.arguments)["task"]
                result = make_simple_call(
                    phone_number=generated_phone_number,
                    task=generated_task
                )
                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": result,
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
