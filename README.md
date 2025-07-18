# Retrieve-and-summarize
# 📚 Smart PDF Assistant (RAG + HuggingFace)

## Overview
Smart PDF Assistant is an AI-powered application that allows you to **upload a PDF**, ask **any question**, and get **context-aware answers**.  
It uses **Retrieval-Augmented Generation (RAG)** to extract relevant information from your document and generate natural language answers.  
Additionally, it provides a **chatbot-like summarizer and explainer** that can define terms or summarize any paragraph.

---

## Features
- **PDF Q&A:** Upload a PDF and ask questions about its content.
- **AI-Powered Retrieval:** Uses FAISS + LangChain for context search.
- **Text Summarization & Explanation:** Acts like a chatbot to summarize or explain text in beginner-friendly language.
- **User-Friendly UI:** Built using Streamlit, with a clean interface and dedicated “Help Me” assistant button.

---

## Tech Stack
- **Backend:** Python, HuggingFace Transformers, FAISS, LangChain, PyMuPDF
- **Frontend:** Streamlit
- **AI Models:** Google Flan-T5 (HuggingFace)

---




### Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Project Structure
<img width="417" height="532" alt="image" src="https://github.com/user-attachments/assets/e712c0bf-288d-4de2-b319-fae95f2a4913" />



## Installation
Clone the repository:
```bash
git clone https://github.com/sanchari-66/Retrieve-and-summarize.git
cd Retrieve-and-summarize
