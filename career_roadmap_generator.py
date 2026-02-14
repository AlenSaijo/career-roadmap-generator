import json
import re
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any

class CareerRoadmapGenerator:
    def __init__(self):
        # --- DATABASES ---
        self.future_skills_db = {
            "AI/ML": ["MLOps", "LLM Fine-tuning", "Vector Databases", "Prompt Engineering", "AI Safety"],
            "Cloud": ["Kubernetes", "Terraform", "Serverless", "Multi-cloud", "FinOps"],
            "Data": ["Real-time Analytics", "Data Mesh", "dbt", "Streaming", "DataOps"],
            "Security": ["Zero Trust", "DevSecOps", "Cloud Security", "AI Security", "Privacy Engineering"],
            "Web": ["WebAssembly", "Edge Computing", "Micro-frontends", "Web3", "Progressive Web Apps"]
        }

        self.interview_db = {
            "python": ["What is the difference between list and tuple?", "Explain decorators.", "How does memory management work in Python?"],
            "java": ["Explain the concept of OOP.", "What is the difference between JDK, JRE, and JVM?", "Explain Multi-threading."],
            "react": ["What is the Virtual DOM?", "Explain hooks in React.", "What is Redux used for?"],
            "docker": ["What is the difference between an image and a container?", "Explain Docker Compose.", "How do you optimize a Dockerfile?"],
            "general": ["Tell me about a challenging project.", "Where do you see yourself in 5 years?", "How do you handle tight deadlines?"]
        }
        
        self.quiz_db = {
            "python": {"q": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9"], "correct": "8"},
            "docker": {"q": "Which command builds an image?", "options": ["docker build", "docker create", "docker run"], "correct": "docker build"},
            "sql": {"q": "Which keyword is used to retrieve data?", "options": ["GET", "SELECT", "FETCH"], "correct": "SELECT"}
        }

    # --- NEW FEATURE: QUALIFICATION CHECKER ---
    def assess_qualification(self, resume_text: str, job_desc: str) -> Dict[str, Any]:
        """Determines if a candidate is qualified based on keyword matching"""
        resume_lower = resume_text.lower()
        job_lower = job_desc.lower()
        
        # 1. Extract Keywords from Job Description
        # Filter for words longer than 3 chars to avoid 'and', 'the', etc.
        all_words = re.findall(r'\w+', job_lower)
        significant_words = [w for w in all_words if len(w) > 3]
        
        # Find frequency to identify important technical terms
        word_freq = {w: significant_words.count(w) for w in set(significant_words)}
        # Take top 15 most frequent words as "Must Haves"
        required_keywords = sorted(word_freq, key=word_freq.get, reverse=True)[:15]
        
        # 2. Check matches
        matched = [k for k in required_keywords if k in resume_lower]
        missing = [k for k in required_keywords if k not in resume_lower]
        
        # 3. Calculate Score
        score = int((len(matched) / len(required_keywords)) * 100) if required_keywords else 0
        
        # 4. Determine Verdict
        if score >= 70:
            status = "Highly Qualified"
            color = "green"
            message = "Your resume is a strong match! You are ready to apply."
        elif score >= 40:
            status = "Potential Match"
            color = "orange"
            message = "You have some key skills, but gaps exist. Focus on the missing keywords."
        else:
            status = "Not Qualified Yet"
            color = "red"
            message = "Significant skill gaps detected. Follow the roadmap to bridge them."

        return {
            "status": status,
            "score": score,
            "color": color,
            "message": message,
            "matched_skills": matched,
            "missing_skills": missing
        }

    # --- EXISTING FEATURES (Preserved) ---
    def analyze_resume_deep(self, resume_text: str, job_desc: str) -> Dict[str, Any]:
        return self.assess_qualification(resume_text, job_desc) # Reuse logic

    def get_interview_questions(self, role: str) -> List[str]:
        questions = self.interview_db["general"][:]
        role_lower = role.lower()
        for key in self.interview_db:
            if key in role_lower and key != "general":
                questions.extend(self.interview_db[key])
        return random.sample(questions, min(len(questions), 5))

    def predict_salary(self, role: str, experience: int) -> Dict[str, Any]:
        base = 60000
        multiplier = 1 + (experience * 0.15)
        if "senior" in role.lower(): base += 30000
        if "lead" in role.lower(): base += 50000
        predicted = int(base * multiplier)
        return {"min": f"${predicted - 10000:,}", "max": f"${predicted + 15000:,}", "currency": "USD"}

    def get_skill_quiz(self, skill: str) -> Dict[str, Any]:
        skill = skill.lower()
        for key in self.quiz_db:
            if key in skill: return self.quiz_db[key]
        return {"q": f"Rate your confidence in {skill} (1-5)", "options": ["1", "3", "5"], "correct": "5"}

    # --- CORE LOGIC ---
    def analyze_profile(self, resume: str, github: str = "", linkedin: str = "") -> Dict[str, Any]:
        skills = {
            "programming": self._extract_programming_skills(resume + github),
            "frameworks": self._extract_frameworks(resume + github),
            "tools": self._extract_tools(resume + github),
            "soft_skills": self._extract_soft_skills(resume + linkedin),
            "level": self._assess_level(resume + github)
        }
        return {
            "skills": skills,
            "projects": self._extract_projects(resume + github),
            "experience_years": self._estimate_experience(resume)
        }
    
    def analyze_job(self, job_description: str) -> Dict[str, Any]:
        return {
            "required_skills": self._extract_job_skills(job_description),
            "preferred_skills": self._extract_preferred_skills(job_description),
            "responsibilities": self._extract_responsibilities(job_description),
            "priority_ranking": self._rank_skills(job_description)
        }
    
    def identify_gaps(self, profile: Dict, job_requirements: Dict) -> Dict[str, Any]:
        all_profile_skills = set(profile["skills"]["programming"] + profile["skills"]["frameworks"] + profile["skills"]["tools"])
        required = set(job_requirements["required_skills"])
        preferred = set(job_requirements["preferred_skills"])
        
        gaps = {
            "critical_missing": list(required - all_profile_skills),
            "nice_to_have": list(preferred - all_profile_skills),
            "underdeveloped": self._find_underdeveloped(profile, job_requirements),
            "future_proof": self._suggest_future_skills(job_requirements)
        }
        return gaps

    def generate_roadmap(self, profile: Dict, gaps: Dict, job_title: str, hours_per_day: int = 3) -> List[Dict]:
        roadmap = []
        day = 1
        critical = gaps.get("critical_missing", [])
        if not critical: critical = ["Advanced Concepts", "System Design", "Best Practices"]
        
        # Week 1
        for skill in critical[:3]:
            for i in range(3):
                roadmap.append({"day": day, "week": 1, "focus": skill, "task": self._generate_task(skill, i, "Beginner"), "points": 10 + (i*5), "duration_hours": hours_per_day})
                day += 1
                if day > 7: break
            if day > 7: break
        while day <= 7:
            roadmap.append({"day": day, "week": 1, "focus": "Review", "task": "Review Week 1 Concepts", "points": 5, "duration_hours": 2})
            day += 1

        # Week 2
        while day <= 14:
            roadmap.append({"day": day, "week": 2, "focus": "Integration Project", "task": self._generate_integration_task(critical[:2]), "points": 25, "duration_hours": hours_per_day})
            day += 1
        
        # Week 3 & 4 (Simplified filler for brevity)
        while day <= 30:
            roadmap.append({"day": day, "week": 4, "focus": "Advanced Prep", "task": f"Interview Prep for {job_title}", "points": 20, "duration_hours": hours_per_day})
            day += 1
        
        return roadmap

    def create_full_report(self, resume, job_description, job_title, hours_per_day=3):
        profile = self.analyze_profile(resume)
        job_req = self.analyze_job(job_description)
        gaps = self.identify_gaps(profile, job_req)
        roadmap = self.generate_roadmap(profile, gaps, job_title, hours_per_day)
        
        return {
            "target_role": {"title": job_title, "match_percentage": self._calculate_match(profile, job_req)},
            "gamification": {"total_points": sum(d.get('points', 0) for d in roadmap)},
            "gap_analysis": {"skill_gaps_count": len(gaps['critical_missing'])},
            "roadmap": roadmap,
            "extra_features": {
                'resume_analysis': self.assess_qualification(resume, job_description), # Using new logic
                'salary': self.predict_salary(job_title, profile['experience_years']),
                'interview_questions': self.get_interview_questions(job_title),
                'skill_check': self.get_skill_quiz("python")
            }
        }

    # --- HELPERS ---
    def _extract_programming_skills(self, text): return [l for l in ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "Scala"] if l.lower() in text.lower()]
    def _extract_frameworks(self, text): return [f for f in ["React", "Angular", "Django", "Flask", "Spring", "Node.js"] if f.lower() in text.lower()]
    def _extract_tools(self, text): return [t for t in ["Git", "Docker", "Kubernetes", "AWS", "Azure", "Jenkins"] if t.lower() in text.lower()]
    def _extract_soft_skills(self, text): return [s for s in ["leadership", "communication", "teamwork"] if s in text.lower()]
    def _assess_level(self, text): return "Advanced" if "senior" in text.lower() else "Beginner"
    def _extract_projects(self, text): return re.findall(r'project[:\s]+([^\n]+)', text, re.IGNORECASE)[:5]
    def _estimate_experience(self, text): 
        years = re.findall(r'(\d+)\+?\s*years?', text.lower())
        return float(years[0]) if years else 1.0
    def _extract_job_skills(self, text): return list(set(self._extract_programming_skills(text) + self._extract_frameworks(text) + self._extract_tools(text)))
    def _extract_preferred_skills(self, text): return []
    def _extract_responsibilities(self, text): return []
    def _rank_skills(self, text): return {}
    def _find_underdeveloped(self, p, j): return []
    def _suggest_future_skills(self, j): return self.future_skills_db.get("Cloud", [])[:3]
    def _generate_task(self, skill, day, level): return f"Learn {skill} fundamentals" if day==0 else f"Build a {skill} mini-project"
    def _generate_mini_project(self, skill, day): return f"{skill} CRUD App"
    def _get_resources(self, skill, level): return [f"Official {skill} Docs", "YouTube Tutorial"]
    def _generate_integration_task(self, skills): return f"Build app using {', '.join(skills)}"
    def _generate_portfolio_project(self, skills, job): return f"Full Stack {job} Project"
    def _get_project_resources(self): return ["GitHub Templates", "Deployment Guide"]
    def _generate_interview_prep(self, day, job): return f"Solve LeetCode problem #{day+1}"
    def _calculate_match(self, profile, job_req):
        p_skills = set(profile["skills"]["programming"] + profile["skills"]["frameworks"] + profile["skills"]["tools"])
        j_skills = set(job_req["required_skills"])
        if not j_skills: return 50
        return int((len(p_skills.intersection(j_skills)) / len(j_skills)) * 100)
    def _generate_badges(self, roadmap): return []
    def _generate_milestones(self, roadmap): return []