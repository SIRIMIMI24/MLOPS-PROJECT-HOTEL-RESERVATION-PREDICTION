# 🏨 Hotel Reservation Cancellation Prediction  
## End-to-End MLOps Project

---

## 📌 Project Overview

This project implements a production-grade MLOps pipeline to predict whether a customer will cancel a hotel reservation. The objective is to design, build, and deploy a fully automated, reproducible, scalable, and production-ready machine learning system.

The system covers the entire ML lifecycle:

- Data ingestion  
- Data validation & processing  
- Model training  
- Experiment tracking  
- Data & model versioning  
- CI/CD automation  
- Containerization  
- REST API deployment  
- Monitoring & governance  

The repository follows industry-standard MLOps best practices and emphasizes modular architecture, reproducibility, and deployment readiness.

---

## 🎯 Business Problem

Hotel reservation cancellations significantly impact revenue forecasting and operational planning.

### Objective

Predict whether a booking will be:

- `1 → Canceled`
- `0 → Not Canceled`

The model enables proactive decision-making for revenue optimization and risk mitigation.

---

## 📂 Dataset

The dataset contains historical hotel reservation records including:

- Lead time  
- Market segment  
- Deposit type  
- Customer type  
- Previous cancellations  
- Special requests  
- Room type  
- Booking changes  
- Arrival date information  

### Target Variable

```
is_canceled
```

---

## 🏗️ End-to-End MLOps Workflow

```
Database Setup
        ↓
Project Setup
        ↓
Data Ingestion
        ↓
Data Validation
        ↓
Data Processing
        ↓
Model Training
        ↓
Experiment Tracking (MLflow)
        ↓
Data & Model Versioning (DVC)
        ↓
Training Pipeline Automation
        ↓
FastAPI REST Application
        ↓
Docker Containerization
        ↓
CI/CD Deployment
        ↓
Monitoring & Governance
```

---

## 🧱 Project Structure

```
hotel-reservation-mlops/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_processing.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── logger.py
│   ├── custom_exception.py
│   └── utils.py
│
├── app/
│   └── main.py
│
├── Dockerfile
├── requirements.txt
├── .github/workflows/
│   └── ci_cd.yaml
└── README.md
```

---

## ⚙️ System Components

### 1️⃣ Database Setup
- Structured schema for reservation data  
- SQL-based validation  
- ETL integration  

### 2️⃣ Data Ingestion
- Configuration-driven data loading  
- Schema validation  
- Logging and exception handling  
- Artifact storage  

### 3️⃣ Data Versioning
- DVC integration  
- Remote storage configuration  
- Reproducible dataset snapshots  

### 4️⃣ Data Processing
- Missing value handling  
- Outlier treatment  
- Feature engineering  
- Categorical encoding  
- Feature scaling  
- Pipeline serialization  

### 5️⃣ Model Training
- TensorFlow / PyTorch implementation  
- Train-validation split  
- Early stopping  
- Model checkpointing  
- Hyperparameter tuning  
- Evaluation metrics logging  

### 6️⃣ Experiment Tracking (MLflow)

- Parameter logging  
- Metric tracking  
- Model artifact storage  
- Model registry integration  

Run MLflow UI:

```
mlflow ui
```

### 7️⃣ Training Pipeline

The pipeline orchestrates:

- Data ingestion  
- Data processing  
- Model training  
- Model evaluation  

Fully modular and configuration-driven.

### 8️⃣ REST API Deployment (FastAPI)

Endpoints:

- `/predict`
- `/health`

Features:

- Input schema validation  
- Model loading from registry  
- JSON-based prediction response  

Run locally:

```
uvicorn app.main:app --reload
```

### 9️⃣ Docker Containerization

Build image:

```
docker build -t hotel-reservation-app .
```

Run container:

```
docker run -p 8000:8000 hotel-reservation-app
```

Benefits:

- Environment consistency  
- Portability  
- CI/CD compatibility  

---

## 🔁 CI/CD Pipeline

Automated workflow includes:

- Code linting  
- Unit testing  
- Docker build  
- Image push  
- Automated deployment  

Triggers:

- Push to main branch  
- Pull request merge  

---

## 📊 Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- ROC-AUC  

Business-critical metric:

Recall for cancellation class.

---

## 📡 Monitoring Strategy

### Data Drift Monitoring
- Population Stability Index (PSI)  
- Distribution comparison  

### Model Performance Monitoring
- Accuracy tracking  
- Confusion matrix  
- Prediction distribution  

### Logging
- Structured logs  
- Request tracing  
- Exception tracking  

---

## 🧪 Testing Strategy

- Unit tests for components  
- Integration tests for pipeline  
- API endpoint testing  
- Schema validation tests  

---

## 🔒 Reproducibility & Governance

- YAML-based configuration  
- Environment isolation  
- MLflow model registry  
- Git-based version control  
- Deterministic training setup  

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```
git clone <repo_url>
cd hotel-reservation-mlops
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Training Pipeline

```
python src/pipeline/training_pipeline.py
```

### 5️⃣ Start API

```
uvicorn app.main:app --reload
```

---

## 📈 Future Improvements

- Feature store integration  
- Optuna-based hyperparameter tuning  
- Kubernetes deployment  
- Real-time inference pipeline  
- Canary deployment strategy  
- Automated drift retraining  

---

## 🎓 Learning Outcomes

This project demonstrates:

- Production-grade ML system architecture  
- Modular pipeline engineering  
- CI/CD integration for ML systems  
- Data & model versioning strategies  
- Monitoring and governance in production  

---

Author:  
MLOps Project – Hotel Reservation Cancellation Prediction  
Graduate-Level ML System Implementation