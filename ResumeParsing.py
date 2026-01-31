from PyPDF2 import PdfReader
import re
from Dataset.Assets.masterskills import MASTER_SKILLS

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9.+ ]', ' ', text)
    return text


def extract_skills(text, skill_list):
    found_skills = []
    for skill in skill_list:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))

EDUCATION_KEYWORDS = [
    "bachelor", "b.tech", "b.e", "bsc", "msc",
    "master", "m.tech", "phd", "diploma"
]

def extract_education(text):
    education_found = []
    for edu in EDUCATION_KEYWORDS:
        if edu in text:
            education_found.append(edu.upper())
    return list(set(education_found))

def extract_experience(text):
    experience_patterns = [
        r'(\d+)\+?\s+years?',
        r'(\d+)\s+yrs?',
        r'(\d+)\s+year experience'
    ]

    for pattern in experience_patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))

    return 0  # fresher or not mentioned

def parse_resume(file_path):
    raw_text = extract_text_from_pdf(file_path)
    cleaned_text = clean_text(raw_text)

    skills = extract_skills(cleaned_text, MASTER_SKILLS)
    education = extract_education(cleaned_text)
    experience = extract_experience(cleaned_text)

    return {
        "skills": skills,
        "education": education,
        "experience": experience
    }
