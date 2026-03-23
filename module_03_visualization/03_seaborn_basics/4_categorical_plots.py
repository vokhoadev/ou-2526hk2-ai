"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: 4. Categorical Plots
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

tips = sns.load_dataset("tips")


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Count of categorical variable
plt.figure(figsize=(10, 6))
sns.countplot(data=tips, x='day')
plt.title('Count by Day')
plt.show()

# With hue
plt.figure(figsize=(10, 6))
sns.countplot(data=tips, x='day', hue='time')
plt.show()

# Order
plt.figure(figsize=(10, 6))
sns.countplot(data=tips, x='day', 
              order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Bar plot with mean and confidence interval
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill')
plt.title('Average Total Bill by Day')
plt.show()

# With hue
plt.figure(figsize=(12, 6))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
plt.show()

# Custom estimator
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', 
            estimator=np.median, errorbar=None)
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Point plot with lines connecting
plt.figure(figsize=(10, 6))
sns.pointplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Average Bill by Day and Gender')
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Figure-level categorical plot
sns.catplot(data=tips, x='day', y='total_bill', 
            hue='sex', col='time', kind='bar')
plt.show()

# Kinds: 'strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count'
sns.catplot(data=tips, x='day', y='total_bill', 
            kind='violin', col='time')
plt.show()
