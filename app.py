from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Model load karein
model = joblib.load('Diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # 1. User se sirf 5 main inputs capture karein
        age = float(request.form['age'])
        bmi = float(request.form['bmi'])
        hba1c = float(request.form['HbA1c_level'])
        glucose = float(request.form['blood_glucose_level'])
        hypertension = int(request.form['hypertension'])

        # 2. Jin features ki importance close to zero thi, unke sensible defaults
        gender = 0                  # Default: Female/Neutral (weight lagbhag 0 hai)
        heart_disease = 0           # Default: No
        smoking_current = 0
        smoking_ever = 0
        smoking_former = 0
        smoking_never = 1           # Default: Non-smoker
        smoking_not_current = 0

        # 3. Model ke exact 12 columns ka dataframe banayein
        patient_data = pd.DataFrame([{
            'gender': gender,
            'age': age,
            'hypertension': hypertension,
            'heart_disease': heart_disease,
            'bmi': bmi,
            'HbA1c_level': hba1c,
            'blood_glucose_level': glucose,
            'smoking_history_current': smoking_current,
            'smoking_history_ever': smoking_ever,
            'smoking_history_former': smoking_former,
            'smoking_history_never': smoking_never,
            'smoking_history_not current': smoking_not_current
        }])

        # 4. Predict karein
        prediction = model.predict(patient_data)[0]
        probability = model.predict_proba(patient_data)[0][1] * 100

        result = "Diabetic" if prediction == 1 else "Non-Diabetic"
        risk_score = round(probability, 2)

        return render_template('index.html', prediction_text=result, risk_text=risk_score)

if __name__ == '__main__':
    app.run(debug=True)