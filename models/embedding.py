"""
Embedding Model

Load BAAI/bge-small-zh-v1.5
"""

from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL
from utils.logger import logger


@lru_cache(maxsize=1)
def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Load embedding model only once.
    """
    logger.info(
        f"Loading embedding model: {EMBEDDING_MODEL}"
    )

    embedding = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={
            "device": "cpu",
        },
        encode_kwargs={
            "normalize_embeddings": True,
        },
    )

    logger.success("Embedding model loaded.")

    return embedding
