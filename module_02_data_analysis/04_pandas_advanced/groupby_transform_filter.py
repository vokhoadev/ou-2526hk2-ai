"""
Module 02 - Bài 4: groupby transform, filter (theo giáo trình nâng cao).
"""

from pathlib import Path

import pandas as pd

iris_path = Path(__file__).resolve().parent.parent / "data" / "iris.csv"
df = pd.read_csv(iris_path)

# Chuẩn hóa petal_length theo từng loài (transform)
g = df.groupby("species")["petal_length"]
df["petal_z"] = g.transform(lambda s: (s - s.mean()) / s.std())
print(df[["species", "petal_length", "petal_z"]].head(6))

# Chỉ giữ nhóm có số dòng >= 3 (ví dụ filter)
filtered = df.groupby("species").filter(lambda x: len(x) >= 3)
print("\nSố dòng sau filter:", len(filtered))
