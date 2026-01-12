 🌱 Plant Disease Analyzer

A deep learning–based web application that detects plant diseases from leaf images using MobileNetV2 and provides confidence scores, descriptions, and remedies.

 📌 Project Overview

Plant diseases cause major losses in agriculture if not detected early. This project uses computer vision and deep learning to automatically identify plant diseases from leaf images and assist users with remedies.

 🚀 Features

- Upload plant leaf images via web interface  
- Detect plant disease using trained CNN model  
- Displays disease name, confidence, description, and remedies  
- Fast backend using FastAPI  

 🧠 Model Details

- Model: MobileNetV2 (Transfer Learning)  
- Image Size: 224 × 224  
- Classes:
  - Early Blight  
  - Healthy  
  - Late Blight  
  - Leaf Mold  
  - Septoria Leaf Spot  

 📊 Accuracy
- Phase 1 Training: ~85%  
- After Fine-Tuning: ~89%  

 🏗️ Project Structure

Plant-disease-analyzer/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── utils/
├── frontend/
│   ├── index.html
│   ├── app.html
│   ├── style.css
│   └── script.js
├── model/
│   ├── phase1_best_model.h5
│   └── tomato_disease_model.h5
├── training/
│   ├── train_model.ipynb
│   └── split_dataset.py
├── dataset/
├── README.md
└── .gitignore

 ⚙️ Setup Instructions

### 1. Clone Repository
git clone https://github.com/siddhisarode/Plant-disease-analyzer.git  
cd Plant-disease-analyzer  

### 2. Create Virtual Environment
python -m venv plantenv  

Windows:
plantenv\Scripts\activate  

Linux / macOS:
source plantenv/bin/activate  

### 3. Install Backend Dependencies
cd backend  
pip install -r requirements.txt  

### 4. Run Backend
uvicorn app:app --reload  

Backend URL: http://127.0.0.1:8000  
API Docs: http://127.0.0.1:8000/docs  

### 5. Run Frontend
Open frontend/index.html in browser  
or use Live Server in VS Code  

## 🔗 API Endpoints

GET  /        → Health check  
POST /predict → Predict plant disease from image  

## 🛠️ Technologies Used

- Python  
- TensorFlow / Keras  
- MobileNetV2  
- FastAPI  
- HTML, CSS, JavaScript  
- OpenCV  
- NumPy  

 📦 Deployment Status

- Local deployment using FastAPI  
- Cloud deployment: Future scope  

 🚧 Limitations

- Requires clear leaf images  
- Limited to trained disease classes  

 🔮 Future Enhancements

- Cloud deployment  
- Mobile application  
- More crops and diseases  
- Real-time camera detection  

 👩‍💻 Author

Siddhi Sarode  
GitHub: https://github.com/siddhisarode
