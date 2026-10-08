"""
=============================================================================
Student Performance Analytics System
=============================================================================
Course: EWB Courses - Python with AI
Project Title: Student Performance Analytics System
Technology: Python, NumPy, Pandas
Main Entry Script: main.py
=============================================================================
"""

import os
import sys
import numpy as np
import pandas as pd

# Import reusable modules from functions.py
from functions import (
    load_dataset,
    get_subject_list,
    calculate_totals_and_averages,
    evaluate_student_status,
    compute_overall_statistics,
    analyze_subject_performance,
    get_top_performers,
    get_department_analysis,
    answer_practical_questions,
    export_processed_data,
)


# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def print_banner(title: str):
    """Prints a styled section header banner."""
    separator = "=" * 80
    print("\n" + separator)
    print(f" {title.upper()}")
    print(separator)


def print_subbanner(title: str):
    """Prints a styled sub-section header."""
    separator = "-" * 80
    print("\n" + separator)
    print(f" >>> {title}")
    print(separator)


def display_dataframe_nicely(df: pd.DataFrame, index: bool = False):
    """Helper to print DataFrames in a clean, readable text format."""
    try:
        from tabulate import tabulate
        print(tabulate(df, headers="keys", tablefmt="grid", showindex=index))
    except ImportError:
        # Fallback to pandas string format if tabulate is not installed
        print(df.to_string(index=index))


def main():
    print_banner("Student Performance Analytics System")
    print("Welcome to the automated academic performance analysis engine.")
    print("Built with Python, NumPy, and Pandas.")

    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(base_dir, "students.csv")
    output_csv = os.path.join(base_dir, "processed_students.csv")

    # -------------------------------------------------------------------------
    # STEP 1 & 2: Load and Inspect Raw Dataset
    # -------------------------------------------------------------------------
    print_subbanner("Step 1 & 2: Loading and Inspecting Student Dataset")
    raw_df = load_dataset(input_csv)
    subjects = get_subject_list()

    print(f"\n[DATASET OVERVIEW]")
    print(f" - Total Records Loaded: {len(raw_df)}")
    print(f" - Total Columns: {len(raw_df.columns)}")
    print(f" - Column Names: {list(raw_df.columns)}")
    print(f" - Subjects Evaluated: {subjects}")

    print("\n[FIRST 5 STUDENT RECORDS (RAW)]: ")
    display_dataframe_nicely(raw_df.head(5))

    # -------------------------------------------------------------------------
    # STEP 3: Process the Data (Calculations, NumPy Ops, Grading, Pass/Fail)
    # -------------------------------------------------------------------------
    print_subbanner("Step 3: Processing Data (NumPy & Pandas Calculations)")
    print("Performing numerical calculations:")
    print(" 1. Calculating row-wise total marks using np.sum(axis=1)")
    print(" 2. Calculating row-wise average marks using np.mean(axis=1)")
    print(" 3. Applying pass/fail rule (min 40 per subject AND avg >= 50)")
    print(" 4. Assigning academic letter grades (A+, A, B, C, D, F)")
    print(" 5. Computing overall rank based on total marks")

    # Total and Average Calculation using NumPy
    processed_df = calculate_totals_and_averages(raw_df, subjects)

    # Pass/Fail evaluation and grading with loops and NumPy
    processed_df = evaluate_student_status(processed_df, subjects, min_pass_mark=40.0)

    print("\n[PROCESSED STUDENT DATA TABLE (SUMMARY VIEW)]:")
    summary_cols = ["Rank", "StudentID", "Name", "Department", "Total_Marks", "Average_Marks", "Attendance", "Grade", "Status"]
    display_dataframe_nicely(processed_df[summary_cols])

    # Export processed data to CSV
    export_processed_data(processed_df, output_csv)

    # -------------------------------------------------------------------------
    # STEP 4: Perform In-Depth Analysis
    # -------------------------------------------------------------------------
    print_banner("Step 4: Comprehensive Performance Analytics & Insights")

    # 4.1 Overall Class Statistics
    print_subbanner("4.1 Class Overall Statistical Metrics")
    class_stats = compute_overall_statistics(processed_df)
    stats_df = pd.DataFrame(list(class_stats.items()), columns=["Metric", "Value"])
    display_dataframe_nicely(stats_df)

    # 4.2 Subject-Wise Performance Analysis
    print_subbanner("4.2 Subject-Wise Performance Analysis")
    subject_df = analyze_subject_performance(processed_df, subjects, min_pass_mark=40.0)
    display_dataframe_nicely(subject_df)

    # 4.3 Top Performers / Merit List
    print_subbanner("4.3 Academic Merit List - Top 5 Performers")
    top_5 = get_top_performers(processed_df, n=5)
    display_dataframe_nicely(top_5)

    # 4.4 Department-Wise Performance Breakdown
    print_subbanner("4.4 Department-Wise Performance Summary")
    dept_df = get_department_analysis(processed_df)
    display_dataframe_nicely(dept_df)

    # 4.5 Grade Distribution Analysis
    print_subbanner("4.5 Grade Distribution Analysis")
    grade_counts = processed_df["Grade"].value_counts().reindex(["A+", "A", "B", "C", "D", "F"], fill_value=0)
    grade_df = pd.DataFrame({
        "Grade": grade_counts.index,
        "Student Count": grade_counts.values,
        "Percentage (%)": np.round((grade_counts.values / len(processed_df)) * 100, 2)
    })
    display_dataframe_nicely(grade_df)

    # -------------------------------------------------------------------------
    # STEP 5: Answers to Practical Assignment Questions
    # -------------------------------------------------------------------------
    print_banner("Step 5: Executive Answers to Assignment Questions")
    answers = answer_practical_questions(processed_df, subject_df)

    print("\n  Q1: Which student has the highest average?")
    print(f"  --> Answer: {answers['highest_avg_student']}\n")

    print("  Q2: Which subject has the best average?")
    print(f"  --> Answer: {answers['best_avg_subject']}\n")

    print("  Q3: How many students passed?")
    print(f"  --> Answer: {answers['students_passed']}\n")

    print("  Q4: What is the overall class average?")
    print(f"  --> Answer: {answers['class_average']}\n")

    print("=" * 80)
    print(" [COMPLETED] Student Performance Analytics pipeline finished successfully.")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
