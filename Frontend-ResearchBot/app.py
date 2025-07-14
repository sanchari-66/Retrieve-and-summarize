# app.py
import streamlit as st
import tempfile

import sys
from pathlib import Path

# Add Backend to path
backend_path = Path(__file__).resolve().parents[1].parent / "Backend"
sys.path.append(str(backend_path))

from utils.query_engine import process_pdf_and_answer
from summarizer import summarize_paragraph
from smart_helper import smart_helper

st.set_page_config(page_title="📚 PDF Research Assistant", layout="wide")

st.title("📚 AI-Powered PDF Research Assistant")
st.markdown("Upload a PDF and ask any question. The system will read and answer from the document using RAG.")

# --- PDF Upload ---
uploaded_file = st.file_uploader("📄 Upload your PDF file", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    # --- User Question ---
    question = st.text_input("❓ Ask a question based on the uploaded PDF")

    if st.button("🔍 Get Answer") and question:
        with st.spinner("🧠 Thinking..."):
            try:
                answer = process_pdf_and_answer(pdf_path, question)
                st.success("✅ Answer:")
                st.markdown(f"<div style='background-color:#e6f7ff;padding:15px;border-radius:10px'><b>{answer}</b></div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# --- Paragraph Summarizer Section ---
# --- Smart Assistant (Summarizer + Explainer) ---
st.markdown("---")
st.markdown("### 🤖 Smart Assistant (Summarizer & Explainer)")

col1, col2 = st.columns([2, 1])
with col1:
    smart_input = st.text_area("💬 Type a paragraph or a term/question you want help with", height=200)
with col2:
    if st.button("💗 Help Me", key="smart_btn"):
        if smart_input:
            with st.spinner("Thinking..."):
                smart_reply = smart_helper(smart_input)
                st.markdown(
                    f"<div style='background-color:#ffe6f0;padding:15px;border-radius:10px'><b>AI Response:</b><br>{smart_reply}</div>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<div style='background-color:#e6f7ff;padding:15px;border-radius:10px'><b>Human Explanation:</b><br>{smart_helper(smart_reply)}</div>",
                    unsafe_allow_html=True
                )                        
        else:                    
            st.warning("Please enter a paragraph or a term/question.")