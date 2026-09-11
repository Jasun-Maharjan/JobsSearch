import requests

def generate_feedback(resume_text, job):
    prompt = f"""
    You are a job matching assistant.

    Analyze the resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {job}

    Give a short response containing:

    1. Why the candidate matches
    2. Missing skills
    3. One recommendation for improvement
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"]

if __name__ == "__main__":
    resume = "Python developer with experience in Python, SQL and Git."
    job = "Looking for a Python developer with Python, Django, SQL and REST API experience."

    feedback = generate_feedback(resume, job)

    print("\nAI Feedback:\n")
    print(feedback)