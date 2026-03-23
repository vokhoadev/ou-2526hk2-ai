# OU 2526 HK2 — Mã tham chiếu (Python Basics + NumPy/Pandas + Visualization)

Thư mục mẫu tương ứng **Module_01_Python_Basics**, **Module_02_Data_Analysis** và **Module_03_Visualization** trong giáo trình.

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

**Module 2** cần đã cài `numpy` và `pandas`; **Module 3** thêm `matplotlib` và `seaborn` (tất cả trong `requirements.txt`).

## Cấu trúc thư mục (tóm tắt)

- `module_01_python_basics/` — bài 1–6 Python, thư mục con theo chủ đề; `data/` chứa file mẫu.
- `module_02_data_analysis/` — NumPy / Pandas; `data/` có `iris.csv`, `titanic_sample.csv`.
- `module_03_visualization/` — Matplotlib / Seaborn: **chỉ file `.py`** trích từ giáo trình & lab (cấu trúc `01_`…`10_`); tên file **ASCII, không dấu**, không hậu tố kiểu `10_min` / `15_phút`. Mỗi file có **docstring hướng dẫn sinh viên** (bản chất nội dung + cách đọc code) và **dòng `# ----------` phân tách** các khối ví dụ ghép từ Markdown. `data/` copy từ module 2. Tạo lại: `python tools/build_module_03_from_markdown.py` (nguồn: `Module_03_Visualization` cạnh repo). Demo ngắn: `misc/tips_histplot_demo.py`. Kiểm tra chạy hết (không GUI): `MPLBACKEND=Agg python3 tools/check_module_03_visualization.py`.
- `requirements.txt` — phụ thuộc cho Module 2–3.
