import os
import sounddevice as sd
import scipy.io.wavfile as wav
import assemblyai as aai

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

load_dotenv()

# ==========================
# API KEYS
# ==========================

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# ==========================
# LLM
# ==========================

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0.3
)

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="""
    You are a helpful AI voice assistant.
    Give concise and accurate answers.
    """
)

# ==========================
# RECORD AUDIO
# ==========================

def record_audio(filename="voice.wav", duration=5):
    sample_rate = 16000

    print("\n🎤 Speak now...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    wav.write(filename, sample_rate, recording)

    print("✅ Recording complete")

# ==========================
# SPEECH TO TEXT
# ==========================

def speech_to_text(filename):
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(filename)

    if transcript.status == aai.TranscriptStatus.error:
        print("Transcription Error:", transcript.error)
        return None

    return transcript.text

# ==========================
# MAIN LOOP
# ==========================

print("Voice Agent Started")
print("Say 'exit' to stop")

while True:

    record_audio(duration=5)

    user_text = speech_to_text("voice.wav")

    if not user_text:
        continue

    print(f"\n👤 You: {user_text}")

    if user_text.lower() in ["exit", "quit", "stop"]:
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        }
    )

    answer = response["messages"][-1].content

    print(f"\n🤖 Assistant: {answer}")