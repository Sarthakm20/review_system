from flask import Flask
from flask_pymongo import PyMongo
import os

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/movies_db")
    mongo.init_app(app)
    
    from .views import app as views_blueprint
    app.register_blueprint(views_blueprint)
    
    return app
