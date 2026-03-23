"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: 3. Distribution Plots
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

tips = sns.load_dataset('tips')

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', bins=20)
plt.title('Distribution of Total Bill')
plt.show()

# With KDE (Kernel Density Estimation)
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', kde=True)
plt.show()

# KDE only
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x='total_bill')
plt.show()

# Multiple distributions
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', hue='time', kde=True)
plt.show()

# Separate by column
plt.figure(figsize=(12, 5))
sns.histplot(data=tips, x='total_bill', hue='time', 
             multiple='dodge')  # Or 'stack', 'fill'
plt.show()


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Distribution plot with facets
sns.displot(data=tips, x='total_bill', hue='time', 
            kind='kde', col='sex')
plt.show()

# Multiple kinds: 'hist', 'kde', 'ecdf'
sns.displot(data=tips, x='total_bill', kind='ecdf')
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Basic box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title('Total Bill by Day')
plt.show()

# With hue
plt.figure(figsize=(12, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
plt.show()

# Horizontal
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='total_bill', y='day', orient='h')
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Violin plot - combines box plot and KDE
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill')
plt.show()

# Split violin
plt.figure(figsize=(12, 6))
sns.violinplot(data=tips, x='day', y='total_bill', 
               hue='sex', split=True)
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Strip plot - scatter of categorical
plt.figure(figsize=(10, 6))
sns.stripplot(data=tips, x='day', y='total_bill', jitter=True)
plt.show()

# Swarm plot - no overlapping
plt.figure(figsize=(10, 6))
sns.swarmplot(data=tips, x='day', y='total_bill')
plt.show()

# Combined: box + strip
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill')
sns.stripplot(data=tips, x='day', y='total_bill', 
              color='black', alpha=0.3)
plt.show()
