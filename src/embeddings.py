from sentence_transformers import SentenceTransformer
from file_parser import extract_resume_text

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text):
    embedding = model.encode(text) #turns human language into numeric vectors
    return embedding

if __name__ == "__main__":
    resume_path = "data/resume/CV.pdf"

    CV_text = extract_resume_text(resume_path)
    CV_embedding = create_embedding(CV_text)

    print("Embedding done")
    print("Values",len(CV_embedding))
    print(CV_embedding[:10])