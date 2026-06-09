from app.agents.router_agent import route_query
from app.agents.summary_agent import summarize_document
from app.agents.quiz_agent import generate_quiz
from app.rag.rag_chain import generate_answer


def handle_query(query, chunks, retriever, llm):

    # LLM Router
    agent = route_query(query, llm)

    print(f"\nSelected Agent: {agent}\n")

    # Summary Agent
    if "summary" in agent:
        return summarize_document(chunks, llm)

    # Quiz Agent
    elif "quiz" in agent:
        return generate_quiz(chunks, llm)

    # Default → RAG
    else:
        return generate_answer(
            query,
            retriever,
            llm
        )