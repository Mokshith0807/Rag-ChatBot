from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents

documents = load_pdf("data/raw/Unit 1_SCM.pdf")

chunks = split_documents(documents)

print(f"Pages Loaded: {len(documents)}")
print(f"Chunks Created: {len(chunks)}")

print("\nFirst Chunk Metadata:")
print(chunks[0].metadata)

print("\nFirst Chunk Length:")
print(len(chunks[0].page_content))

print("\nFirst Chunk Preview:")
print(chunks[0].page_content[:500])
