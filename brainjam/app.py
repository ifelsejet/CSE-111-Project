from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basketball.db'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Models
class Question_Types(db.Model):
    # qt_id : Field which stores unique id for every row in
    # database table.
    # qt_type: Used to store the question type
   
    qt_id = db.Column(db.Integer, primary_key=True)
    qt_type = db.Column(db.String(20), unique=False, nullable=False)
   
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Question Types : {self.qt_type}"
 

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
    return render_template('game.html')