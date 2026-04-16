# 🤖 AI Agent Workflow Demo – Multi-Agent Orchestration System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green?style=flat-square&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-yellow?style=flat-square)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react)
![OpenAI](https://img.shields.io/badge/OpenAI-Function--Calling-412991?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

A **lightweight multi-agent orchestration system** where specialized AI agents collaborate sequentially to complete complex enterprise-style tasks. Built with **LangChain**, **FastAPI**, and a **React.js** real-time dashboard.

---

## 🧠 Overview

This project simulates an enterprise-grade agentic pipeline where three specialized agents hand off context to each other:

| Agent | Role |
|---|---|
| 🔍 **Research Agent** | Queries structured data sources (CRM/ERP-style) using OpenAI function-calling |
| 📝 **Summarization Agent** | Condenses raw research output into structured summaries |
| 📤 **Output Formatting Agent** | Formats the final response into clean JSON or markdown for downstream use |

---

## ✨ Features

- ✅ Sequential multi-agent pipeline with full **state tracking per session**
- ✅ **Inter-agent communication** via structured JSON tool calls and prompt chaining
- ✅ **OpenAI function-calling API** for structured tool-use by agents
- ✅ **FastAPI** backend exposing RESTful agent pipeline endpoints
- ✅ **React.js dashboard** with real-time step-by-step execution visibility
- ✅ Live monitoring of agent decisions and intermediate outputs
- ✅ Enterprise automation simulation (CRM/ERP query workflows)
- ✅ Session-level context management and handoff tracking

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    React.js Dashboard                   │
│         (Real-time agent step visibility)               │
└────────────────────────┬────────────────────────────────┘
                         │ HTTP / WebSocket
┌────────────────────────▼────────────────────────────────┐
│                  FastAPI Backend                        │
│              (Agent Pipeline Router)                    │
└──────────┬─────────────┬──────────────┬────────────────┘
           │             │              │
    ┌──────▼──────┐ ┌───▼──────┐ ┌────▼──────────┐
    │  Research   │ │ Summary  │ │    Output     │
    │   Agent     │→│  Agent   │→│  Formatter    │
    │(LangChain + │ │(LangChain│ │   Agent       │
    │  OpenAI FC) │ │  Chain)  │ │  (JSON/MD)    │
    └─────────────┘ └──────────┘ └───────────────┘
           │
    ┌──────▼──────┐
    │  OpenAI     │
    │  Function   │
    │  Calling    │
    └─────────────┘
```

---

## 📁 Project Structure

```
AI-Agent-Workflow-Demo-Multi-Agent-Orchestration-System/
│
├── backend/
│   ├── main.py                    # FastAPI app entry point
│   ├── orchestrator.py            # Agent pipeline orchestrator
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── research_agent.py      # Research agent with OpenAI function-calling
│   │   ├── summarization_agent.py # Summarization agent
│   │   └── formatting_agent.py    # Output formatting agent
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── models.py              # Pydantic request/response models
│   ├── tools/
│   │   ├── __init__.py
│   │   └── crm_tools.py           # Simulated CRM/ERP tool definitions
│   └── session/
│       ├── __init__.py
│       └── state_manager.py       # Per-session state tracking
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx                # Root component
│   │   ├── index.js
│   │   ├── components/
│   │   │   ├── AgentPipeline.jsx  # Pipeline visualization
│   │   │   ├── AgentStep.jsx      # Individual agent step card
│   │   │   ├── TaskInput.jsx      # Task submission form
│   │   │   └── OutputPanel.jsx    # Final output display
│   │   ├── services/
│   │   │   └── api.js             # API service layer
│   │   └── styles/
│   │       └── App.css
│   ├── package.json
│   └── .env.example
│
├── requirements.txt
├── .gitignore
├── .env.example
├── docker-compose.yml
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- OpenAI API Key

### Backend Setup

```bash
# Clone the repo
git clone https://github.com/ItsKumarUdit/AI-Agent-Workflow-Demo-Multi-Agent-Orchestration-System.git
cd AI-Agent-Workflow-Demo-Multi-Agent-Orchestration-System

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your OPENAI_API_KEY to .env

# Run the FastAPI server
uvicorn backend.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
# Visit http://localhost:3000
```

### Docker (Optional)

```bash
docker-compose up --build
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/run` | Start a new agent pipeline task |
| `GET` | `/api/session/{session_id}` | Get session state and step outputs |
| `GET` | `/api/sessions` | List all active sessions |
| `DELETE` | `/api/session/{session_id}` | Clear a session |
| `GET` | `/health` | Health check |

### Example Request

```json
POST /api/run
{
  "task": "Find top 5 customers by revenue in Q1 2024 and summarize their purchase patterns",
  "session_id": "session_001"
}
```

### Example Response

```json
{
  "session_id": "session_001",
  "status": "completed",
  "steps": [
    {
      "agent": "ResearchAgent",
      "status": "done",
      "output": { "customers": [...] },
      "tool_calls": ["query_crm_revenue"]
    },
    {
      "agent": "SummarizationAgent",
      "status": "done",
      "output": "Top customers are..."
    },
    {
      "agent": "FormattingAgent",
      "status": "done",
      "output": { "formatted": "..." }
    }
  ],
  "final_output": { ... }
}
```

---

## 🧩 Agent Details

### 🔍 Research Agent
- Uses **OpenAI function-calling** to invoke simulated CRM/ERP tools
- Tools: `query_crm_revenue`, `query_erp_inventory`, `get_customer_profile`
- Returns structured JSON data for downstream agents

### 📝 Summarization Agent
- Receives research output via **prompt chaining**
- Uses LangChain `LLMChain` with a summarization prompt template
- Produces concise, structured summaries

### 📤 Output Formatting Agent
- Final stage of the pipeline
- Formats data into clean JSON or Markdown
- Adds metadata: timestamps, session ID, confidence scores

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend Framework | FastAPI |
| Agent Framework | LangChain |
| LLM Provider | OpenAI (GPT-4 / GPT-3.5) |
| Function Calling | OpenAI Function-Calling API |
| State Management | In-memory session store |
| Frontend | React.js 18 |
| Styling | CSS Modules / Tailwind |
| API Communication | Axios + REST |
| Containerization | Docker + Docker Compose |

---

## 🖥️ Dashboard Preview

The React dashboard provides:
- **Task input form** to submit enterprise queries
- **Live agent step cards** showing each agent's status (pending → running → done)
- **Intermediate output viewer** for each agent step
- **Final output panel** with formatted results
- **Session history** sidebar

---

## 📝 Environment Variables

```env
# Backend .env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4
APP_ENV=development
CORS_ORIGINS=http://localhost:3000

# Frontend .env
REACT_APP_API_URL=http://localhost:8000
```

---

## 🤝 Use Cases

- Enterprise CRM data querying and summarization
- Automated ERP report generation
- Multi-step research pipelines
- AI-powered business intelligence workflows

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Udit Raj Kumar** – [@ItsKumarUdit](https://github.com/ItsKumarUdit)
