AI Agent Workflow Demo – Multi-Agent Orchestration System

A lightweight multi-agent orchestration system where specialized AI agents collaborate sequentially to complete complex tasks. Built using LangChain, FastAPI, and a React.js dashboard.

Overview

This project demonstrates a multi-agent pipeline in which different AI agents handle specific responsibilities and pass results to the next stage.

Agents
Research Agent
Retrieves structured data using OpenAI function calling.
Summarization Agent
Processes raw data and generates concise summaries.
Formatting Agent
Converts output into structured JSON or readable format.
Features
Sequential multi-agent pipeline
Inter-agent communication using structured data
OpenAI function-calling integration
FastAPI backend with REST APIs
React.js frontend dashboard
Real-time execution tracking
Session-based state management
Architecture
User Input
   ↓
Research Agent
   ↓
Summarization Agent
   ↓
Formatting Agent
   ↓
Final Output
Project Structure
AI-Agent-Workflow-Demo-Multi-Agent-Orchestration-System/

backend/
  main.py
  orchestrator.py
  agents/
    research_agent.py
    summarization_agent.py
    formatting_agent.py
  schemas/
    models.py
  tools/
    crm_tools.py
  session/
    state_manager.py

frontend/
  public/
    index.html
  src/
    App.jsx
    index.js
    components/
    services/
    styles/

requirements.txt
docker-compose.yml
README.md
Getting Started
Prerequisites
Python 3.10+
Node.js 18+
OpenAI API Key
Backend Setup
git clone https://github.com/ItsKumarUdit/AI-Agent-Workflow-Demo-Multi-Agent-Orchestration-System.git
cd AI-Agent-Workflow-Demo-Multi-Agent-Orchestration-System

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# Add your OPENAI_API_KEY in .env

uvicorn backend.main:app --reload --port 8000
Frontend Setup
cd frontend
npm install
npm start

Open: http://localhost:3000

Docker Setup (Optional)
docker-compose up --build
API Endpoints
Method	Endpoint	Description
POST	/api/run	Start a new pipeline task
GET	/api/session/{session_id}	Get session details
GET	/api/sessions	List all sessions
DELETE	/api/session/{session_id}	Delete a session
GET	/health	Health check
Example Request
POST /api/run
{
  "task": "Find top 5 customers by revenue in Q1 2024",
  "session_id": "session_001"
}
Example Response
{
  "session_id": "session_001",
  "status": "completed",
  "steps": [
    {
      "agent": "ResearchAgent",
      "status": "done"
    },
    {
      "agent": "SummarizationAgent",
      "status": "done"
    },
    {
      "agent": "FormattingAgent",
      "status": "done"
    }
  ]
}
Use Cases
CRM data analysis
ERP automation workflows
Multi-step AI pipelines
Business intelligence systems
Tech Stack
Backend: FastAPI
AI Framework: LangChain
LLM: OpenAI (GPT-4 / GPT-3.5)
Frontend: React.js
API: REST
Containerization: Docker
Environment Variables
Backend (.env)
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4
APP_ENV=development
CORS_ORIGINS=http://localhost:3000
Frontend (.env)
REACT_APP_API_URL=http://localhost:8000
License

MIT License

Author

Udit Raj Kumar
https://github.com/ItsKumarUdit
