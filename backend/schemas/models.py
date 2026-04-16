from pydantic import BaseModel, Field
from typing import Optional, List, Any
from datetime import datetime
import uuid


class TaskRequest(BaseModel):
    task: str = Field(..., description="The enterprise task to process")
    session_id: Optional[str] = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Session ID for tracking"
    )


class AgentStep(BaseModel):
    agent: str
    status: str
    output: Optional[Any] = None
    tool_calls: Optional[List[str]] = []
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


class TaskResponse(BaseModel):
    session_id: str
    status: str
    steps: List[AgentStep] = []
    final_output: Optional[Any] = None
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class SessionState(BaseModel):
    session_id: str
    task: str
    status: str = "running"
    steps: List[AgentStep] = []
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    completed_at: Optional[str] = None
