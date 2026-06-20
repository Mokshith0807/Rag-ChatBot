from utils.pdf_processor import process_pdf

result = process_pdf("data/raw/Unit 1_SCM.pdf")

print("\nPDF Processing Complete\n")

print(f"Documents: {result['documents']}")

print(f"Chunks: {result['chunks']}")
