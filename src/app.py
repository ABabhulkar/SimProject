from src import app


@app.route("/")
def home():
    return "Hello, this is a Flask Microservices"
