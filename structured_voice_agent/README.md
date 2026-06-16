# 🎙️ Voice Agent

A simple Voice AI Assistant built with Python, Groq, Whisper, and Text-to-Speech.

This project is part of my journey learning Voice Agents, Conversational AI, Speech-to-Text, LLM Integration, and Production-Grade AI Systems.

**Author:** Sujit Sadalage

## Features

- 🎤 Speech-to-Text
- 🤖 Groq LLM Integration
- 🔊 Text-to-Speech
- 🧠 Conversation Memory
- ⚡ Fast Responses
- 📦 Simple Project Structure
- 🚀 Easy to Extend

## Tech Stack

- Python
- Groq API
- Whisper
- Pyttsx3 / Edge TTS
- Python Dotenv

## Project Structure

```text
voice-agent/
│
├── app.py
├── assistant.py
├── chat_memory.py
├── llm.py
├── speech_to_text.py
├── text_to_speech.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/voice-agent.git

cd voice-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

## Run

```bash
python app.py
```

## How It Works

```text
User Voice
    ↓
Speech To Text
    ↓
Groq LLM
    ↓
Text Response
    ↓
Text To Speech
    ↓
Voice Output
```

## Current Learning Goals

- Basic Voice Assistant
- Memory Management
- Whisper Integration
- Tool Calling
- Streaming Responses
- Real-Time Conversations
- Website Voice Agents
- Production Grade Voice Systems

## Future Improvements

- Wake Word Detection
- Real-Time Streaming
- Deepgram Integration
- ElevenLabs Integration
- Cartesia Integration
- LangGraph Workflows
- RAG Integration
- Multi-Agent Systems
- Web Interface
- LiveKit Integration

## Purpose

This repository is created for learning and experimenting with modern Voice AI systems. The goal is to understand how voice agents work internally and gradually build production-ready conversational AI applications.

## About Me

Hi, I'm **Sujit Sadalage**, a Python Developer passionate about AI, Backend Development, Voice Agents, RAG Systems, Automation, and Full-Stack Web Development.

I'm continuously exploring modern AI technologies and building practical projects to strengthen my skills in:

- Artificial Intelligence
- Voice AI Agents
- Retrieval-Augmented Generation (RAG)
- Python Development
- Backend Engineering
- Web Development
- Automation Solutions

## Connect With Me

- GitHub: https://github.com/Sujit1661
- Portfolio: https://sujit1661.github.io/sujit/

## License

MIT License

Feel free to fork, modify, and use this project for learning purposes.