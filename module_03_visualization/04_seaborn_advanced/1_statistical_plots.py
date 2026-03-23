"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Seaborn nang cao
Mục trong giáo trình: 1. Statistical Plots
Nguồn: Seaborn_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Heatmap/pairplot nhìn ma trận tương quan hoặc nhiều cặp biến — chú ý quy mô màu và chú thích.
  • FacetGrid/relplot/catplot tạo lưới theo biến phân loại — giống 'small multiples' trong lý thuyết visualization.
  • Joint plot kết hợp marginal (cạnh) với scatter chính giữa để thấy phân phối từng biến.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(0, 10, 100)
y = np.sin(x)


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Load sample data
tips = sns.load_dataset('tips')

# Box plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[0])
axes[0].set_title('Box Plot')

# Violin plot
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True, ax=axes[1])
axes[1].set_title('Violin Plot')

plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Strip plot
sns.stripplot(data=tips, x='day', y='total_bill', hue='sex', 
              dodge=True, alpha=0.7, ax=axes[0])
axes[0].set_title('Strip Plot')

# Swarm plot
sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex', 
              dodge=True, ax=axes[1])
axes[1].set_title('Swarm Plot')

plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Box plot + Strip plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', palette='pastel')
sns.stripplot(data=tips, x='day', y='total_bill', color='black', alpha=0.5, size=4)
plt.title('Box Plot with Individual Points')
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Barplot với hue
# Lưu ý: Seaborn ≥ 0.12 dùng errorbar='sd'; phiên bản cũ thử ci='sd' hoặc bỏ errorbar.
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[0], errorbar='sd')
axes[0].set_title('Mean total_bill by day (errorbar=sd)')

sns.pointplot(data=tips, x='size', y='tip', hue='sex', ax=axes[1], errorbar=('ci', 95))
axes[1].set_title('Mean tip by party size')
plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 6 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Cùng API: strip | swarm | box | violin | bar | point | count
g = sns.catplot(data=tips, x='day', y='total_bill', hue='sex', col='time',
                kind='box', height=4, aspect=1.1)
g.set_titles('{col_name}')
plt.show()
