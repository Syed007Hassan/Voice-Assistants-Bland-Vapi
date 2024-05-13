SEND_SIMPLE_CALL = {
    "type": "function",
    "function": {
        "name": "forward_simple_call",
        "description": "Send an AI phone call with a custom objective and actions.",
        "parameters": {
            "type": "object",
            "properties": {
                "phone_number": {
                    "type": "string",
                    "description": "The phone number to call. Country code defaults to +1 (US) if not specified. Use E.164 format for predictable results.",
                },
                "task": {
                    "type": "string",
                    "description": "Provide instructions, relevant information, and examples of the ideal conversation flow. Aim for less than 2000 characters where possible. Frame instructions positively. Ends call when objective is complete or voicemail is detected.",
                }
            },
            "required": ["phone_number", "task"]
        }
    }
}
