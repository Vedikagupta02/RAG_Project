# RAG_Project

## Overview

This repository is a simple Retrieval-Augmented Generation (RAG) demo built with Python.

The pipeline:
- Load documents (PDF/TXT/CSV/XLSX/DOCX/JSON) from data/
- Split text into chunks
- Encode chunks into vector embeddings using sentence-transformers
- Store vectors in a local FAISS vector index (aiss_store)
- Query with natural language and retrieve top-k relevant chunks
- Summarize the retrieved context using an LLM (Groq via langchain_groq)

## Key modules

- src/data_loader.py: load documents from disk into LangChain Document objects
- src/embedding.py: text chunking + embedding via SentenceTransformer
- src/vectorstore.py: FAISS index creation, save/load, similarity search
- src/search.py: RAG search + LLM summarization using ChatGroq
- pp.py: sample execution flow

## Requirements

- Python 3.10+ (compatible with your setup)
- aiss-cpu or aiss-gpu
- sentence-transformers
- langchain, langchain_community, langchain_text_splitters, langchain_groq
- python-dotenv

Install dependencies:

`ash
pip install -r requirements.txt
`

## Usage

1. Place your documents in data/ (supported formats above).
2. Run pp.py:

`ash
python app.py
`

3. The script builds or loads aiss_store/faiss.index and queries:

- What is attention mechanism?
- prints a summarization console output

## Notes

- Set your Groq API key in environment or in src/search.py where groq_api_key is used.
- If you want to rebuild the vector store from scratch, delete aiss_store/faiss.index and aiss_store/metadata.pkl then rerun.
