from flask import Blueprint, jsonify, render_template, request

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return jsonify({"message": "welcome to Brick Predict"})

@bp.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    
    if request.method == "POST":
        sqft = request.form.get("sqft")
        if sqft and sqft.isdigit:
            sqft = int(sqft)
            prediction = sqft * 200
        else:
            prediction = "Invalid input. Please enter a number."
        
    return render_template("predict.html", prediction = prediction)