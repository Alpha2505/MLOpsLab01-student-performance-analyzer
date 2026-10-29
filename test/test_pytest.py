"""Pytest tests for the student performance analyzer."""

import pytest

from src.data_loader import load_student_data
from src.performance_analyzer import (
    average_attendance,
    average_exam_score,
    identify_students_for_support,
    validate_student,
)


@pytest.fixture
def sample_students():
    return [
        {
            "student_id": "A01",
            "study_hours_per_week": 10,
            "attendance_percentage": 90,
            "exam_score": 85,
        },
        {
            "student_id": "A02",
            "study_hours_per_week": 4,
            "attendance_percentage": 60,
            "exam_score": 55,
        },
    ]


def test_average_exam_score(sample_students):
    assert average_exam_score(sample_students) == 70


def test_average_attendance(sample_students):
    assert average_attendance(sample_students) == 75


def test_identifies_students_below_threshold(sample_students):
    assert identify_students_for_support(sample_students) == ["A02"]


def test_valid_student_record(sample_students):
    assert validate_student(sample_students[0]) is True


def test_rejects_exam_score_above_100(sample_students):
    sample_students[0]["exam_score"] = 105

    with pytest.raises(ValueError, match="Exam score"):
        validate_student(sample_students[0])


def test_rejects_negative_study_hours(sample_students):
    sample_students[0]["study_hours_per_week"] = -1

    with pytest.raises(ValueError, match="Study hours"):
        validate_student(sample_students[0])


def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="At least one"):
        average_exam_score([])


def test_missing_csv_file_raises_error(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_student_data(tmp_path / "missing.csv")


def test_loads_project_dataset():
    students = load_student_data("data/student_performance.csv")

    assert len(students) == 10
    assert students[0]["student_id"] == "S001"
    assert average_exam_score(students) == pytest.approx(71.9)


def test_rejects_invalid_threshold(sample_students):
    with pytest.raises(ValueError, match="Score threshold"):
        identify_students_for_support(
            sample_students, score_threshold=101
        )
