from embeddings.embedder import load_embedding_model

model = load_embedding_model()

text = "Supply Chain Management is the management of goods and services."

embedding = model.encode(text)

print("Embedding Generated Successfully")

print(f"Vector Length: {len(embedding)}")

print("\nFirst 10 Values:")
print(embedding[:10])
