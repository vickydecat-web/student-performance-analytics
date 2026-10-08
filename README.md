# 🎓 Student Performance Analytics System

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.x-orange.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.x-darkgreen.svg)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

This system automates the evaluation of student academic performance, calculating totals, averages, grades, pass/fail status, subject-wise analytics, and merit rankings using **NumPy** and **Pandas**.

---

## 📑 Table of Contents
1. [Project Overview](#-project-overview)
2. [Project Structure](#-project-structure)
3. [Key Features](#-key-features)
4. [Dataset Details](#-dataset-details)
5. [Grading & Evaluation Rules](#-grading--evaluation-rules)
6. [Sample Output & Findings](#-sample-output--findings)
7. [Submission & Author Info](#-submission--author-info)

---

## 📌 Project Overview
- **Project Title:** Student Performance Analytics System
- **Technologies:** Python, NumPy, Pandas, Tabulate
- **Concepts Covered:** Variables, Data Types, Loops, Functions, NumPy Arrays, Pandas DataFrames, Academic Data Analysis.

Educational institutions routinely handle large volumes of student assessment data. This application provides a deterministic, automated analytics pipeline that:
- Reads student records from `students.csv`.
- Uses **NumPy** for numerical calculations (sums, means, standard deviations, medians).
- Employs **Pandas** for structured tabular manipulation, ranking, grouping, and exporting.
- Evaluates individual subject thresholds alongside overall percentage requirements.
- Generates comprehensive insights for educators and administrators.

---

## 📂 Project Structure

```text
student-performance-analytics/
│
├── students.csv             # Input dataset containing 20 student records
├── processed_students.csv   # Generated dataset with calculated metrics & grades
├── functions.py             # Reusable calculation, grading, and analysis functions
├── main.py                  # Main execution script and terminal dashboard
├── requirements.txt         # Dependencies (numpy, pandas, tabulate)
├── .gitignore               # Ignores venv, caches, and temporary files
├── Project_Documentation.md # Detailed 10-section assessment documentation
└── README.md                # GitHub documentation and user guide
```

---

## ⚡ Key Features

- **Automated Mark Calculations:** Computes individual student totals (out of 500) and percentages using vectorized NumPy operations (`np.sum`, `np.mean`).
- **Two-Tier Pass/Fail Logic:**
  - Requires **$\ge 40$ marks** in every single subject.
  - Requires **$\ge 50\%$ aggregate average**.
  - Any subject fail results in automatic course failure with the count of failed subjects recorded.
- **Academic Letter Grading:** Transparent mapping (`A+`, `A`, `B`, `C`, `D`, `F`).
- **Subject-Wise Analysis:** Calculates average, median, highest, lowest, standard deviation, and identifies subject toppers.
- **Departmental Comparison:** Groups performance across Computer Science, Information Technology, Electronics, Mechanical, and Civil Engineering.
- **Academic Merit List:** Extracts top 5 rankers with attendance and score breakdown.
- **Clean CLI Dashboard:** Uses tabular formatted grids for executive presentation.
- **Automated Data Export:** Writes processed data to `processed_students.csv`.

---

## 📊 Dataset Details

The dataset `students.csv` includes 20 student records with realistic distribution across 5 subjects:
- **Identifier & Info:** `StudentID`, `Name`, `Department`
- **Subjects Evaluated (0–100):** `Mathematics`, `Physics`, `Chemistry`, `ComputerScience`, `English`
- **Engagement:** `Attendance` (percentage)

---

## 🎯 Grading & Evaluation Rules

### Academic Grading Scale
| Range | Grade | Description |
|:-----:|:-----:|:------------|
| $\ge 90.0\%$ | **A+** | Outstanding |
| $80.0\% - 89.9\%$ | **A** | Excellent |
| $70.0\% - 79.9\%$ | **B** | Very Good |
| $60.0\% - 69.9\%$ | **C** | Good |
| $50.0\% - 59.9\%$ | **D** | Pass |
| $< 50.0\%$ OR Failed Any Subject | **F** | Fail |

### Passing Condition
- **Subject Minimum:** $\ge 40.0$ in each of the 5 subjects.
- **Class Average Minimum:** $\ge 50.0\%$.

---

## 📈 Sample Output & Findings

### Answers to Core Practical Questions:
1. **Which student has the highest average?**  
   👉 **Ananya Iyer (S104)** with **95.6%** (Total: 478/500).
2. **Which subject has the best average?**  
   👉 **ComputerScience** with an average score of **76.95 / 100**.
3. **How many students passed?**  
   👉 **17 out of 20 students (85.0% pass rate)**.
4. **What is the overall class average?**  
   👉 **73.9%**.

### Merit List (Top 5 Performers):
| Rank | Student ID | Name | Department | Total | Average | Grade | Attendance |
|:----:|:----------:|:-----|:-----------|:-----:|:-------:|:-----:|:----------:|
| 1 | S104 | Ananya Iyer | Computer Science | 478.0 | 95.6% | A+ | 98.0% |
| 2 | S118 | Neha Kulkarni | Computer Science | 469.0 | 93.8% | A+ | 97.0% |
| 3 | S101 | Aarav Sharma | Computer Science | 458.0 | 91.6% | A+ | 96.5% |
| 4 | S110 | Pooja Hegde | Computer Science | 453.0 | 90.6% | A+ | 94.5% |
| 5 | S108 | Sneha Reddy | Information Technology | 450.0 | 90.0% | A+ | 95.0% |

---

## 👤 Submission & Author Info

- **Course:** EWB Courses | Python with AI
- **Assignment:** Python Project Assignment
- **Submitted by:** Suryavanshi Pratyaksha Thakur
