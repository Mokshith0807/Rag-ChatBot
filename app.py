import streamlit as st

from chains.rag_chain import create_rag_chain, generate_answer
from embeddings.embedder import load_embedding_model
from utils.pdf_processor import process_pdf
from vectorstore.faiss_store import load_vector_store

st.set_page_config(page_title="Local RAG Chatbot", page_icon="📚", layout="wide")

st.title("📚 Local RAG Chatbot (FAISS + llama.cpp)")
st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    save_path = f"data/raw/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing PDF and creating embeddings..."):
        stats = process_pdf(save_path)

    st.success(f"Processed {stats['documents']} pages into {stats['chunks']} chunks.")

question = st.text_input("Ask a question about the uploaded PDF")

if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Loading embedding model..."):
            embedding_model = load_embedding_model()

        with st.spinner("Loading FAISS index..."):
            vector_store = load_vector_store(embedding_model)

        docs = vector_store.similarity_search(question, k=3)

        with st.spinner("Loading local LLM..."):
            llm = create_rag_chain()

        with st.spinner("Generating answer..."):
            answer = generate_answer(llm, docs, question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Source Pages")

        for doc in docs:
            st.write(f"📄 Page {doc.metadata.get('page', 'Unknown')}")
