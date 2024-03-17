import os

# App Initialization
from . import create_app  # from __init__ file

app = create_app(os.getenv("CONFIG_MODE"))
app.app_context().push()

@app.route('/')
def home():
    return 'Welcome to homes'


# Applications Routes
from .routes import routes

if __name__ == "__main__":
    app.run()
