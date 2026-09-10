import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_job_index(jobs):
    job_text =[]

    for job in jobs:
        job_text.append(job["description"])

    embeddings = model.encode(job_text)
    embeddings = np.array(embeddings).astype("float32")
    #data type needs to be float32 to work with faiss

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index

