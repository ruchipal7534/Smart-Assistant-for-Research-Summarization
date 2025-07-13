# 📚 Smart Research Assistant (Ollama Edition)

This project is a lightweight research assistant built with Streamlit that integrates with **Ollama's LLM API (LLaMA 3.2 3B model)**. It allows users to upload documents (PDF or TXT), get auto-generated summaries, ask custom questions, and receive logic-based comprehension challenges.

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/smart-research-assistant.git
cd smart-research-assistant
***2. Create a Virtual Environment (Optional but Recommended)***
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

nginx
Copy
Edit
streamlit
PyMuPDF
requests
4. Start the Ollama Backend
Make sure Ollama is running locally (default: http://127.0.0.1:11434) and the specified model is available:

bash
Copy
Edit
ollama run llama3.2:3b
5. Run the Streamlit App
bash
Copy
Edit
streamlit run chat2.py
🧠 Architecture & Reasoning Flow
🔧 Backend
Ollama API: Handles all LLM processing via a locally running LLaMA model.

Streamlit Interface: Frontend UI for user interaction.

PDF/TXT Handling: PyMuPDF for extracting text from PDF files; UTF-8 for TXT.

🧩 Functional Flow
Document Upload: Accepts PDF or TXT file.

Text Extraction: Extracts readable text using fitz or basic decoding.

Summarization: Generates a short summary of the document via Ollama.

Ask Anything Mode: Accepts user queries and responds contextually.

Challenge Me Mode:

Generates logic/comprehension questions.

Accepts user answers.

Evaluates correctness with LLM feedback.
