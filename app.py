"""
Application Entry
"""

import streamlit as st

from config import (
    APP_TITLE,
    init_project,
)

from ui.sidebar import render_sidebar
from ui.uploader import render_uploader
from ui.chatbot import render_chat
from ui.citation import render_citation


def main():

    init_project()

    st.set_page_config(
        page_title=APP_TITLE,
        layout="wide",
    )

    render_sidebar()

    st.title(APP_TITLE)

    render_uploader()

    st.divider()

    render_chat()

    render_citation()


if __name__ == "__main__":

    main()
