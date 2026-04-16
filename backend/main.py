from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.schemas.models import TaskRequest, TaskResponse
from backend.orchestrator import AgentOrchestrator
from backend.session.state_manager import SessionStateManager
import uvicorn
import os

app = FastAPI(
    title="AI Agent Workflow Demo",
    description="Multi-Agent Orchestration System using LangChain and FastAPI",
    version="1.0.0"
)

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state_manager = SessionStateManager()
orchestrator = AgentOrchestrator(state_manager)


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "AI Agent Workflow Demo"}


@app.post("/api/run", response_model=TaskResponse)
async def run_pipeline(request: TaskRequest):
    """Run the full multi-agent pipeline for a given task."""
    result = await orchestrator.run(request.task, request.session_id)
    return result


@app.get("/api/session/{session_id}")
async def get_session(session_id: str):
    """Get the current state of a session."""
    session = state_manager.get_session(session_id)
    if not session:
        return JSONResponse(status_code=404, content={"error": "Session not found"})
    return session


@app.get("/api/sessions")
async def list_sessions():
    """List all active sessions."""
    return {"sessions": state_manager.list_sessions()}


@app.delete("/api/session/{session_id}")
async def delete_session(session_id: str):
    """Clear a session."""
    state_manager.delete_session(session_id)
    return {"message": f"Session {session_id} deleted"}


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
