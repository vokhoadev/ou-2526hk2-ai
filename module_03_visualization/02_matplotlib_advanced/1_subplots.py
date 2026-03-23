"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Matplotlib nang cao
Mục trong giáo trình: 1. Subplots
Nguồn: Matplotlib_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Subplots/GridSpec là cách chia nhiều panel trong một Figure để so sánh cùng thang đo hoặc kể một chuỗi hình.
  • Twin axes: hai trục Y khác đơn vị chung trục X — dễ gây hiểu nhầm nên chỉ dùng khi thật cần và ghi rõ nhãn.
  • savefig + dpi/định dạng vector (PDF/SVG) phục vụ báo cáo; style/ngữ cảnh giúp đồng bộ giao diện nhanh.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Tạo figure với 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Data
x = np.linspace(0, 10, 100)

# Plot 1: Line plot
axes[0, 0].plot(x, np.sin(x), 'b-', label='sin(x)')
axes[0, 0].set_title('Line Plot')
axes[0, 0].legend()
axes[0, 0].grid(True)

# Plot 2: Scatter plot
axes[0, 1].scatter(np.random.rand(50), np.random.rand(50), c='red', alpha=0.5)
axes[0, 1].set_title('Scatter Plot')

# Plot 3: Bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
axes[1, 0].bar(categories, values, color='green')
axes[1, 0].set_title('Bar Chart')

# Plot 4: Histogram
data = np.random.randn(1000)
axes[1, 1].hist(data, bins=30, edgecolor='black')
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# GridSpec cho layout phức tạp
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(2, 3, figure=fig)

# Subplot chiếm 2 cột
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(x, np.sin(x))
ax1.set_title('Wide Plot')

# Subplot bình thường
ax2 = fig.add_subplot(gs[0, 2])
ax2.bar(['A', 'B'], [10, 20])
ax2.set_title('Narrow Plot')

# Subplot chiếm toàn bộ hàng dưới
ax3 = fig.add_subplot(gs[1, :])
ax3.scatter(np.random.rand(100), np.random.rand(100))
ax3.set_title('Full Width Plot')

plt.tight_layout()
plt.show()
