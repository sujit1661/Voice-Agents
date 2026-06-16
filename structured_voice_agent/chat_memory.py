messages = [
    {
        "role": "system",
        "content": "You are a helpful voice assistant."
    }
]


def add_user_msg(message):
    messages.append({
        "role": "user",
        "content": message
    })


def add_AI_msg(message):
    messages.append({
        "role": "assistant",
        "content": message
    })


def get_messages():
    return messages