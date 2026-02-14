from flask import Flask, render_template, request, jsonify
from career_roadmap_generator import CareerRoadmapGenerator
import traceback
from pypdf import PdfReader  # Make sure to run: pip install pypdf
import io

app = Flask(__name__)
generator = CareerRoadmapGenerator()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate_roadmap():
    try:
        data = request.json
        report = generator.create_full_report(
            resume=data.get('resume', ''),
            job_description=data.get('job_description', ''),
            job_title=data.get('job_title', ''),
            hours_per_day=int(data.get('hours_per_day', 3))
        )
        # Ensure the resume_analysis has 'feedback' and 'message' fields
        if 'extra_features' in report and 'resume_analysis' in report['extra_features']:
            res_analysis = report['extra_features']['resume_analysis']
            res_analysis['feedback'] = res_analysis.get('message', '')
        
        return jsonify(report)
    except Exception as e:
        print("ERROR:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    try:
        # 1. Get the file and Job Description
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']
        job_description = request.form.get('job_description', '')

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # 2. Extract Text from PDF
        if file and file.filename.endswith('.pdf'):
            reader = PdfReader(file.stream)
            resume_text = ""
            for page in reader.pages:
                resume_text += page.extract_text()
        else:
            return jsonify({"error": "Only PDF files are supported"}), 400

        # 3. Analyze Qualification
        result = generator.assess_qualification(resume_text, job_description)
        
        return jsonify(result)

    except Exception as e:
        print("PDF ERROR:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route('/validate-skill', methods=['POST'])
def validate_skill():
    try:
        data = request.json
        skill = data.get('skill', '')
        quiz = generator.get_skill_quiz(skill)
        return jsonify(quiz)
    except Exception as e:
        print("SKILL VALIDATION ERROR:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

# Additional API endpoints for extended functionality
@app.route('/api/interview-questions', methods=['POST'])
def interview_questions():
    try:
        data = request.json
        role = data.get('role', '')
        questions = generator.get_interview_questions(role)
        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/salary-prediction', methods=['POST'])
def salary_prediction():
    try:
        data = request.json
        role = data.get('role', '')
        experience = int(data.get('experience', 1))
        result = generator.predict_salary(role, experience)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze-profile', methods=['POST'])
def analyze_profile():
    try:
        data = request.json
        resume = data.get('resume', '')
        github = data.get('github', '')
        linkedin = data.get('linkedin', '')
        result = generator.analyze_profile(resume, github, linkedin)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze-job', methods=['POST'])
def analyze_job():
    try:
        data = request.json
        job_description = data.get('job_description', '')
        result = generator.analyze_job(job_description)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)