def generate_answer(query, retriever, llm):

    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not in the context, say:
"I could not find the answer in the document."

DO NOT show reasoning.
DO NOT show thinking steps.
DO NOT use <think> tags.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content