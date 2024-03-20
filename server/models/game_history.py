from sqlalchemy import JSON, inspect, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .game import Game

from .. import db


class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, ForeignKey('game.id'), nullable=False)
    round_score = db.Column(JSON)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now)

    game = relationship("Game", backref="game_entries1")

    # How to serialize SqlAlchemy SQLite Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.name


# Game.game_history = relationship("GameHistory", back_populates="game")
