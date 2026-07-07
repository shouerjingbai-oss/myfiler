"""
RAG Pipeline

End-to-end pipeline for building and managing the knowledge base.
"""

from pathlib import Path

from langchain_core.documents import Document

from rag.document_loader import PDFLoader
from rag.text_splitter import DocumentSplitter
from rag.knowledge_base import KnowledgeBase

from utils.logger import logger


class RAGPipeline:
    """
    End-to-end RAG pipeline.

    Workflow:
        PDF
          ↓
      Document Loader
          ↓
      Text Splitter
          ↓
      Knowledge Base
          ↓
      Vector Database
    """

    def __init__(self) -> None:
        """Initialize all RAG components."""

        self.loader = PDFLoader()
        self.splitter = DocumentSplitter()
        self.knowledge_base = KnowledgeBase()

    def build(self, pdf_path: str | Path) -> int:
        """
        Build a knowledge base from a PDF document.

        Parameters
        ----------
        pdf_path : str | Path
            Path to the PDF document.

        Returns
        -------
        int
            Number of generated chunks.
        """

        logger.info("=" * 60)
        logger.info("Start building knowledge base...")

        # 1. Load PDF
        documents = self.loader.load(pdf_path)

        # 2. Split documents
        chunks = self.splitter.split(documents)

        # 3. Store into vector database
        self.knowledge_base.add_documents(chunks)

        logger.success(
            f"Knowledge base created successfully "
            f"({len(chunks)} chunks)"
        )

        return len(chunks)

    def load_documents(
        self,
        pdf_path: str | Path,
    ) -> list[Document]:
        """
        Load PDF without splitting.

        Parameters
        ----------
        pdf_path : str | Path

        Returns
        -------
        list[Document]
        """

        return self.loader.load(pdf_path)

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Split documents into chunks.

        Parameters
        ----------
        documents : list[Document]

        Returns
        -------
        list[Document]
        """

        return self.splitter.split(documents)

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        """
        Search relevant documents.

        Parameters
        ----------
        query : str

        top_k : int

        Returns
        -------
        list[Document]
        """

        return self.knowledge_base.search(
            query=query,
            top_k=top_k,
        )

    def clear(self) -> None:
        """
        Clear the entire knowledge base.
        """

        self.knowledge_base.clear()

        logger.warning("Knowledge base cleared.")

    def size(self) -> int:
        """
        Number of chunks stored in the knowledge base.
        """

        return self.knowledge_base.size()
