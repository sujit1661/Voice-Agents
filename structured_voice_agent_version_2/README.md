# LangGraph Voice Agent (Structured Version 2)

A lightweight conversational AI agent built with LangGraph, LangChain Core, and Groq LLMs. The agent is equipped with two local tools: a system time retriever and a calculator.

## Project Structure

```text
structured_voice_agent_version_2/
├── Tools/
│   └── tools.py         # Custom LangChain tools (get_time, calculator)
├── graphs/
│   └── graph.py         # Agent setup and LangGraph initialization
├── app.py               # Main CLI interface for interacting with the agent
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (API Keys)
```

---

## Getting Started

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory of the project and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## Running the Agent

Start the interactive console chat loop:
```bash
python app.py
```

Inside the CLI, type your questions and press Enter. To exit the loop, type `exit`.

### Example Interactions
```text
You: What is the current time?
Agent: The current time is 09:27:08.

You: What is 12345 * 54321?
Agent: The result of the multiplication is 670592745.

You: exit
```

---

## Tool Definitions

The agent has access to the following tools defined in `Tools/tools.py`:
*   `get_time`: Returns the current system time in `HH:M:S` format.
*   `calculator`: Evaluates simple mathematical expressions passed as a string.
