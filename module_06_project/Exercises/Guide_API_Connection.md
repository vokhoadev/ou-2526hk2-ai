# Hướng dẫn kết nối với API (Flask + Client)

## Mục đích

Sau khi đã **lưu mô hình** (Bước 6), bước triển khai (Bước 7) là tạo **API** (vd Flask) để nhận input từ client (Postman, frontend React, script) và trả về kết quả dự đoán. Tài liệu này mô tả:
- Cách xây dựng endpoint predict trên Flask.
- Format request/response.
- Cách client (curl, JavaScript fetch) gọi API.
- Một số lưu ý (CORS, lỗi, thứ tự feature).

---

## 1. Luồng tổng quan

```
Client (Postman / React / curl)
    │
    │  POST /predict  { "features": [5.1, 3.5, 1.4, 0.2] }
    ▼
Flask API
    │  load model + scaler
    │  scaler.transform(features)
    │  model.predict(...)
    ▼
Response  { "prediction": 0, "species": "setosa" }
```

---

## 2. Flask app mẫu (Iris)

### 2.1. Cấu trúc thư mục

```
project/
├── app.py           # Flask app
├── models/
│   ├── iris_model.joblib
│   └── iris_scaler.joblib
└── requirements.txt
```

### 2.2. Code app.py

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model và scaler khi khởi động app (chỉ 1 lần)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'iris_model.joblib')
SCALER_PATH = os.path.join(os.path.dirname(__file__), 'models', 'iris_scaler.joblib')

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
TARGET_NAMES = ['setosa', 'versicolor', 'virginica']

@app.route('/health', methods=['GET'])
def health():
    """Kiểm tra API còn sống."""
    return jsonify({"status": "healthy"})

@app.route('/model-info', methods=['GET'])
def model_info():
    """Trả về thông tin model (metrics, features) — dùng cho báo cáo/demo."""
    return jsonify({
        "model_type": "LogisticRegression",
        "features": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
        "classes": TARGET_NAMES
    })

@app.route('/predict', methods=['POST'])
def predict():
    """
    Nhận JSON: { "features": [5.1, 3.5, 1.4, 0.2] }
    Trả về: { "prediction": 0, "species": "setosa" }
    """
    try:
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({"error": "Thiếu 'features' trong body"}), 400

        features = np.array(data['features'], dtype=float)
        # Iris: 4 features, có thể 1 mẫu [4] hoặc batch (n, 4)
        if features.ndim == 1:
            features = features.reshape(1, -1)
        if features.shape[1] != 4:
            return jsonify({"error": "Cần đúng 4 features (sepal length, sepal width, petal length, petal width)"}), 400

        features_scaled = scaler.transform(features)
        preds = model.predict(features_scaled)

        # Trả về từng prediction (nếu batch thì trả list)
        if len(preds) == 1:
            return jsonify({
                "prediction": int(preds[0]),
                "species": TARGET_NAMES[preds[0]]
            })
        else:
            return jsonify({
                "predictions": [int(p) for p in preds],
                "species": [TARGET_NAMES[p] for p in preds]
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## 3. Chạy và test bằng curl

### Chạy server

```bash
python app.py
# Server chạy tại http://127.0.0.1:5000
```

### Test bằng curl

```bash
# Health check
curl http://localhost:5000/health

# Model info
curl http://localhost:5000/model-info

# Predict (POST, JSON body)
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
```

Kết quả mẫu: `{"prediction":0,"species":"setosa"}`.

---

## 4. Client gọi từ JavaScript (Frontend / React)

Frontend (React hoặc trang HTML) gọi API qua **fetch** hoặc **axios**. Domain của frontend (vd `http://localhost:3000`) khác domain API (`http://localhost:5000`) nên cần cấu hình **CORS** ở Flask.

### 4.1. Bật CORS trên Flask

```bash
pip install flask-cors
```

```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Cho phép mọi origin (dev); production nên giới hạn origin
```

### 4.2. Gọi từ JavaScript (fetch)

```javascript
const API_URL = 'http://localhost:5000';

// Predict
async function predict(features) {
  const res = await fetch(`${API_URL}/predict`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ features })
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// Ví dụ
predict([5.1, 3.5, 1.4, 0.2]).then(data => {
  console.log(data);  // { prediction: 0, species: "setosa" }
});
```

### 4.3. React ví dụ (form gửi 4 số)

```jsx
const [values, setValues] = useState([0, 0, 0, 0]);
const [result, setResult] = useState(null);

const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    const res = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ features: values })
    });
    const data = await res.json();
    setResult(data);
  } catch (err) {
    setResult({ error: err.message });
  }
};
```

---

## 5. Lưu ý khi kết nối

| Vấn đề | Giải pháp |
|--------|-----------|
| **CORS** | Dùng `flask-cors` và `CORS(app)` khi frontend khác domain. |
| **Thứ tự feature** | API và client phải thống nhất thứ tự: [sepal length, sepal width, petal length, petal width]. Có thể trả về `feature_names` trong `/model-info`. |
| **Lỗi 400/500** | API nên trả về JSON `{"error": "mô tả"}` và status code phù hợp; client check `res.ok` và hiển thị lỗi. |
| **Batch predict** | Nếu gửi nhiều mẫu `[[...], [...]]`, reshape thành (n, 4) và trả về list predictions. |

---

## 6. Checklist BTL (Demo FE ↔ BE ↔ AI)

- [ ] Backend (Flask) có endpoint **POST /predict** nhận `features`, trả về prediction (và tên lớp nếu classification).
- [ ] Có endpoint **GET /model-info** (hoặc /health) để demo và báo cáo.
- [ ] Đã test bằng **curl** hoặc Postman.
- [ ] Frontend (React) có form nhập đủ feature và gọi API, hiển thị kết quả.
- [ ] (Nếu FE/BE khác port) Đã bật CORS và test end-to-end.
- [ ] Có screenshot hoặc video demo để nộp.

---

## 7. Tài liệu tham chiếu

- Module_06: [03_Flask_API_Intro.md](../../Module_06_Project/03_Flask_API_Intro.md)
- Lab: [Lab_02_Flask_API.md](../../Module_06_Project/Exercises/Lab_02_Flask_API.md)
- Trong ProjectSample: [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 7.
