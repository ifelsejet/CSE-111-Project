from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/createRoom")
def createRoom():
    return render_template('create.html')
@app.route("/lobby")
def hello_lobby():
    return "<p>Welcome to Lobby</p>"

@app.route("/game")
def hello_game():
    return "<p>Welcome to the game</p>"