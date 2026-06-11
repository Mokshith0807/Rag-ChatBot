from pypdf import PdfReader

pdf_path = "data/raw/Unit 1_SCM.pdf"

reader = PdfReader(pdf_path)

print(f"Total Pages: {len(reader.pages)}")

first_page = reader.pages[0].extract_text()

print("\n===== FIRST PAGE PREVIEW =====\n")
print(first_page[:1000])
