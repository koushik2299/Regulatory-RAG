import os
from embedding_utils import process_pdfs_and_generate_embeddings

# Folder where PDFs were downloaded
pdf_folder = "downloaded_pdfs"

if __name__ == "__main__":
    # Process the PDFs and generate embeddings
    embeddings, metadata = process_pdfs_and_generate_embeddings(pdf_folder)

    print("\n🎉 Successfully generated embeddings for the 3 PDFs!")
    print(f"Total Chunks Processed: {len(metadata)}")
