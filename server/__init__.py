from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys
from .config import config

db = SQLAlchemy()
sk = os.getenv("SECRET_KEY")


def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    return app


__all__ = ['backend', 'controllers', 'models', 'routes']

# To stop generating __py* folders in workspace
sys.dont_write_bytecode = True
