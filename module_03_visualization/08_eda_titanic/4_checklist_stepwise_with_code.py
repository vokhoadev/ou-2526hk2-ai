"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): Guide_EDA_Visualization_Titanic.md
Mục trong giáo trình: 4. Checklist   tung buoc co code
Nguồn: Guide_EDA_Visualization_Titanic.md

Nắm bản chất — gợi ý đọc code:
  • EDA: từ cấu trúc dữ liệu (shape, dtype, missing) → phân phối → quan hệ → so sánh nhóm — visualization là công cụ suy nghĩ.
  • Mỗi biểu đồ nên kèm một câu hỏi (ví dụ: fare lệch phải? tuổi thiếu nhiều không?).

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

x = np.linspace(0, 10, 100)
y = np.sin(x)

print(df.shape)
df.info()
df.describe(include="all").T  # T: dễ đọc hàng là cột


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print("Numeric:", numeric_cols)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.histplot(df["age"].dropna(), kde=True, ax=axes[0], color="steelblue")
axes[0].set_title("Tuổi (age) — phân phối + KDE")

sns.histplot(df["fare"], kde=True, ax=axes[1], color="coral")
axes[1].set_title("Giá vé (fare) — thường lệch phải (skew)")

plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

missing = df.isna().sum().sort_values(ascending=False)
missing = missing[missing > 0]
print(missing)

plt.figure(figsize=(8, 4))
sns.barplot(x=missing.values, y=missing.index.astype(str), palette="Reds_r", orient="h")
plt.xlabel("Số ô trống")
plt.title("Missing theo cột (Titanic)")
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

plt.figure(figsize=(10, 5))
sns.heatmap(df.isna(), cbar=False, yticklabels=False, cmap="YlOrRd")
plt.title("Vị trí missing (mỗi cột một vạch dọc)")
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

target = "survived"
vc = df[target].value_counts().sort_index()
print(vc)
print("Tỷ lệ sống:", df[target].mean().round(3))

plt.figure(figsize=(5, 4))
sns.countplot(data=df, x=target, palette="Set2")
plt.title("Phân phối target: survived (0/1)")
plt.xlabel("survived")
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 6 (khối ghép từ giáo trình; có thể chạy riêng) ----------

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

sns.countplot(data=df, x="class", hue="survived", ax=axes[0], palette="pastel")
axes[0].set_title("Số người theo class × survived")

sns.barplot(data=df, x="sex", y="survived", ax=axes[1], palette="muted", errorbar="sd")
axes[1].set_ylabel("Tỷ lệ survived (mean)")
axes[1].set_title("Tỷ lệ sống theo giới (bar = mean)")

plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 7 (khối ghép từ giáo trình; có thể chạy riêng) ----------

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="class", y="age", estimator=np.median, errorbar=("pi", 95), palette="Blues")
plt.title("Tuổi trung vị theo hạng vé (median + khoảng tin cậy)")
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 8 (khối ghép từ giáo trình; có thể chạy riêng) ----------

num = df.select_dtypes(include=[np.number]).drop(columns=["survived"], errors="ignore")
# Giữ survived để xem tương quan với số — có thể concat tạm:
corr_df = df[["survived", "age", "fare", "pclass", "sibsp", "parch"]].corr(numeric_only=True)

plt.figure(figsize=(7, 5))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="coolwarm", center=0, square=True)
plt.title("Correlation (Pearson) — các biến số chọn lọc")
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 9 (khối ghép từ giáo trình; có thể chạy riêng) ----------

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.boxplot(data=df, y="fare", ax=axes[0], color="lightblue")
axes[0].set_title("Boxplot fare — thấy outlier phía trên")

sns.boxplot(data=df, x="class", y="fare", ax=axes[1], palette="pastel")
axes[1].set_title("Fare theo class")
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 10 (khối ghép từ giáo trình; có thể chạy riêng) ----------

plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="age", y="fare", hue="survived", alpha=0.6, palette="Set1")
plt.title("Age vs fare (màu = survived)")
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 11 (khối ghép từ giáo trình; có thể chạy riêng) ----------

cols = ["survived", "age", "fare", "pclass"]
sns.pairplot(df[cols].dropna(), hue="survived", corner=True, plot_kws={"alpha": 0.4, "s": 20})
plt.suptitle("Pairplot (góc dưới) — survived", y=1.02)
plt.show()


# ---------- Ví dụ / bước 12 (khối ghép từ giáo trình; có thể chạy riêng) ----------

g = sns.FacetGrid(df, col="class", hue="survived", height=3.5, aspect=1)
g.map(sns.histplot, "age", kde=True, alpha=0.5)
g.add_legend()
g.figure.suptitle("Phân phối tuổi theo class (màu = survived)", y=1.05)
plt.tight_layout()
plt.show()
