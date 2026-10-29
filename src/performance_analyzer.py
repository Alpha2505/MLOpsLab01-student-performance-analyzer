"""Analyze student performance records."""

from statistics import mean


def validate_student(student):
    """Validate one student's performance record."""
    required = {
        "student_id",
        "study_hours_per_week",
        "attendance_percentage",
        "exam_score",
    }

    if not required.issubset(student):
        raise ValueError("Student record is missing required fields.")

    if not student["student_id"]:
        raise ValueError("Student ID cannot be empty.")

    study_hours = student["study_hours_per_week"]
    attendance = student["attendance_percentage"]
    score = student["exam_score"]

    if study_hours < 0:
        raise ValueError("Study hours cannot be negative.")

    if not 0 <= attendance <= 100:
        raise ValueError("Attendance must be between 0 and 100.")

    if not 0 <= score <= 100:
        raise ValueError("Exam score must be between 0 and 100.")

    return True


def average_exam_score(students):
    """Return the average exam score for a collection of students."""
    if not students:
        raise ValueError("At least one student record is required.")

    for student in students:
        validate_student(student)

    return mean(student["exam_score"] for student in students)


def average_attendance(students):
    """Return the average attendance percentage."""
    if not students:
        raise ValueError("At least one student record is required.")

    for student in students:
        validate_student(student)

    return mean(
        student["attendance_percentage"] for student in students
    )


def identify_students_for_support(
    students, score_threshold=60, attendance_threshold=75
):
    """Identify students below either academic support threshold."""
    if not 0 <= score_threshold <= 100:
        raise ValueError("Score threshold must be between 0 and 100.")

    if not 0 <= attendance_threshold <= 100:
        raise ValueError("Attendance threshold must be between 0 and 100.")

    for student in students:
        validate_student(student)

    return [
        student["student_id"]
        for student in students
        if student["exam_score"] < score_threshold
        or student["attendance_percentage"] < attendance_threshold
    ]
