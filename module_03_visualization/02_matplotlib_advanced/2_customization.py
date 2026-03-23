"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Matplotlib nang cao
Mục trong giáo trình: 2. Customization
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
y1, y2 = np.sin(x), np.cos(x)
y3, y4 = np.sin(x) * 0.5, np.cos(x) * 0.5

fig, ax = plt.subplots(figsize=(10, 6))

# Line styles
ax.plot(x, y1, 'r-', linewidth=2, label='Solid Red')
ax.plot(x, y2, 'b--', linewidth=1.5, label='Dashed Blue')
ax.plot(x, y3, 'g:', linewidth=2, label='Dotted Green')
ax.plot(x, y4, 'm-.', linewidth=1, label='Dash-dot Magenta')

# Markers (ví dụ trên đoạn ngắn)
ax.plot(x[:20], y1[:20], 'o-', markersize=8, markerfacecolor='yellow',
        markeredgecolor='black', markeredgewidth=2, label='With markers')

ax.legend(loc='upper right', fontsize=8)
ax.set_title('Colors, line styles, markers')
plt.show()

# Scatter với colormap (figure riêng để colorbar gọn)
fig, ax = plt.subplots(figsize=(8, 6))
sizes = np.random.rand(50) * 200 + 20
colors = np.random.rand(50)
sc = ax.scatter(np.random.rand(50) * 10, np.random.rand(50), c=colors, cmap='viridis', s=sizes, alpha=0.7)
plt.colorbar(sc, ax=ax, label='Value')
ax.set_title('Scatter with colormap')
plt.show()


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y1)

# Title và labels
ax.set_title('My Plot', fontsize=16, fontweight='bold')
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis', fontsize=12)

# Axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Ticks
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['Zero', 'Two', 'Four', 'Six', 'Eight', 'Ten'])

# Grid
ax.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='upper right', fontsize=10)


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Giả sử đã có fig, ax, x, y (mảng numpy)
x = np.linspace(0, 10, 100)
y = np.sin(x)
x_max, y_max = x[np.argmax(y)], y.max()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y)

# Text annotation
ax.annotate('Maximum', xy=(x_max, y_max), xytext=(x_max + 1, y_max + 0.3),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=12, color='red')

# Vertical/Horizontal lines
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=5, color='r', linestyle='--', linewidth=1)

# Shaded region giữa hai đường
ax.fill_between(x, np.sin(x), np.cos(x), alpha=0.3, color='blue')
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

fig, ax1 = plt.subplots(figsize=(10, 6))
x = np.arange(1, 13)
temp = np.random.uniform(20, 35, 12)
rain = np.random.uniform(0, 300, 12)

ax1.bar(x, rain, alpha=0.4, color='steelblue', label='Rain (mm)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Rainfall (mm)', color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')

ax2 = ax1.twinx()
ax2.plot(x, temp, color='orangered', marker='o', linewidth=2, label='Temp (°C)')
ax2.set_ylabel('Temperature (°C)', color='orangered')
ax2.tick_params(axis='y', labelcolor='orangered')
plt.title('Twin axes example')
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

fig, axes = plt.subplots(2, 2, figsize=(10, 8), constrained_layout=True)
for ax in axes.flat:
    ax.plot([0, 1], [0, 1])
fig.suptitle('Using constrained_layout=True')
plt.show()
