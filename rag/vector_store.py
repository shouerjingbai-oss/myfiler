"""
Vector Store Manager

Only responsible for ChromaDB operations.
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_chroma import Chroma

from config import CHROMA_DIR
from models.embedding import get_embedding_model
from utils.logger import logger


class VectorStore:
    """
    ChromaDB manager.
    """

    def __init__(self):

        self.embedding = get_embedding_model()

        self.db = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=self.embedding,
        )

    def add_documents(
        self,
        documents: List[Document],
    ) -> None:

        logger.info(
            f"Adding {len(documents)} chunks..."
        )

        self.db.add_documents(documents)

        logger.success("Knowledge base updated.")

    def similarity_search(
        self,
        query: str,
        k: int = 5,
    ) -> List[Document]:

        return self.db.similarity_search(
            query=query,
            k=k,
        )

    def as_retriever(
        self,
        k: int = 5,
    ):

        return self.db.as_retriever(
            search_kwargs={
                "k": k,
            }
        )

    def count(self) -> int:

        return self.db._collection.count()

    def clear(self):

        self.db.reset_collection()

    def is_empty(self):

        return self.count() == 0
