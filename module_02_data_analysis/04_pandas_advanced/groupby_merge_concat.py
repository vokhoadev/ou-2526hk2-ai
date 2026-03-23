"""
Module 02 - Bài 4 Pandas: groupby/agg, merge, concat.
"""

from pathlib import Path

import pandas as pd

IRIS = Path(__file__).resolve().parent.parent / "data" / "iris.csv"
df = pd.read_csv(IRIS)

print("groupby species — mean sepal_length:\n", df.groupby("species")["sepal_length"].mean())
print(
    "\nagg:\n",
    df.groupby("species").agg(
        mean_petal=("petal_length", "mean"),
        count=("species", "count"),
    ),
)

left = pd.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
right = pd.DataFrame({"id": [2, 3, 4], "score": [10, 20, 30]})
print("\nmerge inner:\n", pd.merge(left, right, on="id", how="inner"))

print("\nconcat axis=0:\n", pd.concat([left, left], axis=0, ignore_index=True))
