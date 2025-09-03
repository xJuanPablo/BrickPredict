from flask import Flask
from flack_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app)
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app