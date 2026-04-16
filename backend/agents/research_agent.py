import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from backend.tools.crm_tools import get_crm_tools


class ResearchAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        self.tools = get_crm_tools()
        self.tool_map = {t["name"]: t for t in self.tools}

    async def run(self, task: str) -> dict:
        """Research agent uses OpenAI function-calling to query CRM/ERP tools."""
        system_prompt = (
            "You are a research agent for enterprise CRM/ERP systems. "
            "Use the available tools to gather relevant data for the given task."
        )
        openai_tools = [
            {"type": "function", "function": {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["parameters"]
            }} for t in self.tools
        ]
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Task: {task}")
        ]
        response = self.llm.invoke(messages, tools=openai_tools, tool_choice="auto")
        tool_calls_made = []
        research_data = {}
        if response.tool_calls:
            for tool_call in response.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                tool_calls_made.append(tool_name)
                if tool_name in self.tool_map:
                    result = self.tool_map[tool_name]["function"](**tool_args)
                    research_data[tool_name] = result
        return {
            "output": research_data if research_data else {"raw": response.content},
            "tool_calls": tool_calls_made
        }
