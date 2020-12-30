import sqlite3

def connectData():
    con = sqlite3.connect("data_GUI.db") # if not exists, create new.
    #con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db") # This is my path.
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data_GUI(id INTEGER PRIMARY KEY,\
day text, month text, year text, money text, note text)")
    con.commit()
    con.close()

def addIdRec(day, month, year, money, note):
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("INSERT INTO data_GUI VALUES (NULL, ?, ?, ?, ?, ?)",
                (day, month, year, money, note))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM data_GUI")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("DELETE FROM data_GUI WHERE id = ?", (id,))
    con.commit()
    con.close()

def searchData(day = "", month = "", year = "", money = ""):
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM data_GUI WHERE day = ? AND month = ? AND year = ?\
OR money = ?", (day, month, year, money))
    # if you want to find particular day or month or year
    #cur.execute("SELECT * FROM data_GUI WHERE day = ? OR month = ? OR year = ? OR money = ?", (day, month, year, money))
    rows = cur.fetchall()
    con.close()
    return rows

def updateData(id, day = "", month = "", year = "", money = "", note = ""):
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur= con.cursor()
    cur.execute("UPDATE data_GUI SET day = ?, month = ?, year = ?, money = ?, \
note = ? WHERE ID = ?", (day, month, year, money, note, id))
    con.commit()
    con.close()
# Calculate the total of money
def total():
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT money FROM data_GUI")
    rows = cur.fetchall()
    con.close()
    summ = count = 0
    for i in rows:
        summ += float(i[0])
        count += 1
    summ = "{:,}".format(int(summ))
    return summ, count

def lookup_month(m, y):
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT money FROM data_GUI WHERE month = %s AND year = %s" %(m, y))
    rows = cur.fetchall()
    con.close()
    summ = 0
    for i in rows:
        summ += float(i[0])
    summ = "{:,}".format(int(summ))
    return summ #string value

def lookup_year(y):
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT money FROM data_GUI WHERE year = %s" %y)
    rows = cur.fetchall()
    con.close()
    summ = 0
    for i in rows:
        summ += float(i[0]) # if dollar
    summ = "{:,}".format(int(summ))
    return summ # string value

def lookup_week():
    con = sqlite3.connect("D:/Training_Python/Count/data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT money FROM data_GUI")
    rows = cur.fetchall()
    con.close()
    w = rows[-7:]
    summ = 0
    for i in w:
        summ += float(i[0])
    summ = "{:,}".format(int(summ))
    return summ # string value

connectData()
    
