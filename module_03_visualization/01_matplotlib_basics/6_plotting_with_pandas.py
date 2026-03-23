"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Matplotlib co ban
Mục trong giáo trình: 6. Plotting with Pandas
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
import pandas as pd

# Direct plotting from DataFrame
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 120, 150, 130, 170],
    'Expenses': [80, 90, 100, 95, 110]
})

# Line plot
df.plot(x='Month', y=['Sales', 'Expenses'], figsize=(10, 6))
plt.title('Sales vs Expenses')
plt.show()

# Bar plot
df.plot(x='Month', y='Sales', kind='bar', figsize=(10, 6))
plt.show()

# Multiple plot types
df.set_index('Month')[['Sales', 'Expenses']].plot(kind='bar')
plt.show()

# Histogram
df['Sales'].plot(kind='hist', bins=10)
plt.show()

# Scatter
df.plot(x='Sales', y='Expenses', kind='scatter', figsize=(8, 6))
plt.show()
