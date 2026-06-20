from langchain_core.documents import Document

from embeddings.embedder import load_embedding_model
from vectorstore.faiss_store import create_vector_store


def test_faiss_creation():
    model = load_embedding_model()
    docs = [Document(page_content="Hello world", metadata={"page": 1})]
    store = create_vector_store(docs, model)
    assert store is not None
