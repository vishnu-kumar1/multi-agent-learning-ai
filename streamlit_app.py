import sys
import os
import tempfile
 
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
 
import streamlit as st
 
from app.rag.pdf_loader import load_pdf
from app.rag.chunker import split_documents
from app.rag.embeddings import get_embedding_model
from app.rag.vector_store import store_in_chroma
from app.rag.retriever import get_retriever
from app.rag.llm import get_llm
from app.agents.agent_controller import handle_query
 
st.set_page_config(
    page_title="Multi-Agent Learning Assistant",
    page_icon="📘",
    layout="wide"
)
 
st.title("📘 Multi-Agent Research & Learning Assistant")
st.markdown(
    "Upload any PDF and ask questions, request a summary, or generate a quiz — "
    "powered by a **Multi-Agent RAG system** built with LangChain, FAISS, and Groq LLM."
)
 
st.sidebar.header("How to use")
st.sidebar.markdown("""
1. Upload a PDF document
2. Wait for processing
3. Ask a question:
   - **Q&A**: *"What is machine learning?"*
   - **Summary**: *"Summarize this document"*
   - **Quiz**: *"Generate quiz questions"*
""")
 
uploaded_file = st.file_uploader("Upload PDF", type="pdf")
 
if uploaded_file:
    tmp_dir = tempfile.gettempdir()
    tmp_path = os.path.join(tmp_dir, uploaded_file.name)
    with open(tmp_path, "wb") as f:
        f.write(uploaded_file.read())
 
    with st.spinner("Processing document..."):
        docs = load_pdf(tmp_path)
        chunks = split_documents(docs)
        embeddings = get_embedding_model()
        db = store_in_chroma(chunks, embeddings)
        retriever = get_retriever(db)
        llm = get_llm()
 
    st.success(f"Document processed — {len(chunks)} chunks ready")
 
    query = st.text_input("Ask something about your document")
 
    if query:
        with st.spinner("Thinking..."):
            response = handle_query(query, chunks, retriever, llm)
 
        st.subheader("AI Response")
        st.write(response)