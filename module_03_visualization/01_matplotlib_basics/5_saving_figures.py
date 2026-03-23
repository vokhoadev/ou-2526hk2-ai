"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: 5. Saving Figures
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

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y)

# Save as PNG
fig.savefig('figure.png')
fig.savefig('figure.png', dpi=300)

# Save as PDF
fig.savefig('figure.pdf')

# Save as SVG (vector)
fig.savefig('figure.svg')

# Common options
fig.savefig('figure.png',
    dpi=300,
    bbox_inches='tight',     # Remove extra whitespace
    facecolor='white',       # Background color
    transparent=False        # Transparent background
)
