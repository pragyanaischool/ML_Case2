# -*- coding: utf-8 -*-
"""ML_Case2_Streamlite.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gMC0uO4jtJlyQmVBFXcTi5HlpwCtBpbB
"""

import streamlit as st
import pandas as pd
from sklearn import svm
import joblib
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


#Loading up the Regression model we created
svm = svm.SVC()
model = joblib.load('svm.joblib')
#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium,sex, smoking, time ):
    if sex == 'Male':
        sex = 1
    elif sex == 'Female':
        sex = 0
    if smoking == 'Yes':
        smoking = 1
    elif smoking == 'No':
        smoking = 0

    df = pd.DataFrame([[age, ejection_fraction, serum_creatinine, serum_sodium]], columns=['age', 'ejection_fraction', 'serum_creatinine', 'serum_sodium'])
    data = pd.read_csv("heart_failure_clinical_records_dataset.csv") #path folder of the data file
    X = data[['age', 'ejection_fraction',  'serum_creatinine', 'serum_sodium',]]
    scaler.fit_transform(X)
    x_test = scaler.transform(df)
    prediction = model.predict(x_test)
    return prediction


st.title('Heart Failure_Death_Prediction: 0 No death, 1 Death')
st.image("""https://familydoctor.org/wp-content/uploads/2000/09/42187220_l.jpg""")
st.header('Enter the characteristics of the Heart:')
age = st.number_input('Age:', min_value=1, max_value=100, value=1)
ejection_fraction = st.number_input('ejection_fraction:', min_value=1, max_value=100, value=1)
anaemia = st.number_input('anaemia:', min_value=0, max_value=1, value=1)
creatinine_phosphokinase = st.number_input('creatinine_phosphokinase:',min_value=0, max_value=10000, value=1)
diabetes = st.number_input('diabetes:', min_value=0, max_value=1, value=1)
high_blood_pressure = st.number_input('high_blood_pressure:', min_value=0, max_value=1, value=1)
sex = st.radio('Gender:', ('Male', 'Female'))
smoking = st.radio('Smoking :', ('Yes', 'No'))
time = st.number_input('Time:', min_value=0.1, max_value=100.0, value=1.0)
serum_sodium = st.number_input('serum_sodium:', min_value=100, max_value=200, value=100)
platelets =st.number_input('platelets:', min_value=1000, max_value=565000, value=10000)
serum_creatinine =st.number_input('serum_creatinine:', min_value=0.1, max_value=10.0, value=1.0)

if st.button('SUBMIT : Values'):
    death = predict(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium,sex, smoking,time)
    st.success(f'The predicted of heart Failur (1 Death, 0 not Death) : {death[0]:.2f}')
