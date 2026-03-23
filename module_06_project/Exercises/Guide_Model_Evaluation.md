# Hướng dẫn đánh giá mô hình

## Mục đích

Tài liệu này tóm tắt **cách đánh giá mô hình** theo từng loại bài toán (Classification, Regression) và cách **so sánh nhiều model** để chọn model tốt nhất cho pipeline và BTL.

---

## 1. Classification

### 1.1. Metrics cơ bản

| Metric | Ý nghĩa | Code (sklearn) |
|--------|---------|----------------|
| **Accuracy** | Tỷ lệ dự đoán đúng tổng thể | `accuracy_score(y_test, y_pred)` |
| **Precision** | Trong các dự đoán Positive, bao nhiêu đúng | `precision_score(..., average='macro' hoặc 'weighted')` |
| **Recall** | Trong các Positive thực tế, bao nhiêu được phát hiện | `recall_score(..., average='macro' hoặc 'weighted')` |
| **F1-Score** | Trung bình điều hòa Precision & Recall | `f1_score(..., average='macro' hoặc 'weighted')` |

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')  # multi-class
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

# Báo cáo đầy đủ từng lớp
print(classification_report(y_test, y_pred, target_names=['setosa', 'versicolor', 'virginica']))
```

**Khi nào dùng metric nào?**

- Lớp cân bằng: Accuracy, F1 macro/weighted.
- Lớp mất cân bằng: Ưu tiên Precision hoặc Recall (tùy bài toán); F1.
- BTL thường yêu cầu: Accuracy, Precision, Recall, F1 và (nếu có) AUC.

### 1.2. Confusion Matrix

Ma trận: hàng = thực tế, cột = dự đoán. Đường chéo = dự đoán đúng.

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

cm = confusion_matrix(y_test, y_pred)

# Cách 1: sklearn ConfusionMatrixDisplay
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Cách 2: Seaborn heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
```

### 1.3. ROC Curve và AUC

Dùng khi model có `predict_proba`. ROC thể hiện trade-off TPR vs FPR; AUC càng cao càng tốt.

- **Binary:** `roc_curve(y_test, y_prob[:, 1])`, `roc_auc_score(y_test, y_prob[:, 1])`.
- **Multi-class:** Có thể binarize từng lớp (one-vs-rest) rồi tính AUC trung bình.

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Binary: giả sử lớp 1 là positive
y_prob = model.predict_proba(X_test_scaled)[:, 1]
fpr, tpr, _ = roc_curve(y_test_binary, y_prob)
auc_score = roc_auc_score(y_test_binary, y_prob)

plt.plot(fpr, tpr, label=f'ROC (AUC = {auc_score:.3f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.title('ROC Curve')
plt.show()
```

---

## 2. Regression

### 2.1. Metrics thường dùng

| Metric | Ý nghĩa | Code |
|--------|---------|------|
| **MAE** | Sai lệch trung bình tuyệt đối | `mean_absolute_error(y_test, y_pred)` |
| **RMSE** | Căn bậc hai MSE, cùng đơn vị với y | `np.sqrt(mean_squared_error(y_test, y_pred))` |
| **R²** | Hệ số xác định (1 = fit hoàn hảo) | `r2_score(y_test, y_pred)` |

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"MAE:  {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")
```

### 2.2. Biểu đồ đánh giá

- **Actual vs Predicted:** scatter plot `y_test` vs `y_pred`; điểm gần đường y=x là tốt.
- **Residuals:** `y_test - y_pred` theo `y_test` hoặc theo index.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()
```

---

## 3. So sánh nhiều model

Tạo bảng tổng hợp metrics của từng model, sắp xếp theo metric chính (vd Accuracy hoặc F1, RMSE hoặc R²).

```python
import pandas as pd

results = []
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    results.append({
        'Model': name,
        'Accuracy': accuracy_score(y_test, y_pred),
        'F1 (macro)': f1_score(y_test, y_pred, average='macro')
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Accuracy', ascending=False)
print(results_df)
```

Bước tiếp theo: chọn model có metric tốt nhất (hoặc cân bằng Precision/Recall nếu cần), dùng model đó cho bước lưu mô hình và API.

---

## 4. Learning curves (khuyến khích cho BTL)

Giúp nhận biết overfitting/underfitting: vẽ accuracy (hoặc loss) theo kích thước train set hoặc epoch.

```python
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

train_sizes, train_scores, test_scores = learning_curve(
    model, X_train_scaled, y_train, cv=5,
    train_sizes=np.linspace(0.1, 1.0, 5)
)
plt.plot(train_sizes, train_scores.mean(axis=1), label='Train')
plt.plot(train_sizes, test_scores.mean(axis=1), label='Validation')
plt.xlabel('Training set size')
plt.ylabel('Score')
plt.legend()
plt.title('Learning Curves')
plt.show()
```

---

## 5. Tài liệu tham chiếu

- Module_04: [05_Evaluation_Metrics.md](../../Module_04_Supervised_Learning/05_Evaluation_Metrics.md)
- Module_05: Cross-Validation, Hyperparameter Tuning (GridSearchCV) — dùng để đánh giá ổn định và chọn hyperparameters.
