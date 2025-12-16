from llm import call_llm

def generate_answer(question, retrieved_chunks):

    if not retrieved_chunks:
        return "Insufficient context to answer the question."

    context = ""

    for chunk in retrieved_chunks:
        MAX_CHARS = 2000

        text = chunk["text"][:MAX_CHARS]
        context += f"\nFILE: {chunk['path']}\n{text}\n"

    prompt = f"""
    You are a Codebase Assistant.
    Use ONLY the provided code below to answer the question.
    Cite file names.
    If the answer is not present, say you cannot answer.

    QUESTION:
    {question}

    CODE:
    {context}
    """

    return call_llm(prompt)