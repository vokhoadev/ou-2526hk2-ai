"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN VI   Bai tap tong hop
Mục trong giáo trình: VI.1 Nam bai tap co loi giai (dataset `tips`)
Nguồn: Seaborn_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Tương tự phần Matplotlib: đối chiếu Axes-level vs Figure-level khi đọc ví dụ và lời giải.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import numpy as np

import seaborn as sns

x = np.linspace(0, 10, 100)
y = np.sin(x)

tips = sns.load_dataset("tips")


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(data=tips, x="total_bill", kde=True, ax=ax, color="steelblue")
ax.set_title("Phân phối total_bill (tips)")
fig.tight_layout()
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=tips, x="day", y="total_bill", hue="time", ax=ax, palette="pastel")
ax.set_title("Total bill theo ngày — tách Lunch/Dinner")
fig.tight_layout()
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", alpha=0.7, ax=ax)
ax.set_title("Tip vs total bill (màu = time)")
fig.tight_layout()
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
num = tips.select_dtypes("number")
corr = num.corr()

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, square=True, ax=ax)
ax.set_title("Correlation — tips (numeric)")
fig.tight_layout()
plt.show()


# ---------- Ví dụ / bước 6 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
g = sns.catplot(
    data=tips, kind="violin", x="day", y="total_bill", col="sex",
    height=4, aspect=1.1, palette="muted",
)
g.figure.suptitle("Phân phối total_bill theo ngày — facet theo sex", y=1.02)
plt.show()
