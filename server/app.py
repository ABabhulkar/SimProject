import os
# App Initialization
from . import create_app, init_db  # from __init__ file
from .config import config

app = create_app(os.getenv("CONFIG_MODE"))
app.app_context().push()


@app.route('/')
def home():
    return 'Welcome to homes'


# Applications Routes
from .routes import routes, core
from .models import *
from . import command

init_db(app)

if __name__ == "__main__":
    app.run()
