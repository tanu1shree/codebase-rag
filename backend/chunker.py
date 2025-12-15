def chunk_files(files):
    chunks = []

    for f in files:
        chunks.append({
            "path": f["path"],
            "text": f["content"]
        })

    return chunks

if __name__ == "__main__":
    from loader import load_codebase

    files = load_codebase(".")
    chunks = chunk_files(files)

    print(f"Created {len(chunks)} chunks")
    if chunks:
        print("Example chunk:")
        print("Path:", chunks[0]["path"])
        print("Text length:", len(chunks[0]["text"]))