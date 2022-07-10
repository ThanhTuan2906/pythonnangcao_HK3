import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def connectData():
    con = sqlite3.connect("data_GUI.db") # if not exists, create new.
    #con = sqlite3.connect("data_GUI.db") # This is my path.
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data_GUI(id INTEGER PRIMARY KEY,\
day text, month text, year text, money text, note text)")
    con.commit()
    con.close()

def addIdRec(day, month, year, money, note):
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    cur.execute("INSERT INTO data_GUI VALUES (NULL, ?, ?, ?, ?, ?)",
                (day, month, year, money, note))
    con.commit()
    con.close()
    return cur.lastrowid

def viewData():
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM data_GUI")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    cur.execute("DELETE FROM data_GUI WHERE id = ?", (id,))
    con.commit()
    con.close()

def searchData(day = "", month = "", year = ""):
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    query = "SELECT * FROM data_GUI"
    if day != "" and month == "" and year == "":
        query += " WHERE day=?"
        cur.execute(query, (day, ))
    elif day == "" and month != "" and year == "":
        query += " WHERE month=?"
        cur.execute(query, (month, ))
    elif day == "" and month == "" and year != "":
        query += " WHERE year=?"
        cur.execute(query, (year, ))
    elif day != "" and month != "" and year == "":
        query += " WHERE day=? AND month=?"
        cur.execute(query, (day, month, ))
    elif day == "" and month != "" and year != "":
        query += " WHERE month=? AND year=?"
        cur.execute(query, (month, year, ))
    elif day != "" and month == "" and year != "":
        query += " WHERE day=? AND year=?"
        cur.execute(query, (day, year, ))
    elif day != "" and month != "" and year != "":
        query += " WHERE day=? AND month=? AND year=?"
        cur.execute(query, (day, month, year, ))
    

    rows = cur.fetchall()
    con.close()
    return rows

def updateData(id, day = "", month = "", year = "", money = "", note = ""):
    con = sqlite3.connect("data_GUI.db")
    cur= con.cursor()
    cur.execute("UPDATE data_GUI SET day = ?, month = ?, year = ?, money = ?, \
note = ? WHERE ID = ?", (day, month, year, money, note, id))
    con.commit()
    con.close()
# Calculate the total of money
def total():
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT sum(money) FROM data_GUI")
    rows = cur.fetchall()
    cur.execute("SELECT count(*) FROM data_GUI")
    count = cur.fetchall()
    con.close()
    if rows[0][0] != None:
        return "{:,}".format(int(rows[0][0])), count[0][0]
    else:
        return str(0), count[0][0]

def lookup_month(m, y):
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT sum(money) FROM data_GUI WHERE month = %s AND year = %s" %(m, y))
    rows = cur.fetchall()
    con.close()
    return "{:,}".format(int(rows[0][0])) if rows[0][0] != None else str(0)
#=======For statistics ==============
def get_month(m, y):
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT sum(money) FROM data_GUI WHERE month = %s AND year = %s" %(m, y))
    rows = cur.fetchall()
    con.close()
    return rows[0][0] if rows[0][0] != None else 0

def getData(y):
    data = {"month": [i for i in range(1, 13)],
            "total": [get_month(month, y) for month in range(1, 13)]}
    df = pd.DataFrame(data, columns = ["month", "total"])
    return df
    
def plotting(y):
    fig, ax = plt.subplots(figsize = (10, 5))
    data = getData(y)
    plots = sns.barplot(x = "month", y = "total", data = data)
    for bar in plots.patches:
        plots.annotate("{:,.0f}".format(bar.get_height()), (bar.get_x() + bar.get_width() / 2,
                                                             bar.get_height()), ha= "center", va = "center", size = 8,
                      xytext = (0, 8), textcoords = "offset points")
    ax.set_title("AMOUNT STATISTICS\nTotal in %s: %s vnd"%(y, "{:,.0f}".format(sum(data['total']))) ,
                 fontsize = 17, color = "purple")
    plt.xlabel("Month", size = 15)
    plt.ylabel("Total (vnd)", size = 15)
    plt.show()
    
def lookup_year(y):
    con = sqlite3.connect("data_GUI.db")
    cur = con.cursor()
    cur.execute("SELECT sum(money) FROM data_GUI WHERE year = %s" %y)
    rows = cur.fetchall()
    con.close()
    return "{:,}".format(int(rows[0][0])) if rows[0][0] != None else str(0)

def lookup_week():
    con = sqlite3.connect("data_GUI.db")
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
    
