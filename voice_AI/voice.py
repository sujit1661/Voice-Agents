"""
Groq Voice Agent — CMD Edition
================================
Mic → Groq Whisper STT → Groq Llama LLM → Windows TTS (pyttsx3) → Speakers

All you need: a GROQ_API_KEY in .env.local
No LiveKit, no extra accounts, runs 100% locally for audio.

Usage:
    python voice.py
    python voice.py --model llama-3.1-8b-instant   (faster/cheaper)
    python voice.py --voice 1                        (change TTS voice index)

Controls (in the terminal):
    Press Enter  →  start recording
    Press Enter  →  stop recording and send
    Type q       →  quit
"""

import argparse
import io
import os
import sys
import threading
import time

import numpy as np
import pyttsx3
import sounddevice as sd
import soundfile as sf
from dotenv import load_dotenv
from groq import Groq

# ── Config ───────────────────────────────────────────────────────────────────
load_dotenv(".env.local")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
STT_MODEL    = "whisper-large-v3-turbo"
LLM_MODEL    = "llama-3.3-70b-versatile"
SAMPLE_RATE  = 16000
CHANNELS     = 1

SYSTEM_PROMPT = (
    "You are a helpful voice assistant powered by Groq. "
    "Keep replies SHORT — 1 to 3 sentences unless the user asks for detail. "
    "Never use bullet points, markdown, emojis, asterisks, or special characters. "
    "Speak naturally as if talking to a person face to face."
)

# ── ANSI colours ─────────────────────────────────────────────────────────────
R      = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
DIM    = "\033[2m"


# ── TTS engine (pyttsx3 — Windows built-in voices, no API needed) ─────────────
def make_tts_engine(voice_index: int = 0) -> pyttsx3.Engine:
    engine = pyttsx3.init()
    engine.setProperty("rate", 185)    # words per minute
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    if voices:
        idx = voice_index % len(voices)
        engine.setProperty("voice", voices[idx].id)
        print(f"  {DIM}TTS voice : {voices[idx].name}{R}")
    return engine


def speak(engine: pyttsx3.Engine, text: str) -> None:
    engine.say(text)
    engine.runAndWait()


# ── Audio recording ───────────────────────────────────────────────────────────
def record_until_enter() -> np.ndarray:
    """Start recording; block until user presses Enter; return int16 audio."""
    frames: list[np.ndarray] = []
    stop_event = threading.Event()

    def _callback(indata, frame_count, time_info, status):
        if not stop_event.is_set():
            frames.append(indata.copy())

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        callback=_callback,
    )

    print(f"  {CYAN}{BOLD}🎤 Recording ...{R}  (press Enter to stop)", flush=True)
    with stream:
        input()
        stop_event.set()
        time.sleep(0.05)  # flush last callback

    if not frames:
        return np.array([], dtype=np.int16)
    return np.concatenate(frames, axis=0).flatten()


# ── Groq STT ──────────────────────────────────────────────────────────────────
def transcribe(client: Groq, audio: np.ndarray) -> str:
    buf = io.BytesIO()
    sf.write(buf, audio, SAMPLE_RATE, format="WAV", subtype="PCM_16")
    buf.seek(0)
    buf.name = "audio.wav"
    result = client.audio.transcriptions.create(
        model=STT_MODEL,
        file=buf,
        language="en",
    )
    return result.text.strip()


# ── Groq LLM ──────────────────────────────────────────────────────────────────
def chat(client: Groq, history: list[dict], user_text: str, model: str) -> str:
    history.append({"role": "user", "content": user_text})
    response = client.chat.completions.create(
        model=model,
        messages=history,
    )
    reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": reply})
    return reply


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(description="Groq Voice Agent — CMD")
    parser.add_argument("--model", default=LLM_MODEL,
                        help="Groq LLM model (default: llama-3.3-70b-versatile)")
    parser.add_argument("--voice", type=int, default=0,
                        help="TTS voice index (0 = first available voice)")
    args = parser.parse_args()

    if not GROQ_API_KEY:
        print(f"{RED}ERROR: GROQ_API_KEY not set in .env.local{R}")
        sys.exit(1)

    client = Groq(api_key=GROQ_API_KEY)
    history: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]

    # ── Startup banner ────────────────────────────────────────────────────
    print(f"""
{BOLD}{CYAN}╔══════════════════════════════════════════╗
║       Groq Voice Agent — CMD Edition     ║
╚══════════════════════════════════════════╝{R}
  {DIM}STT  : {STT_MODEL} (Groq)
  LLM  : {args.model} (Groq)
  TTS  : Windows built-in (pyttsx3){R}
""")

    # ── Init TTS ──────────────────────────────────────────────────────────
    tts = make_tts_engine(args.voice)

    # ── Mic check ─────────────────────────────────────────────────────────
    try:
        sd.query_devices(kind="input")
    except Exception as e:
        print(f"{RED}No microphone found: {e}{R}")
        sys.exit(1)

    print(f"  {YELLOW}Type {BOLD}q{R}{YELLOW} + Enter to quit.  "
          f"Press Enter to start talking.{R}\n")

    # ── Conversation loop ─────────────────────────────────────────────────
    while True:
        print(f"{CYAN}{BOLD}[ Press Enter to speak, or type q to quit ]{R} ", end="", flush=True)
        trigger = input().strip().lower()

        if trigger == "q":
            print(f"{DIM}Goodbye!{R}")
            speak(tts, "Goodbye!")
            break

        # Record
        audio = record_until_enter()
        duration = len(audio) / SAMPLE_RATE
        if duration < 0.5:
            print(f"  {YELLOW}Too short, try again.{R}\n")
            continue

        # Transcribe
        print(f"  {DIM}Transcribing...{R}", end="\r")
        try:
            user_text = transcribe(client, audio)
        except Exception as e:
            print(f"  {RED}STT error: {e}{R}\n")
            continue

        if not user_text:
            print(f"  {YELLOW}Nothing detected, try again.{R}\n")
            continue

        print(f"  {CYAN}{BOLD}You :{R} {user_text}")

        # LLM
        print(f"  {DIM}Thinking...   {R}", end="\r")
        try:
            reply = chat(client, history, user_text, args.model)
        except Exception as e:
            print(f"  {RED}LLM error: {e}{R}\n")
            history.pop()   # remove failed user turn
            continue

        print(f"  {GREEN}{BOLD}Agent:{R} {reply}\n")

        # Speak
        speak(tts, reply)


if __name__ == "__main__":
    main()
