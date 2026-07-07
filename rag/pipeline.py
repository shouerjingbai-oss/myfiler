"""
RAG Pipeline

Build knowledge base from PDF documents.
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document

from rag.document_loader import PDFLoader
from rag.text_splitter import DocumentSplitter
from rag.vector_store import VectorStore

from utils.logger import logger


class RAGPipeline:
    """
    End-to-end RAG pipeline.

    PDF
        ↓
    Load
        ↓
    Split
        ↓
    Embedding
        ↓
    ChromaDB
    """

    def __init__(self):

        self.loader = PDFLoader()

        self.splitter = DocumentSplitter()

        self.vector_store = VectorStore()

    def build(
        self,
        pdf_path: str | Path,
    ) -> int:
        """
        Build vector database from a PDF.

        Returns
        -------
        int
            Number of generated chunks.
        """

        logger.info("=" * 60)
        logger.info("Building Knowledge Base")

        documents = self.loader.load(pdf_path)

        chunks = self.splitter.split(documents)

        self.vector_store.add_documents(chunks)

        logger.success(
            f"Knowledge Base Created ({len(chunks)} chunks)"
        )

        return len(chunks)

    def load_documents(
        self,
        pdf_path: str | Path,
    ) -> List[Document]:

        return self.loader.load(pdf_path)

    def split_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:

        return self.splitter.split(documents)
