from assistant import chat
from text_to_speech import speak

while True:
    user=input("you:")
    if user == "quit":
        break

    reply=chat(user)

    speak(reply)
