import yaml
from .models.game_entries import GameEntries
from .models.game import Game
from .models.user import User
from . import db
from sqlalchemy import text

from .app import app


def truncate_tables():
    db.session.execute(text("DELETE FROM game_entries"))
    db.session.execute(text("DELETE FROM user"))
    db.session.execute(text("DELETE FROM game"))
    db.session.commit()


def load_data_from_yaml(filename):
    truncate_tables()
    with open(filename, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

        for model_data in data:
            model_class = model_data['model']
            items = model_data['items']

            if model_class == 'user.User':
                for item in items:
                    u = User(**item)
                    db.session.add(u)

            elif model_class == 'game.Game':
                for item in items:
                    g = Game(**item)
                    db.session.add(g)

            # game_entry = GameEntries(user_id=2,game_id=1,shortname="rtd",filepath="gfghhgfhg",is_valid=True)
            # db.session.add(game_entry)
            elif model_class == 'game_entries.GameEntries':
                for item in items:
                    game_entry = GameEntries(**item)
                    db.session.add(game_entry)

        db.session.commit()


@app.cli.command('load_db')
def load_command():
    """Here info that will be shown in flask --help"""
    print("hh")
    load_data_from_yaml("server/test/resources/fixtures.yaml")
