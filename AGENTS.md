# Agents & Architecture

This document explains the AI agent architecture used by the RAG Chatbot.

High level

- Retriever: Encodes documents and queries into vector embeddings. We use
  a sentence-transformer or compatible embedding model (see
  `embeddings/embedder.py`).
- Vector Store: FAISS index for fast nearest-neighbour lookup
  (`vectorstore/faiss_store.py`).
- Generator: Local LLM chain that accepts retrieved context and the
  user query and produces an answer with source attribution
  (`chains/rag_chain.py`).

Flow

1. Document ingestion: PDFs are processed and split into chunks. Chunks
   are embedded and stored in FAISS.
2. Query handling: The user question is embedded and matched against
   FAISS to find top-K relevant chunks.
3. Context building: Retrieved chunks are assembled into a prompt that
   balances relevance and token budget.
4. Generation: The generator LLM produces an answer and returns cited
   source pages.

Design considerations

- Privacy: Designed for local-only usage.
- Extensibility: Retrieval and generation components are modular.
- Reproducibility: Indexes are deterministic given the same chunking
  and embedding model.
