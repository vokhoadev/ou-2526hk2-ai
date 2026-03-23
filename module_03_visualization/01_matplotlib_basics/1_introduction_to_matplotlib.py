"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: 1. Introduction to Matplotlib
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

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = np.sin(x)


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# For Jupyter notebooks
# %matplotlib inline


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Pyplot interface (simple, stateful)
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()

# Object-oriented interface (more control)
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()
