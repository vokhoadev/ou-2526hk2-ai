"""
Module 02 - Bài 3: Đọc Excel (tùy chọn).

Cài thêm: pip install openpyxl

Ví dụ (bỏ comment khi đã có file .xlsx):

    import pandas as pd
    df = pd.read_excel("du_lieu.xlsx", sheet_name=0, engine="openpyxl")
    print(df.head())

Ở đây chỉ in hướng dẫn để tránh phụ thuộc openpyxl trong môi trường tối thiểu.
"""

def main():
    print(__doc__)


if __name__ == "__main__":
    main()
