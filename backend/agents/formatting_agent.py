import os
import json
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


class FormattingAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    async def run(self, task: str, summary: str, session_id: str) -> dict:
        """Format the final output into clean structured JSON."""
        system_prompt = (
            "You are an output formatting agent. Format the provided summary into a clean "
            "structured JSON response for enterprise reporting. "
            "Include: executive_summary, key_findings (list), recommendations (list)."
        )
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Task: {task}\n\nSummary:\n{summary}\n\nRespond with valid JSON only.")
        ]
        response = self.llm.invoke(messages)
        try:
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            formatted = json.loads(content)
        except Exception:
            formatted = {
                "executive_summary": response.content,
                "key_findings": [],
                "recommendations": []
            }
        formatted["metadata"] = {
            "session_id": session_id,
            "generated_at": datetime.utcnow().isoformat(),
            "agent": "FormattingAgent"
        }
        return {"output": formatted}
