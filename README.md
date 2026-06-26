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
├── railway.toml
└── Language_Classifier_Model.keras   ← place your model here
```

## Local Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API runs at: http://localhost:8000  
Docs at: http://localhost:8000/docs

## Deploy on Railway.app

1. Push this project to GitHub
2. Add your `Language_Classifier_Model.keras` to the repo
3. Go to https://railway.app → New Project → Deploy from GitHub
4. Select your repo → Railway auto-detects and deploys
5. Go to Settings → Networking → Generate Domain
6. Your API URL will be: `https://your-service.up.railway.app`

## Deploy Frontend on GitHub Pages

1. Move `frontend/index.html` to root of repo as `index.html`
2. Replace API_URL in `index.html`:
   ```js
   const API_URL = "https://your-service.up.railway.app";
   ```
3. Go to GitHub repo → Settings → Pages → Deploy from main branch
4. Your site: `https://yourusername.github.io/language-classifier/`

## Supported Languages
ar, bg, de, el, en, es, fr, hi, it, ja, nl, pl, pt, ru, sw, th, tr, ur, vi, zh
