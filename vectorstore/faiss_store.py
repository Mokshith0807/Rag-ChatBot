from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings

from config.settings import FAISS_PATH


class SentenceTransformerEmbeddings(Embeddings):
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()


def create_vector_store(chunks, embedding_model):
    embeddings = SentenceTransformerEmbeddings(embedding_model)

    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store


def save_vector_store(vector_store):
    vector_store.save_local(FAISS_PATH)


def load_vector_store(embedding_model):
    embeddings = SentenceTransformerEmbeddings(embedding_model)

    vector_store = FAISS.load_local(
        FAISS_PATH, embeddings, allow_dangerous_deserialization=True
    )

    return vector_store
