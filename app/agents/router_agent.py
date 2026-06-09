def route_query(query, llm):

    prompt = f"""
You are an AI Router Agent.

Your task:
Classify the user query into EXACTLY ONE category.

Available categories:

1. rag
Use for:
- factual questions
- asking information
- document Q&A
- explanations

Examples:
- What is machine learning?
- Who is the candidate?
- What skills are mentioned?
- Explain RAG

2. summary
Use for:
- summarization
- notes generation
- concise overview

Examples:
- Summarize this document
- Give short notes
- Create overview

3. quiz
Use for:
- MCQs
- interview questions
- assessments
- quizzes

Examples:
- Generate quiz
- Create MCQs
- Interview questions

IMPORTANT:
Return ONLY ONE WORD:
rag
summary
quiz

User Query:
{query}
"""

    response = llm.invoke(prompt)

    agent = response.content.strip().lower()

    # STRICT CLEANING
    if agent == "summary":
        return "summary"

    elif agent == "quiz":
        return "quiz"

    else:
        return "rag"