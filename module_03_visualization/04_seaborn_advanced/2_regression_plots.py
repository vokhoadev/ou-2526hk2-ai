"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Seaborn nang cao
Mục trong giáo trình: 2. Regression Plots
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

# regplot - single plot
plt.figure(figsize=(8, 6))
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha': 0.5})
plt.title('Regression Plot')
plt.show()

# lmplot - with faceting
g = sns.lmplot(data=tips, x='total_bill', y='tip', 
               hue='smoker', col='time', row='sex',
               height=4, aspect=1.2)
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

plt.figure(figsize=(8, 6))
sns.residplot(data=tips, x='total_bill', y='tip', lowess=False)
plt.title('Residual Plot')
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

fmri = sns.load_dataset('fmri')
g = sns.relplot(data=fmri, x='timepoint', y='signal', hue='event', style='event',
                col='region', kind='line', height=4, facet_kws={'sharex': False})
plt.show()
