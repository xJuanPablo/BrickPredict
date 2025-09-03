import os
from flask import Blueprint, render_template, request, jsonify
import joblib

bp = Blueprint("main", __name__)

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)


@bp.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    
    if request.method == "POST":
        try:
            sqft_val = float(request.form.get("sqft"))
            bedrooms = float(request.form.get("bedrooms"))
            bathrooms = float(request.form.get("bathrooms"))
            condition = float(request.form.get("condition"))
            prediction = model.predict([[sqft_val, bedrooms, bathrooms, condition]])[0]
            return jsonify({"prediction": prediction})
        except ValueError:
            prediction = "Invalid input. Please enter a number."
        
    return render_template("predict.html", prediction=prediction)
