# Importing Libraries
import streamlit as st 
 
import pandas as pd 
 
import joblib 
# Loading CSS File
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Loading the Saved Machine Learning Model
model=joblib.load("KNN_heart.pkl") 
 
 
# Loading the Saved Scaler
scaler=joblib.load("scaler.pkl") 
 
 
# Loading the Expected Columns
expected_columns=joblib.load("columns.pkl") 
 
 
# Creating the Application Title
st.title("Intelligent Heart Health Assessment") 
 
 
# Providing Instructions to the User
st.markdown("Provide the following Details") 
 
 
# Taking Age as Input
age=st.slider("Age",18,100,40) 
 
 
# Taking Gender as Input
sex=st.selectbox("SEX",['M','F']) 
 
 
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
cholesterol=st.number_input("Cholesterol(mg/dL)",100,600,200) 
 
 
# Taking Fasting Blood Sugar as Input
fasting_bs=st.selectbox("Fasting Blood Sugar>120 mg/dL",[0,1]) 
 
 
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
max_hr = st.selectbox("Max Heart Rate", list(range(60, 221))) 
 
 
# Taking Exercise-Induced Angina as Input
exercise_angina= st.selectbox("Exercise-Induced Angina",["Y" ," N"]) 
 
 
# Taking Oldpeak Value as Input
oldpeak=st.slider("oldpeak(ST Depression)",0.0,0.6,1.0) 
 
 
# Creating Predict Button
if st.button("Predict"): 
 
    # 1. Store user inputs in raw format matching original dataset column names 
    raw_input = { 
        'Age': age, 
        'RestingBP': resting_bp, 
        'Cholesterol': cholesterol, 
        'FastingBS': fasting_bs, 
        'MaxHR': max_hr, 
        'Oldpeak': oldpeak, 
        'Sex': sex, 
        'ChestPainType': chest_pain_value, 
        'RestingECG': resting_ecg_value, 
        'ExerciseAngina': exercise_angina.strip() 
    } 
 
    # 2. Convert raw input into DataFrame 
    input_df = pd.DataFrame([raw_input]) 
 
    # 3. Add missing columns 
    for col in expected_columns: 
        if col not in input_df.columns: 
            input_df[col]=0 
 
    # 4. Arrange columns in expected order 
    input_df=input_df[expected_columns] 
 
    # 5. Scale the Input Data
    scaled_input=scaler.transform(input_df) 
 
    # 6. Make Prediction Using the KNN Model
    prediction=model.predict(scaled_input)[0] 
 
    # 7. Display Prediction Result
    if prediction==1: 
        st.error("High Risk of heart Disease") 
    else: 
        st.success("Low Risk of heart Disease")