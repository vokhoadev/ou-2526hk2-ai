"""
Module 02 - Bài 3 Pandas: read_csv, head/info/describe, [], loc, iloc.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data" / "titanic_sample.csv"

df = pd.read_csv(DATA)
print("head():\n", df.head())
print("\ninfo():")
df.info()
print("\ndescribe():\n", df.describe())

print("\nCột Sex:\n", df["Sex"])
print("\niloc[0:3, 0:3]:\n", df.iloc[0:3, 0:3])
print("\nloc[:, ['Name','Fare']] (3 dòng đầu):\n", df.loc[0:2, ["Name", "Fare"]])

print("\nLọc Survived == 1:\n", df[df["Survived"] == 1][["Name", "Pclass"]])
