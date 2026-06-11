from utils.pdf_loader import load_pdf

docs = load_pdf("data/raw/Unit 1_SCM.pdf")

print(f"Documents Loaded: {len(docs)}")

print("\nMetadata:")
print(docs[0].metadata)

print("\nContent Preview:")
print(docs[0].page_content[:500])
