# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:32:27 2021

@author: Hein Htet Hlaing
"""

import streamlit as st
from pyngrok import ngrok

st.set_page_config(
	layout="centered",
	initial_sidebar_state="auto",
	page_title="Assistance",	
    page_icon="⚕",
)

st.write('''
# Heart Disease Detector Assistance
''')

st.info('This will help you to fill the required fields from the Heart Disease Detection App.')

st.subheader('Chest Pain Type')
st.write("""
It is a symptom of an underlying heart problem, usually coronary heart disease (CHD).\n
*Typical Angina* usually causes uncomfortable pressure, fullness, squeezing or pain in the center of the chest. You may also feel the discomfort in your neck, jaw, shoulder, back or arm. \n
*Atypical Angina* symptoms of a heart attack may include fatigue, shortness of breath, discomfort in the throat, jaw, neck, arms, back and stomach—a feeling described almost like a muscle pull or pain. \n
*Non anginal pain* is a term used to describe chest pain that resembles heart pain (also called angina) in patients who do not have heart disease. The pain typically is felt behind the breast bone (sternum) and is described as oppressive, squeezing or pressure-like. \n
*Asymptomatic :* Being asymptomatic means that you have no symptoms
""")

st.subheader('Resting Blood Sugar')
st.write('''
Blood sugar, or glucose, is the main sugar found in your blood. It comes from the food you eat, and is your body's main source of energy. \n
Normal is less than 140 mg/dL. (7.8mmol/L) \n
Between 140 and 199 mg/dL (7.8 mmol/L and 11.0 mmol/L) indicates prediabetes. Its symptoms are - Increased thirst, Frequent urination, Excess hunger, Fatigue, Blurred vision.
Over 200 mg/dL (11.1 mmol/L) after two hours indicates diabetes and its symptoms - Urinate (pee) a lot, often at nigt, very thirsty, Lose weight without trying, very hungry, blurry vision, Have numb or tingling hands or feet, Feel very tired, Have very dry skin.
If over 300 mg/dL, it is very dangeous. Call Your Doctor.
''')

st.subheader('Resting Electrocardiographic Results')
st.write('''
Electrocardiography (ECG) is a non-invasive test that can detect abnormalities including arrhythmias, evidence of coronary heart disease, left ventricular hypertrophy and bundle branch blocks. \n
*Nothing to note* is for Normal people. \n
*ST-T abnormality* on an electrocardiogram (ECG) is known to independently predict subsequent morbidity and mortality from cardiovascular diseases. \n
*Left ventricular hypertrophy, or LVH*, is a term for a heart's left pumping chamber that has thickened and may not be pumping efficiently.
''')

st.subheader('Serum Cholestoral')
st.write('''
Cholesterol is a type of body fat, or lipid. A person's serum cholesterol level represents the amount of total cholesterol in their blood. A person's serum cholesterol level comprises the amount of high-density lipoprotein (HDL), low-density lipoprotein (LDL), and triglycerides in the blood. \n
Normal people have cholesterol level between 100 mg/dL to 240 mg/dL. |n
Less than 100 mg/dL is considered as Low-Density Lipoprotein (LDL) and more than 240 mg/dL is High-Density Lipoprotein (HDL). \n
*High or Low Cholesterol level Symptoms* are angina, chest pain, nausea, extreme fatigue, shortness of breath, pain in the neck, jaw, upper abdomen, or back, numbness or coldness in your extremities.
''')

st.subheader('Fasting Blood Sugar')
st.write('''
*Fasting blood sugar*: A test to determine how much glucose (sugar) is in a blood sample after an overnight fast. The fasting blood glucose test is commonly used to detect diabetes mellitus. \n
A fasting blood sugar level of 99 mg/dL or lower is normal. \n
100 to 125 mg/dL indicates you have prediabetes, and \n
126 mg/dL or higher indicates you have diabetes.
''')

st.subheader('Maximum Heart Rate Achieved')
st.write('''
You can calculate your maximum heart rate by subtracting your age from 220. \n 
For example, if you're 45 years old, subtract 45 from 220 to get a maximum heart rate of 175. \n
This is the average maximum number of times your heart should beat per minute during exercise.
''')

st.subheader('Exercise Induced Angina')
st.write('''
Stable angina is usually triggered by physical activity. When you climb stairs, exercise or walk, your heart demands more blood, but narrowed arteries slow down blood flow.
''')

st.subheader('Oldpeak')
st.write('''
exercise relative to rest(oldpeak), the slope of the peak. \n
less than 2 is Low Level. \n
Between 2 to 5 is Middle. \n
And Greater than 5 is Terrible.
''')

st.subheader('Heart Rate Slope')
st.write("[Upsloping Heart Rate example image](...)")
st.write("[Flatsloping Heart Rate example image](...)")
st.write("[Downsloping Heart Rate example image](...)")

st.subheader('Number of Major Vessels Colored by Flourosopy')
st.write('''
The major blood vessels connected to your heart are the aorta, the superior vena cava, the inferior vena cava, the pulmonary artery (which takes oxygen-poor blood from the heart to the lungs where it is oxygenated), the pulmonary veins (which bring oxygen-rich blood from the lungs to the heart), and the coronary. \n
There are 4 major vessels for a normal people.
''')

st.subheader('Thallium Stress Result')
st.write('''
The results of Thallium Stress test will tell you about the flow of blood to your heart through your coronary arteries. An abnormal test result can reveal coronary blockages as well as damage from heart attacks. The test can also spot an enlarged heart and other heart complications. \n
*For Normal People*, choose normal.
''')

st.write("===========================")
st.write('''
##### Thanks for using my app. \n
##### May you be healthy and prosperous.
''')
