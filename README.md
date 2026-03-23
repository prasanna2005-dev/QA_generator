# 🤖 RAG QA Generator (AI Document Question Answering System)

An AI-powered Question Answering system that extracts accurate answers from PDF documents using Retrieval-Augmented Generation (RAG).

Built using **LangChain, FAISS, HuggingFace Embeddings, and Mistral AI**, this project enables users to query documents and receive context-based, explainable answers with relevant clauses.

---

## 🚀 Features

* 📄 Upload and process PDF documents
* 🔍 Semantic search using vector embeddings
* 🧠 Context-aware answer generation using LLM (Mistral AI)
* 📌 Extracts relevant clauses/lines from documents
* ⚡ Fast retrieval using FAISS vector database
* 💬 Streamlit-based interactive UI (if applicable)

---

## 🏗️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM:** Mistral AI (`mistral-large-latest`)
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **Vector DB:** FAISS
* **Framework:** LangChain

---

## 📂 Project Structure

```
qa-generator/
│
├── app.py                # Streamlit UI
├── rag.py                # RAG pipeline logic
├── requirements.txt      # Dependencies
├── .env                  # API keys (ignored)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/rag-qa-generator.git
cd rag-qa-generator
```

---

### 2. Create Virtual Environment

```
python -m venv rag_env
rag_env\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file:

```
MISTRAL_API_KEY=your_mistral_api_key
HF_TOKEN=your_huggingface_token   # optional
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 🧠 How It Works (RAG Pipeline)

1. 📄 Load PDF using PyPDFLoader
2. ✂️ Split text into chunks
3. 🔢 Convert text into embeddings
4. 📦 Store embeddings in FAISS
5. 🔍 Retrieve relevant chunks based on query
6. 🤖 Generate answer using Mistral LLM

---

## 📌 Example Use Cases

* 📜 Legal document analysis
* 🏥 Medical report Q&A
* 📊 Research paper understanding
* 📄 Policy/insurance document querying

---

## 🔐 Security Notes

* Do NOT expose `.env` file
* API keys are stored securely using environment variables

---

## 🚀 Future Improvements

* ✅ Multi-document support
* ✅ Chat history & memory
* ✅ Highlight answers in PDF
* ✅ Deploy on Streamlit Cloud / HuggingFace Spaces
* ✅ Structured JSON outputs for explainability

---

## 👩‍💻 Author

**Lakshmi Prasanna Chittiboina**



Give it a ⭐ on GitHub and share your feedback!
