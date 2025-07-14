# utils/query_engine.py
import sys
from pathlib import Path

# Add Backend to path
backend_path = Path(__file__).resolve().parents[1].parent / "Backend"
sys.path.append(str(backend_path))

# Imports
from retriever.pdf_loader import load_and_chunk_pdf
from retriever.embed_store import embed_and_store
from rag_pipeline import load_vectorstore
from generator import generate_answer  # use huggingface version

def process_pdf_and_answer(pdf_path, question):
    # 1. Load & chunk PDF
    chunks = load_and_chunk_pdf(pdf_path)

    # 2. Embed & store
    embed_and_store(chunks)

    # 3. Load vector store and search
    db = load_vectorstore()
    docs = db.similarity_search(question, k=5)

    # 4. Extract context from docs
    context = "\n\n".join([doc.page_content for doc in docs])

    # 5. Generate answer using HuggingFace
    return generate_answer(context, question)

# if __name__ == "__main__":
#     pdf_path = "path/to/your/pdf.pdf"
#     question = "What is the purpose of this PDF?"
#     answer = process_pdf_and_answer(pdf_path, question)
#     print("Answer:", answer)