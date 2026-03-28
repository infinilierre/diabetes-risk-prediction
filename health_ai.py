"""Flask API: ana sayfa (index.html) + /predict — Chrome'da http://127.0.0.1:5000/ kullanın."""
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent
# Model eğitimindeki sütun sırasıyla aynı olmalı
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
        row = {col: float(data[col]) for col in FEATURE_COLUMNS}
        query = pd.DataFrame([row], columns=FEATURE_COLUMNS)
        prediction_prob = model.predict_proba(query)[0][1]

        return jsonify(
            {
                "status": "success",
                "risk_score": round(float(prediction_prob) * 100, 2),
                "interpretation": "High Risk" if prediction_prob > 0.5 else "Low Risk",
            }
        )
    except KeyError as e:
        return jsonify({"status": "error", "message": f"Eksik alan: {e}"}), 400
    except (ValueError, TypeError) as e:
        return jsonify(
            {"status": "error", "message": f"Geçersiz veya sayısal olmayan değer: {e}"}
        ), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)