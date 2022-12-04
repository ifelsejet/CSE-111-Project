from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basketball.db'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

def get_db_connection():
    conn = sqlite3.connect('basketball.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cur= conn.cursor()
    questionTypeSQL = "SELECT * FROM questionTypes ORDER BY RANDOM() LIMIT 2;"
    cur.execute(questionTypeSQL)
    questionType = cur.fetchall()
    print(str(questionType[0][1]))
    return render_template('home.html')
@app.route("/createRoom")
def createRoom():
    return render_template('create.html')
@app.route("/joinRoom")
def joinRoom():
    return render_template('join.html')
@app.route("/lobby")
def hello_lobby():
    return "<p>Welcome to Lobby</p>"

@app.route("/game")
def hello_game():
    return render_template('game.html')