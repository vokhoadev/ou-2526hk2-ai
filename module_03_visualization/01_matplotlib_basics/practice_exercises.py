"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: Practice Exercises
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

# Create the following plots:
# 1. Line plot of y = x^2 for x in [-5, 5]
# 2. Scatter plot with 100 random points, color by quadrant
# 3. Bar chart of 5 products and their sales
# 4. Histogram of 1000 normally distributed values


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Create a publication-quality figure:
# - Two subplots (side by side)
# - Left: line plot with grid, legend, labels
# - Right: bar chart with annotations
# - Add overall title
# - Save as PNG (300 DPI) and PDF


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Using Titanic dataset:
# Create a 2x2 subplot figure:
# 1. Bar chart of survival by class
# 2. Histogram of ages
# 3. Pie chart of gender distribution
# 4. Scatter plot of age vs fare
