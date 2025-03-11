# 📜 Regulatory RAG Assistant
**A Retrieval-Augmented Generation (RAG) system for regulatory documents, leveraging OpenAI embeddings and FAISS for efficient semantic search.**

---

## 🚀 **Overview**
This project processes **regulatory PDFs**, extracts key information, and enables **semantic search** using OpenAI’s `text-embedding-ada-002` model and FAISS (vector search). The system is designed to help **regulatory affairs experts** quickly retrieve relevant guidelines, policies, and FDA documentation.

✅ Extracts text from **PDFs stored in Google Cloud Storage**  
✅ Converts text into **embeddings using OpenAI**  
✅ Stores embeddings in **FAISS** (efficient local vector search)  
✅ Performs **semantic search** for regulatory queries  

---

## 🛠️ **Installation**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/Regulatory-RAG.git
cd Regulatory-RAG
```

### 2️⃣ **Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up OpenAI API Key**
1. Create a `.env` file in the project root:
```bash
touch .env
```
2. Add your **OpenAI API Key** inside `.env`:
```text
OPENAI_API_KEY=your-openai-api-key-here
```

---

## 📂 **Project Structure**
```
📜 Regulatory-RAG/
│── downloaded_pdfs/       # 📂 PDFs downloaded from GCP
│── embeddings/            # 📂 Stores FAISS embeddings (auto-created)
│── .env                   # 🔑 API Key (ignored in Git)
│── .gitignore             # 🚫 Ignores sensitive files
│── README.md              # 📄 Project Documentation
│── requirements.txt       # 📦 Required dependencies
│── main.py                # 🚀 Main script to run the pipeline
│── gcs_utils.py           # 📥 Fetches PDFs from GCP
│── pdf_utils.py           # 📖 Extracts text from PDFs
│── embedding_utils.py     # 🔍 Embedding generation and text chunking
│── vector_store.py        # 🗄️ FAISS-based search & retrieval
```

---

## 🔥 **How to Run the Project**
### 1️⃣ **Download & Process PDFs from GCP**
```bash
python main.py
```
✅ This will:
- Download **3 PDFs from Google Cloud Storage**  
- Extract text  
- Generate **OpenAI embeddings**  
- Store them in **FAISS**  

### 2️⃣ **Perform a Test Search**
Modify the search query in `main.py`:
```python
query = "What are the FDA regulations for drug approval?"
search_results = search_similar_text(query)
```

Then, run:
```bash
python main.py
```

Example Output:
```bash
🎉 Successfully stored embeddings in FAISS. Now performing a test search...

🔍 Search Results:

📄 Source: 094.pdf
📜 Text Chunk: "FDA guidance on Substantial Equivalence Determinations..."
🔢 Distance Score: 0.3734
```

---

## ⚙️ **Customization**
### 📌 **Change the Number of PDFs**
Modify the `main.py` script:
```python
pdf_files = list_pdfs(bucket_name, prefix="Guidelines/")[:3]  # Change '3' to desired number
```

### 📌 **Improve Search Results**
- **Increase chunk size** in `embedding_utils.py`:
  ```python
  def chunk_text(text, max_tokens=1000):  # Increase to get better context
  ```
- **Use a better query** → Instead of **"What are FDA regulations?"**, try:  
  🟢 `"What is the FDA approval process for new drugs?"`  

---

## 🛠️ **Future Improvements**
✅ **Deploy FAISS on a cloud server**  
✅ **Implement Hybrid Search (BM25 + FAISS)**  
✅ **Integrate GPT-4 for regulatory summaries**  
✅ **Build a Web UI for better interaction**  

---

## 🤝 **Contributing**
Pull requests are welcome! Please follow the best practices when submitting improvements. 

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 👨‍💻 **Author**
**Koushik**  
📩 Contact: [your email]  
🌐 GitHub: [your GitHub profile]
