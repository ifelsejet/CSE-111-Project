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

        # Jet - removing p_id, p_games, p_stats for now (11/7)
        sql = """CREATE TABLE player (
                    p_name TEXT not null,
                    p_draftYear int not null,
                    p_draftpos int)
                    """

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
        print("AYOOO")

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
        # 		

        sql = """CREATE TABLE stats (
                    s_name TEXT not null,
                    s_years int not null,
                    s_games int not null,
                    s_pts int not null,
                    s_trb int not null,
                    s_ast int not null,
                    s_fgp int not null,
                    s_fgt int not null,
                    s_ftp int not null,
                    s_efg int not null,
                    s_allStar int not null,
                    s_allNBA int not null,
                    s_allRookie int not null,
                    s_allDefensive int not null,
                    s_blkChamp int not null,
                    s_stlChamp int not null,
                    s_trbChamp int not null,
                    s_astChamp int not null,
                    s_scoreChamp int not null,
                    s_mostImprovedChamp int not null,
                    s_sixthManChamp int not null,
                    s_dpoyChamp int not null,
                    s_royChamp int not null,
                    s_allStarMVP int not null,
                    s_confMVP int not null,
                    s_finalsMVP int not null,
                    s_MVP int not null,
                    s_rings int not null,
                    s_nba75 int not null
                    )"""

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
    file = open('data/players.csv' , encoding="utf8")
 
    # Reading the contents of the
    # players.csv file
    contents = csv.reader(file)
 
    # SQL query to insert data into the
    # person table
    insert_records = "INSERT INTO player VALUES(?, ?, ?)"
 
    # Importing the contents of the file
    # into our person table
    cur.executemany(insert_records, contents)
    print("++++++++++++++++++++++++++++++++++")

def populateTeamTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Team Table")
    cur=_conn.cursor()
    # Opening the person-records.csv file
    file = open('data/NBA_team_table.csv', encoding="utf8")
 
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

   # Opening the stats.csv file
    file = open('data/stats.csv', encoding="utf8")
 
    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)
 
    # SQL query to insert data into the
    # stats table
    insert_records = "INSERT INTO stats VALUES(?, ?, ?, ?, ?, ? ,?, ?,?, ?, ?, ?, ?, ? ,?, ?,?, ?, ?, ?, ?, ? ,?, ?,?, ?, ?,?,?)"
 
    # Importing the contents of the file
    # into our stats table
    cur.executemany(insert_records, contents)
    print("Populated stats!")
    print("++++++++++++++++++++++++++++++++++")

def populateQuestionsTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate tables")
    cur=_conn.cursor()
    # Opening the person-records.csv file
    file = open('data/questions.csv', encoding="utf8")
 
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
    file = open('data/NBA-salaries.csv', encoding="utf8")
 
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
    file = open('data/questionTypes.csv', encoding="utf8")
 
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
    #print("Grab Question")
    # 20 random queries
    for x in range(1,21):
        print("Grab Sample Question %d" % (x))
        cur=_conn.cursor()
        questionTypeSQL = "SELECT * FROM questionTypes ORDER BY RANDOM() LIMIT 1;"
        cur.execute(questionTypeSQL)
        questionType = cur.fetchall()
        print(questionType[0][1])
        questionSQL = """SELECT * 
                        FROM questions 
                        WHERE q_type = '{}'
                        ORDER BY RANDOM() LIMIT 1
                        """.format(questionType[0][1])
        cur.execute(questionSQL)
        questionTuple = cur.fetchall()
        print(questionTuple)
        print("Question: "+ questionTuple[0][1])
        print("Stat: " + questionTuple[0][4])
        print(questionType[0][1])
        if questionType[0][1] == "stats":
            print("IS IN STATS BLOCK")
            statTuple = questionTuple[0][4].split()
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
                print(questionTuple[0][1].format(statType,fullQuestion[0][1]))
                print("Answer: " + str(fullQuestion[0][0]))
            elif len(statTuple) == 2:
                fullQuestionSQL = """
                        SELECT {}, {}
                        FROM {}
                        ORDER BY RANDOM() LIMIT 1
                        """.format(statTuple[0], statTuple[1], questionTuple[0][2])
                cur.execute(fullQuestionSQL)
                fullQuestion = cur.fetchall()
                print(questionTuple[0][1].format(fullQuestion[0][0]))
                print("Answer: " + str(fullQuestion[0][1]))
            elif len(statTuple) == 1:
                fullQuestionSQL = """
                        SELECT {}
                        FROM {}
                        ORDER BY RANDOM() LIMIT 1
                        """.format(statTuple[0], questionTuple[0][2])
                cur.execute(fullQuestionSQL)
                fullQuestion = cur.fetchall()
                print(questionTuple[0][1].format(fullQuestion[0][0]))
                print("Answer: " + str(fullQuestion[0][1]))
        # elif questionType[0][1] == "payroll":
        #     print("IS IN PAYROLL")
        #     statTuple = questionTuple[0][4].split()
        #     fullQuestionSQL = """
        #                 SELECT {}, {}, {}
        #                 FROM {}
        #                 ORDER BY RANDOM() LIMIT 1
        #     """.format(statTuple[0], statTuple[1], statTuple[2], questionTuple[0][2])
        
        #     cur.execute(fullQuestionSQL)
        #     fullQuestion = cur.fetchall()
        #     print(questionTuple[0][1].format(fullQuestion[0][0],fullQuestion[0][1]))
        #     print("Answer: " + str(fullQuestion[0][2]))
        # elif questionType[0][1] == "team":
        #     print("IS IN TEAM")
        #     statTuple = questionTuple[0][4].split()
        #     print(statTuple)
        #     if len(statTuple) == 1:
        #         fullQuestionSQL = """
        #                 SELECT  {}
        #                 FROM {}
        #                 """.format(statTuple[0], questionTuple[0][2])
        #         cur.execute(fullQuestionSQL)
        #         fullQuestion = cur.fetchall()
        #         print(questionTuple[0][1].format(fullQuestion[0][0]))
        #         print("Answer: " + str(fullQuestion[0][0]))
        #     else:
        #         fullQuestionSQL = """
        #                 SELECT  {}, {}
        #                 FROM {}
        #                 ORDER BY RANDOM() LIMIT 1
        #         """.format(statTuple[0], statTuple[1], questionTuple[0][2])
        
        #         cur.execute(fullQuestionSQL)
        #         fullQuestion = cur.fetchall()
        #         print(questionTuple[0][1].format(fullQuestion[0][0],fullQuestion[0][1]))
        #         print("Answer: " + str(fullQuestion[0][1]))



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
            print(questionTuple[0][1].format(sqlInputs[1]))
            print("Answer: " + str(fullQuestion[0][0]))

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
            print(questionTuple[0][1].format(sqlInputs[1], sqlInputs[2]))
            print("Answer: " + str(fullQuestion[0][0]))

        if (x == 20):
            print("SAMPLE GAMEPLAY DEMO")
            p1guess = input("Player 1 enter guess: ")
            p1guess = int(p1guess)
            # 0 - lower, 1- higher (for now)
            p2guess = input("Player 2, higher (1) or lower(0) ?: ")
            p2guess = int(p2guess)
            if(p1guess < fullQuestion[0][len(fullQuestion[0])-1] and p2guess == 1):
                print("Player 2 wins a point!")
            elif(p1guess > fullQuestion[0][len(fullQuestion[0])-1] and p2guess == 0):
                print("Player 2 wins a point!")
            else:
                print("Player 1 wins a point!")
        ##print("Answer: " + str(fullQuestion[0][2]))
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
        populateStatsTable(conn)
        populatePayrollTable(conn)
        populateQuestionsTable(conn)
        populateQuestionTypesTable(conn)
    GrabQuestion(conn)
    closeConnection(conn, database)


if __name__ == '__main__':
    main()