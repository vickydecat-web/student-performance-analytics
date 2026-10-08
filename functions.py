"""
Student Performance Analytics System - Reusable Functions Module
Author: EWB Python with AI Student
Purpose: Reusable functions for data loading, processing, numerical analysis,
         grading, pass/fail evaluation, and performance reporting.
"""

import numpy as np
import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Loads student dataset from a CSV file into a Pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded DataFrame containing student records.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully loaded dataset from '{file_path}' with {len(df)} records.")
        return df
    except FileNotFoundError:
        print(f"[ERROR] The file '{file_path}' was not found.")
        raise
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while loading data: {e}")
        raise


def get_subject_list() -> list:
    """
    Returns the standard list of subjects evaluated in this system.
    """
    return ["Mathematics", "Physics", "Chemistry", "ComputerScience", "English"]


def calculate_totals_and_averages(df: pd.DataFrame, subjects: list) -> pd.DataFrame:
    """
    Calculates total marks and average percentage marks for each student
    using NumPy array calculations for efficiency and precision.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        subjects (list): List of subject column names.
        
    Returns:
        pd.DataFrame: DataFrame with 'Total_Marks' and 'Average_Marks' columns added.
    """
    data_copy = df.copy()
    
    # Extract marks matrix as a NumPy 2D array
    marks_matrix = data_copy[subjects].to_numpy()
    
    # Use NumPy functions for row-wise sum and mean
    totals = np.sum(marks_matrix, axis=1)
    averages = np.mean(marks_matrix, axis=1)
    
    data_copy["Total_Marks"] = np.round(totals, 2)
    data_copy["Average_Marks"] = np.round(averages, 2)
    
    return data_copy


def assign_grade(average_mark: float, has_failed_subject: bool) -> str:
    """
    Assigns a letter grade based on a clearly defined academic rule.
    If a student failed any subject, grade F is assigned regardless of average.
    
    Grading Scale:
        Average >= 90: A+ (Outstanding)
        Average >= 80: A  (Excellent)
        Average >= 70: B  (Very Good)
        Average >= 60: C  (Good)
        Average >= 50: D  (Pass)
        Average < 50 or Failed Subject: F (Fail)
    """
    if has_failed_subject or average_mark < 50.0:
        return "F"
    elif average_mark >= 90.0:
        return "A+"
    elif average_mark >= 80.0:
        return "A"
    elif average_mark >= 70.0:
        return "B"
    elif average_mark >= 60.0:
        return "C"
    else:
        return "D"


def evaluate_student_status(df: pd.DataFrame, subjects: list, min_pass_mark: float = 40.0) -> pd.DataFrame:
    """
    Evaluates pass/fail status and assigns grades for all students using
    a loop across records combined with NumPy evaluation logic.
    
    Passing Condition:
        1. Must score >= 40 marks in EVERY individual subject.
        2. Must achieve an overall average mark of >= 50.
        
    Parameters:
        df (pd.DataFrame): DataFrame with calculated marks and averages.
        subjects (list): List of subject column names.
        min_pass_mark (float): Minimum passing mark per subject (default 40.0).
        
    Returns:
        pd.DataFrame: DataFrame with 'Status', 'Grade', and 'Failed_Subjects_Count'.
    """
    data_copy = df.copy()
    statuses = []
    grades = []
    failed_counts = []
    
    # Use loop to iterate through each student record
    for index, row in data_copy.iterrows():
        # Convert student marks to a NumPy array for vectorized condition checking
        student_marks = np.array([row[sub] for sub in subjects])
        
        # Identify how many subjects are below minimum passing mark using NumPy
        failed_subject_mask = student_marks < min_pass_mark
        num_failed = np.count_nonzero(failed_subject_mask)
        failed_counts.append(num_failed)
        
        # Student passes only if NO subject is failed and overall average is >= 50
        is_pass = (num_failed == 0) and (row["Average_Marks"] >= 50.0)
        status_label = "Pass" if is_pass else "Fail"
        statuses.append(status_label)
        
        # Assign grade
        grade_label = assign_grade(row["Average_Marks"], has_failed_subject=(not is_pass))
        grades.append(grade_label)
        
    data_copy["Failed_Subjects_Count"] = failed_counts
    data_copy["Status"] = statuses
    data_copy["Grade"] = grades
    
    # Calculate Rank based on Total_Marks (descending)
    data_copy["Rank"] = data_copy["Total_Marks"].rank(ascending=False, method="min").astype(int)
    
    return data_copy


def compute_overall_statistics(df: pd.DataFrame) -> dict:
    """
    Computes overall class summary metrics using NumPy statistical functions.
    
    Returns a dictionary of key statistics.
    """
    avg_marks = df["Average_Marks"].to_numpy()
    total_marks = df["Total_Marks"].to_numpy()
    attendance = df["Attendance"].to_numpy()
    
    total_students = len(df)
    passed_students = int(np.count_nonzero(df["Status"].to_numpy() == "Pass"))
    failed_students = total_students - passed_students
    pass_percentage = (passed_students / total_students) * 100.0
    
    stats = {
        "Total Students": total_students,
        "Passed Students": passed_students,
        "Failed Students": failed_students,
        "Pass Percentage": np.round(pass_percentage, 2),
        "Class Average Mark (%)": np.round(np.mean(avg_marks), 2),
        "Class Median Mark (%)": np.round(np.median(avg_marks), 2),
        "Class Standard Deviation": np.round(np.std(avg_marks), 2),
        "Highest Average Mark (%)": np.round(np.max(avg_marks), 2),
        "Lowest Average Mark (%)": np.round(np.min(avg_marks), 2),
        "Highest Total Marks": np.round(np.max(total_marks), 2),
        "Lowest Total Marks": np.round(np.min(total_marks), 2),
        "Average Attendance (%)": np.round(np.mean(attendance), 2)
    }
    return stats


def analyze_subject_performance(df: pd.DataFrame, subjects: list, min_pass_mark: float = 40.0) -> pd.DataFrame:
    """
    Performs subject-wise statistical analysis using NumPy calculations inside a loop.
    
    Returns a DataFrame containing performance metrics for each subject.
    """
    subject_stats = []
    
    # Loop across each subject
    for subject in subjects:
        scores = df[subject].to_numpy()
        
        mean_score = np.mean(scores)
        median_score = np.median(scores)
        std_score = np.std(scores)
        max_score = np.max(scores)
        min_score = np.min(scores)
        passed_count = np.count_nonzero(scores >= min_pass_mark)
        pass_rate = (passed_count / len(scores)) * 100.0
        
        # Find student with highest mark in this subject
        top_idx = np.argmax(scores)
        top_student = df.iloc[top_idx]["Name"]
        
        subject_stats.append({
            "Subject": subject,
            "Average Mark": np.round(mean_score, 2),
            "Median Mark": np.round(median_score, 2),
            "Highest Mark": int(max_score),
            "Lowest Mark": int(min_score),
            "Std Deviation": np.round(std_score, 2),
            "Pass Rate (%)": np.round(pass_rate, 2),
            "Subject Topper": top_student
        })
        
    return pd.DataFrame(subject_stats)


def get_top_performers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Identifies top N performing students based on total marks and average.
    """
    columns_to_show = ["Rank", "StudentID", "Name", "Department", "Total_Marks", "Average_Marks", "Grade", "Attendance"]
    sorted_df = df.sort_values(by=["Total_Marks", "Average_Marks"], ascending=[False, False])
    return sorted_df[columns_to_show].head(n).reset_index(drop=True)


def get_department_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes department-wise performance summary using Pandas aggregation and NumPy means.
    """
    dept_summary = df.groupby("Department").agg(
        Total_Students=("StudentID", "count"),
        Average_Score=("Average_Marks", lambda x: np.round(np.mean(x), 2)),
        Highest_Score=("Average_Marks", lambda x: np.round(np.max(x), 2)),
        Pass_Count=("Status", lambda x: (x == "Pass").sum()),
        Avg_Attendance=("Attendance", lambda x: np.round(np.mean(x), 2))
    ).reset_index()
    
    dept_summary["Pass_Rate (%)"] = np.round(
        (dept_summary["Pass_Count"] / dept_summary["Total_Students"]) * 100.0, 2
    )
    return dept_summary


def answer_practical_questions(df: pd.DataFrame, subject_df: pd.DataFrame) -> dict:
    """
    Explicitly answers the practical questions required by Step 4 of the guidelines:
    1. Which student has the highest average?
    2. Which subject has the best average?
    3. How many students passed?
    4. What is the overall class average?
    """
    # 1. Student with highest average
    best_student_row = df.loc[df["Average_Marks"].idxmax()]
    best_student = f"{best_student_row['Name']} ({best_student_row['StudentID']}) with {best_student_row['Average_Marks']}%"
    
    # 2. Subject with best average
    best_subject_row = subject_df.loc[subject_df["Average Mark"].idxmax()]
    best_subject = f"{best_subject_row['Subject']} with an average of {best_subject_row['Average Mark']}"
    
    # 3. How many students passed
    pass_count = int(np.count_nonzero(df["Status"].to_numpy() == "Pass"))
    pass_info = f"{pass_count} out of {len(df)} students ({np.round((pass_count / len(df)) * 100, 2)}%)"
    
    # 4. Overall class average
    overall_avg = float(np.round(np.mean(df["Average_Marks"].to_numpy()), 2))
    class_avg_info = f"{overall_avg}%"
    
    return {
        "highest_avg_student": best_student,
        "best_avg_subject": best_subject,
        "students_passed": pass_info,
        "class_average": class_avg_info
    }


def export_processed_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Saves the processed DataFrame with totals, averages, grades, and ranks to CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"[INFO] Processed student data successfully saved to '{output_path}'.")
