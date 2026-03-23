"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN II   Matplotlib nang cao
Mục trong giáo trình: 3. Luu Figure
Nguồn: Matplotlib_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Subplots/GridSpec là cách chia nhiều panel trong một Figure để so sánh cùng thang đo hoặc kể một chuỗi hình.
  • Twin axes: hai trục Y khác đơn vị chung trục X — dễ gây hiểu nhầm nên chỉ dùng khi thật cần và ghi rõ nhãn.
  • savefig + dpi/định dạng vector (PDF/SVG) phục vụ báo cáo; style/ngữ cảnh giúp đồng bộ giao diện nhanh.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import matplotlib.pyplot as plt

# PNG (high quality)
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

# PDF (vector, tốt cho publications)
plt.savefig('plot.pdf', bbox_inches='tight')

# SVG (vector, tốt cho web)
plt.savefig('plot.svg', bbox_inches='tight')

# JPEG
plt.savefig('plot.jpg', dpi=150)


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

plt.savefig('plot.png', dpi=300, transparent=True, bbox_inches='tight')
