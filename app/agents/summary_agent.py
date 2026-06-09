def summarize_document(chunks, llm):

    # Combine ALL chunks
    context = "\n".join(
        [chunk.page_content for chunk in chunks]
    )

    prompt = f"""
You are a professional AI summarization assistant.

Generate:
1. Short Professional Summary
2. Key Points
3. Important Skills
4. Technologies Used

Rules:
- Use bullet points
- Keep concise
- Do NOT hallucinate
- Use ONLY provided context
- Format clearly

Context:
{context}
"""

    response = llm.invoke(prompt)

    return response.content