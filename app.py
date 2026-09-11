import streamlit as sl
from pathlib import Path
from src.job.agent import run_job_matching

sl.set_page_config(
    page_title="AI Job Matcher",
    layout="centered"
)

sl.title("AI Job Matcher")
sl.write("Upload your resume to find the most relevant jobs.")

file = sl.file_uploader("Upload your resume",type=["pdf", "docx", "txt"])

if file:
    file_extension = Path(file.name).suffix
    temp_path = f"temp_resume{file_extension}"

    with open(temp_path, "wb") as temp_file:
        temp_file.write(file.read())

    if sl.button("Find Matching Jobs"):
        with sl.spinner("Analyzing your resume..."):
            results = run_job_matching(
                temp_path,
                "data/job/Sample_jobs.csv"
            )

        sl.success("Analysis complete!")

        for result in results:
            sl.subheader(result["title"])
            sl.write(f"Match Score: {result['score']}%")
            sl.write("### AI Feedback")
            sl.write(result["feedback"])