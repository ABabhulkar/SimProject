from sqlalchemy import inspect, JSON
from datetime import datetime
from flask_validator import ValidateEmail, ValidateString
from sqlalchemy.orm import validates
from enum import Enum

from .. import db  # from __init__.py


class UserRole(Enum):
    admin = 'admin'
    user = 'user'


class User(db.Model):
    # Auto Generated Fields:
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)

    # Input by User Fields:
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(10), default='user')
    mdeta = db.Column(JSON)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now)

    # Validations => https://flask-validator.readthedocs.io/en/latest/index.html
    @classmethod
    def __declare_last__(cls):
        ValidateEmail(User.email, True, True, throw_exception=True)
        ValidateString(User.username, True, True, "The username type must be string")

    # Set an empty string to null for username field => https://stackoverflow.com/a/57294872
    @validates('username')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '':
            return "def"
        else:
            return value

    # How to serialize SqlAlchemy SQLite Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.email
