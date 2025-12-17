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
        "You are a codebase assistant.\n"
        "Answer the question using ONLY the code below.\n"
        "If the answer is not present, say \"Insufficient context.\"\n\n"
        f"QUESTION:\n{question}\n\n"
        f"CODE:\n{context}"
    )

    return call_llm(prompt)