import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

import pyttsx3
import speech_recognition as sr

client=Groq(api_key=os.getenv("GROQ_API_KEY"))


engine = pyttsx3.init()

def speak(text):
    print("Agent:" ,text)
    engine.say(text)
    engine.runAndWait()



def listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("You:", text)
        return text

    except:
        return None



while True:
    query=listen()

    if not query:
        continue

    if query.lower() in ["quit","exit"]:
        break

    response=client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role":"system","content":"you are a helpful assistant"},
            {"role":"user","content":query},
        ]
    )

    answer=response.choices[0].message.content
    speak(answer)
