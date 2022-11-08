import sqlite3
import csv
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createPlayerTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        # w_warehousekey decimal(9,0) not null,
        #             w_name char(100) not null,
        #             w_capacity decimal(6,0) not null,
        #             w_suppkey decimal(9,0) not null,
        #             w_nationkey decimal(2,0) not null
        sql = """CREATE TABLE player (
                    p_id decimal(9,0) not null,
                    p_name TEXT not null,
                    p_draftYear decimal(6,0) not null,
                    p_draftpos decimal(9,0) not null,
                    p_games decimal(2,0) not null,
                    p_stats decimal(9,0) not null)"""

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createStatsTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        # w_warehousekey decimal(9,0) not null,
        #             w_name char(100) not null,
        #             w_capacity decimal(6,0) not null,
        #             w_suppkey decimal(9,0) not null,
        #             w_nationkey decimal(2,0) not null
        sql = """CREATE TABLE stats (
                    s_id decimal(9,0) not null,
                    s_category TEXT not null,
                    s_type TEXT not null,
                    s_answer TEXT not null)"""

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createQuestionsTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        # w_warehousekey decimal(9,0) not null,
        #             w_name char(100) not null,
        #             w_capacity decimal(6,0) not null,
        #             w_suppkey decimal(9,0) not null,
        #             w_nationkey decimal(2,0) not null
        sql = """CREATE TABLE questions (
                    q_id decimal(9,0) not null,
                    q_question TEXT not null,
                    q_type TEXT not null,
                    q_category TEXT not null,
                    q_stat TEXT not null)"""

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createQuestionTypesTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        # w_warehousekey decimal(9,0) not null,
        #             w_name char(100) not null,
        #             w_capacity decimal(6,0) not null,
        #             w_suppkey decimal(9,0) not null,
        #             w_nationkey decimal(2,0) not null
        sql = """CREATE TABLE questionTypes (
                    qt_id decimal(9,0) not null,
                    qt_type char(100) not null)"""

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createTeamTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        # w_warehousekey decimal(9,0) not null,
        #             w_name char(100) not null,
        #             w_capacity decimal(6,0) not null,
        #             w_suppkey decimal(9,0) not null,
        #             w_nationkey decimal(2,0) not null
        sql = """CREATE TABLE team (
                    t_id decimal(9,0) not null,
                    t_name char(100) not null,
                    t_yearFounded decimal(6,0) not null,
                    t_numChampionships decimal(9,0) not null)"""

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createPayrollTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        # w_warehousekey decimal(9,0) not null,
        #             w_name char(100) not null,
        #             w_capacity decimal(6,0) not null,
        #             w_suppkey decimal(9,0) not null,
        #             w_nationkey decimal(2,0) not null
        sql = """CREATE TABLE payroll (
                    rank decimal(6,0) not null,
                    player_name TEXT not null,
                    position TEXT not null,
                    team TEXT not null,
                    player_salary decimal(9,0) not null,
                    pl_year decimal(6,0) not null)"""

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def populatePlayerTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate tables")
    cur=_conn.cursor()
    file = open('data/players.csv')
 
    # Reading the contents of the
    # players.csv file
    contents = csv.reader(file)
 
    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO player VALUES(?, ?, ?, ?)"
 
    # Importing the contents of the file
    # into our person table
    cur.executemany(insert_records, contents)
    print("++++++++++++++++++++++++++++++++++")

def populateTeamTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Team Table")
    cur=_conn.cursor()
    # Opening the person-records.csv file
    file = open('data/NBA_team_table.csv')
 
    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)
 
    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO team VALUES(?, ?, ?, ?)"
 
    # Importing the contents of the file
    # into our person table
    cur.executemany(insert_records, contents)
    print("++++++++++++++++++++++++++++++++++")

def populateStatsTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate tables")
    cur=_conn.cursor()

    cur.execute("INSERT INTO player VALUES ({},'{}',{},{},{},{})".format(1,'Lebron James', 2007, 1, 5000, 1))
    cur.execute("INSERT INTO player VALUES ({},'{}',{},{},{},{})".format(2,'Steph Curry', 2012, 1, 4210, 2))
    cur.execute("INSERT INTO player VALUES ({},'{}',{},{},{},{})".format(3,'Kyrie Irving', 2010, 1, 4120, 3))
    cur.execute("INSERT INTO player VALUES ({},'{}',{},{},{},{})".format(4,'Anthony Davis', 2014, 22, 3200, 4))
    cur.execute("INSERT INTO player VALUES ({},'{}',{},{},{},{})".format(5,'James Harden', 2008, 3, 4200, 5))
    cur.execute("INSERT INTO player VALUES ({},'{}',{},{},{},{})".format(6,'Russell Westbrook', 2008, 1, 3200, 6))
    counter=1
    print("++++++++++++++++++++++++++++++++++")

def populateQuestionsTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate tables")
    cur=_conn.cursor()
    # Opening the person-records.csv file
    file = open('data/questions.csv')
 
    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)
 
    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO questions VALUES(?, ?, ?, ?, ?)"
 
    # Importing the contents of the file
    # into our person table
    cur.executemany(insert_records, contents)
    print("++++++++++++++++++++++++++++++++++")

def populatePayrollTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Payroll tables")
    cur=_conn.cursor()
        # Opening the person-records.csv file
    file = open('data/NBA-salaries.csv')
 
    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)
 
    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO payroll VALUES(?, ?, ?, ?, ?, ?)"
 
    # Importing the contents of the file
    # into our person table
    cur.executemany(insert_records, contents)
    print("++++++++++++++++++++++++++++++++++")

def populateQuestionTypesTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate tables")
    cur=_conn.cursor()
    # Opening the person-records.csv file
    file = open('data/questionTypes.csv')
 
    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)
 
    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO questionTypes VALUES(?, ?)"
 
    # Importing the contents of the file
    # into our person table
    cur.executemany(insert_records, contents)
    print("++++++++++++++++++++++++++++++++++")

def dropTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    _conn.execute("BEGIN")
    try:
        playerSql = "DROP TABLE player"
        questionsSql = "DROP TABLE questions"
        questionTypesSql = "DROP TABLE questionTypes"
        teamSql = "DROP TABLE team"
        payrollSql = "DROP TABLE payroll"
        statsSql = "DROP TABLE stats"

        _conn.execute(playerSql)
        _conn.execute(questionsSql)
        _conn.execute(questionTypesSql)
        _conn.execute(teamSql)
        _conn.execute(payrollSql)
        _conn.execute(statsSql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
        #_conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def GrabQuestion(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Grab Question")
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
    stat = questionTuple[0][4]
    stat = stat[1:-1]
    stat = stat.split()
    fullQuestionSQL = """
                    SELECT {}, {}, player_salary
                    FROM payroll
                    ORDER BY RANDOM() LIMIT 2
    """.format(stat[0], stat[1])

    cur.execute(fullQuestionSQL)
    fullQuestion = cur.fetchall()
    print(questionTuple[0][1].format(fullQuestion[0][0],fullQuestion[0][1]))
    print("Answer: " + str(fullQuestion[0][2]))
    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"basketball.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTeamTable(conn)
        createPayrollTable(conn)
        createPlayerTable(conn)
        createStatsTable(conn)
        createQuestionsTable(conn)
        createQuestionTypesTable(conn)
        populatePlayerTable(conn)
        populateTeamTable(conn)
        populatePayrollTable(conn)
        populateQuestionsTable(conn)
        populateQuestionTypesTable(conn)
    GrabQuestion(conn)
    closeConnection(conn, database)


if __name__ == '__main__':
    main()