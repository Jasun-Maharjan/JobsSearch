from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from file_parser import extract_resume_text

model = SentenceTransformer("all-MiniLM-L6-v2")

def check_similarity(resume_text, job_text):
    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_text])

    similarity = cosine_similarity(resume_embedding,job_embedding)

    return similarity[0][0]

def get_score(result):
    return result["score"]

def rank_jobs(resume_text,jobs):
    results=[]

    for job in jobs:
        score = cosine_similarity(resume_text,job["description"])

        results.append({
            "Title": job["title"],
            "Similarity score": score
        })

    results.sort(key=get_score, reverse=True)
    return results

if __name__ == "__main__":
    resume = extract_resume_text("data/resume/CV.pdf")
    sample_job = []

    results = rank_jobs(resume, sample_job)
    print("Jobs Rankings:-")

    for result in results:
        Match_percent = round(result["score"]*100, 2)

        print(result["Title"],"-->",Match_percent,"%")


