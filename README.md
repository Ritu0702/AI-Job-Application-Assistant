# 💼 AI Job Application Assistant

An AI-powered job application assistant that analyzes a candidate's resume against a job description and provides an intelligent job-match analysis.

## 🚀 Project Overview

The AI Job Application Assistant helps candidates understand how well their resume matches a particular job role.

The application accepts:
- A Resume in PDF format
- A Job Description

It then uses an AI-powered n8n workflow to analyze both and generate a detailed job-match report.

## ✨ Features

- 📄 Resume PDF Upload
- 💼 Job Description Analysis
- 🤖 AI-powered Resume Analysis
- 🎯 Job Match Score out of 100
- ✅ Matching Skills Identification
- ❌ Missing Skills Identification
- 🎓 Education Match Analysis
- 💼 Experience Match Analysis
- 💡 Final Job Recommendation
- ✉️ Personalized Cover Letter Generation for high-match candidates
- 🌐 Streamlit Web Interface
- ⚙️ n8n Agentic AI Workflow

## 🔄 Workflow

```text
Resume + Job Description
          ↓
       Webhook
       ↙      ↘
Resume Analyzer   Job Description Analyzer
       ↘      ↙
         Merge
           ↓
       Job Matcher
           ↓
      Match Score
           ↓
       IF Score ≥ 70
        ↙        ↘
      TRUE       FALSE
       ↓           ↓
Cover Letter    Match Result
Generator        Result
       ↘          ↙
         Final Result
