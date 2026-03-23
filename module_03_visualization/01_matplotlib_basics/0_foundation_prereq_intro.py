"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: 0. Nen tang (doc truoc muc 1)
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
# Trong Jupyter — ảnh nhúng notebook:
# %matplotlib inline
