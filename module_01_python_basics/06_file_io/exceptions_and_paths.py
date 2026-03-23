"""
Module 01 - Bài 6: xử lý ngoại lệ khi đọc file, pathlib (Path, mkdir, exists).
"""

from __future__ import annotations

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "data"
MISSING = BASE / "khong_ton_tai.txt"


def read_safe(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Không tìm thấy file:", path)
        return None
    except OSError as e:
        print("Lỗi OS:", e)
        return None


def main():
    out_dir = BASE / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    print("Thư mục tồn tại?", out_dir.exists(), "->", out_dir)

    read_safe(MISSING)
    ok = BASE / "sample.txt"
    content = read_safe(ok)
    if content:
        print("Đọc OK, độ dài:", len(content))


if __name__ == "__main__":
    main()
