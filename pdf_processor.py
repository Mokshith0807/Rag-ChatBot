import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# ---------- 1. Extract text from PDF ----------
def extract_text_from_pdf(pdf_file):
    text = ""

    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in doc:
        text += page.get_text()

    return text


# ---------- 2. Split text into chunks ----------
def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)
    return chunks


# ---------- 3. Create FAISS vector store ----------
def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_texts(chunks, embeddings)

    return vectorstore


# ---------- 4. Full pipeline ----------
def process_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    chunks = chunk_text(text)
    vectorstore = create_vector_store(chunks)

    return vectorstore
