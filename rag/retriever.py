"""Simple retriever abstraction used by the Streamlit app.

This is a lightweight wrapper that calls the existing vectorstore
implementation. Kept minimal for testing and clarity.
"""

from typing import List


def retrieve(vector_store, query: str, k: int = 3) -> List[dict]:
    """Return top-k documents from a vector store for the given query.

    Args:
        vector_store: object with `similarity_search` method
        query: user query
        k: number of results

    Returns:
        List of documents (dictionaries)
    """
    docs = vector_store.similarity_search(query, k=k)
    return docs
