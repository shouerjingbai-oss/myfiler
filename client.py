"""
LLM Client

Unified LangChain Chat Model
"""

from functools import lru_cache

from langchain_openai import ChatOpenAI

from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    LLM_MODEL,
)

from utils.logger import logger


@lru_cache(maxsize=1)
def get_llm() -> ChatOpenAI:
    """
    Load ChatOpenAI client only once.
    """

    logger.info("Initializing DeepSeek Chat Model...")

    llm = ChatOpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL,
        model=LLM_MODEL,
        temperature=0.2,
    )

    logger.success("DeepSeek Chat Model Ready.")

    return llm
