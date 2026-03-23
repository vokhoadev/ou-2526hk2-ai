"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: 7. Multi-Plot Grids
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

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Pairwise relationships
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species')
plt.show()

# Customized
sns.pairplot(iris, hue='species', 
             diag_kind='kde',
             plot_kws={'alpha': 0.6})
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Scatter with marginal distributions
sns.jointplot(data=tips, x='total_bill', y='tip', kind='scatter')
plt.show()

# Kinds: 'scatter', 'kde', 'hist', 'hex', 'reg'
sns.jointplot(data=tips, x='total_bill', y='tip', 
              kind='kde', fill=True)
plt.show()

# Regression
sns.jointplot(data=tips, x='total_bill', y='tip', 
              kind='reg', height=8)
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Create grid manually
g = sns.FacetGrid(tips, col='time', row='sex', height=4)
g.map(sns.histplot, 'total_bill')
g.add_legend()
plt.show()

# With different plot types
g = sns.FacetGrid(tips, col='time', hue='sex', height=5)
g.map(sns.scatterplot, 'total_bill', 'tip')
g.add_legend()
plt.show()
