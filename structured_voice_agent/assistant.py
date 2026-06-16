from chat_memory import *
from text_to_speech import speak
from llm import *

def chat(text):
    # add user msg to history
    add_user_msg(text)

    # pass messages to AI
    answer=generate_response(get_messages())

    # add AI msg to history
    add_AI_msg(answer)

    return answer