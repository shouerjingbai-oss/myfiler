"""
Chat Component
"""

import streamlit as st

from agent.agent_executor import create_agent


def render_chat() -> None:

    if "messages" not in st.session_state:

        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    prompt = st.chat_input(
        "Ask something..."
    )

    if prompt is None:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    agent = create_agent()

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = agent.invoke(
                {
                    "input": prompt,
                }
            )

            answer = response["output"]

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )
