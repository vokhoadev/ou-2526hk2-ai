"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: 3. Plot Customization
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

# Named colors
plt.plot(x, y, color='red')
plt.plot(x, y, color='steelblue')

# Hex colors
plt.plot(x, y, color='#FF5733')

# RGB tuple
plt.plot(x, y, color=(0.1, 0.2, 0.5))

# Line styles
plt.plot(x, y, linestyle='-')    # Solid
plt.plot(x, y, linestyle='--')   # Dashed
plt.plot(x, y, linestyle=':')    # Dotted
plt.plot(x, y, linestyle='-.')   # Dash-dot

# Markers
plt.plot(x, y, marker='o')       # Circle
plt.plot(x, y, marker='s')       # Square
plt.plot(x, y, marker='^')       # Triangle
plt.plot(x, y, marker='*')       # Star

# Combined format string
plt.plot(x, y, 'ro-')    # Red circles, solid line
plt.plot(x, y, 'bs--')   # Blue squares, dashed


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Figure size and DPI
fig = plt.figure(figsize=(12, 6), dpi=100)

# Title and labels
plt.title('Main Title', fontsize=16, fontweight='bold')
plt.xlabel('X Label', fontsize=12)
plt.ylabel('Y Label', fontsize=12)

# Axis limits
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# Axis ticks
plt.xticks([0, 2, 4, 6, 8, 10])
plt.yticks([-1, 0, 1], ['Low', 'Mid', 'High'])

# Grid
plt.grid(True)
plt.grid(True, linestyle='--', alpha=0.7)

# Legend
plt.legend(loc='upper right')  # 'best', 'upper left', etc.
plt.legend(loc='upper right', fontsize=10, framealpha=0.9)


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)

# Add text
plt.text(5, 0.5, 'Text here', fontsize=12, color='red')

# Add annotation with arrow
plt.annotate('Maximum', xy=(np.pi/2, 1), xytext=(3, 1.3),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=10)

# Add horizontal/vertical lines
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=np.pi, color='r', linestyle=':', alpha=0.5)

plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Available styles
print(plt.style.available)

# Use a style
plt.style.use('seaborn-v0_8')
plt.style.use('ggplot')
plt.style.use('dark_background')
plt.style.use('fivethirtyeight')

# Reset to default
plt.style.use('default')

# Use temporarily
with plt.style.context('seaborn-v0_8'):
    plt.plot(x, y)
    plt.show()
