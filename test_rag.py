from embeddings.embedder import load_embedding_model

from vectorstore.faiss_store import (
    load_vector_store
)

from chains.rag_chain import (
    create_rag_chain,
    generate_answer
)


print("Loading Embedding Model...")
embedding_model = load_embedding_model()

print("Loading FAISS Index...")
vector_store = load_vector_store(
    embedding_model
)

question = "What are the responsibilities of operations manager?"

print("\nSearching Documents...")

documents = vector_store.similarity_search(
    question,
    k=3
)

print("Loading Gemini...")
llm = create_rag_chain()

print("Generating Answer...\n")

answer = generate_answer(
    llm,
    documents,
    question
)

print("QUESTION:")
print(question)

print("\nANSWER:")
print(answer)

print("\nSOURCE PAGES:")

for doc in documents:
    print(
        f"Page {doc.metadata['page']}"
    )
