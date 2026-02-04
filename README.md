
# 🌱 Plant Disease Analyzer

A deep learning–based web application that detects plant diseases from leaf images using **MobileNetV2** and provides confidence scores, descriptions, and remedies.

---

## 📌 Project Overview

Plant diseases cause major losses in agriculture if not detected early. This project uses **computer vision and deep learning** to automatically identify plant diseases from leaf images and assist users with accurate diagnosis and remedies.

---

## 🚀 Features

- Upload plant leaf images via web interface  
- Detect plant disease using trained CNN model  
- Displays disease name, confidence score, description, and remedies  
- Fast and lightweight backend using **FastAPI**  

---

## 🧠 Model Details

- **Model:** MobileNetV2 (Transfer Learning)  
- **Image Size:** 224 × 224  
- **Classes:**
  - Early Blight  
  - Healthy  
  - Late Blight  
  - Leaf Mold  
  - Septoria Leaf Spot  

---

## 📊 Model Accuracy

- **Phase 1 Training:** ~85%  
- **After Fine-Tuning:** ~89%  

---

## 🏗️ Project Structure

```

Plant-disease-analyzer/
│── backend/            # FastAPI backend
│   ├── app.py
│   ├── requirements.txt
│   └── utils/
│
│── frontend/           # HTML, CSS, JS frontend
│   ├── index.html
│   ├── app.html
│   ├── style.css
│   └── script.js
│
│── model/              # Trained models
│   ├── phase1_best_model.h5
│   └── tomato_disease_model.h5
│
│── training/           # Training notebooks & scripts
│   ├── train_model.ipynb
│   └── split_dataset.py
│
│── dataset/            # Train / Val / Test data (optional)
│── README.md
│── .gitignore

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/siddhisarode/Plant-disease-analyzer.git
cd Plant-disease-analyzer
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv plantenv
```

**Windows**

```bash
plantenv\Scripts\activate
```

**Linux / macOS**

```bash
source plantenv/bin/activate
```

---

### 3️⃣ Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

### 4️⃣ Run Backend

```bash
uvicorn app:app --reload
```

* Backend URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 5️⃣ Run Frontend

* Open `frontend/index.html` in browser
* OR use **Live Server** in VS Code

---

## 🔗 API Endpoints

| Method | Endpoint | Description                      |
| ------ | -------- | -------------------------------- |
| GET    | /        | Health check                     |
| POST   | /predict | Predict plant disease from image |

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* MobileNetV2
* FastAPI
* HTML, CSS, JavaScript
* OpenCV
* NumPy

---

## 📦 Deployment Status

* Local deployment using FastAPI
* Cloud deployment: **Future scope**

---

## 🚧 Limitations

* Requires clear and well-lit leaf images
* Limited to trained disease classes

---

## 🔮 Future Enhancements

* Cloud deployment
* Mobile application
* Support for more crops and diseases
* Real-time camera-based detection

---

## 👩‍💻 Author

**Siddhi Sarode**
GitHub: [https://github.com/siddhisarode](https://github.com/siddhisarode)

---

## 📄 License

This project is intended for **educational and research purposes**.






