"""
Module 01 - Bài 6: Đọc/ghi file văn bản, with open, encoding UTF-8.
Chạy từ thư mục chứa file này hoặc dùng đường dẫn tương đối tới data/.
"""

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "data"
SAMPLE = BASE / "sample.txt"
OUT = BASE / "output_demo.txt"


def main():
    # Đọc toàn bộ
    with open(SAMPLE, "r", encoding="utf-8") as f:
        content = f.read()
    print("--- read() ---\n", content)

    # Đọc từng dòng
    print("--- for line ---")
    with open(SAMPLE, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

    # Ghi file
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("Dòng ghi mới\n")
        f.write("Tham chiếu Module 01 - File I/O\n")
    print("Đã ghi:", OUT)


if __name__ == "__main__":
    main()
