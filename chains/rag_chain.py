from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import GEMINI_MODEL

load_dotenv()


def create_rag_chain():

    llm = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    return llm


def build_context(documents):

    context = ""

    for doc in documents:

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        context += f"\n\n[Page {page}]\n"
        context += doc.page_content

    return context


def generate_answer(
    llm,
    documents,
    question
):

    context = build_context(
        documents
    )

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the provided context.

If the answer is not available in the context,
respond exactly:

I could not find the answer in the document.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(
        prompt
    )

    return response.content
