import streamlit as sl
from pathlib import Path
from src.job.agent import run_job_matching

sl.set_page_config(
    page_title="AI Job Matcher",
    page_icon="🤖",
    layout="wide"
)

sl.markdown("""
<style>

    .main-title {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #6b7280;
        margin-bottom: 40px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    .job-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid #e5e7eb;
    }

    .job-title {
        font-size: 24px;
        font-weight: 700;
    }

    .score {
        font-size: 22px;
        font-weight: 700;
        color: #2563eb;
    }

    .feedback-box {
        background: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #2563eb;
        margin-top: 15px;
    }

</style>
""", unsafe_allow_html=True)


sl.markdown(
    '<div class="main-title">🤖 AI Job Matcher</div>',
    unsafe_allow_html=True
)

sl.markdown(
    '<div class="subtitle">Upload your resume and let AI find the jobs that best match your skills.</div>',
    unsafe_allow_html=True
)


sl.divider()

left, center, right = sl.columns([1, 2, 1])

with center:

    sl.subheader("📄 Upload Your Resume")

    uploaded_file = sl.file_uploader(
        "Supported formats: PDF, DOCX, TXT",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:

        sl.success(f"Uploaded: {uploaded_file.name}")

        file_extension = Path(uploaded_file.name).suffix
        temp_path = f"temp_resume{file_extension}"

        with open(temp_path, "wb") as temp_file:
            temp_file.write(uploaded_file.getvalue())

        analyze_button = sl.button(
            "🔍 Find Matching Jobs",
            use_container_width=True
        )

if uploaded_file and analyze_button:

    progress = sl.progress(0)

    status = sl.empty()

    try:

        status.write("📄 Extracting resume information...")
        progress.progress(25)

        status.write("🧠 Analyzing your skills...")
        progress.progress(50)

        with sl.spinner("🤖 Finding your best job matches and generating AI feedback..."):

            results = run_job_matching(
                temp_path,
                "data/job/Sample_jobs.csv"
            )

        progress.progress(100)
        status.empty()

        sl.success("🎉 Analysis complete!")

        sl.session_state["results"] = results

    except Exception as error:

        progress.empty()
        status.empty()

        sl.error("Something went wrong during analysis.")
        sl.code(str(error))


if "results" in sl.session_state:

    results = sl.session_state["results"]

    sl.markdown(
        '<div class="section-title">🏆 Your Top Job Matches</div>',
        unsafe_allow_html=True
    )

    for rank, result in enumerate(results, start=1):

        score = result["score"]

        sl.markdown(
            f"""
            <div class="job-card">

                <div style="display:flex; justify-content:space-between; align-items:center;">

                    <div class="job-title">
                        #{rank} {result["title"]}
                    </div>

                    <div class="score">
                        {score}% Match
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        sl.progress(min(int(score), 100))

        with sl.expander("🤖 View AI Analysis", expanded=(rank == 1)):

            sl.markdown(
                '<div class="feedback-box">',
                unsafe_allow_html=True
            )

            sl.write(result["feedback"])

            sl.markdown(
                '</div>',
                unsafe_allow_html=True
            )