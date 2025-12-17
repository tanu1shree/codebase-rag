from loader import load_codebase
from chunker import chunk_files
from retriever import Retriever
from planner import Planner
from generator import generate_answer

if __name__ == "__main__":
    repo_path = "."
    question = "What does this project do?"

    print("STEP 1: starting")

    files = load_codebase(repo_path)
    print(f"STEP 2: loaded {len(files)} files")

    chunks = chunk_files(files)
    print(f"STEP 3: created {len(chunks)} chunks")

    retriever = Retriever(chunks)
    print("STEP 4: retriever ready")

    planner = Planner()
    print("STEP 5: planner ready")

    plan = planner.plan(question)
    print(f"STEP 6: plan = {plan}")

    retrieved = retriever.retrieve(question, top_k=plan["top_k"])
    print(f"STEP 7: retrieved {len(retrieved)} chunks")

    answer = generate_answer(question, retrieved)
    print("STEP 8: answer generated")

    print("\nFINAL ANSWER:\n")
    print(answer)