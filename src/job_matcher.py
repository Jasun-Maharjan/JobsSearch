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
    return result["Score"]

def rank_jobs(resume_text,jobs):
    results=[]

    for job in jobs:
        score = check_similarity(resume_text,job["description"])

        results.append({
            "Title": job["title"],
            "Score": score
        })

    results.sort(key=get_score, reverse=True)
    return results

if __name__ == "__main__":
    resume = extract_resume_text("data/resume/CV.pdf")
    sample_job = [{
            "title": "Python Developer",
            "description": """
            Looking for a Python developer with experience
            in machine learning, SQL and backend development.
            """
        },
        {
            "title": "Java Developer",
            "description": """
            Looking for a Java developer with strong
            experience in Spring Boot and Java enterprise systems.
            """
        },
        {
            "title": "Machine Learning Intern",
            "description": """
            Looking for someone with Python, machine learning,
            PyTorch and data analysis experience.
            """
        }]

    results = rank_jobs(resume, sample_job)
    print("Jobs Rankings:-")

    for result in results:
        Match_percent = round(result["Score"]*100, 2)

        print(result["Title"],"-->",Match_percent,"%")


