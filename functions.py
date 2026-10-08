"""
Student Performance Analytics System - Core Functions Module
Author: EWB Python with AI Student
Technologies: Python, NumPy, Pandas

This module contains reusable functions for reading, processing, calculating,
and analyzing student academic performance datasets.
"""

from typing import Dict, List, Tuple
import numpy as np
import pandas as pd


# Default subject list used across analysis
DEFAULT_SUBJECTS: List[str] = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Computer_Science",
    "English"
]

# Pass mark threshold per subject
PASS_MARK_THRESHOLD: float = 40.0
# Minimum attendance threshold required
MINIMUM_ATTENDANCE_THRESHOLD: float = 75.0


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Loads student data from a CSV file into a Pandas DataFrame.
    Validates structure and checks for missing values.

    Args:
        file_path (str): Relative or absolute path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned and loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The dataset file '{file_path}' was not found.")
    except Exception as e:
        raise RuntimeError(f"Error loading CSV file: {e}")

    # Strip any extra whitespace from string columns
    str_cols = df.select_dtypes(include=["object"]).columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()

    # Fill or report missing values if any exist
    if df.isnull().values.any():
        print("[Notice] Missing values detected. Filling missing numeric values with 0.")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(0)

    return df


def calculate_student_metrics(
    df: pd.DataFrame, 
    subject_columns: List[str]
) -> pd.DataFrame:
    """
    Calculates total marks and average percentage for each student using NumPy.

    Args:
        df (pd.DataFrame): Input student DataFrame.
        subject_columns (List[str]): List of column names representing subjects.

    Returns:
        pd.DataFrame: DataFrame updated with 'Total_Marks' and 'Average_Marks'.
    """
    df_copy = df.copy()

    # Extract subject marks as a NumPy 2D array (N x M)
    marks_matrix = df_copy[subject_columns].to_numpy(dtype=float)

    # Use NumPy vector operations for fast and accurate calculations
    total_marks = np.sum(marks_matrix, axis=1)
    average_marks = np.mean(marks_matrix, axis=1)

    df_copy["Total_Marks"] = np.round(total_marks, 2)
    df_copy["Average_Marks"] = np.round(average_marks, 2)

    return df_copy


def assign_grade(average_score: float) -> str:
    """
    Assigns an academic letter grade based on a clearly defined grading scale:
      - 90 <= Score <= 100 : A+ (Outstanding)
      - 80 <= Score < 90   : A  (Excellent)
      - 70 <= Score < 80   : B  (Good)
      - 60 <= Score < 70   : C  (Average)
      - 50 <= Score < 60   : D  (Pass)
      - Score < 50         : F  (Fail)

    Args:
        average_score (float): The average percentage score.

    Returns:
        str: Grade label.
    """
    if average_score >= 90.0:
        return "A+"
    elif average_score >= 80.0:
        return "A"
    elif average_score >= 70.0:
        return "B"
    elif average_score >= 60.0:
        return "C"
    elif average_score >= 50.0:
        return "D"
    else:
        return "F"


def evaluate_student_results(
    df: pd.DataFrame, 
    subject_columns: List[str],
    pass_mark: float = PASS_MARK_THRESHOLD,
    min_attendance: float = MINIMUM_ATTENDANCE_THRESHOLD
) -> pd.DataFrame:
    """
    Assigns grades and determines Pass/Fail status for each student.
    Demonstrates the required use of loops and conditional logic across records.

    Rules:
      1. Pass Condition: Student must score >= pass_mark (40) in EVERY subject.
      2. If any subject is below pass_mark, Status is 'Fail'.
      3. Attendance Warning: Flagged if Attendance < min_attendance (75%).

    Args:
        df (pd.DataFrame): DataFrame with 'Average_Marks'.
        subject_columns (List[str]): List of subject column names.
        pass_mark (float): Minimum mark in each subject to pass.
        min_attendance (float): Minimum attendance threshold.

    Returns:
        pd.DataFrame: DataFrame enriched with 'Grade', 'Result_Status', and 'Attendance_Status'.
    """
    df_copy = df.copy()

    grades: List[str] = []
    statuses: List[str] = []
    attendance_flags: List[str] = []
    failed_subjects_list: List[str] = []

    # Iteration through records using a loop as required by assignment guidelines
    for _, row in df_copy.iterrows():
        # 1. Assign Grade based on student's average
        avg = row["Average_Marks"]
        grades.append(assign_grade(avg))

        # 2. Check each subject individually using a loop
        failed_subs = []
        for subject in subject_columns:
            if row[subject] < pass_mark:
                failed_subs.append(subject)

        # 3. Determine overall Result Status
        if len(failed_subs) == 0 and avg >= pass_mark:
            statuses.append("Pass")
            failed_subjects_list.append("None")
        else:
            statuses.append("Fail")
            failed_subjects_list.append(", ".join(failed_subs) if failed_subs else "Low Avg")

        # 4. Check Attendance status
        attendance_val = row["Attendance"] if "Attendance" in row else 100.0
        if attendance_val < min_attendance:
            attendance_flags.append("Shortage")
        else:
            attendance_flags.append("Regular")

    df_copy["Grade"] = grades
    df_copy["Result_Status"] = statuses
    df_copy["Failed_Subjects"] = failed_subjects_list
    df_copy["Attendance_Status"] = attendance_flags

    return df_copy


def calculate_class_summary(
    df: pd.DataFrame, 
    subject_columns: List[str]
) -> Dict[str, float]:
    """
    Calculates overall class summary statistics using NumPy.

    Args:
        df (pd.DataFrame): Processed DataFrame with 'Average_Marks' and 'Result_Status'.
        subject_columns (List[str]): List of subject column names.

    Returns:
        Dict[str, float]: Summary dictionary of class statistics.
    """
    averages_arr = df["Average_Marks"].to_numpy()
    total_students = len(df)

    passed_count = int(np.sum(df["Result_Status"].to_numpy() == "Pass"))
    failed_count = total_students - passed_count
    pass_percentage = (passed_count / total_students) * 100 if total_students > 0 else 0.0

    summary = {
        "Total_Students": total_students,
        "Class_Average": float(np.round(np.mean(averages_arr), 2)),
        "Highest_Average": float(np.round(np.max(averages_arr), 2)),
        "Lowest_Average": float(np.round(np.min(averages_arr), 2)),
        "Median_Average": float(np.round(np.median(averages_arr), 2)),
        "Standard_Deviation": float(np.round(np.std(averages_arr), 2)),
        "Passed_Students": passed_count,
        "Failed_Students": failed_count,
        "Pass_Percentage": float(np.round(pass_percentage, 2))
    }
    return summary


def generate_subject_wise_analysis(
    df: pd.DataFrame, 
    subject_columns: List[str],
    pass_mark: float = PASS_MARK_THRESHOLD
) -> pd.DataFrame:
    """
    Computes detailed subject-wise statistics (Average, Highest, Lowest, Std Dev,
    Pass Count, Fail Count, Pass Rate) using loops and NumPy.

    Args:
        df (pd.DataFrame): Input DataFrame.
        subject_columns (List[str]): List of subject names.
        pass_mark (float): Cutoff mark for passing a subject.

    Returns:
        pd.DataFrame: Subject performance analysis table.
    """
    subject_data = []

    # Iterating through subject columns using a loop
    for subject in subject_columns:
        marks = df[subject].to_numpy(dtype=float)

        sub_avg = float(np.round(np.mean(marks), 2))
        sub_highest = float(np.max(marks))
        sub_lowest = float(np.min(marks))
        sub_std = float(np.round(np.std(marks), 2))
        sub_passed = int(np.sum(marks >= pass_mark))
        sub_failed = int(np.sum(marks < pass_mark))
        sub_pass_rate = float(np.round((sub_passed / len(marks)) * 100, 2))

        subject_data.append({
            "Subject": subject,
            "Average_Marks": sub_avg,
            "Highest_Mark": sub_highest,
            "Lowest_Mark": sub_lowest,
            "Std_Dev": sub_std,
            "Passed_Count": sub_passed,
            "Failed_Count": sub_failed,
            "Pass_Rate_%": sub_pass_rate
        })

    analysis_df = pd.DataFrame(subject_data)
    return analysis_df


def get_top_performers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Identifies the top N performing students sorted by Average Marks.

    Args:
        df (pd.DataFrame): Processed student DataFrame.
        n (int): Number of top performers to retrieve.

    Returns:
        pd.DataFrame: Top N students with rank, ID, name, department, and score.
    """
    cols_to_show = [
        "StudentID", "Name", "Department", "Total_Marks", 
        "Average_Marks", "Grade", "Result_Status"
    ]
    available_cols = [c for c in cols_to_show if c in df.columns]

    top_df = df.sort_values(by="Average_Marks", ascending=False).head(n).copy()
    top_df.insert(0, "Rank", range(1, len(top_df) + 1))
    return top_df[["Rank"] + available_cols]


def get_lowest_performers(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """
    Identifies the lowest performing students requiring academic intervention.

    Args:
        df (pd.DataFrame): Processed student DataFrame.
        n (int): Number of records.

    Returns:
        pd.DataFrame: Lowest N students.
    """
    cols_to_show = [
        "StudentID", "Name", "Department", "Total_Marks", 
        "Average_Marks", "Grade", "Result_Status", "Failed_Subjects", "Attendance"
    ]
    available_cols = [c for c in cols_to_show if c in df.columns]
    bottom_df = df.sort_values(by="Average_Marks", ascending=True).head(n).copy()
    return bottom_df[available_cols]


def get_department_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates department-wise comparison metrics: student count, department average,
    highest average, and pass rate.

    Args:
        df (pd.DataFrame): Processed DataFrame.

    Returns:
        pd.DataFrame: Department summary DataFrame.
    """
    dept_summary = []
    departments = df["Department"].unique()

    for dept in departments:
        dept_data = df[df["Department"] == dept]
        dept_count = len(dept_data)
        dept_avg = float(np.round(np.mean(dept_data["Average_Marks"].to_numpy()), 2))
        dept_highest = float(np.max(dept_data["Average_Marks"].to_numpy()))
        dept_passed = int(np.sum(dept_data["Result_Status"].to_numpy() == "Pass"))
        dept_pass_rate = float(np.round((dept_passed / dept_count) * 100, 2))

        dept_summary.append({
            "Department": dept,
            "Total_Students": dept_count,
            "Average_Marks": dept_avg,
            "Top_Score": dept_highest,
            "Pass_Rate_%": dept_pass_rate
        })

    summary_df = pd.DataFrame(dept_summary).sort_values(by="Average_Marks", ascending=False)
    return summary_df


def get_grade_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the distribution and percentage of each grade category.

    Args:
        df (pd.DataFrame): Processed DataFrame.

    Returns:
        pd.DataFrame: Grade count and percentage distribution.
    """
    grade_order = ["A+", "A", "B", "C", "D", "F"]
    grade_counts = df["Grade"].value_counts().to_dict()
    total = len(df)

    dist_data = []
    for g in grade_order:
        count = grade_counts.get(g, 0)
        percentage = np.round((count / total) * 100, 2) if total > 0 else 0.0
        dist_data.append({
            "Grade": g,
            "Student_Count": count,
            "Percentage_%": percentage
        })

    return pd.DataFrame(dist_data)


def export_processed_dataset(df: pd.DataFrame, output_path: str) -> None:
    """
    Saves the analyzed dataset to a CSV file.

    Args:
        df (pd.DataFrame): Enriched DataFrame.
        output_path (str): Destination path.
    """
    df.to_csv(output_path, index=False)
