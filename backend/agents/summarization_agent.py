import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json


class SummarizationAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            temperature=0.3,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        self.prompt = PromptTemplate(
            input_variables=["task", "research_data"],
            template=(
                "You are a summarization agent. Given the original task and research data,"
                " produce a concise, structured summary highlighting key findings.\n\n"
                "Original Task: {task}\n\nResearch Data: {research_data}\n\nSummary:"
            )
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    async def run(self, task: str, research_data) -> dict:
        """Summarize research output into structured insights."""
        research_str = json.dumps(research_data, indent=2) if isinstance(research_data, dict) else str(research_data)
        result = await self.chain.arun(task=task, research_data=research_str)
        return {"output": result}
