def generate_quiz(chunks, llm):

    # Combine all chunks
    context = "\n".join(
        [chunk.page_content for chunk in chunks]
    )

    prompt = f"""
You are an expert AI quiz generator.

Generate:
- 5 interview questions
- Include answers
- Questions should be based ONLY on the provided context

Rules:
- Keep questions clear
- Avoid hallucinations
- Use concise answers
- Format properly

Context:
{context}
"""

    response = llm.invoke(prompt)

    return response.content