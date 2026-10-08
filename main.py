"""
Student Performance Analytics System
================================================================================
EWB Courses | Python with AI Assignment
Project: Student Performance Analytics System
Technology: Python, NumPy, Pandas
================================================================================
"""

import os
import sys
import pandas as pd
import numpy as np

# Ensure UTF-8 output encoding on Windows terminals if supported
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Import custom reusable functions from functions.py
from functions import (
    DEFAULT_SUBJECTS,
    load_dataset,
    calculate_student_metrics,
    evaluate_student_results,
    calculate_class_summary,
    generate_subject_wise_analysis,
    get_top_performers,
    get_lowest_performers,
    get_department_analysis,
    get_grade_distribution,
    export_processed_dataset,
)


def print_banner(title: str) -> None:
    """Prints a styled decorative banner."""
    width = 78
    print("\n" + "=" * width)
    print(f" {title.upper()} ".center(width, "="))
    print("=" * width)


def print_section(title: str) -> None:
    """Prints a styled section header."""
    print(f"\n--- [ {title} ] " + "-" * (74 - len(title)))


def display_dataframe_table(df: pd.DataFrame, max_rows: int = None) -> None:
    """Displays a pandas dataframe cleanly without index truncation."""
    with pd.option_context(
        'display.max_columns', None,
        'display.width', 1000,
        'display.colheader_justify', 'left'
    ):
        if max_rows:
            print(df.head(max_rows).to_string(index=False))
        else:
            print(df.to_string(index=False))


def run_pipeline(data_file: str = "students.csv", export_file: str = "processed_students.csv") -> pd.DataFrame:
    """
    Executes the complete student analytics pipeline from ingestion to reporting.
    """
    print_banner("Student Performance Analytics System")
    print("Developed with: Python 3, NumPy, Pandas")
    print(f"Dataset Source: {data_file}")

    # -------------------------------------------------------------------------
    # STEP 1 & 2: Load and Inspect Dataset
    # -------------------------------------------------------------------------
    print_section("Step 1 & 2: Dataset Ingestion and Inspection")
    if not os.path.exists(data_file):
        print(f"[Error] Dataset file '{data_file}' not found. Please verify the file path.")
        sys.exit(1)

    df_raw = load_dataset(data_file)
    print(f"[OK] Successfully loaded dataset with {len(df_raw)} records and {len(df_raw.columns)} columns.")
    print(f"[OK] Columns detected: {list(df_raw.columns)}")
    print("\nFirst 5 Raw Records Preview:")
    display_dataframe_table(df_raw, max_rows=5)

    # -------------------------------------------------------------------------
    # STEP 3: Process the Data (NumPy & Reusable Functions)
    # -------------------------------------------------------------------------
    print_section("Step 3: Data Processing, Total Marks, Averages, Grades & Pass/Fail")
    
    # Identify subject columns
    subjects = [s for s in DEFAULT_SUBJECTS if s in df_raw.columns]
    print(f"[OK] Subjects analyzed ({len(subjects)}): {', '.join(subjects)}")

    # Calculate Totals & Averages using NumPy
    df_calc = calculate_student_metrics(df_raw, subjects)

    # Assign Grades and Pass/Fail Status via Loops & Conditions
    df_processed = evaluate_student_results(df_calc, subjects)

    print("[OK] Calculated Total Marks, Average Marks, Letter Grade, and Result Status for all students.")
    print("\nProcessed Student Records (First 10 records):")
    cols_display = [
        "StudentID", "Name", "Department", "Total_Marks", 
        "Average_Marks", "Grade", "Result_Status", "Attendance"
    ]
    display_dataframe_table(df_processed[cols_display], max_rows=10)

    # -------------------------------------------------------------------------
    # STEP 4: Analytical Insights & Answering Practical Questions
    # -------------------------------------------------------------------------
    print_section("Step 4: Answers to Key Analytical Questions")
    
    class_summary = calculate_class_summary(df_processed, subjects)
    subject_analysis = generate_subject_wise_analysis(df_processed, subjects)
    
    # 1. Which student has highest average?
    top_student = df_processed.sort_values(by="Average_Marks", ascending=False).iloc[0]
    # 2. Which subject has best average?
    best_subject_row = subject_analysis.sort_values(by="Average_Marks", ascending=False).iloc[0]
    # 3. How many students passed?
    passed_count = class_summary["Passed_Students"]
    total_students = class_summary["Total_Students"]
    # 4. What is the overall class average?
    overall_avg = class_summary["Class_Average"]

    print(f"1. Which student has the highest average?")
    print(f"   => {top_student['Name']} ({top_student['StudentID']}, {top_student['Department']})")
    print(f"      Score: {top_student['Average_Marks']}% (Total: {top_student['Total_Marks']}/500, Grade: {top_student['Grade']})\n")

    print(f"2. Which subject has the best average?")
    print(f"   => {best_subject_row['Subject']}")
    print(f"      Subject Average: {best_subject_row['Average_Marks']} / 100 (Pass Rate: {best_subject_row['Pass_Rate_%']}%)\n")

    print(f"3. How many students passed?")
    print(f"   => {passed_count} out of {total_students} students passed ({class_summary['Pass_Percentage']}% pass rate)")
    print(f"      Failed Students: {class_summary['Failed_Students']} (Scored < 40 in one or more subjects)\n")

    print(f"4. What is the overall class average?")
    print(f"   => {overall_avg}% across all students and subjects")
    print(f"      Class Range: {class_summary['Lowest_Average']}% (Lowest) to {class_summary['Highest_Average']}% (Highest)")
    print(f"      Median: {class_summary['Median_Average']}%, Std Dev: {class_summary['Standard_Deviation']}")

    # -------------------------------------------------------------------------
    # STEP 5: Deep-Dive Reports & Tables
    # -------------------------------------------------------------------------
    print_section("Subject-Wise Performance Analysis")
    display_dataframe_table(subject_analysis)

    print_section("Department-Wise Performance Summary")
    dept_df = get_department_analysis(df_processed)
    display_dataframe_table(dept_df)

    print_section("Academic Grade Distribution")
    grade_df = get_grade_distribution(df_processed)
    display_dataframe_table(grade_df)

    print_section("Top 5 Performing Students (Merit List)")
    top_5 = get_top_performers(df_processed, n=5)
    display_dataframe_table(top_5)

    print_section("Students Requiring Academic Attention / Low Performance")
    struggling = get_lowest_performers(df_processed, n=4)
    display_dataframe_table(struggling)

    # -------------------------------------------------------------------------
    # Attendance Alert
    # -------------------------------------------------------------------------
    low_att = df_processed[df_processed["Attendance_Status"] == "Shortage"]
    if not low_att.empty:
        print_section("Attendance Warning (< 75% Attendance)")
        display_dataframe_table(low_att[["StudentID", "Name", "Department", "Attendance", "Average_Marks", "Result_Status"]])

    # -------------------------------------------------------------------------
    # STEP 6: Save and Export
    # -------------------------------------------------------------------------
    print_section("Data Export")
    export_processed_dataset(df_processed, export_file)
    print(f"[OK] Fully processed dataset saved to '{export_file}'.")
    print_banner("Analysis Complete - Student Analytics System Ready")

    return df_processed


def interactive_menu(df_processed: pd.DataFrame) -> None:
    """Provides an interactive CLI menu to query individual students or departments."""
    while True:
        print("\n" + "=" * 50)
        print(" INTERACTIVE STUDENT QUERY MENU")
        print("=" * 50)
        print("1. Search Student by ID or Name")
        print("2. Filter Students by Department")
        print("3. View Grade-wise Student List")
        print("4. Re-run Full Analytics Report")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            query = input("Enter Student ID (e.g., STU001) or Name: ").strip().lower()
            match = df_processed[
                df_processed["StudentID"].str.lower().str.contains(query) |
                df_processed["Name"].str.lower().str.contains(query)
            ]
            if not match.empty:
                display_dataframe_table(match[[
                    "StudentID", "Name", "Department", "Mathematics", 
                    "Physics", "Chemistry", "Computer_Science", "English",
                    "Total_Marks", "Average_Marks", "Grade", "Result_Status", "Attendance"
                ]])
            else:
                print(f"No student matching '{query}' found.")

        elif choice == "2":
            dept = input("Enter Department name (or part of it): ").strip().lower()
            match = df_processed[df_processed["Department"].str.lower().str.contains(dept)]
            if not match.empty:
                display_dataframe_table(match[[
                    "StudentID", "Name", "Department", "Total_Marks", 
                    "Average_Marks", "Grade", "Result_Status"
                ]])
            else:
                print(f"No records found for department '{dept}'.")

        elif choice == "3":
            grade = input("Enter Grade to filter (A+, A, B, C, D, F): ").strip().upper()
            match = df_processed[df_processed["Grade"] == grade]
            if not match.empty:
                print(f"\nStudents with Grade {grade}:")
                display_dataframe_table(match[["StudentID", "Name", "Department", "Average_Marks", "Result_Status"]])
            else:
                print(f"No students found with Grade '{grade}'.")

        elif choice == "4":
            run_pipeline()

        elif choice == "5":
            print("Exiting Student Performance Analytics System. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, 4, or 5.")


def main():
    """Main entry point."""
    # Check if run with --non-interactive or if standard execution
    is_interactive = "--interactive" in sys.argv or (len(sys.argv) > 1 and sys.argv[1] == "-i")
    
    df_processed = run_pipeline()

    if is_interactive:
        interactive_menu(df_processed)


if __name__ == "__main__":
    main()
