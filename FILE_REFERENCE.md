# 📑 File Reference Index

Quick lookup guide for all files in the Career Roadmap Generator project.

---

## 🔧 Core Application Files

### `app.py`
**Purpose**: Flask backend server and API endpoints  
**Created/Updated**: Core Flask application  
**Key Functions**:
- `/` - Serves main HTML interface
- `/generate` - Creates career roadmap (POST)
- `/upload-resume` - Analyzes PDF resume (POST)
- `/validate-skill` - Gets skill quiz (POST)
- Additional API endpoints for extended features

**Usage**: `python app.py` to start server

**Modifications**: 
- Change port number
- Add authentication
- Configure database connection

---

### `career_roadmap_generator.py`
**Purpose**: Core business logic and algorithms  
**Contains**: 
- `CareerRoadmapGenerator` class
- Skill extraction methods
- Roadmap generation algorithms
- Interview question database
- Salary prediction logic
- Resume qualification assessment

**Main Methods**:
- `create_full_report()` - Generate complete career analysis
- `assess_qualification()` - Check qualifications against job
- `generate_roadmap()` - Create 30-day learning plan
- `get_interview_questions()` - Get interview prep questions
- `predict_salary()` - Estimate salary range

**No Modifications Needed** - Already fully functional

---

## 🎨 Frontend Files

### `templates/home.html`
**Purpose**: Main user interface template  
**Contains**:
- Navigation sidebar
- 5 main tabs (Navigator, Resume AI, PDF Checker, Interview Coach, Relax Zone)
- Form inputs and display areas
- Canvas for game
- Links to CSS and JS files

**Key Sections**:
```html
<div id="home">         - Navigator tab (main roadmap generator)
<div id="resume">       - Resume analyzer tab
<div id="upload">       - PDF qualification checker tab
<div id="interview">    - Interview preparation tab
<div id="game">         - Snake game tab
```

**When to Modify**: 
- Add new tabs/features
- Change form labels
- Add input fields
- Modify layout structure

---

### `static/style.css`
**Purpose**: Styling and layout theming  
**Contains**:
- CSS variables for theme colors
- Responsive design rules
- Component styles (cards, buttons, badges)
- Animations and transitions
- Media queries for mobile

**Key CSS Variables**:
```css
--bg: #0f172a;           /* Background color */
--surface: #1e293b;      /* Card/surface background */
--primary: #6366f1;      /* Primary action color */
--accent: #8b5cf6;       /* Secondary accent color */
--text: #f1f5f9;         /* Text color */
--text-dim: #94a3b8;     /* Dimmed text color */
```

**When to Modify**:
- Change color scheme
- Adjust spacing/padding
- Modify responsive breakpoints
- Update animations

---

### `static/script.js`
**Purpose**: Frontend interactivity and API communication  
**Contains**:
- Section navigation logic
- Form validation
- API fetch calls
- Response processing
- DOM manipulation
- Snake game implementation

**Key Functions**:
- `showSection(id)` - Switch between tabs
- `generateRoadmap()` - Call /generate API
- `checkQualification()` - Upload and analyze PDF
- `checkAnswer()` - Validate quiz responses
- `startGame()` - Initialize snake game
- `gameLoop()` - Game update logic

**When to Modify**:
- Add new API calls
- Change game mechanics
- Modify validation logic
- Update response handling

---

## 📖 Documentation Files

### `README.md` - COMPREHENSIVE GUIDE
**Page Length**: ~500 lines  
**Sections**:
- Project overview and structure
- Installation & setup instructions
- Feature descriptions
- API endpoint documentation
- Response examples
- Customization guide
- Troubleshooting section
- Advanced usage and deployment

**Best For**: Learning everything about the project

**Read When**: First time setup, feature exploration, deployment

---

### `QUICKSTART.md` - FAST SETUP GUIDE
**Page Length**: ~80 lines  
**Sections**:
- 3-step installation
- First roadmap generation walkthrough
- 5-minute feature overview
- Simple troubleshooting
- Pro tips

**Best For**: Getting running immediately  

**Read When**: Just want to start using the app quickly

---

### `CONFIG.md` - ADVANCED CONFIGURATION
**Page Length**: ~400 lines  
**Sections**:
- Virtual environment setup
- Flask configuration modes
- UI customization
- API customization
- Database setup
- Game configuration
- Security setup
- Docker deployment
- Environment variables
- Performance optimization
- Testing setup

**Best For**: Customization and deployment  

**Read When**: Want to change colors, deploy to production, add database

---

### `SETUP_SUMMARY.md` - ARCHITECTURE OVERVIEW
**Page Length**: ~300 lines  
**Sections**:
- Project structure visualization
- Connection flow diagrams
- API endpoint reference table
- Data flow explanation
- Technology stack
- File responsibility summary
- Deployment options
- Verification checklist

**Best For**: Understanding how everything works together  

**Read When**: Want complete system architecture overview

---

## 📦 Configuration & Dependency Files

### `requirements.txt`
**Purpose**: Python package dependencies  
**Contents**:
```
Flask==2.3.3
pypdf==3.18.0
Werkzeug==2.3.7
```

**Usage**: `pip install -r requirements.txt`

**When to Update**: Adding new Python packages

**Installation Method**: 
```bash
# In virtual environment
pip install -r requirements.txt

# Or in conda
conda install -c pip -r requirements.txt
```

---

## 📊 Data Files

### `career_roadmap.json`
**Purpose**: Sample generated roadmap  
**Format**: JSON structure with example roadmap data  
**Usage**: Reference for expected API response structure  
**When to Use**: 
- Understanding response format
- Manual testing
- Template for saved roadmaps

---

### `roadmaps/` (Directory)
**Purpose**: Storage for generated roadmaps  
**Contains**: Generated JSON files for user roadmaps  
**Auto-created**: On first roadmap generation  

**File Naming Convention** (optional):
```
roadmap_20240214_143022.json
        ^date      ^time
```

---

## 🗂️ Other Project Directories

### `templates/` Directory
**Contains**: HTML template files  
**Currently**: 
- `home.html` - Main interface template
- All template files here are served by Flask

**When to Add**: 
- New HTML pages
- Email templates
- Report templates

---

### `static/` Directory
**Contains**: Static assets (CSS, JS, images, fonts)  
**Currently**:
- `style.css` - Stylesheet
- `script.js` - JavaScript
- Can be extended with images, icons, fonts

**File Organization**:
```
static/
├── style.css
├── script.js
├── images/ (optional)
├── fonts/ (optional)
└── icons/ (optional)
```

---

### `__pycache__/` Directory
**Purpose**: Python bytecode cache (auto-generated)  
**Safe to**: Delete (will be recreated)  
**Do Not**: Manually edit files here

---

### `roadmaps/` Directory
**Purpose**: Generated roadmap storage  
**Created**: Automatically on first use  
**Contains**: JSON files of generated roadmaps  

---

## 📋 File Modification Guide

### High Priority (Likely to Modify)
| File | Reason | Difficulty |
|------|--------|-----------|
| `static/style.css` | Change colors/theme | ⭐ Easy |
| `career_roadmap_generator.py` | Add skills/customization | ⭐⭐ Medium |
| `static/script.js` | Add new features | ⭐⭐ Medium |
| `templates/home.html` | Modify layout/add tabs | ⭐⭐ Medium |

### Medium Priority (Occasional Modification)
| File | Reason | Difficulty |
|------|--------|-----------|
| `app.py` | Add API endpoints | ⭐⭐ Medium |
| `requirements.txt` | Add Python packages | ⭐ Easy |
| `README.md` | Update documentation | ⭐ Easy |

### Low Priority (Rarely Modified)
| File | Reason | Difficulty |
|------|--------|-----------|
| `CONFIG.md` | Update guide | ⭐ Easy |
| `QUICKSTART.md` | Update guide | ⭐ Easy |
| Other docs | Update guides | ⭐ Easy |

---

## 🔄 File Dependencies

```
app.py
├── imports: career_roadmap_generator.py
├── imports: Flask framework
├── serves: templates/home.html
├── serves: static/style.css
└── serves: static/script.js

career_roadmap_generator.py
├── used by: app.py
└── imported as: CareerRoadmapGenerator class

templates/home.html
├── linked CSS: static/style.css
├── linked JS: static/script.js
└── served by: app.py

static/style.css
├── linked from: templates/home.html
└── applies to: HTML elements

static/script.js
├── linked from: templates/home.html
├── calls: app.py API endpoints
└── manipulates: HTML DOM
```

---

## 🎯 Common Tasks & Which Files to Edit

### Change the App's Color Theme
**Edit**: `static/style.css` (lines 1-10)  
**Modify**: CSS variables in `:root` selector

### Add a New Skill Category
**Edit**: `career_roadmap_generator.py` (lines 11-18)  
**Modify**: `future_skills_db` dictionary

### Add a New Navigation Tab
**Edit 1**: `templates/home.html` (add nav item)  
**Edit 2**: `templates/home.html` (add section div)  
**Edit 3**: `static/script.js` (add section styles if needed)  
**Edit 4**: `static/style.css` (add CSS if needed)

### Deploy to Production
**Read**: `CONFIG.md` (Docker/Gunicorn sections)  
**Edit**: `app.py` (debug=False, port configuration)  
**Use**: `requirements.txt` (dependency installation)

### Add Database Support
**Read**: `CONFIG.md` (Database Configuration section)  
**Edit**: `app.py` (add database connection)  
**Edit**: `career_roadmap_generator.py` (add save methods)

### Speed Up the Snake Game
**Edit**: `static/script.js` (line ~250)  
**Change**: `setInterval(gameLoop, 100)` value

---

## 📞 Quick Reference

**To Start**: `python app.py`  
**To Access**: `http://localhost:5000`  
**To Install Dependencies**: `pip install -r requirements.txt`  
**To Change Colors**: Edit `static/style.css` top section  
**To Customize Skills**: Edit `career_roadmap_generator.py` databases  
**To Add Features**: Modify `templates/home.html` and `static/script.js`  
**To Deploy**: Follow `CONFIG.md` deployment section  

---

## ✅ File Status Checklist

- [x] `app.py` - Backend API created
- [x] `career_roadmap_generator.py` - Business logic exists
- [x] `templates/home.html` - Frontend created
- [x] `static/style.css` - Styling created
- [x] `static/script.js` - Interactivity created
- [x] `requirements.txt` - Dependencies listed
- [x] `README.md` - Complete documentation
- [x] `QUICKSTART.md` - Quick start guide
- [x] `CONFIG.md` - Configuration guide
- [x] `SETUP_SUMMARY.md` - Architecture overview
- [x] `FILE_REFERENCE.md` - This file

---

**All files are present and ready to use!** 🎉

For specific file details, use this index to quickly find what you need.
