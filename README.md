# Student Performance Analyzer

## Course and Lab

This project was developed as part of **Lab 1 for IE-7374 (MLOps)** at Northeastern University.

The lab covers Python development, virtual environments, GitHub repository management, automated testing with `pytest` and `unittest`, and continuous integration using GitHub Actions.

For this implementation, I developed a student performance analyzer with a synthetic CSV dataset to demonstrate these concepts.

## Project Overview

The Student Performance Analyzer is a Python application that analyzes student performance records stored in a CSV file. It calculates average exam scores and attendance percentages and identifies students who may benefit from additional academic support.

The project demonstrates data loading, input validation, basic data analysis, automated testing, and continuous integration.

## Features

- Load student performance records from a CSV file.
- Validate student records and reject invalid data.
- Calculate the average exam score.
- Calculate the average attendance percentage.
- Identify students below specified exam-score or attendance thresholds.
- Handle missing files, missing fields, and invalid values.
- Test functionality using both `pytest` and `unittest`.
- Automatically run tests through GitHub Actions.

## Dataset

The dataset is stored in `data/student_performance.csv` and contains **10 synthetic sample records** created for this project.

Each record includes the following fields:

| Field | Description |
|---|---|
| `student_id` | Unique student identifier |
| `study_hours_per_week` | Number of hours spent studying per week |
| `attendance_percentage` | Student attendance percentage |
| `exam_score` | Exam score out of 100 |

The dataset is intended for demonstration and testing. It does not contain real student records.

## Project Structure

```text
MLOpsLab01-student-performance-analyzer/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├── data/
│   └── student_performance.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── main.py
│   └── performance_analyzer.py
├── test/
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.11 or a compatible Python version
- pip
- Git
- A GitHub account to use GitHub Actions

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Alpha2505/MLOpsLab01-student-performance-analyzer.git
cd MLOpsLab01-student-performance-analyzer
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Application

From the project root directory, run:

```bash
python -m src.main
```

The application displays the number of student records analyzed, the average exam score, the average attendance percentage, and the student IDs flagged for support.

For the included dataset, the expected output is:

```text
Students analyzed: 10
Average exam score: 71.90
Average attendance: 79.60%
Students flagged for support: ['S003', 'S006', 'S010']
```

The default support thresholds are an exam score below 60 or attendance below 75%. These thresholds are illustrative and are used to demonstrate the program's functionality.

## Testing

The project includes separate test suites for `pytest` and Python's built-in `unittest` framework.

### Run pytest

```bash
python -m pytest -v
```

The pytest suite tests calculations, record validation, threshold handling, empty inputs, CSV loading, and missing-file handling.

### Run unittest

```bash
python -m unittest test.test_unittest -v
```

The unittest suite tests the analysis functions, input validation, custom thresholds, and CSV loading.

Both suites should pass when run from the project root with the included dataset.

## Continuous Integration with GitHub Actions

The project includes two GitHub Actions workflows under `.github/workflows/`.

### Pytest Tests

The `pytest_action.yml` workflow:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs the required dependencies.
4. Runs the pytest suite.

### Unittest Tests

The `unittest_action.yml` workflow:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs the required dependencies.
4. Runs the unittest suite.

Both workflows are configured to run when changes are pushed to the `main` branch or when a pull request targets `main`.

Workflow results can be viewed in the **Actions** tab of the GitHub repository.

## Technologies Used

- Python
- CSV
- pytest
- unittest
- Git and GitHub
- GitHub Actions

## Conclusion

This project demonstrates how to build a small Python application, organize its source code and dataset, validate inputs, write automated tests using two testing frameworks, and configure GitHub Actions to run tests automatically.

The implementation provides a practical example of basic software development and continuous integration concepts covered in MLOps Lab 1.
