# Map Pipeline – Kỹ năng đã học

## Mục đích

Tài liệu này map **7 bước quy trình ML end-to-end** với **kỹ năng bạn đã học** ở từng module/lab, giúp bạn biết "làm mỗi bước cần dùng gì và làm gì cụ thể".

---

## Bảng map 7 bước

| Bước pipeline | Kỹ năng đã học (Module/Lab) | Công việc cụ thể | Tham chiếu |
|---------------|-----------------------------|------------------|------------|
| **1. Định nghĩa bài toán** | Buổi 3–4 (ML intro, loại bài toán) | Viết mục tiêu, chọn metric (Accuracy/MAE/…), xác định Classification/Regression | Module_04 01_ML_Introduction |
| **2. Thu thập & khám phá (EDA)** | Pandas (Lab_02), Matplotlib/Seaborn (Lab 01–02) | `read_csv` / load data, `info()`, `describe()`, `isnull().sum()`, histogram, heatmap, boxplot | Module_02 Lab_02_Pandas, Module_03 Labs |
| **3. Tiền xử lý** | Module_04 02_Data_Preprocessing, Pipeline (Module_05) | Imputer, encoder, scaler, `train_test_split`, (optional) Pipeline | 02_Data_Preprocessing.md, 05_Pipeline.md |
| **4. Xây dựng mô hình** | Module_04 Lab_Classification / Lab_Regression | Fit 2–3 model khác loại, so sánh | Lab_Classification, Lab_Regression |
| **5. Đánh giá & tinh chỉnh** | Module_04 05_Evaluation, Module_05 03_Cross_Validation, 04_Hyperparameter_Tuning | accuracy_score, classification_report, GridSearchCV | Các file tương ứng |
| **6. Lưu mô hình** | Module_05/06 Model Persistence | `joblib.dump(pipe, '...')`, `joblib.load`, predict với data mới | 02_Model_Persistence.md, Lab_01_Model_Persistence |
| **7. Triển khai (giới thiệu)** | Buổi 2 Flask cơ bản, Module_06 03_Flask_API_Intro | Load model trong Flask, endpoint `/predict` | 03_Flask_API_Intro.md, Lab_02_Flask_API |

---

## Hướng dẫn nhanh từng bước

### Bước 1: Định nghĩa bài toán

**Làm bước này bạn chỉ cần:** Trả lời bài toán là Classification hay Regression (hay Clustering), mục tiêu là gì, metric nào dùng để đánh giá (Accuracy, F1, MAE, RMSE…). Không cần code; có thể viết vài dòng trong notebook.

```python
# Ví dụ: ghi chú trong notebook
# Bài toán: Phân loại loài hoa Iris (Classification, 3 lớp)
# Metric: Accuracy, F1-score (macro)
# Target: species (setosa, versicolor, virginica)
```

---

### Bước 2: Thu thập và khám phá dữ liệu (EDA)

**Làm bước này bạn chỉ cần:** Load data (Pandas hoặc sklearn), gọi `df.info()`, `df.describe()`, `df.isnull().sum()`, vẽ ít nhất 2–3 biểu đồ (phân bố target, correlation heatmap, boxplot). Dùng kỹ năng Pandas + Matplotlib/Seaborn đã học.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')  # hoặc load từ sklearn
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Biểu đồ phân bố target
df['target'].value_counts().plot(kind='bar')
# Heatmap correlation
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```

---

### Bước 3: Tiền xử lý dữ liệu

**Làm bước này bạn chỉ cần:** Xử lý missing (imputer hoặc drop), encode categorical nếu có (LabelEncoder/OneHotEncoder), scale số (StandardScaler/MinMaxScaler), rồi `train_test_split`. Có thể gộp vào sklearn `Pipeline` (Module_05).

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Ví dụ: tách X, y
X = df.drop('target', axis=1)
y = df['target']

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

### Bước 4: Xây dựng mô hình

**Làm bước này bạn chỉ cần:** Khởi tạo 2–3 model khác loại (vd: LogisticRegression, RandomForest, SVC), gọi `.fit(X_train, y_train)` cho từng model, lưu kết quả để so sánh. Dùng đúng API sklearn đã học ở Lab_Classification / Lab_Regression.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'SVM': SVC(random_state=42)
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    acc = model.score(X_test_scaled, y_test)
    print(f"{name}: {acc:.4f}")
```

---

### Bước 5: Đánh giá và tinh chỉnh

**Làm bước này bạn chỉ cần:** Tính metrics (accuracy_score, classification_report, confusion_matrix), vẽ confusion matrix/ROC nếu classification. Dùng Cross-validation và GridSearchCV (hoặc RandomizedSearchCV) để chọn hyperparameters. So sánh các model bằng bảng.

```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

# Đánh giá model tốt nhất
y_pred = best_model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Tinh chỉnh (ví dụ)
param_grid = {'C': [0.1, 1, 10], 'kernel': ['rbf', 'linear']}
grid = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train_scaled, y_train)
print("Best params:", grid.best_params_)
```

---

### Bước 6: Lưu mô hình

**Làm bước này bạn chỉ cần:** Lưu pipeline hoặc model + scaler (và encoder nếu có) bằng `joblib.dump`. Có đoạn code load bằng `joblib.load` và gọi `predict` với dữ liệu mới để chứng minh dùng lại được.

```python
import joblib
import os

os.makedirs('models', exist_ok=True)
joblib.dump(best_model, 'models/model.joblib')
joblib.dump(scaler, 'models/scaler.joblib')

# Demo load và predict
loaded_model = joblib.load('models/model.joblib')
loaded_scaler = joblib.load('models/scaler.joblib')
new_scaled = loaded_scaler.transform(X_new)
pred = loaded_model.predict(new_scaled)
```

---

### Bước 7: Triển khai (giới thiệu)

**Làm bước này bạn chỉ cần:** Tạo Flask app, load model và scaler khi khởi động, tạo endpoint (vd: POST `/predict`) nhận features từ JSON, scale và predict, trả về kết quả JSON. Dùng kiến thức Flask cơ bản + Lab_02_Flask_API.

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('models/model.joblib')
scaler = joblib.load('models/scaler.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    features_scaled = scaler.transform(features)
    pred = model.predict(features_scaled)
    return jsonify({'prediction': int(pred[0])})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Tiếp theo

- Làm tuần tự **[Guided_Mini_Project](Exercises/Guided_Mini_Project.md)** (dataset Iris) để thấy từng bước trong một bài hoàn chỉnh.
- Khi làm BTL, dùng **[Project_Steps_Checklist](Exercises/Project_Steps_Checklist.md)** để không bỏ sót bước và đủ deliverable.

---

## Tài liệu bổ sung (theo chủ đề)

Các file dưới đây đi sâu vào từng phần của pipeline, phù hợp khi BTL yêu cầu đầy đủ (wandb, đánh giá chi tiết, lưu mô hình, API):

| Chủ đề | Tài liệu | Nội dung ngắn |
|--------|----------|----------------|
| **Thực nghiệm wandb** | [Guide_Wandb.md](Exercises/Guide_Wandb.md) | Init project, log config/metrics/charts, ≥3 runs, ví dụ Iris |
| **Đánh giá mô hình** | [Guide_Model_Evaluation.md](Exercises/Guide_Model_Evaluation.md) | Metrics classification/regression, confusion matrix, ROC, so sánh models, learning curves |
| **Lưu mô hình** | [Guide_Model_Persistence.md](Exercises/Guide_Model_Persistence.md) | joblib, artifacts, pipeline, metadata, load & predict |
| **Kết nối API** | [Guide_API_Connection.md](Exercises/Guide_API_Connection.md) | Flask predict endpoint, curl/fetch, CORS, demo FE↔BE |
