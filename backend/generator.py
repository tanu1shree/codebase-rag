def generate_answer(question, retrieved_chunks):
    if not retrieved_chunks:
        return "Insufficient context to answer the question."
    
    answer_lines = []
    answer_lines.append(f"Question: {question}")
    answer_lines.append("")
    answer_lines.append("Relevant Code Files:")

    for chunk in retrieved_chunks:
        answer_lines.append(f"- {chunk['path']}")

    answer_lines.append("")
    answer_lines.append("Summary based strictly on retrieved code:")

    for chunk in retrieved_chunks:
        snippet = chunk["text"][:300].replace("\n", " ")
        answer_lines.append(f"[{chunk['path']}] {snippet}...")

    return "\n".join(answer_lines)

if __name__ == "__main__":
    from loader import load_codebase
    from chunker import chunk_files
    from retriever import Retriever
    from planner import Planner

    files = load_codebase(".")
    chunks = chunk_files(files)

    retriever = Retriever(chunks)
    planner = Planner()

    question = "What does this project do?"
    plan = planner.plan(question)

    retrieved = retriever.retrieve(question, top_k = plan["top_k"])
    answer = generate_answer(question, retrieved)

    print(answer)