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
        information[email] = email.group()

    phone = re.search(r'(\+?\d[\d\s\-]{8,}\d)', text)
    if phone:
        information["phone"] = phone.group()