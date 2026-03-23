"""
Module 02 - Bài 4 Pandas: thiếu dữ liệu, thêm/xóa cột, sort_values.
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "A": [1, 2, np.nan, 4],
        "B": [5, np.nan, np.nan, 8],
        "Name": ["x", "y", "z", None],
    }
)
print("isnull().sum():\n", df.isnull().sum())

df_drop = df.dropna()
print("\nAfter dropna():\n", df_drop)

df_fill = df.copy()
df_fill["A"] = df_fill["A"].fillna(df_fill["A"].mean())
df_fill["B"] = df_fill["B"].fillna(0)
df_fill["Name"] = df_fill["Name"].fillna("unknown")
print("\nAfter fillna:\n", df_fill)

grades = pd.DataFrame(
    {"Name": ["An", "Binh", "Cuong"], "Math": [80, 90, 85], "English": [75, 88, 92]}
)
grades["Average"] = (grades["Math"] + grades["English"]) / 2
print("\nThêm cột Average:\n", grades.sort_values("Average", ascending=False))
