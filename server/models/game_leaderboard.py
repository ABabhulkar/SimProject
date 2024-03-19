from sqlalchemy import JSON, inspect
from datetime import datetime

from .. import db


class GameLeaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(JSON)
    game = db.Column(JSON)
    ranking = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now)

    # How to serialize SqlAlchemy SQLite Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.name
