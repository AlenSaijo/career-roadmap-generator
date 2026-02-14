# Career Roadmap Generator 🚀

> An AI-powered web application that generates personalized 30-day career development roadmaps. Upload your resume, analyze job requirements, and get actionable learning plans with interview prep and salary predictions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask 2.3](https://img.shields.io/badge/Flask-2.3-green.svg)](https://flask.palletsprojects.com/)

## 📋 Project Structure

```
career_roadmap_generator/
├── career_roadmap_generator.py    # Core business logic
├── app.py                         # Flask backend API
├── templates/
│   └── home.html                 # Main frontend interface
├── static/
│   ├── style.css                 # Styling
│   └── script.js                 # JavaScript functionality
├── career_roadmap.json           # Sample data
└── roadmaps/                     # Generated roadmaps storage
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install flask pypdf
```

### Step 2: Run the Application

```bash
python app.py
```

The application will start at: **http://localhost:5000**

## 🎯 Features

### 1. **AI Career Navigator** (Home Tab)
   - Input your target job title
   - Paste your resume/skills summary
   - Provide job description requirements
   - Get a 30-day personalized learning roadmap
   - View match percentage and estimated salary

### 2. **Resume AI** (Resume Tab)
   - Automatic resume analysis
   - ATS score calculation
   - Missing keywords identification
   - Skill gap analysis
   - Actionable recommendations

### 3. **PDF Qualification Checker** (PDF Checker Tab)
   - Upload your PDF resume
   - Paste job description
   - Get qualification verdict (Highly Qualified, Potential Match, Not Qualified Yet)
   - Identify matched and missing critical skills
   - Receive tailored improvement suggestions

### 4. **Interview Coach** (Interview Coach Tab)
   - Role-specific technical interview questions
   - Interactive skill validation quiz
   - XP-based scoring system
   - Confidence tracking

### 5. **Relax Zone - Snake Game** (Relax Zone Tab)
   - Classic Snake game implementation
   - Use arrow keys to control
   - Stress relief during learning breaks

## 🔌 API Endpoints

### Main Endpoints

#### `POST /generate`
Generates complete career roadmap report
```json
{
  "job_title": "Data Scientist",
  "resume": "Your resume text...",
  "job_description": "Job requirements...",
  "hours_per_day": 3
}
```

#### `POST /upload-resume`
Analyzes PDF resume against job description
- Form Data: `file` (PDF), `job_description` (text)

#### `POST /validate-skill`
Gets skill validation quiz
```json
{
  "skill": "python"
}
```

### Additional API Routes

- `POST /api/interview-questions` - Get role-specific questions
- `POST /api/salary-prediction` - Predict salary based on role/experience
- `POST /api/analyze-profile` - In-depth profile analysis
- `POST /api/analyze-job` - Job requirement analysis

## 📊 Response Examples

### Generate Roadmap Response
```json
{
  "target_role": {
    "title": "Data Scientist",
    "match_percentage": 65
  },
  "gamification": {
    "total_points": 250
  },
  "roadmap": [
    {
      "day": 1,
      "week": 1,
      "focus": "Python Fundamentals",
      "task": "Learn Python basics",
      "points": 10,
      "duration_hours": 3
    }
  ],
  "extra_features": {
    "resume_analysis": {
      "status": "Potential Match",
      "score": 65,
      "message": "You have key skills but gaps exist...",
      "matched_skills": ["Python", "SQL"],
      "missing_skills": ["PySpark", "TensorFlow"]
    }
  }
}
```

## 🎨 Customization

### Changing Colors
Edit the CSS variables in `static/style.css`:
```css
:root {
    --bg: #0f172a;          /* Background */
    --surface: #1e293b;      /* Card background */
    --primary: #6366f1;      /* Primary accent */
    --accent: #8b5cf6;       /* Secondary accent */
    --text: #f1f5f9;         /* Text color */
    --text-dim: #94a3b8;     /* Dimmed text */
}
```

### Modifying Game Parameters
Edit `static/script.js` game settings:
- Snake speed: Change `setInterval(gameLoop, 100)`
- Grid size: Modify the `20` pixel multipliers
- Canvas size: Update gameCanvas width/height

## 📱 Browser Compatibility
- Chrome/Chromium (Recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (responsive design included)

## 🔧 Troubleshooting

### Issue: "pypdf not found"
```bash
pip install pypdf
```

### Issue: Port 5000 already in use
Change the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to different port
```

### Issue: Static files not loading
Ensure the `static/` folder exists and contains `style.css` and `script.js`

### Issue: PDF upload fails
- Ensure file is valid PDF format
- Check file size (should be reasonable)
- Verify pypdf is properly installed

## 🚀 Advanced Usage

### Using Environment Variables
```python
import os
app.run(debug=os.getenv('DEBUG', False), port=int(os.getenv('PORT', 5000)))
```

### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### Production Deployment
Install production server:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📚 API Architecture

```
┌─────────────────┐
│   Frontend      │
│  (HTML+CSS+JS)  │
└────────┬────────┘
         │ HTTP Requests
         ▼
┌─────────────────┐
│  Flask Backend  │
│   (app.py)      │
└────────┬────────┘
         │ Business Logic
         ▼
┌─────────────────────────────────┐
│ CareerRoadmapGenerator Engine    │
│ (career_roadmap_generator.py)    │
└─────────────────────────────────┘
```

## 🔐 Security Notes

- Never expose API keys in frontend code
- Validate all user inputs on backend
- Sanitize PDF uploads
- Use environment variables for configuration
- Implement rate limiting for production

## 📝 Data Flow

1. **User Input** → Frontend collects resume, job description, preferences
2. **API Call** → Frontend sends data to Flask backend
3. **Processing** → CareerRoadmapGenerator analyzes inputs
4. **Response** → Backend returns structured roadmap and insights
5. **Display** → Frontend renders interactive dashboard

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [CSS Grid & Flexbox](https://css-tricks.com/)

## 💡 Tips for Best Results

1. **Resume Input**: Include specific technical skills, frameworks, and tools
2. **Job Description**: Paste complete requirements for accurate matching
3. **Hours/Day**: Set realistic time commitment (2-4 hours recommended)
4. **Regular Updates**: Update profile as you learn new skills
5. **Track Progress**: Monitor points and complete daily tasks

## 🤝 Contributing

To extend functionality:
1. Add new endpoints in `app.py`
2. Create corresponding frontend handlers in `static/script.js`
3. Update `career_roadmap_generator.py` with new business logic

## 📧 Support

For issues or feature requests, check the application logs:
```bash
tail -f app.log
```

## ⚖️ License

This project is provided as-is for educational purposes.

---

**Happy Learning! 🚀**
