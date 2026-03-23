# OU 2526 HK2 — Mã tham chiếu (Python Basics + NumPy/Pandas)

Thư mục mẫu tương ứng **Module_01_Python_Basics** và **Module_02_Data_Analysis** trong giáo trình.

## Cài đặt

Tại thư mục gốc `ou-2526hk2-ai`:

```bash
python -m pip install -r requirements.txt
```

*(Trên một số máy macOS/Linux, lệnh Python là `python3` — khi đó dùng `python3 -m pip install -r requirements.txt`.)*

## Chạy thử (ví dụ)

```bash
cd ou-2526hk2-ai
python module_01_python_basics/01_introduction/hello.py
```

Các script khác: chạy tương tự với đường dẫn tới file `.py` (ví dụ `python module_01_python_basics/06_file_io/text_files_demo.py`).

**Module 2** cần đã cài `numpy` và `pandas` (qua `requirements.txt`).

## Cấu trúc thư mục (tóm tắt)

- `module_01_python_basics/` — bài 1–6 Python, thư mục con theo chủ đề; `data/` chứa file mẫu.
- `module_02_data_analysis/` — NumPy / Pandas; `data/` có `iris.csv`, `titanic_sample.csv`.
- `requirements.txt` — phụ thuộc cho Module 2.
