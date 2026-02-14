// ============================================
// Section Navigation
// ============================================
function showSection(id) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    event.currentTarget.classList.add('active');
}

// ============================================
// Career Roadmap Generation
// ============================================
async function generateRoadmap() {
    const jobTitle = document.getElementById('job_title').value.trim();
    const resume = document.getElementById('resume_text').value.trim();
    const jobDesc = document.getElementById('job_description').value.trim();

    if (!jobTitle || !resume || !jobDesc) {
        alert('Please fill in all fields: Job Title, Resume/Skills, and Job Description');
        return;
    }

    document.getElementById('loader').style.display = 'block';
    const data = {
        job_title: jobTitle,
        resume: resume,
        job_description: jobDesc
    };

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.error) throw new Error(result.error);

        document.getElementById('loader').style.display = 'none';
        document.getElementById('dashboard-results').style.display = 'block';

        // 1. Dashboard Stats
        const matchScore = result.target_role.match_percentage || 0;
        const salary = result.extra_features.salary || {};
        document.getElementById('score-display').innerText = matchScore + '%';
        document.getElementById('salary-display').innerText = salary.min || '$0';

        // 2. Roadmap Timeline
        const roadmapHtml = (result.roadmap || []).map(day => `
            <div style="padding:12px; border-left:3px solid var(--primary); margin-bottom:10px; background:rgba(99, 102, 241, 0.08); border-radius:6px;">
                <strong style="color:var(--primary);">Day ${day.day || ''}: ${day.focus || 'Task'}</strong>
                <p style="color:var(--text-dim); margin-top:5px; font-size:0.9rem;">${day.task || ''}</p>
                <span style="font-size:0.8rem; color:var(--accent);">⏱️ ${day.duration_hours || 3}h | 🎯 ${day.points || 0} XP</span>
            </div>
        `).join('');
        document.getElementById('roadmap-list').innerHTML = roadmapHtml || '<p>No roadmap data available</p>';

        // 3. Resume Analysis
        if (result.extra_features && result.extra_features.resume_analysis) {
            const resData = result.extra_features.resume_analysis;
            const scoreColor = resData.score > 70 ? '#4ade80' : resData.score > 40 ? '#fb923c' : '#f87171';
            const feedback = resData.message || resData.feedback || 'Assessment complete.';
            
            document.getElementById('resume-feedback').innerHTML = `
                <h3>Qualification Status: <span style="color:${scoreColor}">${resData.status}</span></h3>
                <h3>Match Score: <span style="color:${scoreColor}">${resData.score}%</span></h3>
                <p style="margin: 15px 0; font-size: 1.1rem;">${feedback}</p>
                <div style="margin-top:15px;">
                    <strong>✅ Matched Skills:</strong> <span style="color:#4ade80;">${(resData.matched_skills || []).join(', ') || 'None'}</span><br><br>
                    <strong>❌ Missing Skills:</strong> <span style="color:#f87171;">${(resData.missing_skills || []).join(', ') || 'None'}</span>
                </div>
            `;
        }

        // 4. Interview Questions
        if (result.extra_features && result.extra_features.interview_questions) {
            const questions = result.extra_features.interview_questions;
            document.getElementById('interview-list').innerHTML = questions.map((q, i) => 
                `<li style="margin-bottom:12px;"><strong>${i + 1}. ${q}</strong></li>`
            ).join('');
        }

        // 5. Skill Quiz
        if (result.extra_features && result.extra_features.skill_check) {
            const quiz = result.extra_features.skill_check;
            document.getElementById('quiz-question').innerText = quiz.q || 'Loading quiz...';
            document.getElementById('quiz-options').innerHTML = (quiz.options || []).map(opt =>
                `<button style="margin: 5px 5px 5px 0; background:#334155;" onclick="checkAnswer('${opt}', '${quiz.correct}', this)">${opt}</button>`
            ).join('');
            document.getElementById('quiz-result').innerText = '';
        }

    } catch (err) {
        alert('Error: ' + err.message);
        document.getElementById('loader').style.display = 'none';
    }
}

// ============================================
// Qualification Checker (PDF Upload)
// ============================================
async function checkQualification() {
    const fileInput = document.getElementById('pdfFile');
    const jd = document.getElementById('pdf_jd').value.trim();

    if (!fileInput.files[0]) {
        alert('Please select a PDF file');
        return;
    }

    if (!jd) {
        alert('Please paste the Job Description');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('job_description', jd);

    try {
        const response = await fetch('/upload-resume', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.error) throw new Error(result.error);

        const resultDiv = document.getElementById('qual-result');
        const badge = document.getElementById('qual-badge');

        resultDiv.style.display = 'block';
        const colorClass = `qual-${result.color || 'red'}`;
        badge.className = `qual-badge ${colorClass}`;
        badge.innerText = result.status || 'Assessment Complete';
        document.getElementById('qual-score').innerText = `Score: ${result.score || 0}/100`;
        document.getElementById('qual-msg').innerText = result.message || '';
        document.getElementById('qual-matched').innerHTML = (result.matched_skills || [])
            .map(s => `<span class="skill-tag matched">${s}</span>`)
            .join('') || 'None';
        document.getElementById('qual-missing').innerHTML = (result.missing_skills || [])
            .map(s => `<span class="skill-tag missing">${s}</span>`)
            .join('') || 'None';

    } catch (err) {
        alert('Error analyzing PDF: ' + err.message);
    }
}

// ============================================
// Quiz Answer Check
// ============================================
function checkAnswer(selected, correct, buttonEl) {
    const res = document.getElementById('quiz-result');
    const isCorrect = selected === correct;
    
    res.innerText = isCorrect ? '✅ Correct! +50 XP' : '❌ Wrong! Try again.';
    res.style.color = isCorrect ? '#4ade80' : '#f87171';
    
    if (buttonEl) {
        buttonEl.style.background = isCorrect ? '#4ade80' : '#f87171';
        buttonEl.style.color = '#0f172a';
    }
}

// ============================================
// Snake Game Logic
// ============================================
let canvas = document.getElementById('gameCanvas');
let ctx = canvas ? canvas.getContext('2d') : null;
let snake = [{ x: 200, y: 200 }];
let food = { x: 0, y: 0 };
let dx = 20;
let dy = 0;
let gameInterval = null;
let score = 0;

function startGame() {
    if (!canvas || !ctx) return;
    
    if (gameInterval) clearInterval(gameInterval);
    
    snake = [{ x: 200, y: 200 }];
    dx = 20;
    dy = 0;
    score = 0;
    
    placeFood();
    gameInterval = setInterval(gameLoop, 100);
    document.addEventListener('keydown', changeDirection);
}

function placeFood() {
    food.x = Math.floor(Math.random() * 20) * 20;
    food.y = Math.floor(Math.random() * 20) * 20;
}

function changeDirection(e) {
    const k = e.keyCode;
    
    // Prevent default scrolling
    if ([37, 38, 39, 40].includes(k)) {
        e.preventDefault();
    }
    
    // Left arrow
    if (k === 37 && dx === 0) {
        dx = -20;
        dy = 0;
    }
    // Up arrow
    if (k === 38 && dy === 0) {
        dx = 0;
        dy = -20;
    }
    // Right arrow
    if (k === 39 && dx === 0) {
        dx = 20;
        dy = 0;
    }
    // Down arrow
    if (k === 40 && dy === 0) {
        dx = 0;
        dy = 20;
    }
}

function gameLoop() {
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };

    // Check collisions with walls
    if (head.x < 0 || head.x >= 400 || head.y < 0 || head.y >= 400) {
        endGame();
        return;
    }

    // Check collision with self
    if (snake.some(s => s.x === head.x && s.y === head.y)) {
        endGame();
        return;
    }

    snake.unshift(head);

    // Check if food is eaten
    if (head.x === food.x && head.y === food.y) {
        score++;
        placeFood();
    } else {
        snake.pop();
    }

    // Draw game
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, 400, 400);

    // Draw food
    ctx.fillStyle = '#f43f5e';
    ctx.fillRect(food.x, food.y, 18, 18);

    // Draw snake
    ctx.fillStyle = '#6366f1';
    snake.forEach((part, index) => {
        if (index === 0) {
            ctx.fillStyle = '#8b5cf6'; // Head color
        } else {
            ctx.fillStyle = '#6366f1'; // Body color
        }
        ctx.fillRect(part.x, part.y, 18, 18);
    });

    // Draw score
    ctx.fillStyle = '#f1f5f9';
    ctx.font = '14px Arial';
    ctx.fillText(`Score: ${score}`, 10, 390);
}

function endGame() {
    if (gameInterval) clearInterval(gameInterval);
    alert(`Game Over! Final Score: ${score}\n\nUse arrow keys to play.`);
    snake = [{ x: 200, y: 200 }];
    dx = 20;
    dy = 0;
    score = 0;
}

// Initialize canvas size on page load
window.addEventListener('load', function() {
    const gameCanvas = document.getElementById('gameCanvas');
    if (gameCanvas) {
        gameCanvas.width = 400;
        gameCanvas.height = 400;
    }
});
