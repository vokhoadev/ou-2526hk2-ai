"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: 2. Basic Plots
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

# Simple line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# # Multiple lines
y2 = np.cos(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.legend()
plt.title('Sine and Cosine')
plt.grid(True)
plt.show()

# # Line styles
# plt.plot(x, y, 'r-', linewidth=2)      # Red solid
# plt.plot(x, y2, 'b--', linewidth=1.5)  # Blue dashed
# plt.plot(x, y + 1, 'g:', linewidth=2)  # Green dotted
# plt.plot(x, y2 + 1, 'k-.', linewidth=1)  # Black dash-dot


# # ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# # Basic scatter
# np.random.seed(42)
# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.figure(figsize=(8, 6))
# plt.scatter(x, y)
# plt.title('Scatter Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# # With size and color
# sizes = np.random.rand(50) * 500
# colors = np.random.rand(50)

# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')
# plt.colorbar(label='Value')
# plt.title('Scatter with Size and Color')
# plt.show()


# # ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# # Simple bar chart
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [23, 45, 56, 78, 32]

# plt.figure(figsize=(8, 6))
# plt.bar(categories, values, color='steelblue', edgecolor='black')
# plt.title('Bar Chart')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()

# # Horizontal bar
# plt.figure(figsize=(8, 6))
# plt.barh(categories, values, color='coral')
# plt.title('Horizontal Bar Chart')
# plt.show()

# # Grouped bar chart
# x = np.arange(len(categories))
# width = 0.35
# values1 = [23, 45, 56, 78, 32]
# values2 = [30, 40, 50, 65, 45]

# fig, ax = plt.subplots(figsize=(10, 6))
# bars1 = ax.bar(x - width/2, values1, width, label='2023')
# bars2 = ax.bar(x + width/2, values2, width, label='2024')
# ax.set_xticks(x)
# ax.set_xticklabels(categories)
# ax.legend()
# plt.title('Grouped Bar Chart')
# plt.show()

# # Stacked bar chart
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.bar(categories, values1, label='2023')
# ax.bar(categories, values2, bottom=values1, label='2024')
# ax.legend()
# plt.title('Stacked Bar Chart')
# plt.show()


# # ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# # Basic histogram
# data = np.random.randn(1000)

# plt.figure(figsize=(10, 6))
# plt.hist(data, bins=30, edgecolor='black')
# plt.title('Histogram')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()

# # With customization
# plt.figure(figsize=(10, 6))
# plt.hist(data, bins=30, density=True, alpha=0.7, 
#          color='steelblue', edgecolor='black')
# plt.title('Normalized Histogram')
# plt.show()

# # Multiple histograms
# data1 = np.random.randn(1000)
# data2 = np.random.randn(1000) + 2

# plt.figure(figsize=(10, 6))
# plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
# plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
# plt.legend()
# plt.show()


# # ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# sizes = [35, 25, 20, 15, 5]
# labels = ['A', 'B', 'C', 'D', 'E']
# explode = (0.1, 0, 0, 0, 0)  # Explode first slice

# plt.figure(figsize=(8, 8))
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# plt.title('Pie Chart')
# plt.axis('equal')
# plt.show()
