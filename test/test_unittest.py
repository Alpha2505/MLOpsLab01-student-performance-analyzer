"""Unit tests for the student performance analyzer."""

import unittest

from src.data_loader import load_student_data
from src.performance_analyzer import (
    average_attendance,
    average_exam_score,
    identify_students_for_support,
    validate_student,
)


class TestPerformanceAnalyzer(unittest.TestCase):

    def setUp(self):
        self.students = [
            {
                "student_id": "B01",
                "study_hours_per_week": 8,
                "attendance_percentage": 90,
                "exam_score": 80,
            },
            {
                "student_id": "B02",
                "study_hours_per_week": 3,
                "attendance_percentage": 65,
                "exam_score": 50,
            },
        ]

    def test_average_exam_score(self):
        self.assertEqual(average_exam_score(self.students), 65)

    def test_average_attendance(self):
        self.assertEqual(average_attendance(self.students), 77.5)

    def test_identifies_students_for_support(self):
        self.assertEqual(
            identify_students_for_support(self.students), ["B02"]
        )

    def test_valid_student(self):
        self.assertTrue(validate_student(self.students[0]))

    def test_rejects_attendance_above_100(self):
        self.students[0]["attendance_percentage"] = 105

        with self.assertRaisesRegex(ValueError, "Attendance"):
            validate_student(self.students[0])

    def test_rejects_missing_fields(self):
        with self.assertRaisesRegex(ValueError, "missing required fields"):
            validate_student({"student_id": "B03"})

    def test_rejects_empty_student_id(self):
        self.students[0]["student_id"] = ""

        with self.assertRaisesRegex(ValueError, "Student ID"):
            validate_student(self.students[0])

    def test_empty_list_raises_error(self):
        with self.assertRaisesRegex(ValueError, "At least one"):
            average_attendance([])

    def test_loads_csv_dataset(self):
        students = load_student_data("data/student_performance.csv")

        self.assertEqual(len(students), 10)
        self.assertAlmostEqual(average_exam_score(students), 71.9)

    def test_custom_thresholds(self):
        result = identify_students_for_support(
            self.students,
            score_threshold=55,
            attendance_threshold=70,
        )

        self.assertEqual(result, ["B02"])


if __name__ == "__main__":
    unittest.main()
