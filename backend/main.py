from loader import load_codebase
from chunker import chunk_files
from retriever import Retriever
from planner import Planner
from generator import generate_answer

if __name__ == "__main__":
    repo_path = "."
    question = "What does this project do?"

    files = load_codebase(repo_path)
    chunks = chunk_files(files)

    retriever = Retriever(chunks)
    planner = Planner()

    plan = planner.plan(question)
    retrieved = retriever.retrieve(question, top_k=plan["top_k"])

    answer = generate_answer(question, retrieved)

    print("\n=== ANSWER ===\n")
    print(answer)