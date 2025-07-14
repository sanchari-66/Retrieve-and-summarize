# # backend/retriever/pdf_loader.py

# backend/retriever/pdf_loader.py

import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_pdf(pdf_path, chunk_size=500, chunk_overlap=100):
    doc = fitz.open(pdf_path)
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    for page_number, page in enumerate(doc, start=1):
        text = page.get_text()
        if not text.strip():
            continue  # Skip empty pages

        page_chunks = splitter.split_text(text)
        for chunk in page_chunks:
            chunks.append({
                "content": chunk,
                "metadata": {"page": page_number}
            })

    print(f"✅ Loaded {len(chunks)} chunks from {os.path.basename(pdf_path)}")
    return chunks





# import os
# import fitz  # PyMuPDF
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# def load_and_chunk_pdf(pdf_path, chunk_size=500, chunk_overlap=100):
#     # Load text from PDF
#     doc = fitz.open(pdf_path)
#     full_text = ""
#     for page in doc:
#         full_text += page.get_text()
    
#     # Chunk the text
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     chunks = splitter.split_text(full_text)
    
#     print(f"✅ Loaded {len(chunks)} chunks from {os.path.basename(pdf_path)}")
#     return chunks
