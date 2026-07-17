# 🫁 Chest X-Ray Classifier | End-to-End Deep Learning MLOps Project

![Python](https://img.shields.io/badge/Python-3.12-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Flask](https://img.shields.io/badge/Flask-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![DVC](https://img.shields.io/badge/DVC-Pipeline-purple)
![AWS](https://img.shields.io/badge/AWS-Deployment-yellow)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)

---

# 📌 Overview

This project is an end-to-end **Chest X-ray Image Classification System** built using **Deep Learning, TensorFlow, Flask, Docker, DVC, and AWS**.

The system automatically classifies chest X-ray images to assist in disease detection. The project follows a complete **MLOps workflow**, from data ingestion and model training to deployment using Docker and AWS.

---

# 🚀 Features

- End-to-End Deep Learning Pipeline
- Transfer Learning using CNN
- DVC Pipeline Management
- Data Version Control
- Flask REST API
- Docker Containerization
- GitHub Actions CI/CD
- AWS Deployment (ECR + EC2)
- YAML Configuration
- Modular Project Structure

---

# 🏗️ Project Architecture

```
Chest X-ray Images
        │
        ▼
Data Ingestion
        │
        ▼
Data Preprocessing
        │
        ▼
CNN Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Saved Model
        │
        ▼
Flask API
        │
        ▼
Docker
        │
        ▼
AWS Deployment
```

---

# 📂 Project Structure

```
Chest-Xray-Classifier/

│
├── config/
├── research/
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── utils/
│
├── templates/
├── app.py
├── main.py
├── dvc.yaml
├── params.yaml
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

# 🧠 Deep Learning Pipeline

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation
- Model Prediction

---

# ⚙️ Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python |
| Deep Learning | TensorFlow, Keras |
| API | Flask |
| Version Control | Git |
| Data Versioning | DVC |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | AWS EC2, AWS ECR |
| Configuration | YAML |

---

# 📊 Model Workflow

```
Input Chest X-ray
        │
        ▼
Image Preprocessing
        │
        ▼
CNN Model
        │
        ▼
Prediction
        │
        ▼
Disease Classification
```

---

# ⚡ Installation

Clone Repository

```bash
git clone https://github.com/sourabhbagda24/Chest-Xray-Classifier.git
cd Chest-Xray-Classifier
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

---

# ▶️ Run Training Pipeline

```bash
python main.py
```

or

```bash
dvc repro
```

---

# 🌐 Run Flask Application

```bash
python app.py
```

Application will run at

```
http://localhost:8080
```

---

# 🐳 Docker

Build Image

```bash
docker build -t chest-xray-classifier .
```

Run Container

```bash
docker run -p 8080:8080 chest-xray-classifier
```

---

# ☁️ AWS Deployment

- AWS EC2
- AWS ECR
- Docker
- GitHub Actions

Deployment Flow

```
GitHub Push
      │
      ▼
GitHub Actions
      │
      ▼
Docker Build
      │
      ▼
AWS ECR
      │
      ▼
AWS EC2
      │
      ▼
Flask Application
```

---

# 📈 Future Improvements

- Improve Model Accuracy
- Hyperparameter Tuning
- MLflow Integration
- Grad-CAM Visualization
- Streamlit Frontend
- Model Monitoring
- Explainable AI (XAI)

---

# 👨‍💻 Author

**Sourabh Sharma**

- 💼 LinkedIn: https://www.linkedin.com/in/sourabh-sharma-90758232b/
- 💻 GitHub: https://github.com/sourabhbagda24

---

# ⭐ If you found this project helpful, don't forget to Star the repository.
