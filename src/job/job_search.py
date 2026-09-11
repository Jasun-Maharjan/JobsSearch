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

def calculate_score(distance):
    score = 1/(1+distance)
    return round(score * 100,2)

def search_jobs(resume_text, jobs, index, number_of_results=3):
    resume_embedding = model.encode([resume_text])
    resume_embedding = np.array(resume_embedding).astype("float32")

    distances, positions = index.search(resume_embedding,number_of_results)
    results = []

    for position, distance in zip(positions[0], distances[0]):
        results.append({
            "title": jobs[position]["title"],
            "description": jobs[position]["description"],
            "distance": float(distance),
            "score": calculate_score(float(distance))
        })

    return results