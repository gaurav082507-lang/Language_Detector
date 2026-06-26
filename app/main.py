from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

app = FastAPI(title="Language Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = tf.keras.models.load_model("Language_Classifier_Model.keras")

class_names = [
    'ar', 'bg', 'de', 'el', 'en',
    'es', 'fr', 'hi', 'it', 'ja',
    'nl', 'pl', 'pt', 'ru', 'sw',
    'th', 'tr', 'ur', 'vi', 'zh'
]

language_map = {
    'ar': 'Arabic',    'bg': 'Bulgarian', 'de': 'German',
    'el': 'Greek',     'en': 'English',   'es': 'Spanish',
    'fr': 'French',    'hi': 'Hindi',     'it': 'Italian',
    'ja': 'Japanese',  'nl': 'Dutch',     'pl': 'Polish',
    'pt': 'Portuguese','ru': 'Russian',   'sw': 'Swahili',
    'th': 'Thai',      'tr': 'Turkish',   'ur': 'Urdu',
    'vi': 'Vietnamese','zh': 'Chinese'
}

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Language Classifier API is running!"}

@app.post("/predict")
def predict(input: TextInput):
    tensor = tf.constant([[input.text]], dtype=tf.string)
    predictions = model(tensor)
    probs = predictions[0].numpy()
    idx = int(tf.argmax(probs).numpy())
    code = class_names[idx]
    confidence = float(probs[idx])

    # Top 3 predictions
    top3_idx = np.argsort(probs)[::-1][:3]
    top3 = [
        {"code": class_names[i], "language": language_map[class_names[i]], "confidence": round(float(probs[i]) * 100, 2)}
        for i in top3_idx
    ]

    return {
        "code": code,
        "language": language_map[code],
        "confidence": round(confidence * 100, 2),
        "top3": top3
    }
