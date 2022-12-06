from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
qCount = 0

players = {
    "Player 1" : 0,
    "Player 2" : 0,
    "Current Player" : 1,
    "Waiting Player" : 2, 
    "Winning Player": -1000
}

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basketball.db'
 
# Creating an SQLAlchemy instance
# db = SQLAlchemy(app)

def get_db_connection():
    conn = sqlite3.connect('basketball.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    print("TEST")
    global qCount, players
    qCount = 0
    players["Player 1"] = 0
    players["Player 2"] = 0

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
lastAnswer = ""
@app.route('/local', methods =["GET", "POST"])
def local():
    conn = get_db_connection()
    global qCount
    global players
    global lastAnswer
    player = ""
    print(players["Player 1"])
    print(players["Player 2"])
    print(qCount)

    question, answer, qCount = GrabQuestion(conn)
    question_details = {
        'question' : question,
        'qCount' : qCount, 
        'answer' : answer
    }
    
    submitAnswer = False
    print("before submit: ", lastAnswer)    

    if(request.method == "POST"):
        print("made a request!")
        print("REQUEST PRINTING")
        print(request.form)
        
        guess = request.form.get("guess")
        otherGuess = request.form.get("radio").upper()
        #radio = request.form.get("radio").upper()
        #print("Radio selection is", radio)
        #beforeAnswer = lastAnswer 

        #HIGHER

        print("current player: " + str(players["Current Player"]))
        print("GUESS:", guess)
        print("ANSWER:", lastAnswer)
        print(type(guess), type(lastAnswer))
        '''P1 GUESS: 1; ANSWER: 600000; HIGHER'''
        if(players["Current Player"] == 1):
            if(float(guess) == float(lastAnswer)):
                print("Player 1 got EXACT answer")
                players["Player 1"] += 1
                player = "1"
        if(players["Current Player"] == 2):
            if(float(guess) == float(lastAnswer)):
                print("Player 2 got EXACT answer")
                players["Player 2"] += 1
                player = "2"
        if(float(guess) < float(lastAnswer)):
            if(otherGuess == "HIGHER"):
                if(players["Current Player"] == 1):
                    players["Player 2"] += 1
                    print("Increased player 2 count inside HIGHER block")
                    player = "2"
                else: 
                    players["Player 1"] += 1
                    print("Increased player 1 count inside HIGHER block (else)")
                    player = "1"
            else:
                if(players["Current Player"] == 1):
                    players["Player 1"] += 1
                    print("Increased player 1 count inside HIGHER block")
                    player = "1"
                else: 
                    players["Player 2"] += 1
                    print("Increased player 2 count inside HIGHER block (else)")
                    player = "2"
        #LOWER
        #'''P1 GUESS:4; ANSWER: 1; LOWER'''
        elif(float(guess) > float(lastAnswer)):
            if(otherGuess == "LOWER"):
                if(players["Current Player"] == 1):
                    players["Player 2"] += 1
                    print("Increased player 2 count inside LOWER block")
                    player = "2"

                else: 
                    players["Player 1"] += 1
                    print("Increased player 1 count inside LOWER block (else)")
                    player = "1"
            else:
                if(players["Current Player"] == 1):
                    players["Player 1"] += 1
                    print("Increased player 1 count inside LOWER block")
                    player = "1"
                else: 
                    players["Player 2"] += 1
                    print("Increased player 2 count inside LOWER block (else)")
                    player = "2"
        #print("previous answer", beforeAnswer)
        result_details = {
        'first_guess' : guess,
        'second_guess': otherGuess,
        "answer": lastAnswer,
        "winningPoint": player
        }
        lastAnswer = question_details["answer"]
        #lastAnswer = beforeAnswer
        print("Last answer is: ", lastAnswer)   #qCount += 1
       # print("question count should be ", qCount)
        submitAnswer = True
        if(qCount % 2 != 0):
            players["Current Player"] = 1
            players["Waiting Player"] = 2


        else:
            players["Current Player"] = 2
            players["Waiting Player"] = 1

        if(players["Player 1"] > 2):
            players["Winning Player"] = 1
            return render_template('gameOver.html', playerDetails = players)
        elif(players["Player 2"] > 2):
            players["Winning Player"] = 2
            return render_template('gameOver.html', playerDetails = players)
        return render_template('local.html', questionDetail=question_details, submitAnswer = submitAnswer, resultDetails=result_details, playerDetails = players)
        #return "Your guess was: " + guess + ". Other player guessed " + otherGuess + " TRUE ANSWER: " + answer


    if(qCount % 2 != 0):
        print("set curr player to 1!")
        players["Current Player"] = 1
        players["Waiting Player"] = 2


    else:
        print("set curr player to 2!", qCount)

        players["Current Player"] = 2
        players["Waiting Player"] = 1

    lastAnswer = question_details["answer"]
   
    print("rendered outside form: ", lastAnswer)
    return render_template('local.html', questionDetail=question_details, playerDetails = players)

@app.route("/gameOver")
def end_game():
    return render_template('gameOver.html')

def GrabQuestion(_conn):
    print("++++++++++++++++++++++++++++++++++")
    #print("Grab Question")
    # 20 random queries
    question = ""
    answer = ""
    global qCount
    qCount += 1

    cur=_conn.cursor()
    questionTypeSQL = "SELECT * FROM questionTypes ORDER BY RANDOM() LIMIT 2;"
    cur.execute(questionTypeSQL)
    questionType = cur.fetchall()
    print(questionType[0][1])
    questionSQL = """SELECT * 
                    FROM questions 
                    WHERE q_type = ?
                    ORDER BY RANDOM() LIMIT 1
                    """
    args = [questionType[0][1]] # question_type
    cur.execute(questionSQL, args)
    questionTuple = cur.fetchall()
    print(questionTuple)
    print("Question: "+ questionTuple[0][1])
    print("Stat: " + questionTuple[0][4])
    print(questionType[0][1])
    if questionType[0][1] == "stats":
        print("IS IN STATS BLOCK")
        statTuple = questionTuple[0][4].split()
        print(statTuple)
        print("Length of StatTuple: ", len(statTuple))  # length of 3 is for player stats such as PTS REB ETC.

        if len(statTuple) == 3:

            statType = statTuple[0] # PTS, REB, etc.
            print("FROM ", questionTuple[0][2])
            fullQuestionSQL = """
                        SELECT {}, {}
                        FROM {}
                        ORDER BY RANDOM()
                        """.format(statTuple[1], statTuple[2], questionTuple[0][2])
            cur.execute(fullQuestionSQL)
            fullQuestion = cur.fetchall()
            print(fullQuestion)
            question = (questionTuple[0][1].format(statType,fullQuestion[0][1]))
            answer = (str(fullQuestion[0][0]))
        elif len(statTuple) == 2:
            fullQuestionSQL = """
                        SELECT {}, {}
                        FROM {}
                        ORDER BY RANDOM() LIMIT 1
                        """.format(statTuple[0], statTuple[1], questionTuple[0][2])
            cur.execute(fullQuestionSQL)
            fullQuestion = cur.fetchall()
            question = (questionTuple[0][1].format(fullQuestion[0][0]))
            answer = (str(fullQuestion[0][1]))
        elif len(statTuple) == 1:
            fullQuestionSQL = """
                        SELECT {}
                        FROM {}
                        ORDER BY RANDOM() LIMIT 1
                        """.format(statTuple[0], questionTuple[0][2])
            cur.execute(fullQuestionSQL)
            fullQuestion = cur.fetchall()
            question = (questionTuple[0][1].format(fullQuestion[0][0]))
            answer = (str(fullQuestion[0][1]))
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
        question = (questionTuple[0][1].format(fullQuestion[0][0],fullQuestion[0][1]))
        answer = (str(fullQuestion[0][2]))
    elif questionType[0][1] == "team":
        print("IS IN TEAM")
        statTuple = questionTuple[0][4].split()
        print(statTuple)
        if len(statTuple) == 1:
            fullQuestionSQL = """
                        SELECT  {}
                        FROM {}
                        """.format(statTuple[0], questionTuple[0][2])
            cur.execute(fullQuestionSQL)
            fullQuestion = cur.fetchall()
            question = (questionTuple[0][1].format(fullQuestion[0][0]))
            answer = str(fullQuestion[0][0])
        else:
            fullQuestionSQL = """
                        SELECT  {}, {}
                        FROM {}
                        ORDER BY RANDOM() LIMIT 1
                """.format(statTuple[0], statTuple[1], questionTuple[0][2])
        
            cur.execute(fullQuestionSQL)
            fullQuestion = cur.fetchall()
            question = questionTuple[0][1].format(fullQuestion[0][0],fullQuestion[0][1])
            answer = str(fullQuestion[0][1])
    
    elif questionType[0][1] == "complex1":
            print("IS IN COMPLEX")
            statTuple = questionTuple[0][4].split()
            print(statTuple)
            statType = statTuple[0] # PTS, REB, etc.
            tables = questionTuple[0][3].split()
            print("tables: ", tables)
            sqlInputs = questionTuple[0][4].split()
            fullQuestionSQL = """
                        SELECT COUNT(*)
                        FROM {}
                        JOIN {} ON {}.{} = {}.{}
                        WHERE {} > ?
                        AND {} > ?
                        """.format(tables[0], tables[1], tables[0], sqlInputs[2], tables[1], sqlInputs[3], sqlInputs[4], sqlInputs[5])
            print(fullQuestionSQL)
            arguments = [sqlInputs[1], sqlInputs[0]]
            cur.execute(fullQuestionSQL, arguments)
            fullQuestion = cur.fetchall()
            question = (questionTuple[0][1].format(sqlInputs[1]))
            answer =(str(fullQuestion[0][0]))

    elif questionType[0][1] == "complex2":
        print("IS IN COMPLEX")
        statTuple = questionTuple[0][4].split()
        print(statTuple)
        statType = statTuple[0] # PTS, REB, etc.
        tables = questionTuple[0][3].split()
        print("tables: ", tables)
        sqlInputs = questionTuple[0][4].split()
        fullQuestionSQL = """
                    SELECT COUNT(*)
                    FROM {}
                    JOIN {} ON {}.{} = {}.{}
                    JOIN {} ON {}.{} = {}.{}
                    WHERE {} > ?
                    AND {} > ?
                    AND {} > ?
                    """.format(tables[0], tables[1], tables[0], sqlInputs[3], tables[1], sqlInputs[4], tables[2], tables[2], sqlInputs[5], tables[1], sqlInputs[4],sqlInputs[4], sqlInputs[5], sqlInputs[6])
        arguments = [sqlInputs[1], sqlInputs[0], sqlInputs[2]]
        print(fullQuestionSQL)
        cur.execute(fullQuestionSQL, arguments)
        fullQuestion = cur.fetchall()
        question = (questionTuple[0][1].format(sqlInputs[1], sqlInputs[2]))
        answer = (str(fullQuestion[0][0]))


    return question , answer, qCount
    ##print("Answer: " + str(fullQuestion[0][2]))


