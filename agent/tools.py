"""
Agent Tools
"""

from langchain.tools import tool
from langchain.tools import tool

from rag.manager import get_pipeline



@tool
def search_knowledge(query: str) -> str:
    """
    Search relevant information from the knowledge base.
    """

    pipeline = get_pipeline()

    docs = pipeline.search(query)

    if not docs:
        return "知识库中没有找到相关内容。"

    context = []

    for doc in docs:

        source = doc.metadata.get("source", "Unknown")

        page = doc.metadata.get("page", "-")

        context.append(
            f"[来源:{source} 第{page}页]\n{doc.page_content}"
        )

    return "\n\n".join(context)
