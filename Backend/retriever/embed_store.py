# backend/retriever/embed_store.py

# backend/retriever/embed_store.py

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


from langchain.docstore.document import Document

def embed_and_store(chunks, index_path="vector_store/faiss_index"):
    # Create LangChain Document objects
    #docs = [Document(page_content=chunk) for chunk in chunks]
    docs = [Document(page_content=chunk["content"], metadata=chunk["metadata"]) for chunk in chunks]

    # Initialize HuggingFace Embeddings (Free)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Build FAISS index from documents
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Save index locally
    vectorstore.save_local(index_path)
    print(f"✅ Stored {len(docs)} chunks in FAISS at: {index_path}")
