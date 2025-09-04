import os
from flask import Blueprint, request, jsonify
import joblib

bp = Blueprint("main", __name__)

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)


@bp.route("/predict", methods=["POST"])
def predict():
    prediction = None

    try:
        data = request.get_json()
        sqft_val = float(data.get("sqft"))
        bedrooms = float(data.get("bedrooms"))
        bathrooms = float(data.get("bathrooms"))
        condition = float(data.get("condition"))
        prediction = model.predict([[sqft_val, bedrooms, bathrooms, condition]])[0]
        return jsonify({"prediction": prediction})
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input. Please provide numeric values for sqft, bedrooms, bathrooms, and condition."}), 400
