"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Seaborn nang cao
Mục trong giáo trình: 4. Pair Plots
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

# Load iris dataset
iris = sns.load_dataset('iris')

# Pairplot
sns.pairplot(iris, hue='species', palette='husl')
plt.show()


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Custom diagonal and off-diagonal plots
g = sns.pairplot(iris, hue='species',
                 diag_kind='kde',  # 'hist' or 'kde'
                 plot_kws={'alpha': 0.6},
                 diag_kws={'fill': True})
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

g = sns.PairGrid(iris, hue='species')
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot, kde=True)
g.add_legend()
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

iris = sns.load_dataset('iris')
g = sns.pairplot(iris, hue='species', corner=True, diag_kind='kde',
                 plot_kws={'alpha': 0.5})
plt.show()
