from langchain_chroma import Chroma

def store_in_chroma(chunks, embeddings):

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )
    return vector_db