# ❤️ CardioGuard - Heart Disease Prediction

## 📌 Project Overview

CardioGuard is a Machine Learning based web application that predicts the risk of heart disease based on various health-related parameters.

The application uses a K-Nearest Neighbors (KNN) classification model and is deployed using Streamlit.

## 🚀 Features

- Heart disease risk prediction
- User-friendly Streamlit interface
- KNN Machine Learning model
- Data preprocessing and feature scaling
- One-hot encoding for categorical features
- Interactive input fields
- Real-time prediction

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- HTML/CSS

## 🤖 Machine Learning Model

The project uses:

**K-Nearest Neighbors (KNN)**

The model is trained using health-related features such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

## 📊 Model Performance

The KNN model achieved approximately:

**Accuracy: 86.41%**

**F1 Score: 88.15%**

## 📂 Project Structure

```text
Heart Disease Prediction/
│
├── app.py
├── KNN_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
│
└── static/
    └── style.css