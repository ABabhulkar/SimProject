from sqlalchemy import JSON, inspect, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .game import Game
from .user import User

from .. import db


class GameEntries(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    game_id = db.Column(db.Integer, ForeignKey('game.id'), nullable=False)
    shortname = db.Column(db.String(50), nullable=False)
    filepath = db.Column(db.String, nullable=False)
    is_valid = db.Column(db.Boolean, default=False, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now)

    user = relationship("User", back_populates="game_entries")
    game = relationship("Game", back_populates="game_entries")

    # How to serialize SqlAlchemy SQLite Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.name


User.game_entries = relationship("GameEntries", back_populates="User")
Game.game_entries = relationship("GameEntries", back_populates="Game")
