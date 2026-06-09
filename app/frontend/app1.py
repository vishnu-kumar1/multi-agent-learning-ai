import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

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
    layout="wide"
)

st.title("📘 Multi-Agent Research & Learning Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    # Save uploaded PDF
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded")

    # Load PDF
    docs = load_pdf(uploaded_file.name)

    # Split chunks
    chunks = split_documents(docs)

    # Embeddings
    embeddings = get_embedding_model()

    # Store vectors
    db = store_in_chroma(
        chunks,
        embeddings
    )

    # Retriever
    retriever = get_retriever(db)

    # LLM
    llm = get_llm()

    st.success("Document Processed")

    # User Query
    query = st.text_input(
        "Ask something"
    )

    if query:

        response = handle_query(
            query,
            chunks,
            retriever,
            llm
        )

        st.subheader("AI Response")

        st.write(response)