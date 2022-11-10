from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/lobby")
def hello_lobby():
    return "<p>Welcome to Lobby</p>"

@app.route("/game")
def hello_game():
    return "<p>Welcome to the game</p>"