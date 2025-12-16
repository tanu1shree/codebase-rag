# Codebase Assistant

A local, offline-first **codebase question-answering system** built using **Planner-guided Retrieval-Augmented Generation (RAG)**.

The system retrieves relevant source files from a local repository using semantic search and generates **grounded explanations strictly from retrieved code**, with explicit file-level traceability. All inference runs locally using an open-source language model.

---

## Key Features

- Answers questions about a **local codebase**
- Planner-controlled retrieval (broad vs focused context)
- Semantic vector search over source files using FAISS
- Grounded generation constrained to retrieved code only
- Fully local execution (no cloud, no API keys)
- Offline-capable after initial setup

---

## Technologies

### Backend
- Python
- `sentence-transformers` (embeddings)
- `faiss-cpu` (vector search)
- Custom rule-based planner

### LLM (Local, Offline)
- Ollama (llama.cpp-based runtime)
- Open-source model (e.g. `mistral`)

### Interface
- Minimal local interface (CLI for MVP)
- Architecture supports adding a web UI later without refactor

---

## Architecture

This project implements a **Planner-guided Retrieval-Augmented Generation (RAG)** pipeline.

### High-Level Flow

Loader → Chunker → Retriever → Planner → Generator

### Component Overview

- **Loader**
Reads source files from the local repository and preserves file paths.

- **Chunker**
Uses file-level chunking to maintain traceability between content and source files.

- **Retriever**
Embeds code using sentence-transformers and performs semantic search using FAISS.

- **Planner**
Determines retrieval breadth (`top-k`) based on the user question.

- **Generator**
Builds a constrained prompt and produces answers using only retrieved code via a local LLM.

---

## Design Decisions

- File-level chunking to preserve exact source attribution
- FAISS for fast, in-memory local vector search
- Explicit planner to control retrieval strategy
- Generator strictly constrained to retrieved context to reduce hallucination
- Local LLM execution for privacy and offline capability

---

## Limitations (MVP)

- In-memory vector store (recomputed per run)
- No persistent embedding cache
- Minimal interface by design
- Single-turn question answering (no conversational memory)

These are intentional MVP trade-offs.

---

## Running the Project

This project runs **entirely on your local machine** and does not require an internet connection after setup.

### Prerequisites

- Python 3.9 or newer
- Git
- Ollama (local LLM runtime)

---

### 1. Clone the Repository

### 2. Create and Activate a Virtual Environment

`python -m venv venv`

Activate the virtual environment:

Windows:
`venv\Scripts\activate`

macOS / Linux:
`source venv/bin/activate`

### 3. Install Dependencies

`pip install -r requirements.txt`

### 4. Install and Run the Local LLM

Install Ollama from:
https://ollama.com

Pull an open-source model:

`ollama pull mistral`

Ensure Ollama is running:

`ollama run mistral`

(Ollama runs as a background service after this.)

### 5. Run the Project
`python backend/main.py`

The system will:
* Load the local codebase
* Retrieve relevant files using vector search
* Generate grounded explanations using the local LLM

All processing happens locally. No data is sent externally.

<!--TBA
## Preview--> 
