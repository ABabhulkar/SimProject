from sqlalchemy import JSON, inspect
from datetime import datetime

from .. import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    result_metric = db.Column(JSON, nullable=False)
    other = db.Column(JSON)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now)

    # How to serialize SqlAlchemy SQLite Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.name
