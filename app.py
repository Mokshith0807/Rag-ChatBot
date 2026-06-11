import os
import streamlit as st

from utils.pdf_processor import process_pdf

from embeddings.embedder import (
    load_embedding_model
)

from vectorstore.faiss_store import (
    load_vector_store
)

from chains.rag_chain import (
    create_rag_chain,
    generate_answer
)

from config.settings import TOP_K


st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Chatbot")

st.write(
    "Upload a PDF and chat with it using "
    "FAISS + Gemini"
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


if uploaded_file:

    save_path = os.path.join(
        "data/raw",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    if st.button(
        "Process PDF"
    ):

        with st.spinner(
            "Processing PDF..."
        ):

            result = process_pdf(
                save_path
            )

        st.success(
            "PDF Processed Successfully"
        )

        st.write(
            f"Documents: {result['documents']}"
        )

        st.write(
            f"Chunks: {result['chunks']}"
        )


st.divider()

st.header("💬 Ask Questions")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    with st.spinner(
        "Searching..."
    ):

        embedding_model = (
            load_embedding_model()
        )

        vector_store = (
            load_vector_store(
                embedding_model
            )
        )

        docs = (
            vector_store.similarity_search(
                question,
                k=TOP_K
            )
        )

        llm = create_rag_chain()

        answer = generate_answer(
            llm,
            docs,
            question
        )

    st.subheader("Answer")

    st.write(answer)

    st.subheader(
        "Source Pages"
    )

    pages = sorted(
        list(
            set(
                [
                    doc.metadata.get(
                        "page"
                    )
                    for doc in docs
                ]
            )
        )
    )

    for page in pages:

        st.markdown(
            f"📄 Page {page}"
        )
