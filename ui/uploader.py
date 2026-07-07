"""
PDF Uploader
"""

from pathlib import Path
import streamlit as st

from config import DOC_DIR

from rag.pipeline import RAGPipeline


def render_uploader() -> None:

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
    )

    if uploaded_file is None:
        return

    pdf_path = DOC_DIR / uploaded_file.name

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    pipeline = RAGPipeline()

    with st.spinner("Building knowledge base..."):

        pipeline.clear()

        chunks = pipeline.build(pdf_path)

    st.success(
        f"Knowledge base created ({chunks} chunks)"
    )
