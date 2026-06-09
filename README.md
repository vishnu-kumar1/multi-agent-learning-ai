# 📘 Multi-Agent Research & Learning Assistant

An AI-powered document assistant that uses a **Multi-Agent RAG architecture** to answer questions, summarize documents, and generate quizzes from any uploaded PDF.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

---

## 🚀 Features

- **Smart Router Agent** — Automatically detects query intent (Q&A / Summary / Quiz)
- **RAG Agent** — Answers factual questions using semantic vector search
- **Summary Agent** — Generates structured summaries with key points and skills
- **Quiz Agent** — Creates 5 interview-style questions with answers from the document
- **PDF Upload** — Works with any PDF document in real time

---

## 🏗️ Architecture

```
User Query
    ↓
Router Agent (LLM-based intent classification)
    ↓
┌───────────┬─────────────┬────────────┐
│ RAG Agent │Summary Agent│ Quiz Agent │
└───────────┴─────────────┴────────────┘
    ↓
ChromaDB (Vector Store) ← PDF → Chunker → Embeddings
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Groq (fast inference) |
| Embeddings | Sentence Transformers (HuggingFace) |
| Vector Store | ChromaDB |
| Framework | LangChain + LangGraph |
| Frontend | Streamlit |
| PDF Parsing | PyPDF |

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-learning-ai.git
cd multi-agent-learning-ai
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
# Get free key at: https://console.groq.com
```

### 5. Run the app
```bash
streamlit run streamlit_app.py
```

---

## 🌐 Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set **Main file**: `streamlit_app.py`
5. Add secret: `GROQ_API_KEY = your_key_here`
6. Click Deploy!

---

## 📁 Project Structure

```
multi-agent-learning-ai/
├── streamlit_app.py          # Main entry point
├── requirements.txt
├── .env.example
├── app/
│   ├── agents/
│   │   ├── agent_controller.py   # Routes to correct agent
│   │   ├── router_agent.py       # LLM-based intent classifier
│   │   ├── summary_agent.py      # Document summarization
│   │   └── quiz_agent.py         # Quiz/MCQ generation
│   ├── rag/
│   │   ├── pdf_loader.py         # PDF ingestion
│   │   ├── chunker.py            # Text splitting
│   │   ├── embeddings.py         # HuggingFace embeddings
│   │   ├── vector_store.py       # ChromaDB storage
│   │   ├── retriever.py          # Semantic retrieval
│   │   ├── rag_chain.py          # RAG pipeline
│   │   └── llm.py                # Groq LLM setup
│   └── frontend/
│       └── app1.py               # Original frontend
└── README.md
```

---

## 👨‍💻 Author

**Vishnu Kumar** — AI/ML Engineer  
📧 vishikumar193@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/vishnu-kumar123)  
💻 [GitHub](https://github.com/YOUR_USERNAME)

---

## 📄 License

MIT License — feel free to use and modify.
