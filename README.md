# ARIA – Adaptive Recruiter Intelligence Agent

## Overview

ARIA (Adaptive Recruiter Intelligence Agent) is an AI-powered candidate discovery and ranking system designed to emulate the decision-making process of experienced recruiters.

Traditional recruitment systems rely heavily on keyword matching, often overlooking candidates with strong underlying potential and relevant experience. ARIA addresses this limitation by evaluating candidates holistically through semantic understanding, career progression, behavioral signals, and explainable scoring.

---

## Problem Statement

Recruiters often review hundreds of profiles and still miss high-quality candidates because conventional filtering systems cannot understand context, experience, and candidate intent.

The objective of ARIA is to:

* Understand job requirements beyond keywords.
* Evaluate candidates using multiple signals.
* Produce a trustworthy shortlist of highly relevant candidates.
* Generate explainable rankings that recruiters can understand and trust.

---

## Solution Approach

ARIA follows a multi-stage ranking pipeline:

Job Description
↓
Feature Extraction
↓
Semantic Candidate Matching
↓
Behavioral Signal Analysis
↓
Penalty and Trap Detection
↓
Hybrid Scoring Engine
↓
Explainable Ranking
↓
Top-100 Candidate Recommendations

---

## Core Components

### Data Loader

Efficiently loads and processes candidate datasets.

### Feature Engineering

Extracts structured candidate attributes including:

* Professional experience
* Skills and technologies
* Career history
* Recruiter engagement signals
* Availability indicators

### Semantic Matcher

Computes semantic similarity between job descriptions and candidate profiles using TF-IDF vectorization and cosine similarity.

### Signal Engine

Evaluates recruiter-oriented behavioral signals including:

* Open-to-work status
* Recruiter response rate
* GitHub activity
* Notice period
* Relocation preferences

### Trap Detector

Identifies potentially poor-fit candidates through:

* Inactive profiles
* Low recruiter engagement
* Service-only background penalties
* Other heuristic indicators

### Scoring Engine

Combines semantic matching, behavioral signals, and penalties into a unified candidate score.

### Reason Generator

Produces human-readable explanations describing why candidates were ranked highly or penalized.

### Ranking Engine

Generates a ranked shortlist of Top-100 candidates and exports the results in submission-ready CSV format.

---

## Technology Stack

### Programming Language

* Python 3.10+

### Libraries

* NumPy
* Pandas
* Scikit-Learn
* JSONLines
* Streamlit (optional demonstration interface)

### AI Techniques

* TF-IDF Vectorization
* Cosine Similarity
* Hybrid Scoring Framework
* Explainable AI Ranking
* Rule-Based Signal Reasoning

---

## Output

ARIA generates:

1. Ranked Top-100 candidate recommendations
2. Candidate scores and explanations
3. Submission-ready CSV output

---

## Repository Structure

src/
├── load_data.py
├── feature_engineering.py
├── jd_parser.py
├── signal_engine.py
├── trap_detector.py
├── semantic_matcher.py
├── scoring_engine.py
├── reason_generator.py
└── ranker.py

rank.py
team_aria.csv
requirements.txt
README.md

---

## Team

ARIA – Adaptive Recruiter Intelligence Agent

Built for the Redrob Data & AI Challenge 2026.
