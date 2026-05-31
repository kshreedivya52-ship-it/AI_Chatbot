# app.py

from dotenv import load_dotenv
import streamlit as st

from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from UI.styles import load_css
from UI.header import render_header
from UI.messages import (
    display_user_message,
    display_bot_message,
    show_thinking
)

from chatbot.chat_logic import get_response


load_dotenv()

# Page Config
st.set_page_config(
    page_title="FunnyBot",
    page_icon="🤡",
    layout="centered"
)

# Load CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="You are a funny assistant"
        )
    ]

# Header
st.markdown(
    render_header(),
    unsafe_allow_html=True
)

# Show old messages
for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        display_user_message(msg.content)

    elif isinstance(msg, AIMessage):
        display_bot_message(msg.content)

# Chat Input
prompt = st.chat_input(
    "Say something... or type 0 to clear chat"
)

if prompt:

    if prompt.strip() == "0":

        st.session_state.messages = [
            SystemMessage(
                content="You are a funny assistant"
            )
        ]

        st.rerun()

    else:

        display_user_message(prompt)

        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        thinking = show_thinking()

        response = get_response(
            st.session_state.messages
        )

        thinking.empty()

        st.session_state.messages.append(
            AIMessage(content=response)
        )

        display_bot_message(response)