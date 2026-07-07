"""
PDF Document Loader

Use PyMuPDF to extract text and metadata.
"""
from pathlib import Path
import fitz
from langchain_core.documents import Document
from utils.logger import logger


class PDFLoader:
    """
    PDF loader based on PyMuPDF.
    """

    def load(self, pdf_path: str | Path) -> list[Document]:

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(pdf_path)

        logger.info(f"Loading PDF: {pdf_path.name}")

        pdf = fitz.open(pdf_path)

        documents = []

        for page_index, page in enumerate(pdf):

            text = page.get_text("text").strip()

            if not text:
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path.name,
                        "page": page_index + 1,
                    },
                )
            )

        logger.success(
            f"{len(documents)} pages loaded."
        )

        return documents
