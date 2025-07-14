
# # Backend/generator.py

# backend/generator.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re

HF_MODEL_ID = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(HF_MODEL_ID)

def detect_instruction(question):
    if "one word" in question.lower():
        return "one-word"
    elif "paragraph" in question.lower():
        return "paragraph"
    elif "100 words" in question.lower():
        return "100-words"
    else:
        return "default"

def build_prompt(context, question, mode):
    if mode == "one-word":
        return f"""Answer the question in **only one word** based on the context.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"""
    elif mode == "paragraph":
        return f"""Answer the question in a **complete paragraph** based on the context.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"""
    elif mode == "100-words":
        return f"""Answer the question in **approximately 100 words** based on the context.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"""
    else:
        return f"""Answer the following question clearly based on the context.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"""

def try_huggingface(prompt, max_tokens=300):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=max_tokens)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

def generate_answer(context, question):
    mode = detect_instruction(question)
    prompt = build_prompt(context, question, mode)

    # Adjust token limit based on mode
    if mode == "one-word":
        max_tokens = 5
    elif mode == "paragraph":
        max_tokens = 100
    elif mode == "100-words":
        max_tokens = 150
    else:
        max_tokens = 300

    return try_huggingface(prompt, max_tokens)

# import requests
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# import torch

# # Configuration
# OLLAMA_URL = "http://localhost:11434/api/generate"
# OLLAMA_MODEL = "mistral"
# HF_MODEL_ID = "google/flan-t5-base"

# # Load HuggingFace model & tokenizer once
# tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_ID)
# model = AutoModelForSeq2SeqLM.from_pretrained(HF_MODEL_ID)

# # ---------- Helper Functions ----------

# def try_ollama(prompt):
#     try:
#         response = requests.post(
#             OLLAMA_URL,
#             json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
#             timeout=10,
#         )
#         response.raise_for_status()
#         return response.json()["response"].strip()
#     except Exception as e:
#         print(f"[⚠️ Ollama Error] {e}")
#         return None

# def try_huggingface(prompt):
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
#     outputs = model.generate(**inputs, max_new_tokens=300)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

# def ask_with_fallback(prompt, label="Answer"):
#     # 1. Try Ollama
#     result = try_ollama(prompt)
#     if result:
#         print(f"[✅ Ollama Used] {label}")
#         return result

#     # 2. Fallback to Hugging Face
#     print(f"[🔁 Falling Back to HuggingFace] {label}")
#     return try_huggingface(prompt)

# # ---------- Main Features ----------

# def generate_answer(context, question):
#     prompt = f"""You are a helpful assistant. Based on the context below, answer the question clearly.

# Context:
# {context}

# Question:
# {question}

# Answer:"""
#     return ask_with_fallback(prompt, label="Answer")

# def summarize_paragraph(paragraph):
#     prompt = f"""Summarize the following paragraph in simple, clear language:

# {paragraph}

# Summary:"""
#     return ask_with_fallback(prompt, label="Summary")

# def explain_term(term):
#     prompt = f"""Explain the term "{term}" in simple words suitable for beginners.

# Definition:"""
#     return ask_with_fallback(prompt, label="Explanation")
