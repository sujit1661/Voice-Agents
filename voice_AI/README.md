# Groq Voice Agent

A real-time voice assistant + text chat CLI built with **LiveKit Agents 1.5** and **Groq AI**.

## Stack

| Layer | Provider | Model |
|-------|----------|-------|
| STT   | Groq Whisper | `whisper-large-v3` |
| LLM   | Groq Llama  | `llama-3.3-70b-versatile` |
| TTS   | Groq PlayAI | `playai-tts` |
| VAD   | Silero      | built-in |

---

## Quick start

### 1. Fill in `.env.local`

```
LIVEKIT_URL=wss://your-project.livekit.cloud   # only needed for voice mode
LIVEKIT_API_KEY=your_livekit_api_key           # only needed for voice mode
LIVEKIT_API_SECRET=your_livekit_api_secret     # only needed for voice mode
GROQ_API_KEY=your_groq_api_key                 # required for all modes
```

- Groq key (free): https://console.groq.com/keys
- LiveKit Cloud (free): https://cloud.livekit.io

### 2. Install

```cmd
uv sync
```

### 3. Pick your interface

---

## Interface options

### Option A — Text chat in CMD (no mic, no LiveKit needed)

Just type and chat. Responses stream token-by-token.

```cmd
python src/chat.py
```

Options:
```cmd
python src/chat.py --model llama-3.1-8b-instant
python src/chat.py --system "You are a Python tutor."
```

In-chat commands:
```
/clear          clear conversation history
/model <name>   switch model on the fly
/help           show help
/exit           quit
```

---

### Option B — Voice in terminal (mic + speakers, no browser)

Talk to the agent using your microphone. Audio plays back through your speakers.
No LiveKit Cloud account needed for this mode.

```cmd
uv run python -m livekit.agents download-files
python src/agent.py console
```

Press `Ctrl+C` to stop.

---

### Option C — Voice via browser (LiveKit Cloud)

Connect the agent to LiveKit Cloud and talk through the Agent Console web UI.

```cmd
python src/agent.py dev
```

Then open https://cloud.livekit.io → your project → **Agents** → **Start a session**.

---

## Model options

| Model | Speed | Best for |
|-------|-------|----------|
| `llama-3.3-70b-versatile` | fast | default, most capable |
| `llama-3.1-8b-instant` | fastest | quick answers, lower cost |
| `llama3-70b-8192` | fast | long conversations |
| `gemma2-9b-it` | fast | lightweight alternative |

STT alternatives:
- `whisper-large-v3-turbo` — faster, slightly less accurate
- `distil-whisper-large-v3-en` — English only, cheapest

---

## Project structure

```
.
├── src/
│   ├── agent.py    — LiveKit voice agent (console / dev / start modes)
│   └── chat.py     — Standalone text chat CLI (Groq only, no LiveKit)
├── .env.local      — API keys (never commit this)
├── pyproject.toml  — Dependencies
└── README.md
```
