# chatbot/model.py

from langchain_google_genai import ChatGoogleGenerativeAI


def load_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.9
    )