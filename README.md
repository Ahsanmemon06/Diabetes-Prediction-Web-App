```markdown
# 🩺 DiaGuard AI — Diabetes Diagnostic Web Application

DiaGuard AI is an end-to-end Machine Learning web application designed for early clinical risk assessment of diabetes. The system leverages an optimized **XGBoost Classifier** wrapped inside an inference pipeline with **Scikit-Learn**, served via a lightweight **Flask** web backend and a modern responsive dashboard interface.

---

## 📌 Project Overview

* **Objective:** Predict diabetic risk probability based on critical patient vitals and clinical indicators.
* **Core Classifier:** XGBoost (Extreme Gradient Boosting).
* **Preprocessing:** Feature standardization using `StandardScaler`.
* **Inference Strategy:** Key feature extraction based on tree-based feature importance analysis (Age, BMI, HbA1c, Blood Glucose, Hypertension) with robust backend imputation for neutral demographic defaults.
* **Interface:** Responsive dark-mode dashboard with real-time risk scoring and calibrated diagnostic indicators.

---

## 🚀 Key Features

* **Calibrated Risk Probability:** Computes continuous confidence percentages (`predict_proba`) rather than binary labels only.
* **Clinically Prioritized Inputs:** Avoids manual entry of low-impact features by automating sensible defaults, minimizing user fatigue while preserving model accuracy.
* **Clean MVC Layout:** Strict separation between static assets, Jinja HTML templates, and backend routing.

---

## 🗂️ Project Directory Structure

```text
Diabetes-Prediction-Web-App/
│
├── Notebook/
│   └── Diabetes_prediction_model.ipynb   # Exploratory Data Analysis, Training & Validation
│
├── templates/
│   └── index.html                        # Dashboard User Interface (Jinja2)
│
├── static/
│   └── style.css                         # Custom UI Design & Dynamic Risk Bars
│
├── app.py                                # Flask Routing & Preprocessing Pipeline
├── Diabetes_model.pkl                    # Serialized Machine Learning Model
├── requirements.txt                      # Project Dependencies
├── .gitignore                            # Environment & Cache Exclusion Rules
└── README.md                             # Documentation

```

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.10+
* **Machine Learning:** XGBoost, Scikit-learn, NumPy, Pandas
* **Model Serialization:** Joblib
* **Web Framework:** Flask (Jinja2 Templates)
* **Frontend:** Semantic HTML5, Custom Modern CSS3

---

## ⚙️ Local Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/Ahsanmemon06/Diabetes-Prediction-Web-App.git](https://github.com/Ahsanmemon06/Diabetes-Prediction-Web-App.git)
cd Diabetes-Prediction-Web-App

```

### 2. Set Up a Virtual Environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Launch the Web Application

```bash
python app.py

```

Open your browser and navigate to:

```text
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

```

---

## 📊 Model Evaluation Reference Ranges

| Vital Metric | Normal Range | Elevated / Diabetic Threshold |
| --- | --- | --- |
| **Fasting Blood Glucose** | 70 – 99 mg/dL | ≥ 126 mg/dL |
| **HbA1c Level** | < 5.7% | ≥ 6.5% |
| **BMI** | 18.5 – 24.9 | ≥ 30.0 (Obesity Range) |

---

## 👨‍💻 Author

* **Ahsan Ali Memon** — [GitHub Profile](https://www.google.com/search?q=https://github.com/Ahsanmemon06)

---

*Disclaimer: This web application is developed for educational and portfolio demonstration purposes and should not be used as a replacement for certified medical advice.*

```

---

### Terminal Commands (README Upload Karne Ke Liye)

File paste karne ke baad apne PowerShell terminal par yeh commands chala dein:

```powershell
git add README.md
git commit -m "docs: add project README"
git push origin main

```
