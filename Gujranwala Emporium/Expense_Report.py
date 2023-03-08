from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from fpdf import FPDF
import os
import tkcalendar as tkc
import mysql.connector

class expenseReport:
    def __init__(self,root, pdf):
        self.root = root
        self.pdf = pdf
        self.root.title("Expense Report")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.ln(50)

        # ================================Variables==================================#

        self.flag = 0

        # =============================Window Settings===============================#

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 550
        window_width = 900
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.state('zoomed')

        #===========================================================================#

        # ===============================Title Frame=================================#

        self.titleFrame = Frame(self.root, bg="#00479c")
        self.titleFrame.pack(side=TOP, anchor="nw", pady=10, padx=5, fill="x")

        self.titleLabel = Label(self.titleFrame, text="Expense Report", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        # ============================================================================#

        # ===============================Space Frame=================================#

        self.spaceFrame = Frame(self.root, bg="#ffffff")
        self.spaceFrame.pack(side=TOP, anchor="nw", pady=30, padx=5, fill="x")
        # ============================================================================#

        # ================================Label Frame=================================#

        self.LabelFrame = Frame(self.root, bg="#ffffff")
        self.LabelFrame.pack(side=TOP, anchor="nw", pady=5, padx=90, fill="x")

        # From Date
        self.fromLabel = Label(self.LabelFrame, text="From", bg="#ffffff", fg="black", font="Arial 10")
        self.fromLabel.pack(side=LEFT, anchor="w", pady=0, padx=0)

        self.fromDateEntry = tkc.DateEntry(self.LabelFrame, border=1, relief="solid",
                                          highlightbackground="#00479c",
                                          highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                          date_pattern="yyyy/mm/dd")
        self.fromDateEntry.pack(side=LEFT, anchor="w", pady=0, padx=10, ipady=4, ipadx=44)

        # To Date
        self.toLabel = Label(self.LabelFrame, text="To", bg="#ffffff", fg="black", font="Arial 10")
        self.toLabel.pack(side=LEFT, anchor="w", pady=0, padx=10)

        self.toDateEntry = tkc.DateEntry(self.LabelFrame, border=1, relief="solid",
                                          highlightbackground="#00479c",
                                          highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                          date_pattern="yyyy/mm/dd")
        self.toDateEntry.pack(side=LEFT, anchor="w", pady=0, padx=0, ipady=4, ipadx=44)

        # Search Button
        self.searchButton = Button(self.LabelFrame, text="Search", width=20, height=1,
                                    bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                    command=lambda: [showExpenseTable()])
        self.searchButton.pack(side=RIGHT, anchor="e", ipady=5, padx=0)

        # ============================================================================#

        # ===============================Data Table Frame============================#

        self.dataTableFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.dataTableFrame.pack(side=TOP, anchor="nw", pady=10, padx=90, fill="x")

        scrolly = Scrollbar(self.dataTableFrame, orient=VERTICAL)
        scrollx = Scrollbar(self.dataTableFrame, orient=HORIZONTAL)
        self.ProductTable = ttk.Treeview(self.dataTableFrame, columns=(
            "expenseID", "expenseDate", "expenseType", "expenseDescription", "expenseAmount"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, height=15)
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

        # ================================Label2 Frame=================================#

        self.Label2Frame = Frame(self.root, bg="#ffffff")
        self.Label2Frame.pack(side=TOP, anchor="nw", pady=5, padx=90, fill="x")

        # Total Expense
        self.totalExpenseLabel = Label(self.Label2Frame, text="Total Expense:", bg="#ffffff", fg="black", font="Arial 10 bold")
        self.totalExpenseLabel.pack(side=LEFT, anchor="w", pady=0, padx=0)

        self.expenseHereLabel = Label(self.Label2Frame, text="Total Expense Here", bg="#ffffff", fg="black", font="Arial 10")
        self.expenseHereLabel.pack(side=LEFT, anchor="w", pady=0, padx=10)

        # Print Button
        self.printButton = Button(self.Label2Frame, text="Print", width=20, height=1,
                                   bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                   command=lambda: [pdfData(), openPDF()])
        self.printButton.pack(side=RIGHT, anchor="e", ipady=5, padx=0)

        # ============================================================================#

        def showExpenseTable():
            self.flag = 0
            fromDate = self.fromDateEntry.get()
            toDate = self.toDateEntry.get()
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select * from expense where expenseDate between ? and ?", (fromDate, toDate))
                self.expenseData = cur.fetchall()

                cur.execute(f"select SUM(expenseAmount) from expense where expenseDate between ? and ?", (fromDate, toDate))
                self.totalExpense = cur.fetchone()
                self.expenseHereLabel.config(text=self.totalExpense[0])

                self.ProductTable.delete(*self.ProductTable.get_children())
                for data in self.expenseData:
                    self.ProductTable.insert('', END, values=data)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        showExpenseTable()

        def pdfData():
            if self.flag == 0:
                self.pdf.image('img/logo.png', 75, 8, 60)

                try:
                    self.pdf.set_font('Times', 'B', 14)
                    pdf.cell(0, 6, f'Expenses', 0, 1, 'C')
                    self.pdf.ln(10)


                    line_height = self.pdf.font_size * 1.5
                    col_width = self.pdf.epw / 4
                    self.pdf.set_font('Times', '', 10)

                    #Row1
                    self.pdf.multi_cell(35, line_height, 'From Date:', border=0,
                                   new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, self.fromDateEntry.get(), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    #Row2
                    self.pdf.multi_cell(35, line_height, 'To Date:', border=0,
                                   new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, self.toDateEntry.get(), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    expenseData = self.expenseData

                    expenseHeading = ("Expense ID", "Expense Date", "Expense Type", "Expense Description", "Expense Amount")
                    expenseData.insert(0, expenseHeading)

                    # Data Table
                    self.pdf.set_font("Times", size=10)
                    billline_height = self.pdf.font_size * 2
                    billcol_width = self.pdf.epw / 5

                    for row in expenseData:
                        for data in row:
                            pdf.multi_cell(billcol_width, billline_height, str(data), border=1,
                                           new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
                        pdf.ln(billline_height)

                    self.pdf.ln(5)
                    self.pdf.set_font('Times', 'B', 14)
                    pdf.cell(0, 6, f'Payment Details', 0, 1, 'L')
                    self.pdf.set_font("Times", size=10)

                    # Row5
                    self.pdf.multi_cell(35, line_height, 'Total Expense:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.totalExpense[0]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)


                except Exception as ex:
                    print(ex)

                self.fileName = 'Expense'
                self.pdf.output('ExpenseReport/'+f'{self.fileName}.pdf', 'F')
                self.flag = 1

        def openPDF():
            os.system(f'ExpenseReport\\{self.fileName}.pdf')


if __name__=="__main__":

    root=Tk()
    pdf = FPDF()
    obj=expenseReport(root, pdf)
    root.mainloop()