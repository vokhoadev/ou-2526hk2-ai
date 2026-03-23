"""
Module 01 - Bài 6: CSV (csv module) và JSON — đọc/ghi, DictReader.
"""

import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "data"
STUDENTS_CSV = BASE / "students.csv"
OUT_CSV = BASE / "students_export.csv"
OUT_JSON = BASE / "students.json"


def read_csv_rows():
    print("--- csv.reader ---")
    with open(STUDENTS_CSV, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        print("Header:", header)
        for row in reader:
            name, age, grade = row
            print(f"  {name}: tuổi {age}, điểm {grade}")


def read_csv_dict():
    print("--- DictReader ---")
    with open(STUDENTS_CSV, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print(f"  {row['name']}: {row['grade']}")


def write_csv_and_json():
    rows = [
        ["Name", "Age", "Grade"],
        ["An", "20", "8.5"],
        ["Binh", "21", "9.0"],
    ]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Đã ghi CSV:", OUT_CSV)

    data = [{"name": "An", "age": 20, "grade": 8.5}]
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Đã ghi JSON:", OUT_JSON)

    with open(OUT_JSON, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    print("Đọc lại JSON:", loaded)


if __name__ == "__main__":
    read_csv_rows()
    read_csv_dict()
    write_csv_and_json()
