from flask import Flask
import os
import sys

app = Flask(__name__)
# TODO: replace this with proper key
app.config['SECRET_KEY'] = os.urandom(24)
# app.config.from_object('config')

__all__ = ['src', 'backend', 'controller']

# To stop generating __py* folders in workspace
sys.dont_write_bytecode = True
