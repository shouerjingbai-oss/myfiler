"""
Sidebar Component
"""

import streamlit as st

from config import APP_TITLE

from rag.manager import get_pipeline

pipeline = get_pipeline()


def render_sidebar() -> None:
    """
    Render sidebar.
    """

    pipeline = get_pipeline()

    with st.sidebar:

        st.title(APP_TITLE)

        st.divider()

        st.subheader("Knowledge Base")

        st.metric(
            label="Chunks",
            value=pipeline.size(),
        )

        st.divider()

        st.caption(
            "Powered by LangChain + ChromaDB + DeepSeek"
        )
