#CareerMatch AI 

##AI-powered resume and job matching platform

CareerMatch AI is an AI-powered job matching application that analyzes a user's resume and identifies the most relevant job opportunities. The system extracts resume text from PDF, DOCX, or TXT files, converts resume and
job descriptions into semantic embeddings, uses a vector search system to retrieve relevant jobs, and uses a local Ollama language model to generate personalized feedback about why the candidate matches, which
skills may be missing, and how the candidate can improve. The application provides the results through a Streamlit web interface.

How the project works:

Prerequisites:-

Make sure the following are installed:
- Python 3.10+
- Ollama
- A compatible Ollama language model

Install Python dependencies

From the project root:
python -m pip install streamlit pypdf python-docx sentence-transformers scikit-learn faiss-cpu pandas requests

Project structure:

JobLens/
│
├── app.py
│
├── data/
│   ├── resume/
│   │   └── CV.pdf
│   │
│   └── job/
│       └── Sample_jobs.csv
│
└── src/
    ├── file_parser.py
    │
    └── job/
        ├── agent.py
        ├── job_loader.py
        ├── job_matcher.py
        ├── vector_store.py
        └── llm_feedback.py

Technologies Used
1. Python --- Core development language
2. Streamlit --- Web interface
3. PyPDF --- PDF text extraction
4. python-docx --- DOCX text extraction
5. Sentence Transformers --- Semantic embeddings
6. FAISS --- Vector similarity search
7. Pandas --- Job dataset processing
8. Ollama --- Local large language model inference
9. Requests --- Communication with the Ollama API
