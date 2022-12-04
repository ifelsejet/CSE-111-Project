from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basketball.db'
 
# Creating an SQLAlchemy instance
# db = SQLAlchemy(app)

def get_db_connection():
    conn = sqlite3.connect('brainjam/basketball.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cur= conn.cursor()
    questionTypeSQL = "SELECT * FROM 'questionTypes' ORDER BY RANDOM() LIMIT 2;"
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

@app.route('/local')
def local():
    conn = get_db_connection()
    GrabQuestion(conn)
    return render_template('local.html')

@app.route("/game")
def hello_game():
    return render_template('game.html')

def GrabQuestion(_conn):
    print("++++++++++++++++++++++++++++++++++")
    #print("Grab Question")
    # 20 random queries

    cur=_conn.cursor()
    questionTypeSQL = "SELECT * FROM questionTypes ORDER BY RANDOM() LIMIT 2;"
    cur.execute(questionTypeSQL)
    questionType = cur.fetchall()
    print(questionType[0][1])
    questionSQL = """SELECT * 
                    FROM questions 
                    WHERE q_type = '{}'
                    """.format(questionType[0][1])
    cur.execute(questionSQL)
    questionTuple = cur.fetchall()
    print("Question: "+ questionTuple[0][1])
    print("Stat: " + questionTuple[0][4])
    print(questionType[0][1])
    if questionType[0][1] == "stats":
        print("IS IN STATS BLOCK")
        statTuple = questionTuple[0][4].split()
        statType = statTuple[0] # PTS, REB, etc.
        fullQuestionSQL = """
                    SELECT {}, {}
                    FROM {}
                    ORDER BY RANDOM() LIMIT 1
                    """.format(statTuple[1], statTuple[2], questionTuple[0][2])
        cur.execute(fullQuestionSQL)
        fullQuestion = cur.fetchall()
        print(questionTuple[0][1].format(statType,fullQuestion[0][0]))
        print("Answer: " + str(fullQuestion[0][1]))
    elif questionType[0][1] == "payroll":
        print("IS IN PAYROLL")
        statTuple = questionTuple[0][4].split()
        fullQuestionSQL = """
                    SELECT {}, {}, {}
                    FROM {}
                    ORDER BY RANDOM() LIMIT 1
        """.format(statTuple[0], statTuple[1], statTuple[2], questionTuple[0][2])
    
        cur.execute(fullQuestionSQL)
        fullQuestion = cur.fetchall()
        print(questionTuple[0][1].format(fullQuestion[0][0],fullQuestion[0][1]))
        print("Answer: " + str(fullQuestion[0][2]))
    elif questionType[0][1] == "team":
        print("IS IN TEAM")
        statTuple = questionTuple[0][4].split()
        print(statTuple)
        fullQuestionSQL = """
                    SELECT  {}, {}
                    FROM {}
                    ORDER BY RANDOM() LIMIT 1
        """.format(statTuple[0], statTuple[1], questionTuple[0][2])
    
        cur.execute(fullQuestionSQL)
        fullQuestion = cur.fetchall()
        print(questionTuple[0][1].format(fullQuestion[0][0],fullQuestion[0][1]))
        print("Answer: " + str(fullQuestion[0][1]))
    ##print("Answer: " + str(fullQuestion[0][2]))