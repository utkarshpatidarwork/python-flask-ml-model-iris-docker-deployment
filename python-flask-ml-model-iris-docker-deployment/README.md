# 🐍 Python + Flask + ML Model + Docker Deployment
🚀 End-to-end Machine Learning model deployed as a REST API inside a Docker container, with an HTML UI for testing.

---

## 📌 Project Overview
This project demonstrates how to **train a machine learning model**, **serve it using Flask**, and **deploy it inside a Docker container** so it runs the same on any system.

✅ Trained ML Model (Iris dataset)  
✅ Flask REST API  
✅ Dockerized backend  
✅ Browser-based UI for predictions  
✅ Includes both model file + training script  

---

## 📂 Folder Structure
python-flask-ml-model-iris-docker-deployment/
│
├── app/
│   ├── app.py                  ← Flask API
│   ├── requirements.txt        ← Python dependencies
│   ├── index.html              ← Frontend UI tester
│   ├── train_model.py          ← Script to generate model.pkl
│   └── model/
│       └── model.pkl           ← Pre-trained ML model
│
├── Dockerfile                  ← Build Docker image
├── .dockerignore               ← Ignore useless files in image
├── .gitignore                  ← Ignore pycache, venv, logs, etc.
├── README.md                   ← Full documentation
└── LICENSE                     ← MIT License

