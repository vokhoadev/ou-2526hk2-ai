"""
Module 02 - Bài 4: pivot_table, melt, stack / unstack cơ bản.
"""

import pandas as pd

sales = pd.DataFrame(
    {
        "Ngay": ["T2", "T2", "T3", "T3"],
        "Mat_hang": ["A", "B", "A", "B"],
        "So_luong": [10, 5, 7, 9],
    }
)
pt = sales.pivot_table(values="So_luong", index="Ngay", columns="Mat_hang", aggfunc="sum")
print("pivot_table:\n", pt)

long_df = pd.DataFrame({"id": [1, 2], "Q1": [10, 20], "Q2": [30, 40]})
melted = long_df.melt(id_vars=["id"], var_name="Quy", value_name="Doanh_thu")
print("\nmelt:\n", melted)

wide = pt.stack().reset_index(name="tong")
print("\nstack -> reset_index:\n", wide)
