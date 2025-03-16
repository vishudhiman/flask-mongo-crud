from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.database import mongo
from app.routes import api_blueprint

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    mongo.init_app(app)
    CORS(app)

    app.register_blueprint(api_blueprint) 
    return app
