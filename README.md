# ARIA – Adaptive Recruiter Intelligence Agent

## Overview

ARIA (Adaptive Recruiter Intelligence Agent) is an AI-powered candidate ranking system developed for the **Redrob Data & AI Challenge 2026**.

Instead of relying on traditional keyword-based matching, ARIA evaluates candidates holistically by combining semantic understanding, career progression, recruiter behavior signals, and explainable hybrid scoring to generate a trustworthy shortlist.

---

## Problem Statement

Traditional Applicant Tracking Systems (ATS) primarily depend on keyword matching, often overlooking highly qualified candidates whose experience and skills are expressed differently.

Recruiters need a system that understands **context rather than keywords**, evaluates the complete candidate profile, and produces explainable recommendations.

---

## Solution

ARIA follows a hybrid AI pipeline that combines semantic matching with recruiter-oriented behavioral analysis.

### Pipeline

```
Job Description
        │
        ▼
Feature Extraction
        │
        ▼
Semantic Matching (TF-IDF + Cosine Similarity)
        │
        ▼
Behavioral Signal Analysis
        │
        ▼
Penalty & Trap Detection
        │
        ▼
Hybrid Scoring Engine
        │
        ▼
Reason Generation
        │
        ▼
Top-100 Candidate Ranking
```

---

## Project Architecture

```
src/
├── load_data.py
├── feature_engineering.py
├── jd_parser.py
├── semantic_matcher.py
├── signal_engine.py
├── trap_detector.py
├── scoring_engine.py
├── reason_generator.py
└── ranker.py
```

---

## Core Components

### Data Loader

Loads candidate profiles from the provided dataset.

### Feature Engineering

Extracts recruiter-relevant information including:

* Skills
* Professional experience
* Career history
* Company information
* Behavioral indicators

### Semantic Matcher

Measures semantic similarity between candidate profiles and job descriptions using:

* TF-IDF Vectorization
* Cosine Similarity

### Signal Engine

Evaluates recruiter-centric signals such as:

* Open-to-work status
* Recruiter response rate
* GitHub activity
* Notice period
* Relocation preference

### Trap Detector

Applies penalties for profiles that indicate lower suitability, including inactive or low-engagement candidates.

### Scoring Engine

Combines semantic relevance, behavioral signals, and penalties into a final ranking score.

### Reason Generator

Produces explainable reasons describing why a candidate received a particular score.

### Ranking Engine

Ranks all candidates and exports the Top-100 recommendations in the required submission format.

---

## Technology Stack

### Programming Language

* Python 3.10+

### Libraries

* NumPy
* Pandas
* Scikit-Learn
* JSONLines
* Streamlit (Optional Demo)

### AI Techniques

* TF-IDF Vectorization
* Cosine Similarity
* Hybrid Rule-Based Scoring
* Explainable Candidate Ranking

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Jayanthsadurla/ARIA-Adaptive-Recruiter-Intelligence-Agent.git
cd ARIA-Adaptive-Recruiter-Intelligence-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the dataset inside:

```
data/candidates.jsonl
```

Run:

```bash
python rank.py
```

---

## Output

ARIA generates:

* Ranked Top-100 candidate recommendations
* Explainable ranking reasons
* Submission-ready `team_aria.csv`

---

## Repository

```
src/
data/
rank.py
requirements.txt
README.md
team_aria.csv
```

---

## Team

**ARIA – Adaptive Recruiter Intelligence Agent**

Developed for the **Redrob Data & AI Challenge 2026**.

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
