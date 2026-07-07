"""
DeepSeek Client
"""

from functools import lru_cache

from openai import OpenAI

from config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    LLM_MODEL,
)

from utils.logger import logger


@lru_cache(maxsize=1)
def get_llm() -> OpenAI:
    """
    Create DeepSeek client.
    """

    logger.info("Initializing DeepSeek client...")

    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL,
    )

    logger.success("DeepSeek client initialized.")

    return client


def chat(
    prompt: str,
    temperature: float = 0.2,
) -> str:
    """
    Chat with DeepSeek.
    """

    client = get_llm()

    response = client.chat.completions.create(
        model=LLM_MODEL,
        temperature=temperature,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content
