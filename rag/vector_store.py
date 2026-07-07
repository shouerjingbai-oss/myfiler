"""
Chroma Vector Store
"""

from pathlib import Path
from langchain_chroma import Chroma
from config import CHROMA_DIR
from models.embedding import get_embedding_model
from utils.logger import logger


class VectorStore:

    def __init__(self):

        self.embedding = get_embedding_model()

        self.vector_db = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=self.embedding,
        )

    def add_documents(
        self,
        documents,
    ):

        logger.info(
            f"Adding {len(documents)} chunks..."
        )

        self.vector_db.add_documents(
            documents
        )

        logger.success(
            "Vector database updated."
        )

    def as_retriever(
        self,
        k: int = 5,
    ):

        return self.vector_db.as_retriever(
            search_kwargs={
                "k": k,
            }
        )

    def count(self):

        return self.vector_db._collection.count()
