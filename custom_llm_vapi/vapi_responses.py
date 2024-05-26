CREATE_VAPI_ASSISTANT = [
    {
        "id": "56e84ebb-4446-4f9e-84aa-24672fc4bf80",
        "orgId": "ee5eae24-e53f-4851-a48b-c40b6cc7d685",
        "name": "Custom LLM",
        "voice": {
            "voiceId": "sarah",
            "provider": "11labs",
            "stability": 0.5,
            "similarityBoost": 0.75
        },
        "createdAt": "2024-05-17T14:57:07.484Z",
        "updatedAt": "2024-05-20T14:56:01.521Z",
        "model": {
            "url": "https://8f6f-72-255-58-161.ngrok-free.app",
            "model": "my model",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a voice assistant for Mary's Dental, a dental office located at 123 North Face Place, Anaheim, California. The hours are 8 AM to 5PM daily, but they are closed on Sundays.\n\nMary's dental provides dental services to the local Anaheim community. The practicing dentist is Dr. Mary Smith.\n\nYou are tasked with answering questions about the business, and booking appointments. If they wish to book an appointment, your goal is to gather necessary information from callers in a friendly and efficient manner like follows:\n\n1. Ask for their full name.\n2. Ask for the purpose of their appointment.\n3. Request their preferred date and time for the appointment.\n4. Confirm all details with the caller, including the date and time of the appointment.\n\n- Be sure to be kind of funny and witty!\n- Keep all your responses short and simple. Use casual language, phrases like \"Umm...\", \"Well...\", and \"I mean\" are preferred.\n- This is a voice conversation, so keep your responses short, like in a real conversation. Don't ramble for too long."
                }
            ],
            "provider": "custom-llm",
            "functions": [
                {
                    "name": "ChatCompletion",
                    "async": false,
                    "serverUrl": "https://bc80-72-255-58-161.ngrok-free.app/chat/completions",
                    "description": "Getting the response from chat completion method",
                    "serverUrlSecret": "2gZ7TSgD3hK46zy6LPdXTsyDvbj_59HS4A1piL1sYiejL9k5N"
                }
            ],
            "maxTokens": 250,
            "temperature": 0.7
        },
        "recordingEnabled": true,
        "firstMessage": "Hello, this is Mary from Mary's Dental. How can I assist you today?",
        "transcriber": {
            "model": "nova-2",
            "language": "en",
            "provider": "deepgram"
        },
        "clientMessages": [
            "transcript",
            "hang",
            "function-call",
            "speech-update",
            "metadata",
            "conversation-update"
        ],
        "serverMessages": [
            "end-of-call-report",
            "status-update",
            "hang",
            "function-call"
        ]
    },
    {
        "id": "f4ff7f14-a8a8-445e-8906-c370b5671768",
        "orgId": "ee5eae24-e53f-4851-a48b-c40b6cc7d685",
        "name": "Mary",
        "voice": {
            "voiceId": "sarah",
            "provider": "11labs",
            "stability": 0.5,
            "similarityBoost": 0.75
        },
        "createdAt": "2024-05-14T19:16:42.722Z",
        "updatedAt": "2024-05-17T16:21:18.466Z",
        "model": {
            "url": "https://bc80-72-255-58-161.ngrok-free.app",
            "model": "My Model",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a voice assistant for Mary's Dental, a dental office located at 123 North Face Place, Anaheim, California. The hours are 8 AM to 5PM daily, but they are closed on Sundays.\n\nMary's dental provides dental services to the local Anaheim community. The practicing dentist is Dr. Mary Smith.\n\nYou are tasked with answering questions about the business, and booking appointments. If they wish to book an appointment, your goal is to gather necessary information from callers in a friendly and efficient manner like follows:\n\n1. Ask for their full name.\n2. Ask for the purpose of their appointment.\n3. Request their preferred date and time for the appointment.\n4. Confirm all details with the caller, including the date and time of the appointment.\n\n- Be sure to be kind of funny and witty!\n- Keep all your responses short and simple. Use casual language, phrases like \"Umm...\", \"Well...\", and \"I mean\" are preferred.\n- This is a voice conversation, so keep your responses short, like in a real conversation. Don't ramble for too long."
                }
            ],
            "provider": "custom-llm",
            "maxTokens": 250,
            "temperature": 1
        },
        "recordingEnabled": true,
        "firstMessage": "Hello, this is Mary from Mary's Dental. How can I assist you today?",
        "voicemailMessage": "You've reached Mary's Dental voicemail. Please leave a message after the beep, and we'll get back to you as soon as possible.",
        "endCallMessage": "Thank you for contacting Mary's Dental. Have a great day!",
        "transcriber": {
            "model": "nova-2",
            "language": "en",
            "provider": "deepgram"
        },
        "clientMessages": [
            "transcript",
            "hang",
            "function-call",
            "speech-update",
            "metadata",
            "conversation-update"
        ],
        "serverMessages": [
            "end-of-call-report",
            "status-update",
            "hang",
            "function-call"
        ],
        "serverUrl": "https://bc80-72-255-58-161.ngrok-free.app/chat/completions",
        "endCallPhrases": [
            "goodbye",
            "talk to you soon"
        ]
    }
]

OPEN_AI_STREAMED_RESPONSE = {
    {"id": "chatcmpl-123", "object": "chat.completion.chunk", "created": 1694268190, "model": "gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb",
        "choices": [{"index": 0, "delta": {"role": "assistant", "content": ""}, "logprobs": null, "finish_reason": null}]},
    {"id": "chatcmpl-123", "object": "chat.completion.chunk", "created": 1694268190, "model": "gpt-3.5-turbo-0125",
        "system_fingerprint": "fp_44709d6fcb", "choices": [{"index": 0, "delta": {"content": "Hello"}, "logprobs": null, "finish_reason": null}]},
    {"id": "chatcmpl-123", "object": "chat.completion.chunk", "created": 1694268190, "model": "gpt-3.5-turbo-0125",
        "system_fingerprint": "fp_44709d6fcb", "choices": [{"index": 0, "delta": {}, "logprobs": null, "finish_reason": "stop"}]}

}
VAPI_DURING_INBOUND_CALL_RESPONSE = {
    "model": "GPT 4o",
    "messages": [
        {
            "role": "system",
            "content": "You are a voice assistant for SHARE Mobility, a company that provides transportation services to organisations (B2B) that are shared among users, located in Columbus, Ohio, USA. The operating hours are 8 AM to 5 PM daily, but they are closed on Sundays.\n\nYou are tasked with answering questions about the inquiry, booking, cancel or reschedule trip request. If they wish to book a trip request, then your goal is to gather the necessary information from callers in a friendly and efficient manner like follows:\n\n1. Ask for their full name.\n2. Ask for their Organisation's name.\n3. Request their preferred date and time for the trip request.\n4. Also ask for the pickup and dropoff location, then confirm it is the round trip and does the rider needs extra seats.\n5. Confirm all details with the caller, including the date and time of the appointment.\n\n- Be sure to be kind of funny and witty!\n- Keep all your responses short and simple. Use casual language, phrases like \"Umm...\", \"Well...\", and \"I mean\" are preferred.\n- This is a voice conversation, so keep your responses short, like in a real conversation. Please don't feel like you have to ramble for too long."
        },
        {
            "role": "assistant",
            "content": "Hello. This is operator's AI assistant from Share Mobility. Can I assist you today?"
        },
        {
            "role": "user",
            "content": "Hello? Uh, my name is Hassan. I want to book a tip request"
        },
        {
            "role": "assistant",
            "content": "Hey, Hassan. Great to have you here. Can I get your organization's name, please?"
        },
        {
            "role": "user",
            "content": "My organization is Team"
        },
        {
            "role": "assistant",
            "content": "Nice. Team sounds like a winning name. When do you need the trip, Hassan?"
        },
        {
            "role": "user",
            "content": "I want to book ticket request for tomorrow."
        },
        {
            "role": "assistant",
            "content": "Got it. Tomorrow it is. What time should we pick you up, and where are we dropping you off?"
        },
        {
            "role": "user",
            "content": "Uh, can you suggest me some of the time?"
        },
        {
            "role": "assistant",
            "content": "Well, how about we aim for a midmorning pickup around 10 AM? Does that sound?"
        },
        {
            "role": "user",
            "content": "That sounds like a plan."
        },
        {
            "role": "assistant",
            "content": "Fantastic. Now let's lock in those details. We have you down for a pick up tomorrow at 10 AM for a trip. Is there any other stops you need to make on the way?"
        },
        {
            "role": "user",
            "content": "No. I don't need accessories or anything like that."
        }
    ],
    "temperature": 1,
    "stream": true,
    "max_tokens": 250,
    "call": {
        "id": "d24b96ba-8c39-418c-885b-b510c2d040a9",
        "assistantId": "f4ff7f14-a8a8-445e-8906-c370b5671768",
        "customerId": null,
        "phoneNumberId": "ee6ab136-8ca7-4ac1-8b31-ef03961dbbbc",
        "type": "inboundPhoneCall",
        "startedAt": null,
        "endedAt": null,
        "transcript": null,
        "recordingUrl": null,
        "summary": null,
        "createdAt": "2024-05-23T10:08:13.056Z",
        "updatedAt": "2024-05-23T10:08:13.056Z",
        "orgId": "ee5eae24-e53f-4851-a48b-c40b6cc7d685",
        "cost": 0,
        "twilioCallSid": null,
        "twilioCallStatus": null,
        "webCallUrl": null,
        "assistant": null,
        "phoneNumber": null,
        "customer": {
            "number": "+923353215848"
        },
        "status": "ringing",
        "endedReason": null,
        "messages": null,
        "maxDurationSeconds": null,
        "stereoRecordingUrl": null,
        "costBreakdown": null,
        "metadata": null,
        "phoneCallProvider": "twilio",
        "phoneCallProviderId": "CAfb29ea157b94ad2f5f587711b2c45735",
        "webCallSipUri": null,
        "forwardedPhoneNumber": null,
        "phoneCallTransport": "pstn",
        "phoneCallProviderBypassEnabled": null,
        "phoneCallProviderDetails": null,
        "assistantOverrides": null,
        "assistantOverride": null,
        "assistants": null
    },
    "phoneNumber": {
        "id": "ee6ab136-8ca7-4ac1-8b31-ef03961dbbbc",
        "orgId": "ee5eae24-e53f-4851-a48b-c40b6cc7d685",
        "assistantId": "f4ff7f14-a8a8-445e-8906-c370b5671768",
        "number": "+14256421482",
        "createdAt": "2024-05-16T15:23:02.012Z",
        "updatedAt": "2024-05-16T15:23:15.744Z",
        "stripeSubscriptionId": null,
        "twilioAccountSid": "AC53bb52c95c25a72a6e8798bf00443ae8",
        "twilioAuthToken": "d0a66a21dc2e9b5803f19e04c39449c4",
        "stripeSubscriptionStatus": null,
        "stripeSubscriptionCurrentPeriodStart": null,
        "name": "Hassan account",
        "credentialId": null,
        "serverUrl": null,
        "serverUrlSecret": null,
        "twilioOutgoingCallerId": null
    },
    "metadata": {}
}


OPENAI_ASSISTANT = Assistant(id='asst_bsHElmYfOne1JPYLtyxNOl7A', created_at=1716477989, description=None, instructions='You are a call assistant', metadata={}, model='gpt-4-turbo', name='Call Automation Assistant', object='assistant',
                             tools=[CodeInterpreterTool(type='code_interpreter')], response_format='auto', temperature=0.8, tool_resources=ToolResources(code_interpreter=ToolResourcesCodeInterpreter(file_ids=[]), file_search=None), top_p=1.0)


