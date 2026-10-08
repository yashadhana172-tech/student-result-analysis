# Student Performance Analytics System - Project Documentation

**EWB Courses | Python with AI Program**  
**Course Assignment Submission**

---

## 1. Project Title & Student Details

- **Project Title:** Student Performance Analytics System
- **Domain:** Educational Data Analytics & Academic Performance Tracking
- **Technology Stack:** Python 3, NumPy, Pandas
- **Student Name:** [Your Name Here]
- **Course Name:** Python with AI
- **Submission Date:** October 2026
- **Submission Deadline:** 15 October 2026

---

## 2. Objective

The primary objective of this project is to build an automated, modular, data-driven analytical tool to assess, analyze, and report on student academic performance across multiple disciplines and departments.

### Key Problems Solved:
1. **Manual Grade Computation:** Eliminates tedious manual tabulation of student totals, averages, and grades.
2. **Standardized Evaluation:** Implements uniform subject-wise pass/fail criteria and letter grading scales.
3. **Institutional Insights:** Provides department-level comparisons and subject-difficulty benchmarks (identifying subjects with lower pass rates or high standard deviations).
4. **Early Warning Indicators:** Detects students at risk of failing or with attendance shortages (< 75%) so educators can intervene proactively.

---

## 3. Technologies Used

| Technology / Tool | Version | Purpose & Usage |
| :--- | :--- | :--- |
| **Python** | 3.10+ | Core language for control flow, loops, conditions, and custom functions |
| **NumPy** | 1.24+ | Vectorized numerical operations, multi-dimensional array math, mean, sum, std dev, min/max |
| **Pandas** | 2.0+ | DataFrame loading, indexing, tabular filtering, aggregation, and CSV export |
| **Git / GitHub** | Latest | Version control and public code repository hosting |

---

## 4. Dataset Description

The dataset is maintained in `students.csv` and contains realistic academic records representing an undergraduate student cohort across multiple engineering and computing departments.

- **Total Records:** 22 student records
- **Total Columns:** 9 fields
- **Data Attributes:**

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `StudentID` | String | Unique identifier for each student (e.g., STU001, STU002) |
| `Name` | String | Full name of the student |
| `Department` | String | Academic department (AI & ML, Data Science, Computer Science, Information Tech) |
| `Mathematics` | Integer / Float | Marks scored in Mathematics (out of 100) |
| `Physics` | Integer / Float | Marks scored in Physics (out of 100) |
| `Chemistry` | Integer / Float | Marks scored in Chemistry (out of 100) |
| `Computer_Science` | Integer / Float | Marks scored in Computer Science (out of 100) |
| `English` | Integer / Float | Marks scored in English (out of 100) |
| `Attendance` | Integer / Float | Attendance percentage (0 - 100%) |

---

## 5. Implementation

The implementation is modularized across `functions.py` (reusable processing and math functions) and `main.py` (orchestration, analytics reporting, and CLI interface).

### Step-by-Step Execution Flow:

1. **Dataset Loading & Inspection (`load_dataset`):**
   - Reads `students.csv` using `pd.read_csv()`.
   - Cleans string fields and verifies data cleanliness (checking for null or invalid entries).

2. **NumPy Vectorized Calculations (`calculate_student_metrics`):**
   - Extracts marks for all 5 subjects into an $N \times M$ 2D NumPy array (`to_numpy(dtype=float)`).
   - Computes `Total_Marks` using `np.sum(marks_matrix, axis=1)`.
   - Computes `Average_Marks` using `np.mean(marks_matrix, axis=1)`.

3. **Grading & Pass/Fail Evaluation (`evaluate_student_results`):**
   - **Grading Scale:**
     - $90\% - 100\%$: **A+** (Outstanding)
     - $80\% - 89.9\%$: **A** (Excellent)
     - $70\% - 79.9\%$: **B** (Good)
     - $60\% - 69.9\%$: **C** (Satisfactory)
     - $50\% - 59.9\%$: **D** (Pass)
     - Below $50\%$: **F** (Fail)
   - **Pass/Fail Criteria:** A student passes only if they score $\ge 40$ in **every** individual subject AND maintain an overall average $\ge 40\%$. Loops iterate through subject columns for each student to detect specific failing subjects.
   - **Attendance Verification:** Flags students with attendance $< 75\%$ as `Shortage`.

4. **Aggregate Class Statistics (`calculate_class_summary`):**
   - Computes class mean, median, standard deviation, highest/lowest averages, and passing percentages using NumPy vector aggregations (`np.mean`, `np.std`, `np.median`, `np.max`, `np.min`).

5. **Subject-Wise Deep Dive (`generate_subject_wise_analysis`):**
   - Iterates across subjects with a loop. Computes average score, standard deviation, pass count, fail count, and pass percentage for each course.

6. **Departmental Comparison (`get_department_analysis`):**
   - Groups student records by department to analyze average scores, top scores, and departmental pass rates.

7. **Export (`export_processed_dataset`):**
   - Saves all calculated columns (`Total_Marks`, `Average_Marks`, `Grade`, `Result_Status`, `Failed_Subjects`, `Attendance_Status`) into `processed_students.csv`.

---

## 6. Key Features

- **End-to-End Processing Pipeline:** One-command execution that ingests, cleans, calculates, evaluates, and reports.
- **NumPy & Pandas Synergy:** Combines the vectorized mathematical power of NumPy arrays with the tabular manipulation flexibility of Pandas DataFrames.
- **Explicit Python Control Flow:** Uses loops, conditionals, and modular functions as required by the course syllabus.
- **Detailed Subject Diagnostics:** Identifies high-performing subjects vs. subjects requiring curriculum support.
- **Departmental Benchmarks:** Enables cross-department academic auditing.
- **Interactive Query Tool:** Interactive CLI option (`python main.py -i`) to search students by ID/Name, filter by department, or inspect grade rosters.
- **Automatic Export:** Generates an enriched CSV file ready for downstream administrative reporting.

---

## 7. Output & Results

### Console Execution Output Summary:

```text
==============================================================================
==================== STUDENT PERFORMANCE ANALYTICS SYSTEM ====================
==============================================================================
Developed with: Python 3, NumPy, Pandas
Dataset Source: students.csv

--- [ Step 1 & 2: Dataset Ingestion and Inspection ] ------------------------------
[OK] Successfully loaded dataset with 22 records and 9 columns.
[OK] Columns detected: ['StudentID', 'Name', 'Department', 'Mathematics', 'Physics', 'Chemistry', 'Computer_Science', 'English', 'Attendance']

--- [ Step 3: Data Processing, Total Marks, Averages, Grades & Pass/Fail ] --------
[OK] Subjects analyzed (5): Mathematics, Physics, Chemistry, Computer_Science, English
[OK] Calculated Total Marks, Average Marks, Letter Grade, and Result Status for all students.

--- [ Step 4: Answers to Key Analytical Questions ] -------------------------------
1. Which student has the highest average?
   => Tanvi Kulkarni (STU014, AI & ML)
      Score: 95.4% (Total: 477.0/500, Grade: A+)

2. Which subject has the best average?
   => Computer_Science
      Subject Average: 78.5 / 100 (Pass Rate: 100.0%)

3. How many students passed?
   => 19 out of 22 students passed (86.36% pass rate)
      Failed Students: 3 (Scored < 40 in one or more subjects)

4. What is the overall class average?
   => 74.39% across all students and subjects
      Class Range: 40.0% (Lowest) to 95.4% (Highest)
      Median: 78.9%, Std Dev: 17.79

--- [ Subject-Wise Performance Analysis ] -----------------------------------------
Subject           Average_Marks  Highest_Mark  Lowest_Mark  Std_Dev  Passed_Count  Failed_Count  Pass_Rate_%
Mathematics       72.59          96.0          35.0         19.15    20            2             90.91      
Physics           73.41          95.0          36.0         17.70    21            1             95.45      
Chemistry         73.14          94.0          38.0         17.99    20            2             90.91      
Computer_Science  78.50          99.0          44.0         17.30    22            0             100.00     
English           74.32          94.0          40.0         17.29    22            0             100.00     

--- [ Department-Wise Performance Summary ] ---------------------------------------
Department        Total_Students  Average_Marks  Top_Score  Pass_Rate_%
AI & ML           6               88.23          95.4       100.00      
Data Science      5               83.04          91.0       100.00      
Computer Science  6               68.37          91.8        66.67      
Information Tech  5               56.36          75.4        80.00      

--- [ Academic Grade Distribution ] -----------------------------------------------
Grade  Student_Count  Percentage_%
A+     6              27.27        
A      5              22.73        
B      3              13.64        
C      3              13.64        
D      2               9.09        
F      3              13.64        

--- [ Top 5 Performing Students (Merit List) ] ------------------------------------
Rank  StudentID  Name            Department        Total_Marks  Average_Marks  Grade  Result_Status
1     STU014     Tanvi Kulkarni  AI & ML           477.0        95.4           A+     Pass         
2     STU002     Diya Patel      AI & ML           470.0        94.0           A+     Pass         
3     STU004     Ananya Iyer     Computer Science  459.0        91.8           A+     Pass         
4     STU020     Priyanka Bose   Data Science      455.0        91.0           A+     Pass         
5     STU008     Sneha Nair      Data Science      451.0        90.2           A+     Pass         
```

---

## 8. Final Outcome

The project successfully delivers an end-to-end, error-free analytics pipeline meeting all specifications:
- **Accuracy:** All student metrics (totals, averages, letter grades, pass/fail status) are calculated with 100% precision.
- **Actionable Insights:** Answers every key question posed by the assignment (highest student average, best subject, pass/fail statistics, overall class metrics).
- **Code Cleanliness & Structure:** Fully modular architecture with separation of duties between `functions.py` and `main.py`.
- **Persistent Output:** Automatically exports enriched data to `processed_students.csv` for further reporting.

---

## 9. Challenges & Learning

### Challenges Faced:
1. **Handling Windows Console Encoding:** Initial testing revealed `UnicodeEncodeError` when printing special Unicode symbols (like `✓`) on standard Windows terminals using code page `cp1252`. This was resolved by reconfiguring stdout to UTF-8 and adopting universally compatible status badges (`[OK]`).
2. **Multi-Condition Pass/Fail Logic:** Ensuring that a student with an overall average $\ge 40\%$ is still marked as `Fail` if they failed any individual subject (score $< 40$). This was cleanly solved using a nested loop in `evaluate_student_results()`.
3. **Optimizing Array Operations:** Balancing the speed of NumPy vectorization for aggregates with readable Python loops for row-level granular evaluations.

### Key Learnings:
- Combining Pandas DataFrame indexing with NumPy numerical operations for high readability and execution performance.
- Structuring Python code into reusable modules with type hints, docstrings, and robust exception handling.
- Designing CLI tools that present tabular information clearly without requiring external visual libraries.

---

## 10. GitHub Repository

- **Repository Name:** `student-performance-analytics`
- **Repository URL:** `https://github.com/[Your-GitHub-Username]/student-performance-analytics` *(Update with your repository URL upon push)*
- **Visibility:** Public
