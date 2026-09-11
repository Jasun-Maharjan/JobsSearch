from src.file_parser import extract_resume_text
from src.job.job_loader import load_jobs
from src.job.job_search import create_job_index, search_jobs

resume_file = "data/resume/CV.pdf"
resume = extract_resume_text(resume_file)

jobs = load_jobs("data/job/Sample_jobs.csv")

index = create_job_index(jobs)

results = search_jobs(resume, jobs, index, number_of_results=3)

print("\nMost Matching Jobs\n")
for result in results:
    print("Job: ",result["title"])
    print("Match score: ", result["score"], "%")
    print()