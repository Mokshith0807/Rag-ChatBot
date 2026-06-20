from pathlib import Path

import pymupdf4llm  # type: ignore
from langchain_core.documents import Document


def load_pdf(pdf_path: str):
    """
    Load a PDF using PyMuPDF4LLM and return LangChain Documents.
    """

    pages = pymupdf4llm.to_markdown(pdf_path, page_chunks=True)

    documents = []

    for page_num, page in enumerate(pages, start=1):
        text = page.get("text", "")

        if text and text.strip():
            doc = Document(
                page_content=text,
                metadata={"source": Path(pdf_path).name, "page": page_num},
            )

            documents.append(doc)

    return documents
