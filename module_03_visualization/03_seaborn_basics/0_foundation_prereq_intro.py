"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: 0. Nen tang (doc truoc muc 1)
Nguồn: Seaborn_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Seaborn xây trên Matplotlib, thường nhận data=DataFrame và tên cột — phù hợp dữ liệu dạng bảng (tidy).
  • Phân biệt phân phối (hist/KDE/box/violin), phân loại (bar/count/strip/swarm), quan hệ (scatter/line).
  • hue= tách nhóm bằng màu; một biểu đồ chỉ nên trả lời một câu hỏi phân tích rõ ràng.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
