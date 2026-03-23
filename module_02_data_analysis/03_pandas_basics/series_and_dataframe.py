"""
Module 02 - Bài 3 Pandas: Series, DataFrame tạo từ dict/list, thao tác cơ bản.
"""

import numpy as np
import pandas as pd

print("Pandas version:", pd.__version__)

s = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print(s)
print("s > 25:\n", s[s > 25])
print("describe:\n", s.describe())

df = pd.DataFrame(
    {
        "Name": ["An", "Binh", "Cuong"],
        "Math": [80, 90, 85],
        "English": [75, 88, 92],
    }
)
print("\nDataFrame:\n", df)
print("\n dtypes:\n", df.dtypes)
