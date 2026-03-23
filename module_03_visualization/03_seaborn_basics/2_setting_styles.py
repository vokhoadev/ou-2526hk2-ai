"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: 2. Setting Styles
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

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Available themes: darkgrid, whitegrid, dark, white, ticks
sns.set_theme(style='whitegrid')

# Or use set_style
sns.set_style('darkgrid')

# Reset to default
sns.set_theme()

# Temporary style
with sns.axes_style('dark'):
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.show()


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Built-in palettes
sns.set_palette('husl')
sns.set_palette('Set2')
sns.set_palette('coolwarm')

# Custom palette
custom = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
sns.set_palette(custom)

# View palette
sns.palplot(sns.color_palette('husl', 8))
plt.show()

# Palette types
sns.color_palette('deep')      # Default
sns.color_palette('pastel')    # Soft colors
sns.color_palette('dark')      # Dark colors
sns.color_palette('bright')    # Bright colors
sns.color_palette('colorblind')  # Colorblind-friendly


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Contexts: paper, notebook (default), talk, poster
sns.set_context('talk')        # Larger elements for presentations
sns.set_context('paper')       # Smaller for papers
sns.set_context('poster')      # Even larger

# Custom scaling
sns.set_context('notebook', font_scale=1.2)
