# chatbot/chat_logic.py

from chatbot.model import load_model


def get_response(messages):
    model = load_model()
    response = model.invoke(messages)

    return response.content