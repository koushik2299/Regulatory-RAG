import openai
import numpy as np
import tiktoken
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def chunk_text(text, max_tokens=500):
    """Chunks text into manageable pieces for embedding."""
    encoding = tiktoken.encoding_for_model('text-embedding-ada-002')
    tokens = encoding.encode(text)

    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = encoding.decode(tokens[i:i + max_tokens])
        chunks.append(chunk)
    
    return chunks

def get_embedding(text, model="text-embedding-ada-002"):
    """Generates an embedding for a given text chunk."""
    response = openai.embeddings.create(input=[text], model=model)
    return np.array(response.data[0].embedding)

def process_pdfs_and_generate_embeddings(pdf_folder):
    """Reads PDFs, extracts text, chunks text, and generates embeddings."""
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    all_embeddings = []
    metadata = []

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        text = extract_text_from_pdf(pdf_path)
        chunks = chunk_text(text)

        for chunk in chunks:
            embedding = get_embedding(chunk)
            all_embeddings.append(embedding)
            metadata.append({"source": pdf_file, "chunk_text": chunk})
        
        print(f"✅ Processed {pdf_file}, generated {len(chunks)} embeddings.")

    return all_embeddings, metadata
