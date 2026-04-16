from datetime import datetime
from typing import Optional, List, Dict
from backend.schemas.models import AgentStep


class SessionStateManager:
    """In-memory session state manager with full step tracking per session."""

    def __init__(self):
        self._sessions: Dict[str, dict] = {}

    def create_session(self, session_id: str, task: str) -> None:
        self._sessions[session_id] = {
            "session_id": session_id,
            "task": task,
            "status": "running",
            "steps": [],
            "created_at": datetime.utcnow().isoformat(),
            "completed_at": None
        }

    def update_step(self, session_id: str, step: AgentStep) -> None:
        if session_id not in self._sessions:
            return
        steps = self._sessions[session_id]["steps"]
        for i, s in enumerate(steps):
            if s.get("agent") == step.agent:
                steps[i] = step.dict()
                return
        steps.append(step.dict())

    def complete_session(self, session_id: str) -> None:
        if session_id in self._sessions:
            self._sessions[session_id]["status"] = "completed"
            self._sessions[session_id]["completed_at"] = datetime.utcnow().isoformat()

    def get_session(self, session_id: str) -> Optional[dict]:
        return self._sessions.get(session_id)

    def list_sessions(self) -> List[dict]:
        return list(self._sessions.values())

    def delete_session(self, session_id: str) -> None:
        self._sessions.pop(session_id, None)
