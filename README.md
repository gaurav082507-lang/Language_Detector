# Language Classifier — Gaurav Gupta, BIT Mesra AIML

A character-level Bidirectional LSTM model that detects 20 languages.

## Project Structure
```
language-classifier/
├── app/
│   └── main.py          # FastAPI backend
├── frontend/
│   └── index.html       # Frontend UI
├── requirements.txt
├── render.yaml
└── Language_Classifier_Model.keras   ← place your model here
```

## Local Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API runs at: http://localhost:8000  
Docs at: http://localhost:8000/docs

## Deploy on Render.com

1. Push this project to GitHub
2. Add your `Language_Classifier_Model.keras` to the repo
3. Go to https://render.com → New → Web Service
4. Connect your GitHub repo
5. Render auto-detects `render.yaml` and deploys

## Deploy Frontend

- Open `frontend/index.html`
- Replace `API_URL` with your Render API URL:
  ```js
  const API_URL = "https://your-api-name.onrender.com";
  ```
- Deploy on GitHub Pages / Netlify / Vercel (just drag and drop index.html)

## Supported Languages
ar, bg, de, el, en, es, fr, hi, it, ja, nl, pl, pt, ru, sw, th, tr, ur, vi, zh
