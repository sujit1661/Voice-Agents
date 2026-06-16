import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"\nAgent: {text}\n")
    engine.say(text)
    engine.runAndWait()