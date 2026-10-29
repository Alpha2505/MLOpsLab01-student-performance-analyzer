"""Load student performance records from a CSV file."""

import csv
from pathlib import Path

from src.performance_analyzer import validate_student


def load_student_data(file_path):
    """Load and validate student records from a CSV file."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}")

    students = []

    with path.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        required_columns = {
            "student_id",
            "study_hours_per_week",
            "attendance_percentage",
            "exam_score",
        }

        if not reader.fieldnames or not required_columns.issubset(
            reader.fieldnames
        ):
            raise ValueError("CSV file is missing required columns.")

        for row in reader:
            if not any(value and value.strip() for value in row.values()):
                continue

            try:
                student = {
                    "student_id": row["student_id"].strip(),
                    "study_hours_per_week": float(
                        row["study_hours_per_week"]
                    ),
                    "attendance_percentage": float(
                        row["attendance_percentage"]
                    ),
                    "exam_score": float(row["exam_score"]),
                }
            except (ValueError, TypeError, AttributeError) as error:
                raise ValueError(
                    f"Invalid data in CSV row {reader.line_num}."
                ) from error

            validate_student(student)
            students.append(student)

    if not students:
        raise ValueError("The CSV file contains no student records.")

    return students
