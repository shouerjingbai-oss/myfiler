"""
Document Splitter
"""
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
)


class DocumentSplitter:
    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                "。",
                "！",
                "？",
                "；",
                "，",
            ],
        )

    def split(
        self,
        documents: list[Document],
    ) -> list[Document]:

        return self.splitter.split_documents(
            documents
        )
