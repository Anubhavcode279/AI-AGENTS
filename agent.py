import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Learning Architect", page_icon="🎓", layout="wide")

# Custom CSS for a high-end look
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    .stChatInput { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: Settings & Controls ---
with st.sidebar:
    st.title("🛠️ Agent Settings")
    model_choice = st.selectbox("Choose Brain:", ["qwen2.5:7b", "llama3:8b"], index=0)
    st.info("This agent runs 100% locally on your Mac.")
    if st.button("🗑️ Clear Conversation"):
        st.session_state.chat_history = []
        st.rerun()

st.title("🎓 Personalized Learning Path Agent")
st.caption("Tell me what you want to learn, and I'll architect a week-by-week plan for you.")

# --- INITIALIZE MEMORY ---
# Streamlit reruns the script on every click. We use session_state to persist data.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a brilliant technical mentor. Provide structured learning paths with hands-on projects.")
    ]

# --- DISPLAY CHAT HISTORY ---
# This shows previous messages in the UI
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# --- CHAT INPUT & RESPONSE ---
if user_input := st.chat_input("Ask me to design a course (e.g., 'Learn Snowflake in 4 weeks')"):
    
    # 1. Show user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # 2. Add to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # 3. Generate AI Response
    with st.chat_message("assistant"):
        # Placeholder for streaming effect
        response_placeholder = st.empty()
        full_response = ""
        
        # Initialize LangChain LLM
        llm = ChatOllama(model=model_choice, temperature=0.7)
        
        # Streaming loop
        for chunk in llm.stream(st.session_state.chat_history):
            full_response += chunk.content
            response_placeholder.markdown(full_response + "▌") # Cursor effect
        
        response_placeholder.markdown(full_response)
    
    # 4. Save AI response to history
    st.session_state.chat_history.append(AIMessage(content=full_response))