from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS_DB = [
    "python", "java", "machine learning", "data analysis",
    "sql", "deep learning", "flask", "javascript", "html", "css"
]


def get_similarity_score(resume, job_desc):
    texts = [resume, job_desc]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)


def extract_skills(text):
    return [skill for skill in SKILLS_DB if skill in text]


def get_missing_skills(resume, job_desc):
    job_skills = [skill for skill in SKILLS_DB if skill in job_desc.lower()]
    resume_skills = extract_skills(resume)

    missing = list(set(job_skills) - set(resume_skills))
    return missing
def generate_suggestions(missing_skills):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Consider adding {skill} to your resume.")

    if not suggestions:
        suggestions.append("Your resume looks strong for this role!")

    return suggestions