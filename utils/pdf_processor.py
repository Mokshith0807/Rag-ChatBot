from embeddings.embedder import load_embedding_model
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from vectorstore.faiss_store import create_vector_store, save_vector_store


def process_pdf(pdf_path):
    documents = load_pdf(pdf_path)

    chunks = split_documents(documents)

    embedding_model = load_embedding_model()

    vector_store = create_vector_store(chunks, embedding_model)

    save_vector_store(vector_store)

    return {"documents": len(documents), "chunks": len(chunks)}
