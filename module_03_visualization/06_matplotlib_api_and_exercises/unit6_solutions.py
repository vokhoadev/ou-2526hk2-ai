"""Module 03 — Trực quan hóa dữ liệu (hướng dẫn sinh viên)

Ngữ cảnh (phase): # PHAN VI   Bai tap tong hop (co loi giai + tu luyen)
Mục trong giáo trình: VI.1 Bai tap co loi giai
Nguồn: Matplotlib_Complete.md

Nắm bản chất — gợi ý đọc code:
  • Bảng tham chiếu API + bài tập: tra cứu tham số thường dùng; chạy từng đoạn để xem hành vi thực tế.

Cách học với file này:
  • Chạy cả file (hoặc từng đoạn) và quan sát hình / lỗi — không chỉ đọc tĩnh.
  • Các khối cách nhau bởi dòng `# ---------- Ví dụ ...` là nhiều ví dụ ghép từ giáo trình; mỗi khối thường độc lập.
  • Theo dõi chuỗi: dữ liệu → figure/axes → hàm vẽ (map biến lên trục/màu) → nhãn/legend → show/save.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y = x**2

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color="steelblue", linewidth=2, label=r"$y = x^2$")
ax.set_title("Parabol: bình phương theo x trên đoạn [-5, 5]")
ax.set_xlabel("x (đơn vị tùy chọn)")
ax.set_ylabel("y (đơn vị tùy chọn)")
ax.grid(True, linestyle="--", alpha=0.35)
ax.legend()
fig.tight_layout()
plt.show()


# ---------- Ví dụ / bước 2 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
x = rng.uniform(-1, 1, 120)
y = rng.uniform(-1, 1, 120)

def quadrant_label(a, b):
    if a >= 0 and b >= 0:
        return "Q1 (+,+)"
    if a < 0 and b >= 0:
        return "Q2 (-,+)"
    if a < 0 and b < 0:
        return "Q3 (-,-)"
    return "Q4 (+,-)"

labels = np.array([quadrant_label(xi, yi) for xi, yi in zip(x, y)])
order = ["Q1 (+,+)", "Q2 (-,+)", "Q3 (-,-)", "Q4 (+,-)"]
colors = {"Q1 (+,+)": "C0", "Q2 (-,+)": "C1", "Q3 (-,-)": "C2", "Q4 (+,-)": "C3"}

fig, ax = plt.subplots(figsize=(7, 7))
for lab in order:
    m = labels == lab
    ax.scatter(x[m], y[m], s=28, alpha=0.75, c=colors[lab], label=lab, edgecolors="k", linewidths=0.2)
ax.axhline(0, color="gray", linewidth=0.8)
ax.axvline(0, color="gray", linewidth=0.8)
ax.set_aspect("equal", adjustable="box")
ax.set_title("Scatter 120 điểm — màu theo góc phần tư")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
plt.show()


# ---------- Ví dụ / bước 3 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import numpy as np
import matplotlib.pyplot as plt

items = ["A", "B", "C", "D", "E"]
y1 = np.array([12, 19, 14, 22, 16])
y2 = np.array([15, 17, 18, 20, 21])

x = np.arange(len(items))
w = 0.35

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - w / 2, y1, width=w, label="Năm 1", color="steelblue", edgecolor="black")
ax.bar(x + w / 2, y2, width=w, label="Năm 2", color="coral", edgecolor="black")
ax.set_xticks(x)
ax.set_xticklabels(items)
ax.set_ylabel("Doanh số (đơn vị tùy chọn)")
ax.set_title("So sánh doanh số theo mặt hàng — hai năm")
ax.legend()
ax.grid(True, axis="y", linestyle="--", alpha=0.35)
fig.tight_layout()
plt.show()


# ---------- Ví dụ / bước 4 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
rng = np.random.default_rng(0)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin(x)")

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title("cos(x)")

axes[1, 0].hist(rng.normal(0, 1, 800), bins=35, edgecolor="black", alpha=0.85)
axes[1, 0].set_title("Histogram — N(0,1)")

axes[1, 1].bar(["P1", "P2", "P3"], [4, 7, 5], color="seagreen", edgecolor="black")
axes[1, 1].set_title("Bar 3 nhóm")

fig.suptitle("Bốn biểu đồ trong một figure", fontsize=14, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# ---------- Ví dụ / bước 5 (khối ghép từ giáo trình; có thể chạy riêng) ----------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

x = np.linspace(0, 10, 150)
rng = np.random.default_rng(1)

fig = plt.figure(figsize=(10, 7), constrained_layout=False)
gs = GridSpec(2, 2, figure=fig, height_ratios=[2, 1], hspace=0.3, wspace=0.25)

ax0 = fig.add_subplot(gs[0, :])
ax0.plot(x, np.sin(x), label="sin")
ax0.plot(x, np.cos(x), label="cos", alpha=0.85)
ax0.set_title("Hàng trên — full width")
ax0.legend()

ax1 = fig.add_subplot(gs[1, 0])
ax1.scatter(rng.random(40), rng.random(40), c=rng.random(40), cmap="viridis", alpha=0.8)
ax1.set_title("Scatter")

ax2 = fig.add_subplot(gs[1, 1])
ax2.bar(["a", "b", "c"], [3, 7, 5], color="steelblue", edgecolor="black")
ax2.set_title("Bar")

fig.suptitle("Layout GridSpec — demo lab", fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.savefig("matplotlib_lab5.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.show()
