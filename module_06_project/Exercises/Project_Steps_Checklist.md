# Checklist 7 bước – Bài tập lớn (BTL)

## Thông tin đề tài của tôi

| Mục | Điền |
|-----|------|
| **Dataset** | … (vd: California Housing, Heart Disease UCI, …) |
| **Loại bài toán** | Classification / Regression / Clustering |
| **Metric chính** | … (vd: Accuracy, F1, MAE, RMSE, Silhouette, …) |
| **Biến mục tiêu (target)** | … |

---

## Deliverable mỗi bước (tóm tắt)

| Bước | Deliverable tối thiểu |
|------|------------------------|
| 1 | Ghi chú trong notebook: mục tiêu, metric, loại bài toán |
| 2 | Cell EDA + ít nhất 2 biểu đồ có ý nghĩa (vd: phân bố target, heatmap correlation) |
| 3 | Code preprocessing + train_test_split + (scaler/encoder); có X_train, X_test, y_train, y_test |
| 4 | Ít nhất 2 model đã fit; bảng hoặc in ra metric so sánh |
| 5 | classification_report / regression metrics; confusion matrix hoặc scatter actual vs predicted; (optional) GridSearchCV |
| 6 | File model.joblib (và scaler/artifacts nếu cần) + 1 đoạn code load và predict |
| 7 | (Nếu yêu cầu) Flask API có endpoint predict + demo/screenshot |

---

# Bước 1: Định nghĩa bài toán

- [ ] Đã xác định rõ bài toán là **Classification** / **Regression** / **Clustering**.
- [ ] Đã ghi trong notebook: **mục tiêu** (vd: dự đoán giá nhà, phân loại bệnh tim).
- [ ] Đã chọn **metric đánh giá** phù hợp (Accuracy, F1, MAE, RMSE, …).
- [ ] (Nếu classification) Đã xác định có cần ưu tiên Recall/Precision không (imbalanced).

**Gợi ý:** Nếu chưa rõ, xem [00_Pipeline_Skills_Map.md](../00_Pipeline_Skills_Map.md) Bước 1 và [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 1.

---

# Bước 2: Thu thập và khám phá dữ liệu (EDA)

- [ ] Đã **load data** (read_csv hoặc sklearn/API) vào DataFrame.
- [ ] Đã gọi **`df.info()`** và **`df.describe()`**.
- [ ] Đã kiểm tra **missing values** (`df.isnull().sum()` hoặc tương đương).
- [ ] Đã vẽ **ít nhất 1 biểu đồ phân bố target** (bar chart hoặc histogram).
- [ ] Đã vẽ **ít nhất 1 heatmap correlation** (hoặc pairplot/boxplot có ý nghĩa).

**Gợi ý:** Xem [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 2 và [00_Pipeline_Skills_Map.md](../00_Pipeline_Skills_Map.md) Bước 2.

---

# Bước 3: Tiền xử lý dữ liệu

- [ ] Đã tách **X** (features) và **y** (target).
- [ ] Đã xử lý **missing values** (impute hoặc drop) nếu có.
- [ ] Đã **encode** biến categorical (nếu có) bằng LabelEncoder/OneHotEncoder.
- [ ] Đã **chia train/test** với `train_test_split` (stratify nếu classification).
- [ ] Đã **scale** features (StandardScaler/MinMaxScaler) – fit trên train, transform train và test.

**Gợi ý:** Xem [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 3 và Module_04 02_Data_Preprocessing.

---

# Bước 4: Xây dựng mô hình

- [ ] Đã train **ít nhất 2 model** khác loại (vd: LogisticRegression, RandomForest, SVM / LinearRegression, Ridge, RandomForest).
- [ ] Đã **so sánh** các model (in accuracy/MAE/… hoặc bảng).
- [ ] Đã **chọn 1 model** tốt nhất để dùng cho bước 5 và 6.
- [ ] (Nếu BTL yêu cầu wandb) Mỗi lần train (mỗi model hoặc mỗi config) đã gọi **wandb.init** và **wandb.log** để tạo ≥3 runs.

**Gợi ý:** Xem [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 4, [Guide_Wandb.md](Guide_Wandb.md), Lab_Classification / Lab_Regression.

---

# Bước 5: Đánh giá và tinh chỉnh

- [ ] Đã tính **metrics đầy đủ** (classification_report hoặc MAE/RMSE/R² cho regression).
- [ ] Đã vẽ **confusion matrix** (classification) hoặc **actual vs predicted** (regression).
- [ ] (Khuyến khích) Đã dùng **Cross-validation** (vd: 5-fold) hoặc **GridSearchCV/RandomizedSearchCV** để tinh chỉnh.
- [ ] Đã ghi nhận **model cuối cùng** (sau tune nếu có) để lưu ở Bước 6.
- [ ] (Nếu BTL yêu cầu wandb) Đã **log metrics và charts** lên wandb cho run này; có ≥3 runs để so sánh.

**Gợi ý:** Xem [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 5, [Guide_Model_Evaluation.md](Guide_Model_Evaluation.md), [Guide_Wandb.md](Guide_Wandb.md). Module_04 05_Evaluation, Module_05 03_Cross_Validation.

---

# Bước 6: Lưu mô hình

- [ ] Đã lưu **model** (và **scaler** / encoder nếu cần) bằng **joblib.dump**.
- [ ] Đã viết đoạn code **joblib.load** và **predict** với dữ liệu mới để chứng minh hoạt động.
- [ ] (Nếu yêu cầu) Đã lưu **full pipeline** (preprocessing + model) hoặc **artifacts** gộp trong một file.

**Gợi ý:** Xem [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 6, [Guide_Model_Persistence.md](Guide_Model_Persistence.md), Module_06 02_Model_Persistence.

---

# Bước 7: Triển khai (nếu đề bài yêu cầu)

- [ ] Đã tạo **Flask app** (hoặc FastAPI) load model và scaler.
- [ ] Đã có endpoint **POST /predict** nhận features (JSON), trả về prediction.
- [ ] Đã test bằng Postman/curl; (nếu có FE) đã gọi API từ frontend (fetch/axios), bật CORS nếu cần.
- [ ] Đã có **demo** (screenshot hoặc video) FE↔BE↔AI để nộp.

**Gợi ý:** Xem [Guided_Mini_Project.md](Guided_Mini_Project.md) Bước 7, [Guide_API_Connection.md](Guide_API_Connection.md), Module_06 03_Flask_API_Intro, Lab_02_Flask_API.

---

## Tài liệu bổ sung (chi tiết theo chủ đề)

| Chủ đề | File |
|--------|------|
| Thực nghiệm wandb (≥3 runs, log config/metrics/charts) | [Guide_Wandb.md](Guide_Wandb.md) |
| Đánh giá mô hình (metrics, confusion matrix, ROC, so sánh models) | [Guide_Model_Evaluation.md](Guide_Model_Evaluation.md) |
| Lưu mô hình (joblib, artifacts, pipeline, load & predict) | [Guide_Model_Persistence.md](Guide_Model_Persistence.md) |
| Kết nối API (Flask, curl/fetch, CORS, demo FE↔BE) | [Guide_API_Connection.md](Guide_API_Connection.md) |

---

## Hoàn thành

Khi tất cả ô trên đã được tick (theo yêu cầu đề bài), bạn đã hoàn thành pipeline end-to-end cho BTL. Nhớ nộp đủ: notebook, file model, (nếu yêu cầu) wandb link, báo cáo và (nếu có) link demo/API.
