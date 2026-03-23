"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN IV   Tham chieu API (Matplotlib)
Mục trong giáo trình: Matplotlib `pyplot` / `Axes`   API thuong dung
Nguồn: Matplotlib_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Bảng tham chiếu API + bài tập: tra cứu tham số thường dùng; chạy từng đoạn để xem hành vi thực tế.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (8, 5)
mpl.rcParams['font.size'] = 11
