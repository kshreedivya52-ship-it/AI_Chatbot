from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FunnyBot",
    page_icon="🤡",
    layout="centered",
)

# ─── CSS Styling ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&display=swap');

/* ── Root Variables ── */
:root {
    --bg:        #0a0a0f;
    --surface:   #111118;
    --border:    #2a2a3a;
    --accent:    #f0e040;
    --accent2:   #ff6b35;
    --text:      #e8e8f0;
    --muted:     #6b6b80;
    --user-bg:   #1e1e2e;
    --bot-bg:    #16161f;
    --radius:    16px;
}

/* ── Global Reset ── */
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Mono', monospace !important;
}

[data-testid="stApp"] {
    background: var(--bg) !important;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"] { display: none !important; }

/* ── Main container ── */
[data-testid="stAppViewContainer"] > .main {
    padding: 0 !important;
}
.block-container {
    max-width: 780px !important;
    padding: 0 1.5rem 6rem 1.5rem !important;
    margin: 0 auto !important;
}

/* ── Header ── */
.chat-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: linear-gradient(180deg, #0a0a0f 80%, transparent);
    padding: 2rem 0 1.2rem;
    text-align: center;
}
.chat-header h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.03em;
    margin: 0 !important;
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.chat-header p {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: var(--muted);
    margin: 0.3rem 0 0 !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
.status-dot {
    display: inline-block;
    width: 7px; height: 7px;
    background: #4ade80;
    border-radius: 50%;
    margin-right: 6px;
    animation: pulse 2s ease-in-out infinite;
    vertical-align: middle;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.5; transform: scale(0.8); }
}

/* ── Message bubbles ── */
.msg-row {
    display: flex;
    margin: 0.9rem 0;
    animation: slideIn 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
@keyframes slideIn {
    from { opacity: 0; transform: translateY(12px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}
.msg-row.user  { justify-content: flex-end; }
.msg-row.bot   { justify-content: flex-start; }

.avatar {
    width: 34px; height: 34px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
    margin-top: 2px;
}
.avatar.bot-av  {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent2) 100%);
    margin-right: 10px;
}
.avatar.user-av {
    background: var(--user-bg);
    border: 1px solid var(--border);
    margin-left: 10px;
}

.bubble {
    max-width: 72%;
    padding: 0.75rem 1.1rem;
    border-radius: var(--radius);
    font-size: 0.88rem;
    line-height: 1.65;
    word-break: break-word;
}
.bubble.user {
    background: var(--user-bg);
    border: 1px solid var(--border);
    border-bottom-right-radius: 4px;
    color: var(--text);
}
.bubble.bot {
    background: var(--bot-bg);
    border: 1px solid var(--border);
    border-bottom-left-radius: 4px;
    color: var(--text);
}
.bubble.bot strong { color: var(--accent); }

/* ── Divider ── */
.chat-divider {
    text-align: center;
    margin: 1.5rem 0;
    position: relative;
}
.chat-divider::before {
    content: '';
    position: absolute;
    top: 50%; left: 0; right: 0;
    height: 1px;
    background: var(--border);
}
.chat-divider span {
    position: relative;
    background: var(--bg);
    padding: 0 10px;
    font-size: 0.65rem;
    color: var(--muted);
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

/* ── Thinking indicator ── */
.thinking {
    display: flex; align-items: center;
    gap: 5px;
    padding: 0.6rem 1rem;
    color: var(--muted);
    font-size: 0.78rem;
    letter-spacing: 0.05em;
}
.thinking-dot {
    width: 6px; height: 6px;
    background: var(--accent);
    border-radius: 50%;
    animation: bounce 1.2s ease-in-out infinite;
}
.thinking-dot:nth-child(2) { animation-delay: 0.2s; }
.thinking-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce {
    0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
    40%            { transform: translateY(-6px); opacity: 1; }
}

/* ── Input area ── */
[data-testid="stChatInputContainer"] {
    position: fixed !important;
    bottom: 0 !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 100% !important;
    max-width: 780px !important;
    padding: 1rem 1.5rem 1.4rem !important;
    background: linear-gradient(0deg, #0a0a0f 70%, transparent) !important;
    border: none !important;
    z-index: 999 !important;
}

[data-testid="stChatInput"] {
    background: var(--surface) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 14px !important;
    color: var(--text) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
    transition: border-color 0.2s ease !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(240,224,64,0.08) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ─── Init Session State ─────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny assistant")
    ]

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-header">
    <h1>🤡 FunnyBot</h1>
    <p><span class="status-dot"></span>gemini-2.5-flash-lite · ready to roast</p>
</div>
<div class="chat-divider"><span>conversation start</span></div>
""", unsafe_allow_html=True)

# ─── Render existing chat history ──────────────────────────────────────────────
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.markdown(f"""
        <div class="msg-row user">
            <div class="bubble user">{msg.content}</div>
            <div class="avatar user-av">🧑</div>
        </div>
        """, unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f"""
        <div class="msg-row bot">
            <div class="avatar bot-av">🤖</div>
            <div class="bubble bot">{msg.content}</div>
        </div>
        """, unsafe_allow_html=True)

# ─── Chat Input ─────────────────────────────────────────────────────────────────
prompt = st.chat_input("Say something... or type 0 to clear chat")

if prompt:
    if prompt.strip() == "0":
        st.session_state.messages = [
            SystemMessage(content="You are a funny assistant")
        ]
        st.rerun()
    else:
        # Show user message
        st.markdown(f"""
        <div class="msg-row user">
            <div class="bubble user">{prompt}</div>
            <div class="avatar user-av">🧑</div>
        </div>
        """, unsafe_allow_html=True)

        st.session_state.messages.append(HumanMessage(content=prompt))

        # Thinking indicator
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("""
        <div class="msg-row bot">
            <div class="avatar bot-av">🤖</div>
            <div class="thinking">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                &nbsp;thinking...
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Call Gemini
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.9)
        response = model.invoke(st.session_state.messages)

        thinking_placeholder.empty()

        st.session_state.messages.append(AIMessage(content=response.content))

        # Show bot response
        st.markdown(f"""
        <div class="msg-row bot">
            <div class="avatar bot-av">🤖</div>
            <div class="bubble bot">{response.content}</div>
        </div>
        """, unsafe_allow_html=True)