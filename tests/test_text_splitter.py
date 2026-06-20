from langchain_core.documents import Document

from utils.text_splitter import split_documents


def test_split_documents():
    docs = [
        Document(
            page_content="Hello world " * 500,
            metadata={"page": 1},
        )
    ]

    chunks = split_documents(docs)

    assert len(chunks) > 0
    assert chunks[0].metadata["page"] == 1
