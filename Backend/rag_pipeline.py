# backend/rag_pipeline.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def load_vectorstore(index_path="vector_store/faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    return db

from generator import generate_answer  # ✅ New version with fallback logic
#from rag_pipeline import generate_answer_with_metadata, load_vectorstore


def run_rag_pipeline():
    db = load_vectorstore()
    question = input("Ask your question: ")

    docs = db.similarity_search(question, k=3)

    # Ensure all docs are LangChain Documents
    from langchain.docstore.document import Document
    docs = [Document(page_content=doc) if isinstance(doc, str) else doc for doc in docs]

    print("\n🔍 Top 3 results for: ", question)
    for i, doc in enumerate(docs, 1):
        print(f"Result {i}:\n{doc.page_content}\n{'-'*40}")

    context = "\n\n".join([doc.page_content for doc in docs])
    answer_text = generate_answer(context, question)

    sources = [doc.metadata.get("page", "?") for doc in docs]

    print("\n🧠 Final Answer:\n", answer_text)

    print("📚 Sources (pages):", sources)
    
if __name__ == "__main__":
    run_rag_pipeline()

    # return answer