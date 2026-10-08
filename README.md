# Student Performance Analytics System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.x-013243.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x%2F3.x-150458.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)

> **EWB Courses — Python with AI Project Assignment**  
> A comprehensive, Python-based academic data analytics system that ingests student performance records, computes metrics using NumPy and Pandas, and delivers automated performance intelligence, department benchmarks, and merit leaderboards.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Project Architecture](#project-architecture)
- [Grading & Pass/Fail Rules](#grading--passfail-rules)
- [Quick Start](#quick-start)
- [Sample Output & Practical Questions Answered](#sample-output--practical-questions-answered)
- [Interactive Mode](#interactive-mode)
- [Project Documentation](#project-documentation)
- [GitHub Submission Guide](#github-submission-guide)
- [Author & Submission Details](#author--submission-details)

---

## 🎯 Project Overview

In educational institutions, analyzing student scores across various subjects, assessing passing percentages, and determining subject-wise difficulty is often a cumbersome manual task. 

The **Student Performance Analytics System** automates this workflow:
- Ingests raw student records across multiple departments.
- Calculates total marks and percentages using vectorized **NumPy** operations.
- Evaluates individual subject scores and attendance to assign letter grades and Pass/Fail statuses.
- Generates subject-level diagnostics, department-level comparisons, grade distributions, and top performer leaderboards.
- Exports enriched results to `processed_students.csv`.

---

## ✨ Key Features

1. **Robust Data Ingestion:**
   - Reads `students.csv` into a Pandas DataFrame with validation and handling of whitespace or missing entries.
2. **High-Performance Numerical Computations:**
   - Employs NumPy 2D array operations (`np.sum`, `np.mean`, `np.std`, `np.max`, `np.min`, `np.median`) for fast, precise row-wise and column-wise evaluations.
3. **Multi-Condition Academic Evaluation:**
   - Uses Python loops and conditional statements to assess every subject individually to guarantee that a student has scored $\ge 40$ in all courses before awarding a "Pass".
4. **Attendance Tracking:**
   - Highlights students with attendance below $75\%$ (`Shortage` warning).
5. **Practical Institutional Analytics:**
   - Answers critical administrative questions (top student, best performing subject, pass rate, class average).
   - Subject-wise statistical breakdown (average, min, max, standard deviation, pass rate).
   - Department-wise comparative performance.
   - Merit list (Top 5 performers) and Academic Intervention list.
6. **Dual Execution Modes:**
   - Automated full pipeline execution.
   - Interactive search and query mode (`python main.py -i`).

---

## 📁 Project Architecture

```text
Project2.python ai/
├── students.csv                # Raw student dataset (22 records, 9 columns)
├── functions.py                # Reusable modular analytics functions
├── main.py                     # Main execution pipeline and CLI reporting
├── processed_students.csv      # Exported enriched dataset with calculated results
├── Project_Documentation.md    # Formal 10-section assignment documentation
├── README.md                   # Repository overview, usage guide & docs
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git ignore rules for clean repository
```

---

## 📐 Grading & Pass/Fail Rules

### Letter Grading Scale:
| Average Score Range | Grade | Classification |
| :---: | :---: | :--- |
| **90% - 100%** | **A+** | Outstanding |
| **80% - 89.9%** | **A** | Excellent |
| **70% - 79.9%** | **B** | Good |
| **60% - 69.9%** | **C** | Satisfactory |
| **50% - 59.9%** | **D** | Pass |
| **Below 50%** | **F** | Fail |

### Pass / Fail Condition:
- **Pass:** The student must score $\ge 40$ marks in **every subject** AND have an overall average $\ge 40\%$.
- **Fail:** If a student scores $< 40$ in any subject, they are marked as **Fail**, and the specific failing subjects are recorded.
- **Attendance Warning:** If attendance is $< 75\%$, an `Attendance_Status` flag of `Shortage` is raised.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10+ installed on your system.

### 2. Install Dependencies
Open your terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### 3. Run the Analytics System
To execute the automated end-to-end analytics report:
```bash
python main.py
```

### 4. Run in Interactive Mode
To search for individual students or filter by department/grade:
```bash
python main.py -i
```

---

## 📊 Sample Output & Practical Questions Answered

When you run `python main.py`, the system outputs clean, structured reports:

### Answers to Key Analytical Questions:
1. **Which student has the highest average?**  
   👉 **Tanvi Kulkarni** (`STU014`, AI & ML) with **95.4%** (Total: 477.0 / 500, Grade: A+)
2. **Which subject has the best average?**  
   👉 **Computer Science** with an average of **78.50 / 100** (100% pass rate).
3. **How many students passed?**  
   👉 **19 out of 22 students passed** (**86.36%** pass rate). 3 students failed one or more subjects.
4. **What is the overall class average?**  
   👉 **74.39%** across all students and subjects (Median: 78.9%, Std Dev: 17.79).

### Top 5 Performing Students (Merit List):
| Rank | Student ID | Name | Department | Total Marks | Average Marks | Grade | Status |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | STU014 | Tanvi Kulkarni | AI & ML | 477.0 | 95.4% | A+ | Pass |
| 2 | STU002 | Diya Patel | AI & ML | 470.0 | 94.0% | A+ | Pass |
| 3 | STU004 | Ananya Iyer | Computer Science | 459.0 | 91.8% | A+ | Pass |
| 4 | STU020 | Priyanka Bose | Data Science | 455.0 | 91.0% | A+ | Pass |
| 5 | STU008 | Sneha Nair | Data Science | 451.0 | 90.2% | A+ | Pass |

### Subject-Wise Performance Analysis:
| Subject | Average Marks | Highest Mark | Lowest Mark | Std Dev | Passed Count | Failed Count | Pass Rate % |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Mathematics | 72.59 | 96.0 | 35.0 | 19.15 | 20 | 2 | 90.91% |
| Physics | 73.41 | 95.0 | 36.0 | 17.70 | 21 | 1 | 95.45% |
| Chemistry | 73.14 | 94.0 | 38.0 | 17.99 | 20 | 2 | 90.91% |
| Computer_Science | 78.50 | 99.0 | 44.0 | 17.30 | 22 | 0 | 100.00% |
| English | 74.32 | 94.0 | 40.0 | 17.29 | 22 | 0 | 100.00% |

---

## 🔍 Interactive Mode

Run the application with `-i` or `--interactive`:
```bash
python main.py -i
```
Options provided in the interactive menu:
1. **Search Student by ID or Name:** Quickly view all marks and performance for a specific student.
2. **Filter Students by Department:** Inspect cohort performance within AI & ML, Computer Science, Data Science, or IT.
3. **View Grade-wise Student List:** Filter all students who earned a specific grade (e.g., all `A+` or `F` students).
4. **Re-run Full Analytics Report:** Generates the master report again.
5. **Exit**

---

## 📑 Project Documentation

Full academic project documentation covering the 10 assessment criteria specified by EWB Courses is available in [Project_Documentation.md](Project_Documentation.md):
1. Project Title & Student Details
2. Objective
3. Technologies Used
4. Dataset Description
5. Implementation Details
6. Key Features
7. Output & Results
8. Final Outcome
9. Challenges & Learning
10. GitHub Repository

---

## 📤 GitHub Submission Guide

Follow these simple steps to push this project to GitHub for your assignment submission:

```bash
# 1. Initialize git repository (if not already done)
git init

# 2. Add all project files
git add .

# 3. Create initial commit
git commit -m "Initial submission: Student Performance Analytics System"

# 4. Create a new public repository on GitHub named:
#    student-performance-analytics

# 5. Link local repository to your GitHub remote
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/student-performance-analytics.git

# 6. Push to main branch
git branch -M main
git push -u origin main
```

---

## 👤 Author & Submission Details

- **Program:** Python with AI — EWB Courses
- **Project Title:** Student Performance Analytics System
- **Deadline:** 15 October 2026
- **Submission Components:**
  - [x] Working Python Code (`main.py`, `functions.py`)
  - [x] Student Dataset (`students.csv`)
  - [x] Enriched Processed Dataset (`processed_students.csv`)
  - [x] Documentation (`Project_Documentation.md`)
  - [x] Comprehensive Repository README (`README.md`)
