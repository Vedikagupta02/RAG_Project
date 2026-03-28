# 🔍 RAG-Based Multi-Document Question Answering System

[Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
[FAISS](https://img.shields.io/badge/VectorStore-FAISS-green)
[LLM](https://img.shields.io/badge/LLM-Groq-orange)
[Status](https://img.shields.io/badge/Status-Active-success)

---

## Overview

This project is an **end-to-end Retrieval-Augmented Generation (RAG) system** that enables users to query multiple document formats and receive **accurate, context-aware answers** using Large Language Models (LLMs).

Instead of relying solely on pre-trained knowledge, the system retrieves relevant information from your documents and uses it as context for generating responses.

---

## How It Works

`
Documents → Loaders → Chunking → Embeddings → FAISS → Retriever → LLM → Answer
`

---

## Project Structure

`
.
├── app.py                  # Main entry point
├── src/
│   ├── data_loader.py      # Multi-format document ingestion
│   ├── vectorstore.py      # FAISS-based vector storage
│   ├── search.py           # RAG retrieval + summarization
│   ├── retriever.py        # Similarity search logic
│   ├── embeddings.py       # Embedding generation
├── data/                   # Input documents
├── faiss_store/            # Saved FAISS index
├── requirements.txt
└── README.md
`

---

## Features

### Multi-Format Document Support

* PDF
* TXT
* CSV
* Excel (.xlsx)
* Word (.docx)
* JSON

---

### Intelligent Processing

* Recursive chunking with overlap
* Semantic embeddings using Sentence Transformers
* Efficient similarity search using FAISS

---

### Retrieval System

* Top-K document retrieval
* Similarity threshold filtering (min_score)
* Metadata tracking for sources

---

### LLM Integration (Groq)

* Fast inference using modern models (llama-3.1-*)
* Low temperature for factual responses
* Supports summarization

---

### Advanced RAG Capabilities

* Source citations
* Confidence score (based on similarity)
* Query history tracking
* Streaming (simulated)
* Answer summarization

---

## Tech Stack

* **Python**
* **LangChain**
* **FAISS** (Vector Search)
* **Sentence Transformers** (Embeddings)
* **Groq API** (LLM Inference)

---

## Installation

### 1. Clone the repository

`
git clone <your-repo-url>
cd <project-folder>
`

---

### 2. Create virtual environment

`
python -m venv .venv
.venv\Scripts\activate   # Windows
`

---

### 3. Install dependencies

`
pip install -r requirements.txt
`

---

### 4. Set your API key

`
export GROQ_API_KEY= your_api_key
`

Or in Python:

`python
import os
os.environ[GROQ_API_KEY] = your_api_key
`

---

## Running the Project

`
python app.py
`

---

## Example Usage

`python
query = What is attention mechanism?
summary = rag_search.search_and_summarize(query, top_k=3)

print(Summary:, summary)
`

---

## Sample Output

`
Answer: Attention mechanism allows models to focus on relevant parts of input...

Sources:
[1] paper.pdf (page 3)

Confidence: 0.87
`

---

## Key Parameters

| Parameter       | Description                  |
| --------------- | ---------------------------- |
| 	op_k         | Number of retrieved chunks   |
| min_score     | Minimum similarity threshold |
| 	emperature   | Controls LLM randomness      |
| chunk_size    | Size of text chunks          |
| chunk_overlap | Overlap between chunks       |

---

## Core Concepts

* **Embeddings** → Convert text into vectors
* **Cosine Similarity** → Measure semantic closeness
* **ANN (Approximate Nearest Neighbor)** → Fast retrieval
* **Chunking** → Preserve context across documents
* **Vector Search** → Efficient similarity lookup

---

## FAISS vs ChromaDB

| Feature     | FAISS              | ChromaDB    |
| ----------- | ------------------ | ----------- |
| Type        | Library            | Database    |
| Control     | High               | Medium      |
| Ease of Use | Moderate           | Easy        |
| Use Case    | Production systems | Prototyping |

---

## Future Improvements

* Real-time streaming responses
* Hybrid search (keyword + vector)
* Re-ranking models
* FastAPI backend deployment
* Streamlit / React UI
* Agentic RAG integration

---

## Learning Outcomes

* Built an end-to-end RAG pipeline
* Understood embeddings and vector search
* Implemented FAISS-based retrieval
* Integrated LLMs for grounded generation
* Designed modular and scalable architecture

---

## Conclusion

This project demonstrates a **production-style RAG system** capable of:

* Handling diverse document formats
* Performing efficient semantic search
* Generating accurate, context-aware responses

---

## Acknowledgements

* LangChain
* FAISS
* Sentence Transformers
* Groq

---

## Star the repo if you found it useful!
