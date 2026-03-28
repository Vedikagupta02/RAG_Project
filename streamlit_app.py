import streamlit as st
import os
import re
from dotenv import load_dotenv
from src.search import RAGSearch

# Load environment variables
load_dotenv()

def clean_text(text: str) -> str:
    if not text:
        return "No text available"
    # Remove <EOS> and <pad> tokens which often appear in the PDF datasets
    text = re.sub(r'<(EOS|pad)>', '', text)
    # Normalize excessive whitespace/newlines
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

st.set_page_config(page_title="RAG Search App", page_icon="🔍", layout="centered")

st.title("🔍 RAG Search Assistant")
st.markdown("Ask questions about the documents in your vector database.")

@st.cache_resource
def load_rag_search():
    try:
        # Initialize RAGSearch which will load the Faiss index
        return RAGSearch()
    except Exception as e:
        st.error(f"Error initializing RAG system: {e}")
        return None

with st.spinner("Loading vector database..."):
    rag_search = load_rag_search()

if rag_search:
    st.success("Vector database loaded successfully!")
    
    # Check for Groq API Key
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.warning("⚠️ GROQ_API_KEY is not set in your environment variables. Please add it to your .env file.")
    
    query = st.text_input("Enter your question:")
    top_k = st.slider("Number of source documents to retrieve (Top K)", min_value=1, max_value=10, value=3)
    
    if st.button("Search"):
        if query.strip():
            with st.spinner("Searching and summarizing..."):
                try:
                    summary = rag_search.search_and_summarize(query, top_k=top_k)
                    st.markdown("### 📝 Summary")
                    st.write(summary)
                    
                    # Also fetch the context directly using vectorstore to display sources
                    results = rag_search.vectorstore.query(query, top_k=top_k)
                    if results:
                        with st.expander("Show retrieved source documents"):
                            for i, res in enumerate(results):
                                st.markdown(f"**Document {i+1}**")
                                raw_text = res["metadata"].get("text", "")
                                st.write(clean_text(raw_text))
                                st.markdown("---")
                except Exception as e:
                    st.error(f"An error occurred during search: {e}")
        else:
            st.warning("Please enter a valid question.")
