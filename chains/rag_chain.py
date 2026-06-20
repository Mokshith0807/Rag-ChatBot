from chains.local_llm import (
    generate_local_answer,
    load_local_llm,
)


def create_rag_chain():
    """
    Load the local LLM.
    """
    return load_local_llm()


def build_context(documents):
    """
    Build context string from retrieved documents.
    """

    context = ""

    for doc in documents:
        page = doc.metadata.get("page", "Unknown")

        context += f"\n\n[Page {page}]\n"
        context += doc.page_content

    return context


def generate_answer(llm, documents, question):
    """
    Generate an answer using the local LLM.
    """

    context = build_context(documents)

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply:
"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    return generate_local_answer(llm, prompt)
