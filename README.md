# 🏥 Hospital RAG Assistant

An end-to-end **Retrieval-Augmented Generation (RAG)** system that allows users to upload hospital documents (PDFs) and ask natural language questions. The system retrieves relevant information using vector search and generates accurate answers using an LLM.

---

## 🚀 Live Demo

* 🌐 **Frontend (Streamlit):** https://hospital-rag-55cjnvm2sx7awzvkgjeaau.streamlit.app/
* ⚙️ **Backend (FastAPI):** https://hospital-rag-1.onrender.com

---

## 🧠 Project Overview

This project implements a **production-level RAG pipeline**:

```
User Query → Embedding → Vector Search → Context Retrieval → LLM → Answer
```

It ensures:

* ✅ Accurate answers from documents only
* ❌ No hallucination (strict prompt control)
* ✅ Source attribution (page numbers + text)

---

## 🧩 Features

### ✅ Core Features

* 📄 PDF Upload & Processing
* 🔍 Semantic Search using pgvector (Supabase)
* 🤖 LLM-based Answer Generation (Groq - LLaMA 3.1)
* 📌 Source Attribution (Page + Content)
* 🚫 Hallucination Control

---

### ⭐ Bonus Features

* 🎨 Streamlit UI (Interactive frontend)
* 📁 Multi-document support
* 💬 Chat history memory
* 🖍 Highlighted source text
* 🎤 Voice input (local only)

---

## 🏗️ Tech Stack

| Layer       | Technology                       |
| ----------- | -------------------------------- |
| Backend     | FastAPI                          |
| Frontend    | Streamlit                        |
| Database    | Supabase (PostgreSQL + pgvector) |
| Embeddings  | Sentence Transformers (MiniLM)   |
| LLM         | Groq (LLaMA 3.1)                 |
| PDF Parsing | PyMuPDF                          |
| Deployment  | Render + Streamlit Cloud         |

---

## ⚙️ System Architecture

```
PDF → Text Extraction → Chunking → Embeddings → Supabase (pgvector)
                                                     ↓
User Query → Embedding → Similarity Search → Top-K Chunks
                                                     ↓
                    Context Injection → LLM → Answer
```

---

## 📂 Project Structure

```
hospital-rag-assistant/
│
├── app/
│   ├── main.py        # FastAPI routes
│   ├── ingest.py      # PDF processing + embeddings
│   ├── rag.py         # Retrieval + LLM
│   ├── db.py          # Supabase connection
│   └── utils.py       # Chunking logic
│
├── data/              # Uploaded PDFs
├── streamlit_app.py   # Frontend UI
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## 🔧 Setup Instructions (Local)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/yourusername/hospital-rag.git
cd hospital-rag
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create `.env`:

```env
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
GROQ_API_KEY=your_key
```

---

### 5️⃣ Run backend

```bash
python -m uvicorn app.main:app --reload
```

---

### 6️⃣ Run frontend

```bash
streamlit run streamlit_app.py
```

---

## 📊 Example Queries

* What are OPD timings?
* Who is the cardiologist?
* What is the cost of MRI?
* Can I cancel appointment within 24 hours?
* What is ICU cost per day?
* Emergency number?

---

## ⚠️ Important Constraints

* ❌ The model does NOT use general knowledge
* ✅ Answers are strictly based on retrieved document context
* ❌ If answer not found →
  `"I don't have that information in the provided document."`

---

## 🧠 Key Learnings

* Implemented **vector similarity search (cosine distance)**
* Built **end-to-end RAG pipeline**
* Integrated **LLM with structured prompt engineering**
* Designed **scalable document retrieval system**
* Developed **full-stack AI application**

---

## 💼 Resume Points

* Built a production-grade RAG system using FastAPI, Supabase (pgvector), and Groq LLM
* Implemented semantic search with Sentence Transformers for document retrieval
* Developed an interactive Streamlit UI with multi-document support and chat memory
* Ensured hallucination-free responses using context-grounded prompting

---

## 📌 Future Improvements

* 🔄 Persistent chat memory (database-based)
* 🌐 Multi-language support
* 📊 Better highlighting with NLP
* ☁️ Docker deployment

---

## 👩‍💻 Author

**Mahak Taneja**
B.Tech CSE | AI/ML Enthusiast

---

⭐ If you like this project, give it a star!
