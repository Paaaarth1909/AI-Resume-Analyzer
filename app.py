from flask import Flask, render_template, request
import os
from utils.parser import extract_text
from utils.matcher import (
    get_similarity_score,
    extract_skills,
    get_missing_skills,
    generate_suggestions
)

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        job_desc = request.form['job_desc']

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        resume_text = extract_text(filepath)

        score = get_similarity_score(resume_text, job_desc)
        skills = extract_skills(resume_text)
        missing_skills = get_missing_skills(resume_text, job_desc)
        suggestions = generate_suggestions(missing_skills)

        return render_template(
            'index.html',
            score=score,
            skills=skills,
            missing_skills=missing_skills,
            suggestions=suggestions
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
