from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import datetime
from tkcalendar import DateEntry
import mysql.connector

class Add_Expenses:
    def __init__(self,root):
        self.root = root
        self.root.title("Add Expenses")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        # ================================Variables==================================#

        self.expenseID = IntVar()
        self.expenseDate = StringVar()
        self.expenseType = StringVar()
        self.expenseDescription = StringVar()
        self.expenseAmount = IntVar()
        self.expenseTypeList = ["Petty Cash","Salary","Utility Bills","Debt","Rent","Asset","Markating","Project Expenses","Other"]

        # =============================Window Settings===============================#

        #=============================Centered Screen===============================#

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 550
        window_width = 900
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.state('zoomed')

        #===========================================================================#

        #===============================Title Frame=================================#

        self.titleFrame = Frame(self.root, bg="#00479c")
        self.titleFrame.pack(side=TOP, anchor="nw", pady=10, padx=5, fill="x")

        self.titleLabel = Label(self.titleFrame, text="Add Expense", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        #===========================================================================#

        # ===============================Space Frame=================================#

        self.spaceFrame = Frame(self.root, bg="#ffffff")
        self.spaceFrame.pack(side=TOP, anchor="nw", pady=20, padx=5, fill="x")

        # ===========================================================================#

        # ================================Bottom Frame===============================#

        self.bottomFrame = Frame(self.root, bg="#00479c", border=3)
        self.bottomFrame.pack(side=BOTTOM, anchor="nw", pady=0, padx=5, fill="x")

        self.bottomLabel = Label(self.bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white",
                                 font="Arial 9")
        self.bottomLabel.pack()

        # ============================================================================#

        # ===============================Main Frame=================================#

        self.mainFrame = Frame(self.root, bg="#ffffff")
        self.mainFrame.pack(fill=BOTH, pady=10)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(4, weight=1)

        # ===========================================================================#

        #==============================Expense Info Frame============================#

        self.expenseInfoFrame = Frame(self.mainFrame, width="800", highlightbackground="#00479c", highlightthickness=0, bg="#ffffff")
        self.expenseInfoFrame.grid(row=0, column=1, pady=0, padx=10, rowspan=4)


        # Expense ID
        self.expenseIDLabel = Label(self.expenseInfoFrame, text="Expense ID:", bg='#ffffff')
        self.expenseIDLabel.grid(row=1, column=1, sticky=W, padx=5, pady=10)

        self.expenseIDEntry = Entry(self.expenseInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.expenseID)
        self.expenseIDEntry.grid(row=1, column=2, sticky=W, padx=5, pady=10, ipady=5, ipadx=30)

        # Expense Date
        self.expenseDateLabel = Label(self.expenseInfoFrame, text="Expense Date:", bg='#ffffff')
        self.expenseDateLabel.grid(row=1, column=3, sticky=W, padx=5, pady=10)

        self.expenseDateEntry = DateEntry(self.expenseInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                      date_pattern="yyyy/mm/dd")
        self.expenseDateEntry.grid(row=1, column=4, sticky=W, padx=5, pady=5, ipady=4, ipadx=44)

        # Expense Type
        self.expenseTypeLabel = Label(self.expenseInfoFrame, text="Expense Type:", bg='#ffffff')
        self.expenseTypeLabel.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        self.expenseTypeCombobox = ttk.Combobox(self.expenseInfoFrame, textvariable=self.expenseType,
                                                    values=self.expenseTypeList)
        self.expenseTypeCombobox.grid(row=2, column=2, sticky=W, padx=5, pady=5, ipady=4, ipadx=20)

        # Expense Amount
        self.expenseAmountLabel = Label(self.expenseInfoFrame, text="Expense Amount:", bg='#ffffff')
        self.expenseAmountLabel.grid(row=2, column=3, sticky=W, padx=5, pady=10)

        self.expenseAmountEntry = Entry(self.expenseInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                        highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                        textvariable=self.expenseAmount)
        self.expenseAmountEntry.grid(row=2, column=4, sticky=W, padx=5, pady=10, ipady=5, ipadx=30)

        # Expense Description
        self.expenseDescriptionLabel = Label(self.expenseInfoFrame, text="Expense Description:", bg='#ffffff')
        self.expenseDescriptionLabel.grid(row=3, column=1, sticky=W, padx=5, pady=10)

        self.expenseDescriptionEntry = Entry(self.expenseInfoFrame, border=1, relief="solid", highlightbackground = "#00479c",
                                                 highlightcolor= "#00479c", highlightthickness=1, borderwidth=0, textvariable=self.expenseDescription)
        self.expenseDescriptionEntry.grid(row=3, column=2, sticky=W, padx=5, pady=10, ipady=5, ipadx=181, columnspan=3)

        #============================================================================#

        # ===============================Data Table Frame============================#

        self.dataTableFrame = Frame(self.mainFrame, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.dataTableFrame.grid(row=4, column=1, pady=10, padx=0, columnspan=2, sticky=EW)

        scrolly = Scrollbar(self.dataTableFrame, orient=VERTICAL)
        scrollx = Scrollbar(self.dataTableFrame, orient=HORIZONTAL)
        self.ProductTable = ttk.Treeview(self.dataTableFrame, columns=(
        "expenseID", "expenseDate", "expenseType", "expenseDescription", "expenseAmount"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, height=12)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("#0", text="", anchor=CENTER)
        self.ProductTable.heading("expenseID", text="Expense ID")
        self.ProductTable.heading("expenseDate", text="Expense Date")
        self.ProductTable.heading("expenseType", text="Expense Type")
        self.ProductTable.heading("expenseDescription", text="Expense Description")
        self.ProductTable.heading("expenseAmount", text="Expense Amount")
        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.column("#0", width=0, stretch=NO)
        self.ProductTable.column("expenseID", width=100)
        self.ProductTable.column("expenseDate", width=100)
        self.ProductTable.column("expenseType", width=100)
        self.ProductTable.column("expenseDescription", width=100)
        self.ProductTable.column("expenseAmount", width=100)

        # ===========================================================================#

        # ===============================Button Frame================================#

        self.buttonFrame = Frame(self.mainFrame, bg="#ffffff")
        self.buttonFrame.grid(row=5, column=1, pady=0, padx=0, columnspan=2, sticky=E)

        # Show Button
        self.show_button = Button(self.buttonFrame, text="Show", width=15, height=2, bg='#00479c', fg="White",
                                  font="Arial 9", relief="flat", command=lambda: [showExpense()])
        self.show_button.grid(column=1, row=1, sticky=W, padx=0, pady=0, ipady=1, ipadx=20)

        # Save Button
        self.save_button = Button(self.buttonFrame,text="Save", width=15, height=2, bg='#00479c', fg="White", font="Arial 9", relief="flat", command=lambda:[addExpense()])
        self.save_button.grid(column=2, row=1, sticky=W, padx=15, pady=5, ipady=1, ipadx=20)

        # Update Button
        self.update_button = Button(self.buttonFrame,text="Update", width=15, height=2, bg='#00479c', fg="White", font="Arial 9", relief="flat", command=lambda:[updateExpense()])
        self.update_button.grid(column=3, row=1, sticky=W, padx=0, pady=0, ipady=1, ipadx=20)

        # Clear Button
        self.clear_button = Button(self.buttonFrame, text="Clear", width=15, height=2, bg='#00479c', fg="White",
                                    font="Arial 9", relief="flat", command=lambda: [clearExpenseFields()])
        self.clear_button.grid(column=4, row=1, sticky=W, padx=15, pady=5, ipady=1, ipadx=20)

        # Delete Button
        self.delete_button = Button(self.buttonFrame, text="Delete", width=15, height=2, bg='#E81123', fg="White",
                                   font="Arial 9", relief="flat", command=lambda: [deleteExpense()])
        self.delete_button.grid(column=5, row=1, sticky=W, padx=0, pady=5, ipady=1, ipadx=20)

        # Expense
        def expenseCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
            points = [x1 + radius, y1,
                      x1 + radius, y1,
                      x2 - radius, y1,
                      x2 - radius, y1,
                      x2, y1,
                      x2, y1 + radius,
                      x2, y1 + radius,
                      x2, y2 - radius,
                      x2, y2 - radius,
                      x2, y2,
                      x2 - radius, y2,
                      x2 - radius, y2,
                      x1 + radius, y2,
                      x1 + radius, y2,
                      x1, y2,
                      x1, y2 - radius,
                      x1, y2 - radius,
                      x1, y1 + radius,
                      x1, y1 + radius,
                      x1, y1]

            return self.expenseCard.create_polygon(points, **kwargs, smooth=True, fill="#89A8D0")

        self.expenseCard = Canvas(self.mainFrame, bg="#ffffff", highlightthickness=0, width=350, height=125)
        self.expenseCard.grid(row=0, column=2, pady=0, padx=10, rowspan=4)
        expenseCanvas(0, 0, 350, 125, radius=30)

        self.expenseLabel = Label(self.expenseCard, text='Total Expenses of All Time', fg='#ffffff', bg='#89A8D0',
                                font="Arial 16 bold")
        self.expenseLabel.pack()
        self.expenseCard.create_window(175, 40, window=self.expenseLabel)

        self.totalExpenseLabel = Label(self.expenseCard, text='0', fg='#ffffff', bg='#89A8D0',
                                     font="Arial 18 bold")
        self.totalExpenseLabel.pack()
        self.expenseCard.create_window(175, 80, window=self.totalExpenseLabel)

        # ===========================================================================#

        def automateID():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select MAX(expenseID) from expense")
                maxID = cur.fetchone()
                if maxID[0]==None:
                    self.expenseID.set(1)
                else:
                    self.expenseID.set(int(maxID[0])+1)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        automateID()

        def addExpense():
            if IsValid():
                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
                #                                      database="gujranwalaemporium")
                # cursor = connection.cursor(prepared=True)
                try:
                    cur.execute("select * from expense where expenseID=?", (self.expenseIDEntry.get(),))
                    expenseData = cur.fetchone()
                    if expenseData != None:
                        messagebox.showerror("Error", "This Expense already Exist", parent=self.root)
                    else:
                        cur.execute("Insert into expense(expenseID,expenseDate,expenseType,expenseDescription,expenseAmount)values(?,?,?,?,?)",
                                    (self.expenseIDEntry.get(),
                                     self.expenseDateEntry.get(),
                                     self.expenseType.get(),
                                     self.expenseDescriptionEntry.get(),
                                     self.expenseAmountEntry.get()
                                     ))
                        con.commit()
                        showExpenseTable()
                        messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)
                        clearExpenseFields()
                        getTotalExpense()
                except EXCEPTION as ex:
                    messagebox.showerror("Error", f"due to : {str(ex)}")

        def showExpense():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                if self.expenseIDEntry.get() == "":
                    messagebox.showerror("Error", "Expense ID Must Required", parent=self.root)
                else:
                    cur.execute("select * from expense where expenseID=?", (self.expenseIDEntry.get(),))
                    expenseData = cur.fetchone()
                    if expenseData != None:
                        self.expenseDateEntry.set_date(expenseData[1])
                        index = self.expenseTypeList.index(expenseData[2])
                        self.expenseTypeCombobox.current(index)
                        self.expenseDescription.set(expenseData[3])
                        self.expenseAmount.set(expenseData[4])
                    else:
                        messagebox.showerror("Error", "This Expense does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def updateExpense():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                if self.expenseIDEntry.get() == "":
                    messagebox.showerror("Error", "Expense ID Must Required", parent=self.root)
                else:
                    cur.execute("select * from expense where expenseID=?", (self.expenseIDEntry.get(),))
                    expenseData = cur.fetchone()
                    if expenseData == None:
                        messagebox.showerror("Error", "This Expense Does not Exist", parent=self.root)
                    else:
                        cur.execute("Update expense set expenseDate=?,expenseType=? ,expenseDescription=?,expenseAmount=? where expenseID=?",
                                    (
                                        self.expenseDateEntry.get(),
                                        self.expenseType.get(),
                                        self.expenseDescriptionEntry.get(),
                                        self.expenseAmountEntry.get(),

                                        self.expenseIDEntry.get()
                                     ))
                        con.commit()
                        showExpenseTable()
                        clearExpenseFields()
                        getTotalExpense()
                        messagebox.showinfo("Sucess", "Record updated sucessfully", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def showExpenseTable():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select * from expense")
                rows = cur.fetchall()
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in reversed(rows):
                    expenseRowList = list(row)
                    row = tuple(expenseRowList)
                    self.ProductTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        showExpenseTable()

        def clearExpenseFields():
            automateID()
            self.expenseDateEntry.set_date(datetime.date.today())
            self.expenseAmountEntry.delete(0, 'end')
            self.expenseDescriptionEntry.delete(0, 'end')

        clearExpenseFields()

        def deleteExpense():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.expenseIDEntry.get() == "":
                    messagebox.showerror("Error", "Expense ID Must Required", parent=self.root)
                else:
                    cur.execute("select expenseID from expense where expenseID=?", (self.expenseIDEntry.get(),))
                    expenseData = cur.fetchone()
                    if expenseData == None:
                        messagebox.showerror("Error", "This Expense Does not Exist", parent=self.root)
                    else:
                        cur.execute("delete from expense where expenseID=?", (self.expenseIDEntry.get(), ))
                        con.commit()
                        showExpenseTable()
                        clearExpenseFields()
                        getTotalExpense()
                        messagebox.showinfo("Sucess", "Record deleted sucessfully", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def IsValid():
            if self.expenseIDEntry.get()=='':
                messagebox.showerror("Error", "Expense ID is Required", parent=self.root)
                return False

            if self.expenseIDEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Expense ID", parent=self.root)
                return False

            if self.expenseType.get()=='':
                messagebox.showerror("Error", "Please Select Expense Type", parent=self.root)
                return False

            if self.expenseAmountEntry.get()=='':
                messagebox.showerror("Error", "Expense Amount is Required", parent=self.root)
                return

            if self.expenseAmountEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Expense Amount", parent=self.root)
                return False

            if self.expenseDescriptionEntry.get() == '':
                messagebox.showerror("Error", "Expense Description is Required", parent=self.root)
                return False

            return True

        def getTotalExpense():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT SUM(expenseAmount) FROM expense")
                totalExpense = cur.fetchone()
                self.totalExpenseLabel.config(text=totalExpense[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        getTotalExpense()

if __name__=="__main__":

    root=Tk()
    obj=Add_Expenses(root)
    root.mainloop()