# 🧠 Multimodal Data Processing System

A **FastAPI + Streamlit** based system that processes and searches across **text, image, audio, and video** files using AI.  
It performs **OCR**, **speech-to-text transcription**, **chunking**, **embedding generation**, and **semantic search** — all inside one unified interface.

---

## 🚀 Features

✅ Supports multiple input types:

| File Type | Supported Formats | Processing Type |
|------------|------------------|-----------------|
| **Text** | `.pdf`, `.docx`, `.pptx`, `.md`, `.txt` | Extracts readable text |
| **Image** | `.png`, `.jpg`, `.jpeg` | OCR using Tesseract |
| **Audio / Video** | `.mp3`, `.mp4`, `.wav`, `.m4a`, `.aac`, `.flac` | Speech-to-text using Whisper |
| **YouTube** | YouTube URLs | Downloads & transcribes |

✅ Chunk-based text segmentation  
✅ Vector embeddings using `SentenceTransformer` + `FAISS`  
✅ Search across multimodal content  
✅ Ask questions via Streamlit UI  
✅ Ready for Gemini or any LLM integration  

---

## 🧩 System Architecture

📂 Multimodal Data Processing System/
│
├─ app/
│ ├─ main.py # FastAPI backend (file upload, query)
│ ├─ parsers.py # Extracts text from all formats
│ ├─ ocr.py # OCR using pytesseract
│ ├─ audio.py # Handles YouTube/audio transcription
│ ├─ chunker.py # Splits text into chunks for embeddings
│ ├─ embed_store.py # Manages FAISS vector store
│ ├─ llm_client.py # LLM (Gemini/OpenAI) integration
│
├─ ui_streamlit.py # Streamlit frontend (user interface)
├─ requirements.txt # Python dependencies
└─ README.md # Documentation

yaml
Copy code

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/multimodal-data-processing-system.git
cd multimodal-data-processing-system/app
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv myenv
myenv\Scripts\activate       # On Windows
# or
source myenv/bin/activate    # On macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🧠 Run the Application
Step 1: Start FastAPI Backend
bash
Copy code
cd app
python main.py
✅ Backend will start at:

arduino
Copy code
http://localhost:8000
Step 2: Start Streamlit Frontend
In a new terminal (while backend is running):

bash
Copy code
streamlit run ui_streamlit.py
✅ Streamlit app will open at:

arduino
Copy code
http://localhost:8501
🧪 How It Works
1️⃣ Upload Files

Upload one or more files (PDF, DOCX, PPTX, TXT, MD, PNG, JPG, MP3, MP4, etc.)

FastAPI reads and parses the content using:

PyPDF2, python-docx, python-pptx for text

pytesseract for OCR

whisper for speech-to-text

Each file is chunked into small segments for efficient search.

The chunks are converted into vector embeddings using SentenceTransformer (MiniLM).

Embeddings are stored in a FAISS vector index.

2️⃣ Ask Questions

Enter a natural-language question in the Streamlit UI.

The system searches the FAISS vector store for the most relevant chunks.

Optionally, the system can use Gemini (or any LLM) for a more contextual answer.

3️⃣ Get Answers

The UI displays the answer and the top matching content snippets.

📊 Example Usage
Upload files
→ Choose a resume.pdf and a meeting.mp3
→ Click "Upload"

Ask a question
→ “What did we discuss about pricing?”
→ Get AI-powered answers extracted from audio transcription and text files.

🧰 Tech Stack
Layer	Technology
Backend	FastAPI
Frontend	Streamlit
Embeddings	Sentence Transformers (all-MiniLM-L6-v2)
Vector Store	FAISS
OCR	pytesseract
Speech-to-Text	Whisper
LLM	Gemini (stubbed) / OpenAI-compatible
Others	PyPDF2, python-docx, pydub, yt-dlp, markdown