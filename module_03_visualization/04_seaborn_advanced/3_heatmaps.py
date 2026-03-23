"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Seaborn nang cao
Mục trong giáo trình: 3. Heatmaps
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
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation = tips.select_dtypes(include='number').corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', square=True, linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Pivot table heatmap
pivot = tips.pivot_table(values='tip', index='day', columns='time', aggfunc='mean')

plt.figure(figsize=(8, 6))
sns.heatmap(pivot, annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Average Tip by Day and Time')
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Hierarchical clustering heatmap
g = sns.clustermap(correlation, annot=True, cmap='coolwarm',
                   figsize=(8, 8), fmt='.2f', center=0)
g.fig.suptitle('Clustered Correlation Matrix', y=1.02)
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

plt.figure(figsize=(8, 6))
sns.kdeplot(data=tips, x='total_bill', y='tip', fill=True, levels=5, thresh=0.05)
plt.title('Bivariate KDE: total_bill vs tip')
plt.show()
