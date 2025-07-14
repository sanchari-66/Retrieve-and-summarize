# backend/embed_chunks.py

from retriever.pdf_loader import load_and_chunk_pdf
from retriever.embed_store import embed_and_store

chunks = load_and_chunk_pdf("data/pdfs/sample.pdf")
embed_and_store(chunks)
