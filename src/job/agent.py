from src.file_parser import extract_resume_text
from src.job.job_loader import load_jobs
from src.job.job_matcher import create_job_index, search_jobs
from src.job.llm_feedback import generate_feedback

def run_job_matching(resume_file, jobs_file):
    resume = extract_resume_text(resume_file)
    jobs = load_jobs(jobs_file)
    index = create_job_index(jobs)
    results = search_jobs(resume,jobs,index,number_of_results=3)

    for result in results:
        feedback = generate_feedback(resume, result["description"])
        result["feedback"] = feedback

    return results

