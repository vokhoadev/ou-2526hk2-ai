# Hướng dẫn thực nghiệm với wandb (Weights & Biases)

## Mục đích

Dùng **wandb** để ghi lại mỗi lần chạy thí nghiệm (run): config (hyperparameters, loại model), metrics (accuracy, F1, …), và charts (confusion matrix, ROC). Sau đó so sánh ≥3 runs trên dashboard để chọn model tốt nhất và đáp ứng yêu cầu BTL.

---

## 1. Cài đặt và đăng nhập

```bash
pip install wandb
```

- Đăng ký tài khoản miễn phí tại [wandb.ai](https://wandb.ai).
- Lần đầu chạy sẽ yêu cầu login (browser hoặc API key):

```python
import wandb
wandb.login()  # mở browser hoặc paste API key
```

---

## 2. Init project và config

Mỗi **run** = một lần train (một bộ hyperparameters / một model). **Project** = nhóm các run cùng một bài toán.

```python
import wandb

# Khởi tạo run với tên project (tạo mới hoặc dùng project đã có)
run = wandb.init(
    project="iris-classification",   # tên project trên wandb
    config={
        "model": "LogisticRegression",
        "C": 1.0,
        "max_iter": 1000,
        "test_size": 0.2,
        "random_state": 42
    }
)

# config có thể truy cập sau
print(run.config)
```

**Lưu ý:** Gọi `wandb.init()` **một lần** ở đầu mỗi run (mỗi lần train). Khi đổi model hoặc hyperparameters thì chạy lại notebook/script để tạo run mới.

---

## 3. Log metrics

Sau khi train và đánh giá, log các metric lên wandb để vẽ đồ thị và so sánh runs.

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Giả sử đã có y_test, y_pred
wandb.log({
    "accuracy": accuracy_score(y_test, y_pred),
    "precision": precision_score(y_test, y_pred, average='macro'),
    "recall": recall_score(y_test, y_pred, average='macro'),
    "f1": f1_score(y_test, y_pred, average='macro')
})
```

- **Classification:** Accuracy, Precision, Recall, F1, AUC (nếu có `predict_proba`).
- **Regression:** MAE, RMSE, R².
- **Clustering:** Silhouette score, Davies-Bouldin (nếu đề bài yêu cầu).

---

## 4. Log charts (Confusion Matrix, ROC)

### Confusion Matrix

```python
import wandb
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
# Log dạng table để wandb vẽ confusion matrix
wandb.log({"confusion_matrix": wandb.plot.confusion_matrix(
    probs=None,
    y_true=y_test,
    preds=y_pred,
    class_names=iris.target_names  # ['setosa', 'versicolor', 'virginica']
)})
```

Hoặc đơn giản hơn: log metrics từng lớp, hoặc log image nếu bạn tự vẽ bằng matplotlib/seaborn rồi lưu file:

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', ax=ax, xticklabels=iris.target_names, yticklabels=iris.target_names)
ax.set_title('Confusion Matrix')
wandb.log({"confusion_matrix": wandb.Image(fig)})
plt.close()
```

### ROC Curve (binary hoặc one-vs-rest cho multi-class)

```python
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
import numpy as np

# Multi-class: binarize y
y_test_bin = label_binarize(y_test, classes=[0, 1, 2])
y_prob = model.predict_proba(X_test_scaled)

# Log ROC từng lớp hoặc vẽ rồi log image
fpr, tpr, _ = roc_curve(y_test_bin.ravel(), y_prob.ravel())
roc_auc = auc(fpr, tpr)
wandb.log({"roc_auc": roc_auc})
# Có thể vẽ ROC bằng matplotlib rồi wandb.log({"roc": wandb.Image(fig)})
```

---

## 5. Kết thúc run

```python
wandb.finish()
```

Gọi `wandb.finish()` khi xong một run (cuối cell hoặc cuối script). Nếu quên, wandb thường tự kết thúc khi chương trình thoát.

---

## 6. Ví dụ đủ một run (Iris)

```python
import wandb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# --- Run 1: LogisticRegression C=1.0 ---
run = wandb.init(project="iris-classification", config={"model": "LogisticRegression", "C": 1.0})
model = LogisticRegression(C=1.0, random_state=42)
model.fit(X_train_s, y_train)
y_pred = model.predict(X_test_s)

wandb.log({
    "accuracy": accuracy_score(y_test, y_pred),
    "f1_macro": f1_score(y_test, y_pred, average='macro')
})
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', ax=ax, xticklabels=iris.target_names, yticklabels=iris.target_names)
wandb.log({"confusion_matrix": wandb.Image(fig)})
plt.close()
wandb.finish()

# Chạy thêm Run 2, Run 3 với config khác (vd C=0.1, model RandomForest) để có ≥3 runs.
```

---

## 7. Yêu cầu BTL (tóm tắt)

| Yêu cầu | Chi tiết |
|---------|----------|
| **Init project** | `wandb.init(project="tên-project", config={...})` |
| **Log config** | Hyperparameters, model type trong `config` |
| **Log metrics** | Accuracy, Precision, Recall, F1 (classification); MAE, RMSE, R² (regression) |
| **Log charts** | Confusion matrix, ROC (hoặc ảnh biểu đồ đánh giá) |
| **≥3 runs** | Chạy 3 lần với config khác nhau (vd 3 model, hoặc 3 bộ hyperparameters) |
| **Nộp** | Link project wandb (public) + screenshot dashboard so sánh runs |

---

## 8. Tài liệu thêm

- Docs: [https://docs.wandb.ai/](https://docs.wandb.ai/)
- Quickstart: [https://docs.wandb.ai/quickstart](https://docs.wandb.ai/quickstart)
