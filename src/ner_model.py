import re
from file_parser import extract_resume_text

def extract_information(text):
    information={
        "email" : None,
        "phone": None,
        "skills": [],
        "education": [],
        "experience": []
    }

    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    if email:
        information["email"] = email.group()

    phone = re.search(r'(?<!\d)(?:\+977[-\s]?)?(?:98|97)\d{8}(?!\d)', text)
    if phone:
        information["phone"] = phone.group()

    possible_skills = ["Python","Java","C","C#","C++","Rust","Swift","Javascript","HTML","CSS","React","Node.js"
        "Django","Flask","Relational Databases","SQL","SQLite","Spring Boot","Machine Learning","Artificial Intelligence",
        "AI","Deep Learning","Typescript","TailwindCSS","JDBC","PyTorch","Docker","Git","Github","AWS","Docker"]

    for skill in possible_skills:
        if skill.lower() in text.lower():
            information["skills"].append(skill)
    return information

if __name__ == "__main__":

    resume_path = "data/resume/CV.pdf"

    resume_text = extract_resume_text(resume_path)

    information = extract_information(resume_text)
    print(information)