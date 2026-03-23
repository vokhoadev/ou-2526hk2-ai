"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN I   Seaborn co ban
Mục trong giáo trình: Practice Exercises
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

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# Using tips dataset:
# 1. Create histogram of total_bill with KDE
# 2. Box plot of tip by day and time
# 3. Violin plot of total_bill by sex
# 4. Compare distributions of tips for lunch vs dinner


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Using titanic dataset:
# 1. Count plot of survival by class
# 2. Bar plot of average fare by class and sex
# 3. Point plot of survival rate by age group and class
# 4. Create faceted plot by embark_town


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Using iris dataset:
# 1. Scatter plot of sepal_length vs sepal_width by species
# 2. Pair plot of all features
# 3. Heatmap of correlations
# 4. Joint plot of petal dimensions


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

# Create a comprehensive analysis figure:
# - 2x3 subplot grid
# - Include: histogram, box plot, bar chart, 
#   scatter plot, heatmap, violin plot
# - Use consistent color scheme
# - Add proper titles and labels
