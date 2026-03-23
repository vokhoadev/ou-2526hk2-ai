"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: 4. Subplots
Nguồn: Matplotlib_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Figure là khung tổng thể; Axes là một vùng vẽ có trục — mọi thứ quan trọng thường gắn với ax (OOP) hoặc plt (pyplot).
  • Mỗi loại plot trả lời một câu hỏi: line (xu hướng theo thứ tự), scatter (hai biến số), bar (so sánh nhóm), hist (phân phối một biến).
  • Nhãn trục, tiêu đề, legend không phải trang trí — chúng nói rõ đơn vị, nhóm dữ liệu và thang đo.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Access individual subplots
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine')

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title('Cosine')

axes[1, 0].bar(['A', 'B', 'C'], [1, 2, 3])
axes[1, 0].set_title('Bar')

axes[1, 1].scatter(np.random.rand(50), np.random.rand(50))
axes[1, 1].set_title('Scatter')

plt.tight_layout()
plt.show()


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Share x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))
ax1.plot(x, np.sin(x))
ax2.plot(x, np.cos(x))
plt.show()

# Share y-axis
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12, 5))
ax1.plot(x, y)
ax2.plot(x, y + 0.5)
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# GridSpec for complex layouts
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, :])       # Top row, all columns
ax2 = fig.add_subplot(gs[1, :-1])     # Middle row, first 2 cols
ax3 = fig.add_subplot(gs[1:, -1])     # Right column, last 2 rows
ax4 = fig.add_subplot(gs[-1, 0])      # Bottom left
ax5 = fig.add_subplot(gs[-1, 1])      # Bottom middle

ax1.plot(x, y)
ax1.set_title('Full Width')

ax2.bar(['A', 'B', 'C'], [1, 2, 3])
ax3.scatter(np.random.rand(20), np.random.rand(20))
ax4.hist(np.random.randn(100))
ax5.pie([1, 2, 3])

plt.tight_layout()
plt.show()
