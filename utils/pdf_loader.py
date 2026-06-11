
from pypdf import PdfReader
from langchain_core.documents import Document
from pathlib import Path


def load_pdf(pdf_path: str):
    """
    Load PDF and return LangChain Documents.
    Each page becomes one Document.
    """

    reader = PdfReader(pdf_path)

    documents = []

    for page_num, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text and text.strip():

            doc = Document(
                page_content=text,
                metadata={
                    "source": Path(pdf_path).name,
                    "page": page_num
                }
            )

            documents.append(doc)

    return documents
