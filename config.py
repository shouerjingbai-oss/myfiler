"""
Global Configuration
Author: Your Name
"""
from pathlib import Path
from dotenv import load_dotenv
import os
# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------
load_dotenv()
# --------------------------------------------------
# Project Path
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DOC_DIR = DATA_DIR / "docs"
CHROMA_DIR = DATA_DIR / "chroma_db"
CACHE_DIR = DATA_DIR / "cache"
TEMP_DIR = DATA_DIR / "temp"

# --------------------------------------------------
# Create Directories
# --------------------------------------------------

for folder in [
    DATA_DIR,
    DOC_DIR,
    CHROMA_DIR,
    CACHE_DIR,
    TEMP_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# DeepSeek
# --------------------------------------------------

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

DEEPSEEK_BASE_URL = os.getenv(
    "DEEPSEEK_BASE_URL",
    "https://api.deepseek.com"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "deepseek-chat"
)

# --------------------------------------------------
# Embedding
# --------------------------------------------------

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "BAAI/bge-small-zh-v1.5"
)

# --------------------------------------------------
# Chroma
# --------------------------------------------------

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
    str(CHROMA_DIR)
)

# --------------------------------------------------
# Text Splitter
# --------------------------------------------------

CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", 500)
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", 100)
)

TOP_K = int(
    os.getenv("TOP_K", 5)
)

# --------------------------------------------------
# Streamlit
# --------------------------------------------------

APP_TITLE = os.getenv(
    "APP_TITLE",
    "Personal AI Knowledge Assistant"
)
