"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN IV   Tham chieu API (Seaborn)
Mục trong giáo trình: Style toan cuc Seaborn
Nguồn: Seaborn_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Tương tự phần Matplotlib: đối chiếu Axes-level vs Figure-level khi đọc ví dụ và lời giải.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import seaborn as sns

sns.set_theme(context='notebook', style='whitegrid', palette='husl', font_scale=1.0)
# Hoặc tách: sns.set_style(...); sns.set_palette(...); sns.set_context(...)
