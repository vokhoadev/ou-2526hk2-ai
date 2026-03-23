# Hướng dẫn lưu mô hình và dùng lại

## Mục đích

Sau khi train và chọn được model tốt nhất, cần **lưu** model và các object đi kèm (scaler, encoder) để:
- Không phải train lại mỗi lần cần dự đoán.
- Triển khai lên API (Flask/FastAPI) hoặc script batch.

Tài liệu này tóm tắt **cách lưu/load** với `joblib` và **cách predict với dữ liệu mới** đúng quy trình (scale/encode giống lúc train).

---

## 1. Cần lưu những gì?

| Thành phần | Mục đích khi predict |
|------------|----------------------|
| **Model** | Gọi `.predict(X)` hoặc `.predict_proba(X)` |
| **Scaler** | Transform features mới cùng scale với lúc train: `scaler.transform(X_new)` |
| **Encoder** (nếu có) | Transform nhãn categorical sang số hoặc one-hot giống lúc train |
| **Feature names** (tùy chọn) | Kiểm tra thứ tự cột khi nhận input từ API |
| **Metadata** (tùy chọn) | Version, ngày train, metrics để ghi vào báo cáo/API info |

---

## 2. Lưu từng file với joblib

```python
import joblib
import os

os.makedirs('models', exist_ok=True)

# Lưu model và scaler
joblib.dump(model, 'models/model.joblib')
joblib.dump(scaler, 'models/scaler.joblib')

# Nếu có LabelEncoder cho target (để đổi ngược pred -> tên lớp)
# joblib.dump(label_encoder, 'models/label_encoder.joblib')
```

---

## 3. Lưu gộp nhiều artifacts vào một file

Tiện khi deploy: chỉ cần load một lần.

```python
artifacts = {
    'model': model,
    'scaler': scaler,
    'feature_names': list(X_train.columns),  # hoặc iris.feature_names
    'target_names': ['setosa', 'versicolor', 'virginica'],  # classification
    # 'label_encoder': label_encoder,  # nếu có
}
joblib.dump(artifacts, 'models/artifacts.joblib')
```

---

## 4. Load và predict với dữ liệu mới

### 4.1. Load từng file

```python
model = joblib.load('models/model.joblib')
scaler = joblib.load('models/scaler.joblib')

# Dữ liệu mới (cùng số cột, cùng thứ tự như lúc train)
import numpy as np
X_new = np.array([[5.1, 3.5, 1.4, 0.2]])  # 1 mẫu, 4 features

# Quan trọng: phải scale trước khi predict
X_new_scaled = scaler.transform(X_new)
pred = model.predict(X_new_scaled)
print(pred)  # [0] -> setosa
```

### 4.2. Load từ file artifacts

```python
artifacts = joblib.load('models/artifacts.joblib')
model = artifacts['model']
scaler = artifacts['scaler']
feature_names = artifacts['feature_names']

X_new_scaled = scaler.transform(X_new)
pred = model.predict(X_new_scaled)
# Nếu cần tên lớp:
target_names = artifacts['target_names']
print(target_names[pred[0]])
```

---

## 5. Lưu full Pipeline (sklearn)

Nếu dùng `sklearn.pipeline.Pipeline` (preprocessing + model trong một object), chỉ cần dump pipeline; khi predict pipeline tự scale/encode bên trong.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(random_state=42))
])
pipe.fit(X_train, y_train)

joblib.dump(pipe, 'models/pipeline.joblib')

# Load và predict — không cần scale tay
loaded_pipe = joblib.load('models/pipeline.joblib')
pred = loaded_pipe.predict(X_new)  # X_new chưa scale
```

---

## 6. Metadata (version, metrics)

Để báo cáo hoặc API trả về thông tin model:

```python
metadata = {
    'version': '1.0',
    'trained_date': '2025-03-15',
    'accuracy': 0.97,
    'model_type': 'LogisticRegression',
    'feature_names': list(iris.feature_names)
}
import json
with open('models/metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
```

API có thể đọc `metadata.json` và expose endpoint `/model-info` trả về các thông tin này.

---

## 7. Checklist BTL

- [ ] Đã lưu **model** (và **scaler** nếu dùng scale riêng).
- [ ] Đã lưu **encoder** nếu có biến categorical.
- [ ] Có **đoạn code load** và **predict** với ít nhất 1 mẫu mới để chứng minh hoạt động.
- [ ] (Khuyến khích) Lưu **pipeline** hoặc **artifacts** gộp để deploy đơn giản.
- [ ] (Tùy chọn) Lưu **metadata** (metrics, version) cho báo cáo/API.

---

## 8. Tài liệu tham chiếu

- Module_06: [02_Model_Persistence.md](../../Module_06_Project/02_Model_Persistence.md)
- Lab: [Lab_01_Model_Persistence.md](../../Module_06_Project/Exercises/Lab_01_Model_Persistence.md)
- Trong ProjectSample: [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 6.
