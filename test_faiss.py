from embeddings.embedder import load_embedding_model
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from vectorstore.faiss_store import create_vector_store

print("Loading PDF...")
documents = load_pdf("data/raw/Unit 1_SCM.pdf")

print("Splitting Documents...")
chunks = split_documents(documents)

print("Loading Embedding Model...")
embedding_model = load_embedding_model()

print("Creating FAISS Index...")
vector_store = create_vector_store(chunks, embedding_model)

print("FAISS Index Created Successfully")

print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")
