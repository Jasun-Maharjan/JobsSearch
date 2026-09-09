import re

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

    phone = re.search(r'(\+?\d[\d\s\-]{8,}\d)', text)
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

    sample_text = """
    John Doe
    john@example.com
    +977 9812345678

    Skills:
    Python, Java, SQL, PyTorch, Git
    """

    result = extract_information(sample_text)

    print(result)