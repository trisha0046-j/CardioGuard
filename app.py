# Importing Libraries
import streamlit as st
import pandas as pd
import joblib


# Loading CSS File
with open("static/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# Loading the Saved Machine Learning Model
model = joblib.load("KNN_heart .pkl")


# Loading the Saved Scaler
scaler = joblib.load("scaler .pkl")


# Loading the Expected Columns
expected_columns = joblib.load("columns .pkl")


# Creating the Application Title
st.title("Intelligent Heart Health Assessment")


# Providing Instructions to the User
st.markdown("Provide the following Details")


# Taking Age as Input
age = st.slider("Age", 18, 100, 40)


# Taking Gender as Input
sex = st.selectbox("SEX", ["M", "F"])


# Creating Chest Pain Type Options
chest_pain_options = {

    "Atypical Angina": "ATA",

    "Non-Anginal Pain": "NAP",

    "Typical Angina": "TA",

    "Asymptomatic": "ASY"

}


# Taking Chest Pain Type as Input
chest_pain = st.selectbox(
    "Chest Pain Type",
    list(chest_pain_options.keys())
)


# Converting Chest Pain Type to Dataset Value
chest_pain_value = chest_pain_options[chest_pain]


# Taking Resting Blood Pressure as Input
resting_bp = st.number_input(
    "Resting Blood Pressure(mm Hg)",
    min_value=80,
    max_value=200,
    value=120
)


# Taking Cholesterol Level as Input
cholesterol = st.number_input(
    "Cholesterol(mg/dL)",
    min_value=100,
    max_value=600,
    value=200
)


# Taking Fasting Blood Sugar as Input
fasting_bs = st.selectbox(
    "Fasting Blood Sugar >120 mg/dL",
    [0, 1]
)


# Creating Resting ECG Options
resting_ecg_options = {

    "Normal": "Normal",

    "ST-T Wave Abnormality": "ST",

    "Left Ventricular Hypertrophy": "LVH"

}


# Taking Resting ECG as Input
resting_ecg = st.selectbox(
    "Resting ECG",
    list(resting_ecg_options.keys())
)


# Converting Resting ECG to Dataset Value
resting_ecg_value = resting_ecg_options[resting_ecg]


# Taking Maximum Heart Rate as Input
max_hr = st.slider(
    "Max Heart Rate",
    60,
    220,
    150
)


# Taking Exercise-Induced Angina as Input
exercise_angina = st.selectbox(
    "Exercise-Induced Angina",
    ["Y", "N"]
)


# Taking Oldpeak Value as Input
oldpeak = st.slider(
    "Oldpeak (ST Depression)",
    0.0,
    6.0,
    1.0
)


# Taking ST Slope as Input
st_slope = st.selectbox(
    "ST Slope",
    ["Down", "Flat", "Up"]
)


# Creating Predict Button
if st.button("Predict"):

    # Creating input data in the same format used during model training
    input_data = {

        'Age': age,

        'RestingBP': resting_bp,

        'Cholesterol': cholesterol,

        'FastingBS': fasting_bs,

        'MaxHR': max_hr,

        'Oldpeak': oldpeak,

        'Sex_M': 1 if sex == "M" else 0,

        'ChestPainType_ATA': 1 if chest_pain_value == "ATA" else 0,

        'ChestPainType_NAP': 1 if chest_pain_value == "NAP" else 0,

        'ChestPainType_TA': 1 if chest_pain_value == "TA" else 0,

        'RestingECG_Normal': 1 if resting_ecg_value == "Normal" else 0,

        'RestingECG_ST': 1 if resting_ecg_value == "ST" else 0,

        'ExerciseAngina_Y': 1 if exercise_angina == "Y" else 0,

        'ST_Slope_Flat': 1 if st_slope == "Flat" else 0,

        'ST_Slope_Up': 1 if st_slope == "Up" else 0
    }


    # Converting Input Data into DataFrame
    input_df = pd.DataFrame([input_data])


    # Arranging Columns in the Exact Order Expected by the Model
    input_df = input_df[expected_columns]


    # Scaling the Input Data
    scaled_input = scaler.transform(input_df)


    # Making Prediction Using KNN Model
    prediction = model.predict(scaled_input)[0]


    # Displaying Prediction Result
    if prediction == 1:

        st.error("⚠️ High Risk of Heart Disease")

    else:

        st.success("✅ Low Risk of Heart Disease")


    # Disclaimer
    st.caption(
        "This application is for educational purposes only and is not a medical diagnosis."
    )