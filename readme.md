# 🎓 Personalized AI Learning Path Agent
An interactive, local-first AI mentor built with **LangChain**, **Ollama (Qwen2.5)**, and **Streamlit**.

## 🚀 Features
- **100% Local:** Runs on your Mac using Ollama.
- **Persistent Memory:** Remembers your learning goals during the session.
- **Structured Output:** Generates week-by-week project-based curriculums.
- **Streaming UI:** Real-time response generation.

## 🛠️ Tech Stack
- **Engine:** Ollama (Model: qwen2.5:7b)
- **Framework:** LangChain
- **UI:** Streamlit
- **Environment:** Apple Silicon (M-series) Optimized

## 📦 Installation
1. Install [Ollama](https://ollama.com) and run `ollama pull qwen2.5:7b`.
2. Clone this repo: `git clone <your-repo-url>`
3. Create venv: `python3 -m venv venv && source venv/bin/activate`
4. Install deps: `pip install -r requirements.txt`
5. Run: `streamlit run app.py`
