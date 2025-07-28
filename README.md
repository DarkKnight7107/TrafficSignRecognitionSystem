# Traffic Sign Recognition System

### CNN-based Model to Predict Traffic Signs
- **Code**: [`CNN.ipynb`](CNN.ipynb)
- **Dataset**: [GTSRB - German Traffic Sign Recognition Benchmark](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)
- **Model**: `cnn_model_v01.h5`

---

### YOLO for Detection + CNN for Classification
- **Code**: [`YOLO_CNN.ipynb`](YOLO_CNN.ipynb)
- **Dataset**: [GTSRB - German Traffic Sign Recognition Benchmark](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)
- **Models**: `cnn_model_v01.h5`, `yolov5.pt`

---

### Fine-Tuned YOLO for Traffic Sign Prediction
- **Code**: [`YOLO_fine_tuned_v01.ipynb`](YOLO_fine_tuned_v01.ipynb), [`script.py`](script.py)
- **Dataset**: [GTSDB - German Traffic Sign Detection Benchmark](https://benchmark.ini.rub.de/gtsdb_dataset.html)
- **Model**: `yolov5_fine_tuned_v01.pt`

---

### Creating a Custom Dataset with Fine-Tuned YOLO (Image Collection & Annotation) and Further Fine-Tuning
- **Code**: [`YOLO_fine_tuned_v02.ipynb`](YOLO_fine_tuned_v02.ipynb), [`YOLO_Prepare_Data.ipynb`](YOLO_Prepare_Data.ipynb)
- **Dataset**: Custom prepared dataset
- **Refrences**: [Traffic Signs Meanings](https://routetogermany.com/drivingingermany/road-signs)
- **Model**: `yolov8_fine_tuned_v02.pt`
