"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Seaborn nang cao
Mục trong giáo trình: 6. Joint Plots
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

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Scatter + histograms
sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter')
plt.show()

# With regression line
sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')
plt.show()

# Hexbin
sns.jointplot(data=tips, x='total_bill', y='tip', kind='hex')
plt.show()

# KDE
sns.jointplot(data=tips, x='total_bill', y='tip', kind='kde', fill=True)
plt.show()
