from pathlib import Path
import joblib
import pandas as pd
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent
FEATURE_COLUMNS = ["glucose", "bmi", "age"]

app = Flask(__name__, static_folder=str(BASE_DIR))
CORS(app)

model = joblib.load(BASE_DIR / "diabetes_model.pkl")

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True) or {}
        gender = data.get('gender', 'female')
        
        glucose = float(data.get('glucose', 100))
        bmi = float(data.get('bmi', 25))
        age = int(data.get('age', 25))

        row = {"glucose": glucose, "bmi": bmi, "age": age}
        query = pd.DataFrame([row], columns=FEATURE_COLUMNS)
        ml_prob = model.predict_proba(query)[0][1]

        clinical_risk = (bmi * 0.10) + (glucose * 0.03) + (age * 0.02)
        final_score = (ml_prob * 0.6) + ((clinical_risk / 20) * 0.4)

        if gender == 'male':
            final_score *= 1.05

        return jsonify({
            "status": "success",
            "risk_score": round(min(final_score * 100, 100), 2),
            "interpretation": "High Risk" if final_score > 0.45 else "Low Risk",
            "clinical_data": {
                "bmi_factor": "High Impact" if bmi >= 30 else "Normal",
                "age_shield": "Active" if age < 45 else "Risk Factor"
            },
            "metadata": {"gender_applied": gender}
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    