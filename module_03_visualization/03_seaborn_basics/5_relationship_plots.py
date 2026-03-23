"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: 5. Relationship Plots
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

# Basic scatter
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()

# With hue and size
plt.figure(figsize=(12, 8))
sns.scatterplot(data=tips, x='total_bill', y='tip', 
                hue='time', size='size', sizes=(20, 200))
plt.show()

# With style
plt.figure(figsize=(12, 8))
sns.scatterplot(data=tips, x='total_bill', y='tip', 
                hue='day', style='sex')
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Simple line plot
fmri = sns.load_dataset('fmri')
plt.figure(figsize=(10, 6))
sns.lineplot(data=fmri, x='timepoint', y='signal', hue='event')
plt.show()

# With confidence interval
plt.figure(figsize=(10, 6))
sns.lineplot(data=fmri, x='timepoint', y='signal', 
             hue='event', style='region', ci='sd')
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Scatter with regression line
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title('Tip vs Total Bill with Regression')
plt.show()

# Polynomial regression
plt.figure(figsize=(10, 6))
sns.regplot(data=tips, x='total_bill', y='tip', order=2)
plt.show()

# lmplot - figure-level with facets
sns.lmplot(data=tips, x='total_bill', y='tip', 
           hue='time', col='sex')
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Relationship plot with facets
sns.relplot(data=tips, x='total_bill', y='tip', 
            hue='time', col='day', kind='scatter')
plt.show()

# Kind: 'scatter' or 'line'
sns.relplot(data=fmri, x='timepoint', y='signal', 
            hue='event', col='region', kind='line')
plt.show()
