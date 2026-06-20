from embeddings.embedder import load_embedding_model
from vectorstore.faiss_store import load_vector_store

print("Loading Embedding Model...")
embedding_model = load_embedding_model()

print("Loading Saved FAISS Index...")
vector_store = load_vector_store(embedding_model)

query = "What are the responsibilities of operations manager?"

print("\nSearching...")

results = vector_store.similarity_search(query, k=3)

for i, doc in enumerate(results, start=1):
    print(f"\n========== RESULT {i} ==========")

    print("Metadata:")
    print(doc.metadata)

    print("\nContent:")
    print(doc.page_content[:1000])
