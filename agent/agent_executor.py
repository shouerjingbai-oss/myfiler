"""
Agent Executor
"""

from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent

from langchain_core.prompts import ChatPromptTemplate
from llm.client import get_llm




from agent.prompts import SYSTEM_PROMPT
from agent.tools import search_knowledge


def create_agent():

    llm = get_llm()
    

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                SYSTEM_PROMPT,
            ),
            (
                "human",
                "{input}",
            ),
            (
                "placeholder",
                "{agent_scratchpad}",
            ),
        ]
    )

    tools = [
        search_knowledge,
    ]

    agent = create_tool_calling_agent(
        llm,
        tools,
        prompt,
    )

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )
