import uuid
from datetime import datetime
from backend.agents.research_agent import ResearchAgent
from backend.agents.summarization_agent import SummarizationAgent
from backend.agents.formatting_agent import FormattingAgent
from backend.session.state_manager import SessionStateManager
from backend.schemas.models import TaskResponse, AgentStep


class AgentOrchestrator:
    def __init__(self, state_manager: SessionStateManager):
        self.state_manager = state_manager
        self.research_agent = ResearchAgent()
        self.summarization_agent = SummarizationAgent()
        self.formatting_agent = FormattingAgent()

    async def run(self, task: str, session_id: str = None) -> TaskResponse:
        if not session_id:
            session_id = str(uuid.uuid4())

        steps = []
        self.state_manager.create_session(session_id, task)

        # Step 1: Research Agent
        research_output = await self.research_agent.run(task)
        research_step = AgentStep(
            agent="ResearchAgent",
            status="done",
            output=research_output["output"],
            tool_calls=research_output.get("tool_calls", []),
            started_at=datetime.utcnow().isoformat(),
            completed_at=datetime.utcnow().isoformat()
        )
        steps.append(research_step)

        # Step 2: Summarization Agent
        summary_output = await self.summarization_agent.run(
            task=task, research_data=research_output["output"]
        )
        summary_step = AgentStep(
            agent="SummarizationAgent",
            status="done",
            output=summary_output["output"],
            started_at=datetime.utcnow().isoformat(),
            completed_at=datetime.utcnow().isoformat()
        )
        steps.append(summary_step)

        # Step 3: Formatting Agent
        format_output = await self.formatting_agent.run(
            task=task, summary=summary_output["output"], session_id=session_id
        )
        format_step = AgentStep(
            agent="FormattingAgent",
            status="done",
            output=format_output["output"],
            started_at=datetime.utcnow().isoformat(),
            completed_at=datetime.utcnow().isoformat()
        )
        steps.append(format_step)
        self.state_manager.complete_session(session_id)

        return TaskResponse(
            session_id=session_id,
            status="completed",
            steps=steps,
            final_output=format_output["output"]
        )
