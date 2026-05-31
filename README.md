# 🤡 FunnyBot - AI Chatbot Powered by Gemini

A modern AI chatbot built with **Streamlit**, **Google Gemini 2.5 Flash Lite**, and **LangChain** featuring a custom dark-themed UI, real-time chat interface, conversation history, and modular project architecture.

---

## 🚀 Features

* 🤖 AI-powered conversations using Google Gemini
* 💬 Real-time chat interface
* 🎨 Custom modern dark UI
* ⚡ Fast response generation
* 🧠 Conversation memory using Streamlit Session State
* 🔄 Clear chat functionality
* 📦 Modular code structure
* 🔐 Environment variable support using `.env`
* 📱 Responsive layout

---

## 📂 Project Structure

```text
FunnyBot/
│
├── app.py
├── .env
├── requirements.txt
│
├── chatbot/
│   ├── __init__.py
│   ├── model.py
│   └── chat_logic.py
│
├── ui/
│   ├── __init__.py
│   ├── styles.py
│   ├── header.py
│   └── messages.py
│
└── README.md
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML/CSS
* Custom UI Components

### Backend

* Python
* LangChain

### AI Model

* Google Gemini 2.5 Flash Lite

### Environment Management

* python-dotenv

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/FunnyBot.git

cd FunnyBot
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory.

```env
GOOGLE_API_KEY=your_google_api_key
```

---

### 5. Run Application

```bash
streamlit run app.py
```

---

## 🎯 Usage

1. Launch the application.
2. Type your message in the chat box.
3. Receive AI-generated responses.
4. Type:

```text
0
```

to clear the conversation history.

---

## 📸 Application Workflow

```text
User Message
      │
      ▼
Streamlit UI
      │
      ▼
LangChain
      │
      ▼
Gemini 2.5 Flash Lite
      │
      ▼
AI Response
      │
      ▼
Chat Interface
```

---

## 📦 Requirements

```text
streamlit
python-dotenv
langchain
langchain-core
langchain-google-genai
```

---

## 🔮 Future Improvements

* User Authentication
* Chat History Storage
* Database Integration
* Voice Input
* Voice Output
* Multiple AI Models
* Export Chat as PDF
* Theme Customization
* Streaming Responses
* RAG Integration
* Document Chat Support

---

## 🧑‍💻 Author

Developed as a Generative AI learning project using:

* Python
* Streamlit
* LangChain
* Google Gemini

---

## ⭐ Support

If you found this project useful:

* Star the repository ⭐
* Fork the project 🍴
* Share with fellow developers 🚀

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.
