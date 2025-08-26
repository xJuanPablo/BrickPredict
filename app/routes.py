import os
from flask import Blueprint, render_template, request
import joblib

bp = Blueprint("main", __name__)

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    
    if request.method == "POST":
        sqft = request.form.get("sqft")
        try:
            sqft_val = float(sqft)
            prediction = model.predict([[sqft_val]])[0]
        except ValueError:
            prediction = "Invalid input. Please enter a number."
        
    return render_template("predict.html", prediction=prediction)
