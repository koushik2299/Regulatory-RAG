import os
from embedding_utils import process_pdfs_and_generate_embeddings
from vector_store import store_embeddings, search_similar_text

# Folder where PDFs were downloaded
pdf_folder = "downloaded_pdfs"

if __name__ == "__main__":
    # Step 1: Process PDFs → Generate embeddings
    embeddings, metadata = process_pdfs_and_generate_embeddings(pdf_folder)

    # Step 2: Store embeddings in FAISS
    store_embeddings(embeddings, metadata)

    print("\n🎉 Successfully stored embeddings in FAISS. Now performing a test search...")

    # Step 3: Test search query
    query = "What are the FDA regulations for drug approval?"
    search_results = search_similar_text(query)

    print("\n🔍 Search Results:")
    for result in search_results:
        print(f"\n📄 Source: {result['source']}")
        print(f"📜 Text Chunk: {result['chunk_text'][:300]}...")
        print(f"🔢 Distance Score: {result['distance']:.4f}\n")
