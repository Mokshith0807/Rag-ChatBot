from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents

from embeddings.embedder import load_embedding_model
from vectorstore.faiss_store import create_vector_store


print("Loading PDF...")
documents = load_pdf("data/raw/Unit 1_SCM.pdf")

print("Splitting Documents...")
chunks = split_documents(documents)

print("Loading Embedding Model...")
embedding_model = load_embedding_model()

print("Building FAISS Index...")
vector_store = create_vector_store(
    chunks,
    embedding_model
)

query = "What are the responsibilities of operations manager?"

print("\nSearching...")

results = vector_store.similarity_search(
    query,
    k=3
)

for i, doc in enumerate(results, start=1):

    print(f"\n========== RESULT {i} ==========")

    print("Metadata:")
    print(doc.metadata)

    print("\nContent:")
    print(doc.page_content[:1000])
