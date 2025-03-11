import faiss
import numpy as np
import pickle
from utils.embedding_utils import get_embedding

# File to store FAISS index
FAISS_INDEX_FILE = "faiss_index.pkl"
METADATA_FILE = "metadata.pkl"

# Initialize FAISS index (will be created dynamically)
index = None
metadata = []

def store_embeddings(embeddings, metadata_list):
    """Stores embeddings in FAISS."""
    global index, metadata

    embeddings = np.array(embeddings).astype('float32')

    if index is None:
        index = faiss.IndexFlatL2(embeddings.shape[1])  # Create FAISS index
        index.add(embeddings)
    else:
        index.add(embeddings)

    metadata.extend(metadata_list)  # Store metadata for later retrieval

    # Save index and metadata to disk
    with open(FAISS_INDEX_FILE, "wb") as f:
        pickle.dump(index, f)
    with open(METADATA_FILE, "wb") as f:
        pickle.dump(metadata, f)

    print("✅ Embeddings successfully stored in FAISS!")

def search_similar_text(query, top_k=3):
    """Performs a similarity search in FAISS."""
    global index, metadata

    if index is None:
        with open(FAISS_INDEX_FILE, "rb") as f:
            index = pickle.load(f)
        with open(METADATA_FILE, "rb") as f:
            metadata = pickle.load(f)

    query_embedding = get_embedding(query).astype('float32').reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for i in range(top_k):
        if indices[0][i] < len(metadata):  # Ensure valid index
            results.append({
                "source": metadata[indices[0][i]]["source"],
                "chunk_text": metadata[indices[0][i]]["chunk_text"],
                "distance": distances[0][i]
            })

    return results
