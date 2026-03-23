"""
Module 02 - Bài 4: apply / map, rename cột, drop_duplicates.
"""

import pandas as pd

df = pd.DataFrame({"ten": ["An", "Binh", "An"], "diem": [8, 9, 8]})
df["xep_loai"] = df["diem"].apply(lambda s: "Gioi" if s >= 8.5 else "Kha")
print(df)

df2 = df.rename(columns={"ten": "Name", "diem": "Score"})
print("\nrename:\n", df2)

dup = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print("\ncó trùng?\n", dup.duplicated())
print("\nsau drop_duplicates:\n", dup.drop_duplicates())
