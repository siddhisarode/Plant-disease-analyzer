from fastapi import FastAPI
import tensorflow as tf
import os
from fastapi import UploadFile, File
from backend.utils.image_utils import preprocess_image
from backend.utils.remedies import REMEDIES
from fastapi.middleware.cors import CORSMiddleware



CLASS_NAMES = [
    "Early_Blight",
    "Healthy",
    "Late_Blight",
    "Leaf_Mold",
    "Septoria_Leaf_Spot"
]


app = FastAPI(title="Plant Disease Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "tomato_disease_model.h5")

model = tf.keras.models.load_model(MODEL_PATH)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Plant Disease API is live",
        "model_loaded": True
    }
@app.post("/preprocess")
async def preprocess_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    processed_image = preprocess_image(image_bytes)

    return {
        "status": "success",
        "shape": processed_image.shape
    }

from fastapi import UploadFile, File
import numpy as np

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Preprocess image
    processed_image = preprocess_image(image_bytes)

    # Model prediction
    predictions = model.predict(processed_image)
    confidence = float(np.max(predictions))
    predicted_class = CLASS_NAMES[int(np.argmax(predictions))]

    info = REMEDIES[predicted_class]

    return {
        "prediction": predicted_class,
        "confidence": round(confidence * 100, 2),
        "description": info["description"],
        "remedies": info["remedies"],
        "care_tips": info["care_tips"]
    }



