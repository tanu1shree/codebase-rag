from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.embeddings = self._embed_chunks()
        self.index = self._build_index(self.embeddings)

    def _embed_chunks(self):
        texts = [c["text"] for c in self.chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return np.array(embeddings).astype("float32")
    
    def _build_index(self, embeddings):
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        return index
    
    def retrieve(self, query, top_k=3):
        query_embedding = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results
    
if __name__ == "__main__":
    from loader import load_codebase
    from chunker import chunk_files

    files = load_codebase(".")
    chunks = chunk_files(files)

    retriever = Retriever(chunks)

    query = "What does this project do?"
    results = retriever.retrieve(query)

    print("Retrieved files:")
    for r in results:
        print("-", r["path"])