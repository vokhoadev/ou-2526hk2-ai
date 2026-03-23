"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Seaborn nang cao
Mục trong giáo trình: 5. FacetGrid
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

# Create grid
g = sns.FacetGrid(tips, col='time', row='smoker', height=4)
g.map(sns.scatterplot, 'total_bill', 'tip')
g.add_legend()
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

g = sns.FacetGrid(tips, col='day', col_wrap=2, height=4)
g.map(sns.histplot, 'total_bill', kde=True)
g.set_titles('{col_name}')
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

def custom_plot(x, y, **kwargs):
    plt.scatter(x, y, **kwargs)
    plt.axhline(y.mean(), color='red', linestyle='--')

g = sns.FacetGrid(tips, col='time', row='sex', height=4)
g.map(custom_plot, 'total_bill', 'tip', alpha=0.5)
plt.show()
