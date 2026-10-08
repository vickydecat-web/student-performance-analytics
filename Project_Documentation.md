# Student Performance Analytics System - Project Documentation

**Course:** EWB Courses | Python with AI  
**Assignment:** Python Project Assignment  

---

## 1. Project Title & Student Details

- **Project Title:** Student Performance Analytics System
- **Domain:** Educational Data Analytics / Academic Performance Evaluation
- **Language / Tech Stack:** Python 3, NumPy, Pandas, Tabulate
- **Submitted by:** Suryavanshi Pratyaksha Thakur

---

## 2. Objective

Educational institutions routinely handle large volumes of student assessment data. Manual evaluation of student marks, calculation of percentages, determination of letter grades, and tracking of academic risk are time-consuming and error-prone.

The **Student Performance Analytics System** was developed to automate the end-to-end student evaluation lifecycle:
1. Ingest multi-subject academic records and attendance metrics cleanly into structured data frames.
2. Automate numerical calculations (total scores, average percentage, rank, standard deviation) using fast, vectorized operations.
3. Enforce deterministic grading rules and multi-criteria pass/fail requirements (subject threshold + aggregate average).
4. Uncover cohort-level insights, including subject strengths/weaknesses, top performers, and department comparisons.
5. Answer core academic management questions through structured summary reports.

---

## 3. Technologies Used

| Technology / Library | Purpose in Project |
|----------------------|--------------------|
| **Python 3.13** | Core programming language for logic, loops, functions, and control flow. |
| **NumPy** | Vectorized array operations, statistical metrics (`np.sum`, `np.mean`, `np.std`, `np.median`, `np.max`, `np.min`, `np.argmax`, `np.count_nonzero`). |
| **Pandas** | Tabular data ingestion (`read_csv`), DataFrame transformations, filtering, ranking, aggregations (`groupby`), and CSV export. |
| **Tabulate** | Clean CLI formatting and grid display of results. |
| **Python `venv`** | Isolated virtual environment managing package dependencies. |
| **Git & GitHub** | Source code version control and project delivery. |

---

## 4. Dataset Description

The dataset is stored in `students.csv` and contains realistic academic records for 20 students across diverse engineering departments.

### Schema & Important Columns

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| `StudentID` | String | Unique identifier for each student (e.g., S101 to S120). |
| `Name` | String | Full name of the student. |
| `Department` | String | Academic department (Computer Science, IT, Electronics, Mechanical, Civil). |
| `Mathematics` | Float / Integer | Score in Mathematics (0–100). |
| `Physics` | Float / Integer | Score in Physics (0–100). |
| `Chemistry` | Float / Integer | Score in Chemistry (0–100). |
| `ComputerScience`| Float / Integer | Score in Computer Science (0–100). |
| `English` | Float / Integer | Score in English (0–100). |
| `Attendance` | Float | Percentage attendance recorded across the semester (60% to 100%). |

- **Total Records:** 20 students
- **Total Marks Possible:** 500 (5 subjects × 100 marks)

---

## 5. Implementation Workflow

The implementation follows a modular 5-step methodology:

### Step 1: Dataset Preparation
A realistic dataset was synthesized in `students.csv`, including high achievers (>90%), moderate performers (60–80%), borderline students (50–60%), and failing students (<40% in individual subjects).

### Step 2: Data Loading & Verification (`load_dataset`)
Using `pd.read_csv()`, the file is read into a DataFrame. Schema validation, record counts, and null-value integrity checks are performed before processing.

### Step 3: Numerical Processing & Business Logic
1. **Total & Average Calculation:**  
   The subject columns are extracted as a 2D NumPy array. `np.sum(axis=1)` calculates total marks and `np.mean(axis=1)` calculates overall percentage in a single vectorized step.
2. **Pass/Fail Criteria:**  
   Evaluated per student using a loop and NumPy boolean masking:
   - A student passes if **and only if** they score $\ge 40$ in **every individual subject** AND their overall average is $\ge 50\%$.
   - Any score below 40 in any subject flags the student as `Fail` with the count of failed subjects recorded.
3. **Academic Grading:**  
   Assigned via `assign_grade()`:
   - $90.0\% \le \text{Avg}$: **A+**
   - $80.0\% \le \text{Avg} < 90.0\%$: **A**
   - $70.0\% \le \text{Avg} < 80.0\%$: **B**
   - $60.0\% \le \text{Avg} < 70.0\%$: **C**
   - $50.0\% \le \text{Avg} < 60.0\%$: **D**
   - $\text{Avg} < 50.0\%$ or any failed subject: **F**
4. **Ranking:**  
   Calculated using `rank(ascending=False, method='min')` based on total marks.

### Step 4: Analytical Insights & Aggregations
- **Class-Level Metrics:** Overall mean, median, standard deviation, pass rate, attendance average.
- **Subject-Wise Analysis:** Iterates through each subject using loops to compute mean, min, max, standard deviation, subject pass percentage, and subject topper.
- **Departmental Comparison:** Grouped analysis identifying department-wise average score, pass rates, and attendance.
- **Merit List:** Top 5 rankers extracted for special recognition.

### Step 5: Export & Reporting
- Formatted CLI display with tabular grids.
- Processed student results saved to `processed_students.csv` for downstream reporting.

---

## 6. Key Features

1. **Modular Architecture:** Logic is cleanly separated between reusable library functions (`functions.py`) and execution orchestration (`main.py`).
2. **Vectorized Numerical Computing:** Intensive mathematical operations (row sums, subject means, deviations) leverage high-performance NumPy arrays.
3. **Strict Subject-Level Failure Tracking:** Unlike simple averaging, the system flags students who fail even a single subject despite high marks elsewhere.
4. **Subject-Wise Diagnostic Engine:** Evaluates which subject has the highest difficulty (lowest average) versus highest success rate.
5. **Departmental Benchmarking:** Aggregates multi-department cohorts to identify variance across academic divisions.
6. **Automated Export:** Exports processed data with added columns (`Total_Marks`, `Average_Marks`, `Status`, `Grade`, `Rank`, `Failed_Subjects_Count`).

---

## 7. Output & Results Walkthrough

### 7.1 Practical Questions Answered

| Question | Analytical Finding |
|----------|-------------------|
| **Which student has the highest average?** | **Ananya Iyer (S104)** with **95.6%** (478 / 500) |
| **Which subject has the best average?** | **ComputerScience** with an average score of **76.95 / 100** |
| **How many students passed?** | **17 out of 20 students (85.0%)** |
| **What is the overall class average?** | **73.9%** |

### 7.2 Top 5 Rankers (Merit List)

| Rank | Student ID | Name | Department | Total Marks | Average Marks | Grade | Attendance |
|:----:|:----------:|:-----|:-----------|:-----------:|:-------------:|:-----:|:----------:|
| 1 | S104 | Ananya Iyer | Computer Science | 478.0 | 95.6% | A+ | 98.0% |
| 2 | S118 | Neha Kulkarni | Computer Science | 469.0 | 93.8% | A+ | 97.0% |
| 3 | S101 | Aarav Sharma | Computer Science | 458.0 | 91.6% | A+ | 96.5% |
| 4 | S110 | Pooja Hegde | Computer Science | 453.0 | 90.6% | A+ | 94.5% |
| 5 | S108 | Sneha Reddy | Information Technology | 450.0 | 90.0% | A+ | 95.0% |

### 7.3 Grade Distribution

| Grade | Meaning | Student Count | Percentage |
|:-----:|:--------|:-------------:|:----------:|
| **A+** | Outstanding (90%+) | 5 | 25.0% |
| **A** | Excellent (80–89.9%) | 4 | 20.0% |
| **B** | Very Good (70–79.9%) | 4 | 20.0% |
| **C** | Good (60–69.9%) | 3 | 15.0% |
| **D** | Pass (50–59.9%) | 1 | 5.0% |
| **F** | Fail (<50% or failed subject) | 3 | 15.0% |

---

## 8. Final Outcome

The project successfully delivered:
- A fully functional, production-ready Python command-line application.
- Accurate numerical processing using both NumPy and Pandas without external heavy machine learning frameworks.
- Transparent reporting covering individual, subject-level, and department-level academic metrics.
- Export of enriched student records to CSV.
- Clean code architecture following PEP 8 best practices.

---

## 9. Challenges & Learning

### Challenges Faced:
1. **Differentiating Average Pass from Subject Pass:**  
   A student could have a cumulative average of 54% but score 35% in Mathematics. If grading only checked average marks, the student would incorrectly pass. This was solved by combining NumPy array condition masks (`student_marks < 40`) with aggregate averages.
2. **Handling Multi-Criteria Ranking:**  
   Ensuring tied marks or ranks behaved consistently was solved using Pandas' `.rank(method='min', ascending=False)`.
3. **Clean Output Formatting:**  
   Standard `print(df)` truncates columns on narrow screens; using `tabulate` with grid borders provided readability.

### Key Learnings:
- Combining Pandas DataFrames with underlying NumPy arrays for fast array-level calculations.
- Structuring Python applications into separate modules (`functions.py` and `main.py`).
- Writing reproducible workflows using virtual environments and dependency specifications (`requirements.txt`).

---

## 10. GitHub Repository

- **Repository Link:** `https://github.com/SuryavanshiPratyaksha/student-performance-analytics`
- **Branch:** `main`
- **License:** MIT (or Educational Use)
