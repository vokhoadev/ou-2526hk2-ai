# OU 2526 HK2 — Mã tham chiếu (Python, NumPy/Pandas, Visualization)

Mã mẫu tương ứng **Module_01_Python_Basics**, **Module_02_Data_Analysis** và **Module_03_Visualization** trong giáo trình.

## Cài đặt

Tại thư mục gốc `ou-2526hk2-ai`:

```bash
python -m pip install -r requirements.txt
```

Trên macOS/Linux thường dùng `python3` thay cho `python`.

## Chạy thử

```bash
cd ou-2526hk2-ai
python module_01_python_basics/01_introduction/hello.py
```

Các file `.py` khác chạy tương tự theo đường dẫn. Phụ thuộc chính nằm trong `requirements.txt` (Module 2: NumPy/Pandas; Module 3: thêm Matplotlib/Seaborn).

## Cấu trúc thư mục

| Thư mục | Nội dung |
|--------|----------|
| `module_01_python_basics/` | Bài 1–6 Python, theo chủ đề; có `data/` mẫu. |
| `module_02_data_analysis/` | NumPy / Pandas; `data/` có `iris.csv`, `titanic_sample.csv`. |
| `module_03_visualization/` | Matplotlib / Seaborn: chỉ `.py`, cấu trúc `01_`…`10_`; tên file ASCII. Mỗi file có docstring mở đầu; ví dụ ghép nhiều khối được phân tách bằng dòng `# ---------- Ví dụ ...`. `data/` copy từ module 2. |
| `requirements.txt` | Thư viện cần cho module 2–3. |

### Module 3 — tạo lại từ Markdown

Cần thư mục **`Module_03_Visualization`** cùng cấp với `ou-2526hk2-ai` (tức `../Module_03_Visualization` khi đứng trong repo).

```bash
python3 tools/build_module_03_from_markdown.py
```

Kiểm tra toàn bộ script chạy được (không mở cửa sổ đồ họa):

```bash
MPLBACKEND=Agg python3 tools/check_module_03_visualization.py
```

Ví dụ ngắn: `module_03_visualization/misc/tips_histplot_demo.py`.
