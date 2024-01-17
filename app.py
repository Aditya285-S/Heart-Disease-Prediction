import streamlit as st
import numpy as np
from model_training import RFC_model
import pandas as pd

st.set_page_config(page_title="Heart Disease Prediction")

def provide_advice(has_heart_disease):
    if has_heart_disease:
        heart_disease_advice = [
            "Follow a heart-healthy diet low in saturated and trans fats."
             "Include a variety of fruits and vegetables in your daily meals."
             "Limit the intake of processed and high-sugar foods.",

            "Engage in regular physical activity to maintain a healthy weight."
             "Incorporate both aerobic exercises and strength training into your routine."
             "Consult with a fitness professional for a personalized exercise plan.",

            "Quit smoking and avoid exposure to secondhand smoke."
             "Explore smoking cessation programs and support groups."
             "Seek assistance from healthcare professionals for effective strategies.",

            "Manage stress through relaxation techniques or hobbies."
             "Practice mindfulness meditation or deep breathing exercises."
             "Find activities that bring joy and relaxation, such as hobbies or hobbies.",

            "Take prescribed medications as directed by your healthcare provider."
             "Understand the purpose and potential side effects of your medications."
             "Keep a medication log and adhere to the prescribed schedule.",

            "Limit alcohol intake to moderate levels."
             "Know the recommended limits for alcohol consumption."
             "Consider non-alcoholic alternatives during social events.",

            "Monitor blood pressure and cholesterol levels regularly."
             "Use a home blood pressure monitor and cholesterol test kit if recommended."
             "Share your monitoring results with your healthcare provider.",

            "Get regular check-ups and screenings for heart health."
             "Schedule routine health check-ups with your primary care physician."
             "Discuss the frequency of cardiovascular screenings based on your health profile.",

            "Stay hydrated by drinking an adequate amount of water."
             "Consume water throughout the day to maintain hydration."
             "Limit the intake of sugary beverages and caffeinated drinks.",

            "Consider joining a cardiac rehabilitation program if recommended by your doctor."
             "Participate in structured exercise programs designed for heart health."
             "Engage in education sessions to learn more about managing heart disease."
        ]
        advice = np.random.choice(heart_disease_advice)
    else:
        heart_health_advice = [
            "Adopt a heart-healthy diet rich in fruits, vegetables, and whole grains."
             "Choose whole grains over refined grains for better nutrition."
             "Include sources of lean protein, such as fish, poultry, and legumes.",

            "Engage in regular physical activity to promote cardiovascular health."
             "Find enjoyable physical activities and incorporate them into your routine."
             "Aim for at least 150 minutes of moderate-intensity exercise per week.",

            "Quit smoking or avoid starting if you don't smoke."
             "Seek support from friends, family, or smoking cessation programs."
             "Use nicotine replacement therapies under the guidance of healthcare professionals.",

            "Maintain a healthy weight through balanced nutrition and exercise."
             "Create a well-balanced meal plan with the help of a nutritionist."
             "Set realistic weight management goals and track your progress.",

            "Manage stress through relaxation techniques and self-care."
             "Practice stress-reducing techniques, such as yoga or deep breathing."
             "Take breaks and engage in activities that bring relaxation.",

            "Limit alcohol intake to moderate levels or avoid excessive drinking."
             "Know the recommended limits for alcohol consumption."
             "Be mindful of the alcohol content in beverages and practice moderation.",

            "Get regular check-ups to monitor your overall health."
             "Schedule annual health check-ups with your primary care physician."
             "Discuss any concerns or changes in your health with your healthcare provider.",

            "Know your family history and discuss it with your healthcare provider."
             "Keep a record of your family's health history."
             "Share this information with your healthcare team for personalized care.",

            "Monitor and manage conditions like diabetes that can affect heart health."
             "Adhere to your diabetes management plan, including medication and lifestyle changes."
             "Regularly monitor blood sugar levels and seek guidance from healthcare professionals.",

            "Stay informed about heart health and make informed lifestyle choices."
             "Stay updated on the latest research and guidelines for heart health."
             "Make informed decisions about your diet, exercise, and overall lifestyle."
        ]
        advice = np.random.choice(heart_health_advice)

    return advice

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:20px;margin-bottom:30px">
    <h2 style="color:black;text-align:center"> Heart Disease Prediction</h2>
    </div>
    """

    df = pd.read_csv('heart.csv')

    st.markdown(html_temp,unsafe_allow_html=True)


    age = st.slider("Age", 18, 100)
    sex = st.radio("Gender", ('Male', 'Female'))

    if sex == 'Male':
        sex_value = 0
        sex = 'M'
    else:
        sex_value = 1
        sex = 'F'
    

    chest_pain = st.selectbox("Chest Pain (CP)",('Typical Angina (TA)','Atypical Angina (ATA)','Not Anginal Pain (NAP)','Asymptomatic (Asy)'),index=None,placeholder="Select the CP type...")

    if chest_pain == 'Typical Angina (TA)':
        cp = 3
        chest_pain = 'TA'
    elif chest_pain == 'Atypical Angina (ATA)':
        cp = 0
        chest_pain = 'ATA'
    elif chest_pain == 'Not Anginal Pain (NAP)':
        cp = 1
        chest_pain = 'NAP'
    else:
        cp = 2
        chest_pain = 'ASY'

    trestbps = st.slider("Blood Pressure", 70, 200)
    chol = st.slider("Serum Cholesterol", 100, 580)
    fbs = st.radio("Fasting blood sugar > 120 mg/dl", ('Yes', 'No'))

    if fbs== 'Yes':
        fbs_value = 1
    else:
        fbs_value = 0


    restecg = st.selectbox("Electrocardiographic Result",('Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'),index=None,placeholder="Select resting electrocardiographic results...")

    if restecg == 'Normal':
        restecg_value = 0
        restecg = 'Normal'
    elif restecg == 'ST-T wave abnormality':
        restecg_value = 1
        restecg = 'ST'
    else:
        restecg_value = 2
        restecg = 'LVH'


    thalach = st.slider("Maximum Heart Rate", 70, 200)
    exang = st.radio("Exercise induced angina", ('Yes', 'No'))

    if exang== 'Yes':
        exang_value = 1
        exang = 'Y'
    else:
        exang_value = 0
        exang = 'N'


    oldpeak = st.slider("Enter oldpeak", -3.0, 7.0)
    slope = st.selectbox("Slope of peak",('Up', 'Flat', 'Down'),index=None,placeholder="Select slope of the peak exercise ST segment...")

    if slope == 'Up':
        slope_value = 0
        slope = 'Up'
    elif slope == 'Flat':
        slope_value = 1
        slope = 'Flat'
    else:
        slope_value = 2
        slope = 'Down'


    input_data = (age, sex_value, cp, trestbps, chol, fbs_value, restecg_value, thalach, exang_value, oldpeak, slope_value)

    if st.button('Predict'):
        input_data_reshaped = np.asarray(input_data).reshape(1, -1)
        prediction = RFC_model.predict(input_data_reshaped)

        new_data = {'Age': age, 'Sex': sex, 'ChestPainType': chest_pain, 'RestingBP': trestbps, 'Cholesterol': chol, 'FastingBS': fbs_value, 'RestingECG': restecg, 'MaxHR': thalach, 'ExerciseAngina': exang, 'Oldpeak': oldpeak, 'ST_Slope': slope, 'HeartDisease': prediction[0]}
        new_df = pd.DataFrame([new_data])  # Create a new DataFrame with a single row

        df = pd.concat([df, new_df], ignore_index=True)

        df.to_csv('heart.csv', index=False)

        if prediction[0] == 0:
            st.success('The person does not have heart disease.')
            advice = provide_advice(has_heart_disease=False)
            st.info(f"Preventive Advice: {advice}")
        else:
            st.error('The person has heart disease.')
            advice = provide_advice(has_heart_disease=True)
            st.info(f"Management Advice: {advice}")

if __name__ == "__main__":
    main()