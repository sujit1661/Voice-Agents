# Groq Voice Agent — CMD Edition

A lightweight command-line voice assistant that runs locally on your computer.

It uses:

* 🎤 Microphone Input (`sounddevice`)
* 📝 Speech-to-Text via Groq Whisper
* 🤖 AI Responses via Groq Llama Models
* 🔊 Text-to-Speech via Windows Built-in Voices (`pyttsx3`)

No LiveKit, no browser, no extra cloud voice services required.

---

# Features

* Voice conversations from the terminal
* Fast speech recognition using Groq Whisper
* Natural AI responses using Groq LLMs
* Windows offline text-to-speech
* Conversation memory during the session
* Supports different Groq models
* Supports multiple Windows voices

---

# Demo Flow

```text
You Speak
    ↓
Microphone Recording
    ↓
Groq Whisper STT
    ↓
User Text
    ↓
Groq Llama Model
    ↓
AI Response
    ↓
Windows TTS
    ↓
Audio Output
```

---

# Requirements

* Python 3.10+
* Windows (recommended)
* Working microphone
* Groq API Key

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/groq-voice-agent.git

cd groq-voice-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install groq python-dotenv sounddevice soundfile numpy pyttsx3
```

---

# Project Structure

```text
groq-voice-agent/
│
├── voice.py
├── .env.local
├── requirements.txt
└── README.md
```

---

# Environment Variables

Create a file named:

```text
.env.local
```

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get a key from:

[https://console.groq.com](https://console.groq.com)

---

# Running the Assistant

Default:

```bash
python voice.py
```

---

Use a Different LLM Model

```bash
python voice.py --model llama-3.1-8b-instant
```

Example:

```bash
python voice.py --model llama-3.3-70b-versatile
```

---

Use a Different Voice

```bash
python voice.py --voice 1
```

```bash
python voice.py --voice 2
```

```bash
python voice.py --voice 3
```

---

# Controls

Start Conversation:

```text
Press Enter
```

Stop Recording:

```text
Press Enter
```

Quit:

```text
q + Enter
```

---

# Supported Models

Examples of Groq models:

```text
llama-3.3-70b-versatile
llama-3.1-8b-instant
llama-3.1-70b-versatile
```

You can replace the model name using:

```bash
--model
```

---

# How It Works

## Recording

Audio is captured from the microphone at:

```text
16kHz
Mono Channel
16-bit PCM
```

---

## Speech Recognition

Audio is sent to Groq Whisper:

```python
whisper-large-v3-turbo
```

which converts speech into text.

---

## AI Processing

Conversation history is maintained in memory:

```python
history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]
```

Each user message and AI response is appended to the history so the assistant remembers context during the session.

---

## Text-to-Speech

The assistant uses:

```python
pyttsx3
```

which relies on Windows built-in speech synthesis.

No external TTS APIs are required.

---

# Example Conversation

```text
[ Press Enter to speak ]

You:
What is machine learning?

Agent:
Machine learning is a branch of artificial intelligence that enables computers to learn patterns from data and make predictions without being explicitly programmed.

[ Press Enter to speak ]
```

---

# Troubleshooting

## No Microphone Found

Check available devices:

```python
import sounddevice as sd

print(sd.query_devices())
```

Make sure a microphone is connected and enabled.

---

## GROQ_API_KEY Not Set

Error:

```text
ERROR: GROQ_API_KEY not set in .env.local
```

Solution:

```env
GROQ_API_KEY=your_key_here
```

---

## pyttsx3 Not Speaking

Try:

```bash
pip install pyttsx3
```

Also verify that Windows Speech Services are installed.

---

## Audio Not Recording

Install PortAudio support:

```bash
pip install sounddevice
```

If issues persist:

```bash
pip install pipwin
pipwin install pyaudio
```

---

# Future Improvements

* Voice activity detection (VAD)
* Wake word support
* Streaming responses
* Real-time transcription
* Multi-language support
* GUI version using Streamlit
* Local LLM support via Ollama
* Voice cloning support
* RAG integration
* Tool calling and web search

---

# License

MIT License

---

# Acknowledgements

* [Groq](https://groq.com?utm_source=chatgpt.com)
* [Whisper](https://openai.com/research/whisper?utm_source=chatgpt.com)
* [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/?utm_source=chatgpt.com)
* [SoundDevice](https://python-sounddevice.readthedocs.io/?utm_source=chatgpt.com)
* [NumPy](https://numpy.org/?utm_source=chatgpt.com)

Built with Python, Groq, Whisper, and Windows TTS.
