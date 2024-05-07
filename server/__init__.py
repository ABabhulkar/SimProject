from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
import sys
from .config import config
from flask_cors import CORS

db = SQLAlchemy()
sk = os.getenv("SECRET_KEY")


def create_app(config_mode):
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    app.config.from_object(config[config_mode])
    return app

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


__all__ = ['backend', 'controllers', 'models', 'routes', 'test']

# To stop generating __py* folders in workspace
sys.dont_write_bytecode = True
