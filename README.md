# AI Resume Screener Using Python

 Intelligent Resume Screening System that compares resumes with job descriptions using NLP, TF-IDF, cosine similarity, and skill-based scoring.

---

# 📌 Project Overview

Recruiters often receive hundreds of resumes for a single job opening.  
Manually checking every resume is time-consuming and inefficient.

This project automates the initial resume screening process by analyzing a candidate’s resume against a Job Description (JD) and generating an overall match score.

The system reads PDF resumes, preprocesses text, compares content using Machine Learning techniques, extracts technical skills, and provides matched / missing skills analysis.

---

# 🎯 Main Objectives

- Automate resume screening process
- Compare resume with job description
- Detect relevant technical skills
- Reduce recruiter effort
- Learn NLP and Machine Learning practically
- Build a real-world Python project

---

# 🚀 Features

## ✅ Resume PDF Text Extraction
Extracts text from PDF resumes using PyPDF2.

## ✅ Text Cleaning / NLP Preprocessing

Performs:

- Lowercase conversion
- URL removal
- Symbol removal
- Extra space removal
- Stopword removal

## ✅ Resume Matching

Uses:

- TF-IDF Vectorization
- Cosine Similarity

to compare resume text with Job Description.

## ✅ Skill Extraction

Detects skills such as:

- Python
- Java
- SQL
- C#.Net
- Backend
- Automation
- Git
- GitHub

## ✅ Match Analysis

Displays:

- Resume Skills
- Job Skills
- Matched Skills
- Missing Skills

## ✅ Final Combined Score

Calculates final score using:

Final Score = (40% Text Similarity) + (60% Skill Match)

---

# 🧠 Technologies Used

| Technology   |           Purpose          |
|--------------|----------------------------|
| Python       | Main programming language  |
| PyPDF2       | PDF text extraction        |
| NLTK         | Stopword removal           |
| Scikit-learn | TF-IDF + cosine similarity |
| Regex        | Text cleaning              |
| GitHub       | Version control            |

---

# 📂 Project Structure

```text
AI-Resume-Screener-Using-Python/
│── ResumeScreener.py
│── requirements.txt
│── README.md
│── RESUMES/sample_resume.pdf
```
Step 1: Clone Repository
git clone https://github.com/PankajHarabhare09/AI-Resume-Screener-Using-Python.git
cd AI-Resume-Screener-Using-Python
