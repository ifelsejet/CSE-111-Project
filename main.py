import sqlite3
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
                    t_numChampionships decimal(9,0) not null,
                    t_statsID decimal(2,0) not null)"""

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
                    t_id decimal(9,0) not null,
                    pl_year char(100) not null,
                    p_id decimal(6,0) not null,
                    player_salary decimal(9,0) not null)"""

        _conn.execute(sql)
        # _conn.execute("COMMIT")
        _conn.commit()
        print("success")
    except Error as e:
       # _conn.execute("ROLLBACK")
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTables(_conn):
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
        populateTables(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()