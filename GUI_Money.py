""" The program stores the amount spent each day """

from tkinter import *
from tkinter.ttk import Combobox, Style, Treeview
import time
import calendar
import tkinter.messagebox as mess
import Database_Money
from tkcalendar import Calendar as CAL

class Money(Frame):
    def __init__(self, frame):
        self.frame = frame
        self.init_UI()
        
    def init_UI(self):
        self.frame.title("Expense Management")
        #current time
        self.day = StringVar()
        self.month = StringVar()
        self.year = StringVar()
        # look up month in year
        self.lk_month = StringVar()
        self.lk_year = StringVar()
        #statistics
        self.stat = StringVar()
        # look up year
        self.look_year = StringVar()
        # Amount of money, note
        self.money = StringVar()
        self.note = StringVar()
        # simple calculator with addition, subtraction, multiplication, division
        self.operator = ""
        self.val = StringVar()
        self.english_month = ['January', "Feburary", 'March', 'April', 'May', 'June', 'Jully', 'August', 'September', 'October', 'November', 'December']
        
        """ ----------------------------------------------Main Frame------------------------------------------"""
        MainFrame = Frame(self.frame, width = 800, height = 600, bg = "sea green", bd = 10,
                          relief = RIDGE)
        MainFrame.pack()
        """ -----------------------------------------------Sub Frame--------------------------------------------"""
        # frame contains the name
        titleF = Frame(MainFrame, width = 800, height = 50, bg = "light sea green",
                       padx = 2, pady = 10, relief = RIDGE)
        titleF.pack(side = TOP)
        # frame contains buttons
        buttonF = Frame(MainFrame, width = 800, height = 50, bg = "gold", bd = 5,
                        padx = 2, pady = 2, relief = RIDGE)
        buttonF.pack(side = BOTTOM)
        # frame show details
        detailF = Frame(MainFrame, width = 800, height = 190, bg = "indian red", bd = 5,
                        padx = 2, pady = 2, relief = RIDGE)
        detailF.pack(side = BOTTOM)
        # frame contains Input, Output, Calculator
        dataF = Frame(MainFrame, width = 800, height = 350, bg = "cyan2", bd = 5,
                      padx = 2, pady = 2, relief = RIDGE)
        dataF.pack(side = BOTTOM)
        # frame left in dataF
        left = LabelFrame(dataF, width = 290, height = 280, bg = "powder blue", bd = 5,
                          padx = 2, pady = 2, text = "INPUT", font = ("arial", 12, "bold"), relief = RIDGE)
        left.pack(side = LEFT)
        # frame calculator in dataF
        cal = Frame(dataF, width = 300, height = 280, bg = "deep pink", bd = 5, padx = 2,
                    pady = 2, relief = RIDGE)
        cal.pack(side = RIGHT)
        # frame right in dataF
        right = LabelFrame(dataF, width = 300, height = 280, bg = "powder blue", bd = 5,
                           padx = 2, pady = 2, text = "OUTPUT", font = ("arial", 12, "bold"), relief = RIDGE)
        right.pack(side = RIGHT)
        
        lblTitle = Label(titleF, text = "Expense Management", justify = CENTER, bd = 2, padx = 2, pady = 2,
                         font = ("arial", 28, "bold"), bg = "light sea green")
        lblTitle.pack()
        """ Label and Combobox in frame left """
        lblDay = Label(left, bd = 2, padx = 2, pady = 2, bg = "powder blue", text = "DD",
                       font = ("arial", 10, "bold"))
        lblDay.place(x = 0, y = 0)
        self.cbbDay = Combobox(left, font = ("arial", 10, "bold"), textvariable = self.day,
                               state = "readonly", width = 3)
        self.cbbDay["value"] = tuple([""] + [str(i) for i in range(1, 32)])
        self.cbbDay.current(0)
        self.cbbDay.place(x = 45, y = 0)

        lblMonth = Label(left,  bd = 2, padx = 2, pady = 2, bg = "powder blue", text = "MM",
                         font = ("arial", 10, "bold"))
        lblMonth.place(x = 90, y = 0)
        self.cbbMonth = Combobox(left, font = ("arial", 10, "bold"), textvariable = self.month,
                                 state = "readonly", width = 3)
        self.cbbMonth["value"] = tuple([""] + [str(i) for i in range(1, 13)])
        self.cbbMonth.current(0)
        self.cbbMonth.place(x = 135, y = 0)

        lblYear = Label(left, bd = 2, padx = 2, pady = 2, bg = "powder blue", text = "YYYY",
                        font = ("arial", 10, "bold"))
        lblYear.place(x = 180, y = 0)
        
        #auto set time
        d = str(int(time.strftime("%d")))
        m = str(int(time.strftime("%m")))
        y = str(int(time.strftime("%Y")))
        # ====
        self.cbbYear = Combobox(left, font = ("arial", 10, "bold"), textvariable = self.year,
                                width = 4)
        self.cbbYear["value"] = tuple([""] + [str(i) for i in range(int(y) - 10, int(y) + 6)])
        self.cbbYear.current(0)
        self.cbbYear.place(x = 225, y = 0)
        # ====
        self.day.set(d)
        self.month.set(m)
        self.year.set(y)
        """ Label and entry money, note """
        lblMoney = Label(left,  bd = 2, padx = 2, pady = 2, bg = "powder blue",
                         text = "Amount of Money", font = ("arial", 10, "bold"))
        lblMoney.place(x = 0, y = 30)
        self.txtMoney = Entry(left, width = 20, font = ("arial", 10, "bold"), textvariable = self.money,
                              bd = 2, justify = CENTER)
        self.txtMoney.place(x = 125, y = 30)

        lblNote = Label(left, bd = 2, padx = 2, pady = 2, bg = "powder blue",
                        text = "Note", font = ("arial", 10, "bold"))
        lblNote.place(x = 0, y = 60)
        self.txtNote = Entry(left, width = 20, font = ("arial", 10, "bold"), textvariable = self.note,
                             bd = 2, justify = CENTER)
        self.txtNote.place(x = 125, y = 60)
        """ Label and combobox: lookup """
        lup_month = Label(left, bd =2, padx = 2, pady = 2, text = "Lookup Month",
                          bg = "powder blue", font = ("arial", 10, "bold"))
        lup_month.place(x = 0, y = 90)
        self.cbb_month = Combobox(left, font = ("arial", 10, "bold"), state = "readonly",
                                  width = 3, textvariable = self.lk_month)
        self.cbb_month["value"] = tuple([""] + [str(i) for i in range(1, 13)])
        self.cbb_month.current(0)
        self.cbb_month.place(x = 100, y = 90)
        #lookup month in year
        self.cbb_year = Combobox(left, font = ("arial", 10, "bold"), state = "readonly",
                                  width = 4, textvariable = self.lk_year)
        self.cbb_year["value"] = tuple([""] + [str(i) for i in range(int(y)-10, int(y)+6)])
        self.cbb_year.current(0)
        self.cbb_year.place(x = 150, y = 90)
        
        self.btnMonth = Button(left, font = ("arial", 10, "bold"), text = "Lookup", bd = 2,
                               padx = 2, pady = 2, bg = "cadet blue", command = self.lookup_month)
        self.btnMonth.place(x = 210, y = 86)
        # lookup year and statistics per month in year
        lup_year = Label(left, bd =2, padx = 2, pady = 2, text = "Lookup Year",
                          bg = "powder blue", font = ("arial", 10, "bold"))
        lup_year.place(x = 0, y = 120)
        # is Statistics or None
        self.cbb_stat = Combobox(left, font = ("arial", 10, "bold"), state = "readonly",
                                 width = 5, textvariable = self.stat)
        self.cbb_stat["value"] = tuple(["", "Stat", "None"])
        self.cbb_stat.current(0)
        self.cbb_stat.place(x=90, y = 120)
        # cbb year
        self.cbb_year1 = Combobox(left, font = ("arial", 10, "bold"), state = "readonly",
                                  width = 4, textvariable = self.look_year)
        self.cbb_year1["value"] = tuple([""] + [str(i) for i in range(int(y)-10, int(y)+6)])
        self.cbb_year1.current(0)
        self.cbb_year1.place(x = 150, y = 120)
        
        self.btnYear = Button(left, font = ("arial", 10, "bold"), text = "Lookup", bd = 2,
                               padx = 2, pady = 2, bg = "cadet blue", command = self.lookup_year)
        self.btnYear.place(x = 210, y = 116)
        # lookup week
        lup_week = Label(left, bd = 2, padx = 2, pady = 2, text = "Lookup the past seven days",
                         font = ("arial", 10, "bold"), bg = "powder blue")
        lup_week.place(x = 0, y = 150)
        self.btnWeek = Button(left, font = ("arial", 10, "bold"), text = "Lookup", bd = 2,
                               padx = 2, pady = 2, bg = "cadet blue", command = self.lookup_week)
        self.btnWeek.place(x = 210, y = 146)
        # update current time
        self.btnTime = Button(left, bd = 2, padx = 2, pady = 2, text = "Reset date",
                                 font = ("arial", 10, "bold"), bg = "cadet blue", command = self.resetDay)
        self.btnTime.place(x = 0, y = 170)
        # Show Calendar
        self.btnCalen = Button(left, bd = 2, padx = 2, pady = 2, text = "Calendar",
                            font = ("arial", 10, "bold"), bg = "cadet blue", command = self.showCalen)
        self.btnCalen.place(x = 85, y = 170)
        # total
        self.btnTotal = Button(left, bd = 2, padx = 2, pady = 2, text = "Total",
                            font = ("arial", 10, "bold"), bg = "cadet blue", command = self.totalAll)
        self.btnTotal.place(x = 161, y = 170)
        """ Show information"""
        self.txt_display = Text(right, font = ("ariai", 11, "bold"), width = 26, height = 11)
        self.txt_display.grid()
        
        """ Listbox contains date information, amount of money, notes"""
        # scrollbar
        scrollbary = Scrollbar(DetailF, orient='vertical')
        scrollbarx = Scrollbar(DetailF, orient='horizontal')
        columns = ("id", 'day', 'month', 'year', "money", "note")
        self.treeview = Treeview(DetailF, columns = columns, show='headings')
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side = RIGHT, fill=Y)
        self.treeview.pack(side = LEFT, expand=True, fill=BOTH)
        scrollbary.config(command = self.treeview.yview)
        scrollbarx.config(command = self.treeview.xview)
        self.treeview.config(xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.treeview.bind('<<TreeviewSelect>>', self.selected)
        #Headings
        self.treeview.heading("id", text = "#", anchor=CENTER)
        self.treeview.heading("day", text = "Day", anchor=CENTER)
        self.treeview.heading("month", text = "Month", anchor=CENTER)
        self.treeview.heading("year", text= "Year", anchor=CENTER)
        self.treeview.heading("money", text="How much", anchor=CENTER)
        self.treeview.heading("note", text = "Note", anchor=CENTER)

        # Define the columns
        self.treeview.column("id", width = 80)
        self.treeview.column("day", anchor=CENTER, width=55)
        self.treeview.column("month", anchor=CENTER, width=55)
        self.treeview.column("year", anchor=CENTER, width=55)
        self.treeview.column("money", anchor=CENTER, width=150)
        self.treeview.column("note", anchor=CENTER, width=350, stretch=True)

        style = Style()
        style.theme_use("winnative")
        style.configure("Treeview.Heading", font=('arial', 10, "bold"))
        style.configure("Treeview.Heading", background="beige")
        style.configure("Treeview", font=('arial', 10, "bold"))
        
        """ Create a simple calculator """
        self.entry_input = Entry(cal, font = ("arial", 15, "bold"), width = 20, textvariable = self.val,
                                 justify = RIGHT, bd = 6)
        self.entry_input.grid(row = 0, columnspan = 4, sticky = W + E)
        # button Clear, Back, equal,  number, +, -, *, /
        self.btnC = Button(cal, font = ("arial", 11, "bold"), command = self.clean_cal, bd = 3,
                           padx = 2, pady = 2, text = "C", bg = "powder blue",  width = 5)
        self.btnC.grid(row = 1, column = 0)
        self.btnEmpty = Button(cal, font = ("arial", 11, "bold"), command = None, bd = 3,
                               padx = 2, pady = 2, text = "", bg = "powder blue", width = 5)
        self.btnEmpty.grid(row = 1, column = 1)
        self.btnBack = Button(cal, font = ("arial", 11, "bold"), command = self.Back, bd = 3,
                           padx = 2, pady = 2, text = "Back", bg = "powder blue",  width = 5)
        self.btnBack.grid(row = 1, column = 2)
        self.btnEqual = Button(cal, font = ("arial", 11, "bold"), command = self.equals, bd = 3,
                               padx = 2, pady = 2, text = "=", bg = "powder blue", width =5)
        self.btnEqual.grid(row = 1, column = 3)

        self.btn7 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(7),
                           bd = 3, padx = 2, pady = 2, text = "7", bg = "powder blue",  width = 5)
        self.btn7.grid(row = 2, column = 0)
        self.btn8 = Button(cal, font = ("arial", 11, "bold"), command =  lambda: self.onClick(8),
                           bd = 3, padx = 2, pady = 2, text = "8", bg = "powder blue", width = 5)
        self.btn8.grid(row = 2, column = 1)
        self.btn9 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(9),
                           bd = 3, padx = 2, pady = 2, text = "9", bg = "powder blue",  width = 5)
        self.btn9.grid(row = 2, column = 2)
        self.btn_add = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick("+"),
                             bd = 3, padx = 2, pady = 2, text = "+", bg = "powder blue", width =5)
        self.btn_add.grid(row = 2, column = 3)

        self.btn4 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(4),
                           bd = 3, padx = 2, pady = 2, text = "4", bg = "powder blue",  width = 5)
        self.btn4.grid(row = 3, column = 0)
        self.btn5 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(5),
                           bd = 3, padx = 2, pady = 2, text = "5", bg = "powder blue", width = 5)
        self.btn5.grid(row = 3, column = 1)
        self.btn6 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(6),
                           bd = 3, padx = 2, pady = 2, text = "6", bg = "powder blue",  width = 5)
        self.btn6.grid(row = 3, column = 2)
        self.btnSub = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick("-"),
                             bd = 3, padx = 2, pady = 2, text = "-", bg = "powder blue", width =5)
        self.btnSub.grid(row = 3, column = 3)

        self.btn1 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(1),
                           bd = 3, padx = 2, pady = 2, text = "1", bg = "powder blue",  width = 5)
        self.btn1.grid(row = 4, column = 0)
        self.btn2 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(2),
                           bd = 3, padx = 2, pady = 2, text = "2", bg = "powder blue", width = 5)
        self.btn2.grid(row = 4, column = 1)
        self.btn3 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(3),
                           bd = 3, padx = 2, pady = 2, text = "3", bg = "powder blue",  width = 5)
        self.btn3.grid(row = 4, column = 2)
        self.btnMul = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick("*"),
                             bd = 3, padx = 2, pady = 2, text = "*", bg = "powder blue", width =5)
        self.btnMul.grid(row = 4, column = 3)

        self.btnDot = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick("."),
                             bd = 3, padx = 2, pady = 2, text = ".", bg = "powder blue",  width = 5)
        self.btnDot.grid(row = 5, column = 0)
        self.btn0 = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick(0),
                           bd = 3, padx = 2, pady = 2, text = "0", bg = "powder blue", width = 5)
        self.btn0.grid(row = 5, column = 1)
        self.btnEmpty1 = Button(cal, font = ("arial", 11, "bold"), command = None,
                                bd = 3, padx = 2, pady = 2, text = "", bg = "powder blue",  width = 5)
        self.btnEmpty1.grid(row = 5, column = 2)
        self.btnDiv = Button(cal, font = ("arial", 11, "bold"), command = lambda: self.onClick("/"),
                             bd = 3, padx = 2, pady = 2, text = "/", bg = "powder blue", width =5)
        self.btnDiv.grid(row = 5, column = 3)
        """ BUTTON add delete, display, search, update, clean, exit"""
        self.btnAdd = Button(buttonF, bd = 2, padx = 2, pady = 2, font = ("arial", 12, "bold"),
                             text = "Add", bg = "red", width = 10, command = self.addData)
        self.btnAdd.grid(row = 0, column = 0)
        self.btnDisplay = Button(buttonF, bd = 2, padx = 2, pady = 2, font = ("arial", 12, "bold"),
                             text = "Display", bg = "yellow", width = 10, command = self.displayData)
        self.btnDisplay.grid(row = 0, column = 1)
        self.btnDelete = Button(buttonF, bd = 2, padx = 2, pady = 2, font = ("arial", 12, "bold"),
                             text = "Delete", bg = "green", width = 10, command = self.deleteData)
        self.btnDelete.grid(row = 0, column = 2)
        self.btnSearch = Button(buttonF, bd = 2, padx = 2, pady = 2, font = ("arial", 12, "bold"),
                             text = "Seach", bg = "blue", width = 10, command = self.searchData)
        self.btnSearch.grid(row = 0, column = 3)
        self.btnUpdate = Button(buttonF, bd = 2, padx = 2, pady = 2, font = ("arial", 12, "bold"),
                             text = "Update", bg = "pink", width = 10, command = self.updateData)
        self.btnUpdate.grid(row = 0, column = 4)
        self.btnClean = Button(buttonF, bd = 2, padx = 2, pady = 2, font = ("arial", 12, "bold"),
                             text = "Clean", bg = "purple", width = 10, command = self.Clean)
        self.btnClean.grid(row = 0, column = 5)
        self.btnExit = Button(buttonF, bd = 2, padx = 2, pady = 2, font = ("arial", 12, "bold"),
                             text = "Exit", bg = "cyan", width = 8, command = self.exit)
        self.btnExit.grid(row = 0, column = 6)

    # function
    def resetDay(self):
        self.day.set(str(int(time.strftime("%d"))))
        self.month.set(str(int(time.strftime("%m"))))
        self.year.set(str(int(time.strftime("%Y"))))
    
    def clearTreeView(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
            
    def showCalen(self):
        m = int(time.strftime("%m"))
        y = int(time.strftime("%Y"))
        self.txt_display.delete("1.0", END)
        self.txt_display.insert(END, str(calendar.month(y, m)))
        
    def showCalendar(self):
        self.new_gui = Tk()
        self.new_gui.config(background="white")
        self.new_gui.title("CALENDAR")
        self.new_gui.geometry("280x200+800+100")
        d = int(time.strftime("%d"))
        m = int(time.strftime("%m"))
        y = int(time.strftime("%Y"))
        cal = CAL(self.new_gui, selectmode='day', year=y, month=m, day=d)
        cal.grid(row = 1, column=1, padx=20)
        self.new_gui.mainloop()
        
    """ Function Calculator """
    def onClick(self, e):
        global operator
        self.operator += str(e)
        self.val.set(self.operator)
    def clean_cal(self):
        global operator
        self.operator = ""
        self.entry_input.delete(0, END)
    def equals(self):
        global operator
        SUM = str(eval(self.operator))
        self.val.set(SUM)
        self.operator = SUM
    def Back(self):
        global operator
        s = self.operator
        self.operator = s[:-1]
        self.val.set(self.operator)

    """ Function ADD, DISPLAY, .... EXIT """
    def Clean(self):
        self.clearTreeView()
        self.txtMoney.delete(0, END)
        self.txtNote.delete(0, END)
        self.txt_display.delete("1.0", END)
        self.day.set("")
        self.month.set("")
        self.year.set("")
        self.lk_month.set("")
        self.lk_year.set("")
        self.stat.set("")
        self.look_year.set("")
        self.resetDay()

    def exit(self):
        onExit = mess.askyesno("Exit?", "Confirm 'Yes' if you want to close the progam!")
        if onExit > 0:
            self.frame.destroy()
            return
        
    def addData(self):
        if len(self.money.get()) != 0:
            if self.money.get().isdigit():
                id = Database_Money.addIdRec(self.day.get(), self.month.get(), self.year.get(),
                                        self.money.get(), self.note.get())
                self.clearTreeView()
                row = (id, self.day.get(), self.month.get(), self.year.get(),
                                    self.money.get(), self.note.get())
                self.treeview.insert(parent='', index='end', iid=row[0], values = row)
            else:
                #self.Clean()
                mess.showwarning("Warning", "You must enter the number!")
                
        
    def displayData(self):
        self.clearTreeView()
        for row in Database_Money.viewData():
            self.treeview.insert(parent = '', index='end', iid = row[0],values = row)
    # Select data specified
    def selected(self, event):
        global s
        s = self.treeview.item(self.treeview.selection())['values']
        self.day.set(s[1])
        self.month.set(s[2])
        self.year.set(s[3])
        self.txtMoney.delete(0, END)
        self.txtMoney.insert(END, s[4])
        self.txtNote.delete(0, END)
        self.txtNote.insert(END, s[5])
    # select data specified --> delete
    def deleteData(self):
        if len(self.money.get()) != 0:
            Database_Money.deleteRec(s[0])
            mess.showinfo("Message", "A record with ID = %s was deleted successfully." %s[0])
            self.clearTreeView()
    # select data specified --> update
    def updateData(self):
        if len(self.money.get()) != 0:
            Database_Money.updateData(s[0], self.day.get(), self.month.get(), self.year.get(),
                                      self.money.get(), self.note.get())
            mess.showinfo("Message", "A record with ID = %s was updated successfully." %s[0])
            self.clearTreeView()
            
    # Seach money in day, month and year
    def searchData(self):
        self.clearTreeView()
        rows = Database_Money.searchData(day = str(self.day.get()), month=str(self.month.get()), year=str(self.year.get()))
        for row in rows:
            self.treeview.insert(parent = '', index='end', iid = row[0],values = row)
    """ FUNCTION TOTAL and lookup month, year, week """
    def totalAll(self):
        result, count = Database_Money.total()
        self.txt_display.delete("1.0", END)
        self.txt_display.insert(END, "The total amount spent is\n %s vnd.\n" %result)
        self.txt_display.insert(END, "This is the amount spent in %s days." %count)
    def lookup_month(self):
        if len(self.lk_month.get()) != 0 and len(self.lk_year.get()) != 0:
            result = Database_Money.lookup_month(self.lk_month.get(), self.lk_year.get())
            self.txt_display.delete("1.0", END)
            self.txt_display.insert(END, "The amount used in %s-%s\n is %s vnd." % (self.lk_month.get(),
                                                                            self.lk_year.get(), result))
    def lookup_year(self):
        if len(self.look_year.get()) != 0 and self.stat.get() != 'Stat':
            result = Database_Money.lookup_year(self.look_year.get())
            self.txt_display.delete("1.0", END)
            self.txt_display.insert(END, "The amount used \
in %s is\n %s vnd." %(self.look_year.get(),result))
        else:
            Database_Money.plotting(self.look_year.get())

    def lookup_week(self):
        result = Database_Money.lookup_week()
        self.txt_display.delete("1.0", END)
        self.txt_display.insert(END, "Note: The function only gives correct results when the \
dat-e, month and year are true fo-r the current week for the pa-st week.\n")
        self.txt_display.insert(END, "-----------------------------------------\n")
        self.txt_display.insert(END, "The amount spent in the last 7 days was %s vnd." %result)
        




if __name__ == "__main__":
    root = Tk()
    root.resizable(width = False, height = False) # Not expand
    root.geometry("800x600+350+100")
    GUI = Money(root)
    root.mainloop()

        
