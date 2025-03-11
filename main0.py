import os
from utils.gcs_utils import download_pdf, list_pdfs
from utils.pdf_utils import extract_text_from_pdf

# Folder where PDFs will be downloaded
download_folder = "downloaded_pdfs"
os.makedirs(download_folder, exist_ok=True)  # Create the folder if it doesn't exist

def download_and_extract(bucket_name, source_blob_name, local_pdf_path):
    """Downloads a PDF, extracts text, and keeps the PDF (no deletion)."""
    download_pdf(bucket_name, source_blob_name, local_pdf_path)
    text = extract_text_from_pdf(local_pdf_path)
    return text  # Keep PDF, do not delete

if __name__ == "__main__":
    bucket_name = "datastorev1"

    # Get list of PDFs, but limit to first 3 only
    pdf_files = list_pdfs(bucket_name, prefix="Guidelines/")[:3]

    for pdf_file in pdf_files:
        pdf_filename = pdf_file.split('/')[-1]
        local_pdf_path = os.path.join(download_folder, pdf_filename)

        extracted_text = download_and_extract(bucket_name, pdf_file, local_pdf_path)

        print(f"✅ Extracted text from {pdf_file} (Stored in: {local_pdf_path})")

    print(f"\n🎉 First 3 PDFs downloaded and stored in `{download_folder}/` successfully!")
