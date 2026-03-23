"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): Guide_EDA_Visualization_Titanic.md
Mục trong giáo trình: 3. Tai du lieu & cai nhin dau tien
Nguồn: Guide_EDA_Visualization_Titanic.md

Nắm bản chất — gợi ý đọc code:
  • EDA: từ cấu trúc dữ liệu (shape, dtype, missing) → phân phối → quan hệ → so sánh nhóm — visualization là công cụ suy nghĩ.
  • Mỗi biểu đồ nên kèm một câu hỏi (ví dụ: fare lệch phải? tuổi thiếu nhiều không?).

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
