# backend/smart_helper.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load HuggingFace summarization model
MODEL_ID = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)

def smart_helper(user_input):
    """
    Acts like a chatbot helper: if user gives a paragraph, it summarizes;
    if it's a term or short sentence, it explains.
    """
    if len(user_input.split()) < 15:
        prompt = f"Explain the term or question clearly:\n\n{user_input}\n\nAnswer:"
    else:
        prompt = f"Summarize the following paragraph:\n\n{user_input}\n\nSummary:"
    
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
