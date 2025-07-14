# backend/test_pdf.py

from retriever.pdf_loader import load_and_chunk_pdf

chunks = load_and_chunk_pdf("data/pdfs/sample.pdf")
print(chunks[:2])  # Print first 2 chunks
