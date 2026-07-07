"""
Knowledge Base

High-level interface for vector retrieval.
"""

from typing import List

from langchain_core.documents import Document

from rag.vector_store import VectorStore


class KnowledgeBase:

    def __init__(self):

        self.store = VectorStore()

    def add_documents(
        self,
        documents: List[Document],
    ):

        self.store.add_documents(documents)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Document]:

        return self.store.similarity_search(
            query=query,
            k=top_k,
        )

    def get_retriever(
        self,
        top_k: int = 5,
    ):

        return self.store.as_retriever(
            k=top_k,
        )

    def clear(self):

        self.store.clear()

    def size(self) -> int:

        return self.store.count()
