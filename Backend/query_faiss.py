# backend/query_faiss.py

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def query_faiss(user_question, index_path="vector_store/faiss_index", k=3):
    # Load same embeddings model used during storage
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Load FAISS index
    vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

    # Perform similarity search
    results = vectorstore.similarity_search(user_question, k=k)

    print(f"\n🔍 Top {k} results for: '{user_question}'\n")
    for i, doc in enumerate(results, 1):
        print(f"Result {i}:\n{doc.page_content}\n{'-'*40}")

if __name__ == "__main__":
    question = input("Ask your question: ")
    query_faiss(question)
