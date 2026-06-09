from app.rag.pdf_loader import load_pdf
from app.rag.chunker import split_documents
from app.rag.embeddings import get_embedding_model
from app.rag.vector_store import store_in_chroma
from app.rag.retriever import get_retriever
from app.rag.llm import get_llm

from app.agents.agent_controller import handle_query


# Load PDF
docs = load_pdf("sample.pdf")

# Split text
chunks = split_documents(docs)

# Embeddings
embeddings = get_embedding_model()

# Store vectors
db = store_in_chroma(chunks, embeddings)

# Retriever
retriever = get_retriever(db)

# Load LLM
llm = get_llm()

# User query
query = input("Ask something: ")

# Multi-agent response
response = handle_query(
    query,
    chunks,
    retriever,
    llm
)

print("\nAI Response:\n")
print(response)