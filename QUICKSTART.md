# Quick Start Guide

## ⚡ Get Running in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
python app.py
```

### Step 3: Open in Browser
Visit: **http://localhost:5000**

---

## 🎯 Your First Roadmap

1. **Go to Navigator Tab** (default)
2. **Enter Target Job**: e.g., "Senior Data Scientist"
3. **Paste Your Resume/Skills**: Include relevant technologies
4. **Paste Job Description**: From job posting
5. **Click Generate My Plan**

You'll get:
- ✅ Match score (%)
- 💰 Estimated salary range
- 📅 30-day learning roadmap
- 🎯 Skill gap analysis
- 💬 Interview preparation questions

---

## 🔍 Checking Your Resume Against Jobs

1. **Go to PDF Checker Tab**
2. **Upload Your Resume** (PDF format)
3. **Paste Job Requirements**
4. **Click Check Qualification**

Get instant feedback:
- 🟢 Highly Qualified
- 🟡 Potential Match  
- 🔴 Not Qualified Yet

---

## 📚 Available Features

| Feature | Tab | What It Does |
|---------|-----|-------------|
| Create Roadmap | Navigator | Generate 30-day learning plan |
| Resume Analysis | Resume AI | ATS score & skill gaps |
| PDF Check | PDF Checker | Qualification verdict |
| Interview Prep | Interview Coach | Q&A for interviews |
| Relax | Relax Zone | Play snake game 🐍 |

---

## 🛠️ Troubleshooting

**Problem**: "Port 5000 is already in use"
```bash
# Change port in app.py line 115
app.run(debug=True, port=5001)
```

**Problem**: "Module 'pypdf' not found"
```bash
pip install pypdf
```

**Problem**: Static files not loading
- Ensure `static/` folder exists
- Check `style.css` and `script.js` are present

---

## 💡 Pro Tips

- ✍️ Be specific in your resume input (list actual skills)
- 📋 Use complete job descriptions for accuracy
- ⏱️ Set 2-4 hours/day as realistic commitment
- 🎮 Use the game to unwind during learning breaks
- 📊 Check Resume tab after generating roadmap

---

## 🚀 Next Steps

After getting your roadmap:
1. Bookmark the resources mentioned
2. Join programming communities
3. Start with Day 1 tasks
4. Track your progress daily
5. Update your resume as you learn

---

**Happy Career Building! 🎓**
