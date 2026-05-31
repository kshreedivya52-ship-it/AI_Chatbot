# ui/messages.py

import streamlit as st


def display_user_message(text):
    st.markdown(
        f"""
        <div class="msg-row user">
            <div class="bubble user">{text}</div>
            <div class="avatar user-av">🧑</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def display_bot_message(text):
    st.markdown(
        f"""
        <div class="msg-row bot">
            <div class="avatar bot-av">🤖</div>
            <div class="bubble bot">{text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_thinking():
    placeholder = st.empty()

    placeholder.markdown(
        """
        <div class="msg-row bot">
            <div class="avatar bot-av">🤖</div>
            <div class="thinking">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                &nbsp;thinking...
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    return placeholder