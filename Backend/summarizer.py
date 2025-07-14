# backend/summarizer.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

HF_MODEL_ID = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(HF_MODEL_ID)

def summarize_paragraph(paragraph):
    prompt = f"""Summarize the following paragraph in simple, clear language:

{paragraph}

Summary:"""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
