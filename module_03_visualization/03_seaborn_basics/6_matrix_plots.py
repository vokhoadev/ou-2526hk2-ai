"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: 6. Matrix Plots
Nguồn: Seaborn_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Seaborn xây trên Matplotlib, thường nhận data=DataFrame và tên cột — phù hợp dữ liệu dạng bảng (tidy).
  • Phân biệt phân phối (hist/KDE/box/violin), phân loại (bar/count/strip/swarm), quan hệ (scatter/line).
  • hue= tách nhóm bằng màu; một biểu đồ chỉ nên trả lời một câu hỏi phân tích rõ ràng.

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
correlation = tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', 
            center=0, fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Custom heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, 
            cmap='RdYlBu_r',
            linewidths=0.5,
            square=True,
            vmin=-1, vmax=1)
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Clustered heatmap
iris = sns.load_dataset('iris')
iris_pivot = iris.drop('species', axis=1)

sns.clustermap(iris_pivot.sample(50), 
               cmap='viridis',
               figsize=(10, 10))
plt.show()
