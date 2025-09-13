# FastAPI ML Model Deployment on Render

This repository hosts a FastAPI API that serves predictions from a trained scikit-learn model. The API exposes a `/predict` endpoint that accepts JSON input and returns predictions.

---

## 📝 Prerequisites

- GitHub account
- Render account
- Python 3.13+ (if running locally)
- Docker (optional, for Docker deployment)
- Basic knowledge of Git and Python

### Python Libraries

Dependencies are pinned in `requirements.txt`:
  fastapi==0.111.0
  uvicorn==0.30.6
  scikit-learn==1.4.1.post1
  joblib==1.5.0
  pandas==2.2.3


---

## 📁 Repository Structure

repo/
├─ app.py # FastAPI app
├─ model.pkl # Trained model
├─ requirements.txt # Python dependencies
├─ Dockerfile # Optional, for Docker deployment
├─ Procfile # Optional, for non-Docker deployment
└─ README.md


---

## 🚀 Deployment Steps

### Deploy using Docker

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

2. Ensure your Dockerfile is configured
    - CMD uses $PORT
    - EXPOSE 8000 (metadata)
    - Dependencies installed via requirements.txt

3. Push to GitHub:
   ```
    git add .
    git commit -m "Prepare for deployment"
    git push origin main
   ```

4. On Render:

    - Click New → Web Service
    - Connect your GitHub repo
    - Select Docker environment
    - Set Root Directory if needed
    - Click Create Web Service

5. Watch logs until you see:
   ```
    Application startup complete
   ```

## 🧪 Testing the API

  - You can test your deployed API with this Python script:
  ```
    import requests

    url = "https://fastapi-test-oyda.onrender.com/predict"
    
    patient = {
        "age": 93,
        "sex": 1,
        "bmi": 0.061,
        "bp": 0.01,
        "s1": -0.044,
        "s2": -0.034,
        "s3": -0.043,
        "s4": -0.002,
        "s5": 0.019,
        "s6": -0.017
    }
    
    response = requests.post(url, json=patient)
    print(response.json())
```
  - Anyone with this script can use your API while it's running.


## 🛠 Troubleshooting

 - 404 Not Found → check endpoint URL in app.py

 - App keeps restarting → CMD/Procfile must bind to $PORT

 - Model fails to load → ensure scikit-learn version matches training environment

## ✅ License

MIT - Educational Purpose Only


