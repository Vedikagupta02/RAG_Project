from src.data_loader import load_all_documents
from src.search import RAGSearch
from src.vectorstore import FaissVectorStore
# from src.search import RAGSearch
from src.embedding import EmbeddingPipeline

# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    store=FaissVectorStore("faiss_store")
    store.load()
    # chunks=EmbeddingPipeline().chunk_documents(docs)
    # embeddings=EmbeddingPipeline().embed_chunks(chunks)
    # print("[INFO] Example embedding:", embeddings[0] if len(embeddings) > 0 else None)
    # print(store.query("What is attention is all you need?", top_k=3))
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)