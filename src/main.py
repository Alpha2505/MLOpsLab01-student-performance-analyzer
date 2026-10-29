"""Run the student performance analysis."""

from src.data_loader import load_student_data
from src.performance_analyzer import (
    average_attendance,
    average_exam_score,
    identify_students_for_support,
)


def main():
    students = load_student_data("data/student_performance.csv")

    print(f"Students analyzed: {len(students)}")
    print(f"Average exam score: {average_exam_score(students):.2f}")
    print(f"Average attendance: {average_attendance(students):.2f}%")

    support_ids = identify_students_for_support(students)
    print(f"Students flagged for support: {support_ids}")


if __name__ == "__main__":
    main()
