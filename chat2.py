import streamlit as st
import fitz  # PyMuPDF
import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
OLLAMA_MODEL = "llama3.2:3b"  # Change if you're using a different model

# ---- PDF Text Extraction ----
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    return text

# ---- Ollama Chat Helper ----
def chat_with_ollama(prompt, context=""):
    full_prompt = f"{prompt}\n\n{context}" if context else prompt
    data = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=data)
    if response.ok:
        result = response.json()
        return result.get("message", {}).get("content", "No response from model.")
    else:
        return f"Error: {response.status_code}"

# ---- Summarization ----
def get_summary(text):
    prompt = "Summarize the following document into a concise summary with key points only."
    return chat_with_ollama(prompt, context=text[:4000])  # Limit context size

# ---- Question Answering ----
def ask_question(question, context):
    prompt = f"Answer this question based only on the provided document:\n\nQuestion: {question}"
    return chat_with_ollama(prompt, context=context[:4000])

# ---- Logic Question Generation ----
def generate_logic_questions(context):
    prompt = "Generate 3 logic-based or comprehension-focused questions based on this document:"
    return chat_with_ollama(prompt, context=context[:4000])

# ---- Evaluation ----
def evaluate_answer(question, user_answer, context):
    prompt = f"""Evaluate the correctness of the following user answer based on the given document:

Question: {question}
User Answer: {user_answer}

Provide a brief and objective evaluation."""
    return chat_with_ollama(prompt, context=context[:4000])

# ---- Streamlit UI ----
st.title("📚 Smart Research Assistant (Ollama Edition)")

uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        doc_text = extract_text_from_pdf(uploaded_file)
    else:
        doc_text = uploaded_file.read().decode("utf-8")

    st.subheader("🔍 Auto Summary")
    st.write(get_summary(doc_text))

    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        query = st.text_input("Ask a question based on the document:")
        if query:
            answer = ask_question(query, doc_text)
            st.markdown(f"**Answer:** {answer}")

    elif mode == "Challenge Me":
        st.subheader("🧠 Logic-based Questions")
        logic_qs = generate_logic_questions(doc_text).split("\n")
        for i, q in enumerate([q for q in logic_qs if q.strip()], 1):
            user_resp = st.text_input(f"Q{i}: {q}")
            if user_resp:
                feedback = evaluate_answer(q, user_resp, doc_text)
                st.markdown(f"**Feedback:** {feedback}")
