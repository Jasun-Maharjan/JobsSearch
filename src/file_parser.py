from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_from_docx(file_path):
    document = Document(file_path)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text


def extract_from_txt(file_path):
    return Path(file_path).read_text(encoding="utf-8")


def extract_resume_text(file_path):
    file_path = Path(file_path)
    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_from_pdf(file_path)
    elif extension == ".docx":
        return extract_from_docx(file_path)
    elif extension == ".txt":
        return extract_from_txt(file_path)
    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )



if __name__ == "__main__":
    resume_text = extract_resume_text(
        "data/resume/CV.pdf"
    )

    print(resume_text)