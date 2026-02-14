# Configuration Guide

## Environment Setup

### Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Using Conda

```bash
conda create -n career-navigator python=3.9
conda activate career-navigator
pip install -r requirements.txt
```

## Flask Configuration

### Development Mode (Default)
```python
# app.py
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

Features:
- Auto-reloading on code changes
- Detailed error messages
- Interactive debugger

### Production Mode
```python
# Install production server
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Parameters:
- `-w 4`: 4 worker processes (adjust based on CPU cores)
- `-b 0.0.0.0:5000`: Bind to all interfaces on port 5000

## UI Customization

### Change Theme Colors

Edit `static/style.css` variables:

```css
:root {
    --bg: #0f172a;           /* Main background */
    --surface: #1e293b;      /* Card/surface background */
    --primary: #6366f1;      /* Primary button/accent */
    --accent: #8b5cf6;       /* Secondary/highlight color */
    --text: #f1f5f9;         /* Main text color */
    --text-dim: #94a3b8;     /* Dimmed/secondary text */
}
```

Example: Purple Theme
```css
:root {
    --primary: #a855f7;
    --accent: #d946ef;
    --surface: #2e1065;
}
```

### Change Sidebar Width

Edit `static/style.css`:
```css
.sidebar {
    width: 80px;  /* Default collapsed width */
}

.sidebar:hover {
    width: 220px;  /* Hover expanded width */
}
```

## API Customization

### Add New Career Category

Edit `career_roadmap_generator.py`:

```python
self.future_skills_db = {
    "AI/ML": [...],
    "Cloud": [...],
    "Data": [...],
    "Security": [...],
    "Web": [...],
    "Blockchain": [  # Add new category
        "Solidity",
        "Smart Contracts",
        "Web3.py"
    ]
}
```

### Modify Roadmap Duration

Default: 30 days
Edit `app.py` `/generate` endpoint:

```python
# Currently limits to 30 days
# Modify in career_roadmap_generator.py generate_roadmap() method
```

### Change Default Hours/Day

Current default: 3 hours
```python
# In app.py
hours_per_day=int(data.get('hours_per_day', 3))  # Change 3 to desired default
```

## Database/Storage Configuration

### Save Roadmaps to File

```python
# In app.py, modify /generate endpoint:
import json
from datetime import datetime

report = generator.create_full_report(...)

# Save to JSON file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"roadmaps/roadmap_{timestamp}.json"

with open(filename, 'w') as f:
    json.dump(report, f, indent=2)

return jsonify({**report, "saved_to": filename})
```

### Connect to Database (Example: SQLite)

```python
import sqlite3
from datetime import datetime

def save_roadmap_to_db(report, user_id):
    conn = sqlite3.connect('roadmaps.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO roadmaps (user_id, title, report, created_at)
        VALUES (?, ?, ?, ?)
    ''', (user_id, report['target_role']['title'], json.dumps(report), datetime.now()))
    
    conn.commit()
    conn.close()
```

## Game Configuration

### Adjust Snake Game Speed

Edit `static/script.js`:

```javascript
// Slower speed (ms between moves)
gameInterval = setInterval(gameLoop, 150);  // Default: 100

// Faster speed
gameInterval = setInterval(gameLoop, 50);
```

### Change Canvas Size

```html
<!-- In home.html -->
<canvas id="gameCanvas" width="500" height="500"></canvas>
```

Then update `static/script.js`:
```javascript
// Scale grid to new size (must divide evenly)
const gridSize = 25;  // For 500x500 canvas
```

## Security Configuration

### Enable CORS (for API access from other domains)

```python
# In app.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
```

### Add Authentication

```python
from functools import wraps
import os

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != os.getenv('API_KEY'):
            return jsonify({"error": "Invalid API key"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/protected', methods=['POST'])
@require_api_key
def protected_endpoint():
    # Protected code here
    pass
```

## Logging Configuration

### Add Request Logging

```python
# In app.py
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

## Performance Optimization

### Enable Caching

```python
# In app.py
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/api/future-skills')
@cache.cached(timeout=3600)  # Cache for 1 hour
def get_future_skills():
    return jsonify(generator.future_skills_db)
```

### Minify Static Files

Minify CSS and JavaScript for production:
- Use `cssnano` for CSS
- Use `terser` for JavaScript

## Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Docker Compose

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DEBUG=0
    volumes:
      - ./roadmaps:/app/roadmaps
```

## Environment Variables

Create `.env` file:

```bash
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=your-secret-key-here
DEBUG=0
PORT=5000
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216  # 16MB max file size
```

Load in app.py:
```python
import os
from dotenv import load_dotenv

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH', 16777216))
```

---

## Testing Configuration

### Set Up Testing Environment

```python
# test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_generate_roadmap(self):
        data = {
            'job_title': 'Developer',
            'resume': 'Python, JavaScript',
            'job_description': 'Python experience required'
        }
        response = self.app.post('/generate', json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

Run tests:
```bash
python -m pytest test_app.py
```

---

For more customization options, refer to Flask documentation: https://flask.palletsprojects.com/
