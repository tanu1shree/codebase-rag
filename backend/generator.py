from llm import call_llm

MAX_CHARS_PER_CHUNK = 400
MAX_TOTAL_CHARS = 3000

def generate_answer(question, retrieved_chunks):
    if not retrieved_chunks:
        return "Insufficient context to answer the question."

    context_parts = []
    total_chars = 0

    for chunk in retrieved_chunks:
        snippet = chunk["text"][:MAX_CHARS_PER_CHUNK]
        part = f"FILE: {chunk['path']}\n{snippet}\n"

        if total_chars + len(part) > MAX_TOTAL_CHARS:
            break

        context_parts.append(part)
        total_chars += len(part)

    context = "\n".join(context_parts)

    prompt = (
        "TASK:\n"
        "Explain what the code below does.\n"
        "Use ONLY the provided code.\n"
        "If the answer is not present, respond with: Insufficient context.\n\n"
        f"QUESTION:\n{question}\n\n"
        f"CODE:\n{context}\n\n"
        "ANSWER:\n"
    )

    return call_llm(prompt)