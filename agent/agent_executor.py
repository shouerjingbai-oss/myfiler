"""
Agent Executor
"""

from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent

from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI

from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    LLM_MODEL,
)

from agent.prompts import SYSTEM_PROMPT
from agent.tools import search_knowledge


def create_agent():

    llm = ChatOpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL,
        model=LLM_MODEL,
        temperature=0.2,
    )

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
