from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from fpdf import FPDF
import os
import mysql.connector

class ClientReport:
    def __init__(self,root, pdf):
        self.root = root
        self.pdf = pdf
        self.root.title("Client Report")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.ln(50)

        # ================================Variables==================================#

        self.propertyID = IntVar()
        self.propertyIDList = []
        self.clientPropertyData = []
        self.propertyAmount = IntVar()
        self.downPayment = IntVar()
        self.discount = IntVar()
        self.balance = IntVar()
        self.receive = IntVar()
        self.possessionAmount = IntVar()
        self.fileName = StringVar()
        self.flag = 0

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 550
        window_width = 900
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.root.state('zoomed')

        # ===========================================================================#

        # ===============================Title Frame=================================#

        self.titleFrame = Frame(self.root, bg="#00479c")
        self.titleFrame.pack(side=TOP, anchor="nw", pady=0, padx=5, fill="x")

        self.titleLabel = Label(self.titleFrame, text="Client Report", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        # ===========================================================================#

        # ================================Bottom Frame===============================#

        self.bottomFrame = Frame(self.root, bg="#00479c", border=3)
        self.bottomFrame.pack(side=BOTTOM, anchor="nw", pady=0, padx=5, fill="x")

        self.bottomLabel = Label(self.bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white",
                                 font="Arial 9")
        self.bottomLabel.pack()

        # ===========================================================================#

        # ===============================Client Info Frame===========================#

        self.clientInfoFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.clientInfoFrame.pack(side=TOP, anchor="nw", pady=10, padx=50, fill="x")

        self.clientInfoFrame.grid_columnconfigure(4, weight=1)

        # Client CNIC
        self.clientcnic_label = Label(self.clientInfoFrame, text="Client CNIC:", bg='#ffffff', font="Arial 10 bold")
        self.clientcnic_label.grid(row=0, column=0, sticky=W, padx=15, pady=5)

        self.clientCnicEntry = Entry(self.clientInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0)
        self.clientCnicEntry.grid(row=0, column=1, sticky=W, padx=15, pady=5, ipady=5, ipadx=30)

        self.searchbutton = Button(self.clientInfoFrame, text="Search", bg='#00479c', fg="White",
                                  font="Arial 9", relief="flat", command=lambda:[showClient()])
        self.searchbutton.grid(row=1, column=1, sticky=W, padx=15, pady=5, ipadx=67, ipady=5)

        # Property ID
        self.propertyIDLabel = Label(self.clientInfoFrame, text="Property ID:", bg='#ffffff', font="Arial 10 bold")
        self.propertyIDLabel.grid(row=0, column=2, sticky=W, padx=5, pady=5)

        self.propertyIDCombobox = ttk.Combobox(self.clientInfoFrame, textvariable=self.propertyID, values=self.propertyIDList)
        self.propertyIDCombobox.grid(row=0, column=3, sticky=W, padx=5, pady=5, ipady=4, ipadx=18)

        self.selectPropertybutton = Button(self.clientInfoFrame, text="Select", bg='#00479c', fg="White",
                                           font="Arial 9", relief="flat", command=lambda: [showProperty()])
        self.selectPropertybutton.grid(row=1, column=3, sticky=W, padx=5, pady=5, ipadx=67, ipady=5)

        # Client Name
        self.clientname_label = Label(self.clientInfoFrame, text="Client Name:", bg='#ffffff', font="Arial 10 bold")
        self.clientname_label.grid(row=0, column=5, sticky=W, padx=15, pady=5)

        self.clientnameLabel = Label(self.clientInfoFrame, text="Client Name Here", bg='#ffffff')
        self.clientnameLabel.grid(row=0, column=6, sticky=W, padx=15, pady=5)

        # Client Contact
        self.clientcontact_label = Label(self.clientInfoFrame, text="Client Contact:", bg='#ffffff', font="Arial 10 bold")
        self.clientcontact_label.grid(row=2, column=0, sticky=W, padx=15, pady=5)

        self.clientContactLabel = Label(self.clientInfoFrame, text="Client Contact Here", bg='#ffffff')
        self.clientContactLabel.grid(row=2, column=1, sticky=W, padx=15, pady=5)

        # Client Address
        self.clientaddress_label = Label(self.clientInfoFrame, text="Client Address:", bg='#ffffff', font="Arial 10 bold")
        self.clientaddress_label.grid(row=1, column=5, sticky=W, padx=15, pady=5)

        self.clientAddressLabel = Label(self.clientInfoFrame, text="Client Address Here", bg='#ffffff')
        self.clientAddressLabel.grid(row=1, column=6, sticky=W, padx=15, pady=5)

        # Property Location
        self.propertyLocation_label = Label(self.clientInfoFrame, text="Property Location:", bg='#ffffff', font="Arial 10 bold")
        self.propertyLocation_label.grid(row=3, column=0, sticky=W, padx=15, pady=5)

        self.propertyLocationLabel = Label(self.clientInfoFrame, text="Property Location Here", bg='#ffffff')
        self.propertyLocationLabel.grid(row=3, column=1, sticky=W, padx=15, pady=5)

        # Property Size
        self.propertysize_label = Label(self.clientInfoFrame, text="Property Size:", bg='#ffffff', font="Arial 10 bold")
        self.propertysize_label.grid(row=2, column=5, sticky=W, padx=15, pady=5)

        self.propertySizeLabel = Label(self.clientInfoFrame, text="Property Size Here", bg='#ffffff')
        self.propertySizeLabel.grid(row=2, column=6, sticky=W, padx=15, pady=5)

        # Property Amount
        self.plotamount_label = Label(self.clientInfoFrame, text="Property Amount:", bg='#ffffff', font="Arial 10 bold")
        self.plotamount_label.grid(row=3, column=5, sticky=W, padx=15, pady=5)

        self.plotAmountLabel = Label(self.clientInfoFrame, text="Property Amount Here", bg='#ffffff')
        self.plotAmountLabel.grid(row=3, column=6, sticky=W, padx=15, pady=5)

        # ===========================================================================#

        # ===============================Data Table Frame============================#

        self.dataTableFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.dataTableFrame.pack(side=TOP, anchor="nw", pady=0, padx=50, fill="x")

        scrolly = Scrollbar(self.dataTableFrame, orient=VERTICAL)
        scrollx = Scrollbar(self.dataTableFrame, orient=HORIZONTAL)
        self.ProductTable = ttk.Treeview(self.dataTableFrame, columns=("billID", "receiveDate", "dueDate", "installmentNo", "installmentAmount", "receiveAmount", "paymentType", "balance", "status"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, height=12)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("#0",text="",anchor=CENTER)
        self.ProductTable.heading("billID", text="Bill ID")
        self.ProductTable.heading("receiveDate", text="Receive Date")
        self.ProductTable.heading("dueDate", text="Due Date")
        self.ProductTable.heading("installmentNo", text="Installment NO")
        self.ProductTable.heading("installmentAmount", text="Installment Amount")
        self.ProductTable.heading("receiveAmount", text="Receive Amount")
        self.ProductTable.heading("paymentType", text="Payment Type")
        self.ProductTable.heading("balance", text="Balance")
        self.ProductTable.heading("status", text="Status")
        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.column("#0", width=0,  stretch=NO)
        self.ProductTable.column("billID", width=100)
        self.ProductTable.column("receiveDate", width=100)
        self.ProductTable.column("dueDate", width=100)
        self.ProductTable.column("installmentNo", width=100)
        self.ProductTable.column("installmentAmount", width=100)
        self.ProductTable.column("receiveAmount", width=100)
        self.ProductTable.column("paymentType", width=100)
        self.ProductTable.column("balance", width=100)
        self.ProductTable.column("status", width=100)

        # ===========================================================================#

        # ==================================Account Frame============================#

        self.accountFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.accountFrame.pack(side=TOP, anchor="nw", pady=10, padx=50, fill="x")

        self.accountFrame.grid_columnconfigure(2, weight=1)

        # Total Received
        self.totalreceived_label = Label(self.accountFrame, text="Total Received:", bg='#ffffff', font="Arial 10 bold")
        self.totalreceived_label.grid(row=0, column=0, sticky=W, padx=15, pady=5)

        self.totalReceivedLabel = Label(self.accountFrame, text="Total Received Amount Here", bg='#ffffff')
        self.totalReceivedLabel.grid(row=0, column=1, sticky=W, padx=15, pady=5)

        # Balance
        self.balance_label = Label(self.accountFrame, text="Balance Amount:", bg='#ffffff', font="Arial 10 bold")
        self.balance_label.grid(row=1, column=0, sticky=W, padx=15, pady=5)

        self.balanceLabel = Label(self.accountFrame, text="Balance Amount Here", bg='#ffffff')
        self.balanceLabel.grid(row=1, column=1, sticky=W, padx=15, pady=5)

        # Down Payment
        self.downPayment_label = Label(self.accountFrame, text="Down Payment:", bg='#ffffff', font="Arial 10 bold")
        self.downPayment_label.grid(row=0, column=3, sticky=W, padx=15, pady=5)

        self.downPaymentLabel = Label(self.accountFrame, text="Down Payment Here", bg='#ffffff')
        self.downPaymentLabel.grid(row=0, column=4, sticky=W, padx=15, pady=5)

        # Possession
        self.possession_label = Label(self.accountFrame, text="Possession:", bg='#ffffff', font="Arial 10 bold")
        self.possession_label.grid(row=1, column=3, sticky=W, padx=15, pady=5)

        self.possessionLabel = Label(self.accountFrame, text="Possession Here", bg='#ffffff')
        self.possessionLabel.grid(row=1, column=4, sticky=W, padx=15, pady=5)

        # Discount
        self.discount_label = Label(self.accountFrame, text="Discount:", bg='#ffffff', font="Arial 10 bold")
        self.discount_label.grid(row=2, column=3, sticky=W, padx=15, pady=5)

        self.discountLabel = Label(self.accountFrame, text="Discount Here", bg='#ffffff')
        self.discountLabel.grid(row=2, column=4, sticky=W, padx=15, pady=5)

        # Print Report
        self.printbutton = Button(self.root, text="Save & Print", bg='#00479c', fg="White",
                                   font="Arial 9", relief="flat", command=lambda: [pdfData(), openPDF()])
        self.printbutton.pack(side=TOP, pady=5, padx=50, ipady=5, ipadx=30, anchor="e")

        # ===========================================================================#

        #================================Search Record===============================#

        def showClient():
            self.flag = 0
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            self.propertyIDList = []
            try:
                if self.clientCnicEntry.get() == "":
                    messagebox.showerror("Error", "Client CNIC Must Required", parent=self.root)
                else:
                    cur.execute("select * from client where client_cnic=?", (self.clientCnicEntry.get(),))
                    clientData = cur.fetchone()
                    if clientData != None:
                        cur.execute("select * from property where client_cnic=?", (self.clientCnicEntry.get(),))
                        self.clientPropertyData = cur.fetchall()
                        # print(self.clientPropertyData)
                        if self.clientPropertyData != None:
                            for data in range(len(self.clientPropertyData)):
                                self.propertyIDList.append(self.clientPropertyData[data][0])
                            # print(self.propertyIDList)
                            self.propertyIDCombobox['values'] = self.propertyIDList
                        else:
                            messagebox.showerror("Error", "No Property Assigned to this Client", parent=self.root)

                        self.clientnameLabel.config(text=clientData[1])
                        self.clientContactLabel.config(text=clientData[2])
                        self.clientAddressLabel.config(text=clientData[3])
                    else:
                        messagebox.showerror("Error", "This Client does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def showProperty():
            self.flag = 0
            for data in self.clientPropertyData:
                if self.propertyID.get() == data[0]:
                    self.propertySizeLabel.config(text=data[3])
                    self.plotAmountLabel.config(text=data[4])
                    self.propertyAmount = int(data[4])
                    self.downPaymentLabel.config(text=data[5])
                    self.downPayment = int(data[5])
                    self.discountLabel.config(text=data[8])
                    self.discount = int(data[8])
                    self.propertyLocationLabel.config(text=data[10])
                    self.possessionLabel.config(text=data[13])
                    self.possessionAmount = int(data[13])
                    showBill()
                    account()
            if self.propertyID.get() == 0:
                messagebox.showerror("Error", "Please Select Property ID", parent=self.root)

        def showBill():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select * from bill where propertyID=?", (self.propertyID.get(),))
                rows = cur.fetchall()
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in rows:
                    billrowList = list(row)
                    billrowList.pop(1)
                    row = tuple(billrowList)
                    self.ProductTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        def account():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select SUM(receiveAmount), SUM(balance) from bill where propertyID=?", (self.propertyID.get(),))
                accountData = cur.fetchone()
                if accountData[0]==None:
                    ra = 0
                else:
                    ra = accountData[0]
                self.receive = (float(ra)+float(self.downPayment))
                self.totalReceivedLabel.config(text=self.receive)
                self.balance = int(accountData[1])
                self.balanceLabel.config(text=self.balance)
                print(accountData)
            except Exception as ex:
                messagebox.showerror("Error account", f"due to : {str(ex)}", parent=self.root)

        def pdfData():
            if self.flag == 0:
                self.pdf.image('img/logo.png', 75, 8, 60)

                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
                #                                      database="gujranwalaemporium")
                # cursor = connection.cursor(prepared=True)
                try:
                    self.pdf.set_font('Times', 'B', 14)
                    pdf.cell(0, 6, f'Payment Schedule', 0, 1, 'C')
                    self.pdf.ln(10)
                    cur.execute("select * from client where client_cnic=?", (self.clientCnicEntry.get(),))
                    clientData = cur.fetchone()

                    cur.execute("select * from property where propertyID=?", (self.propertyID.get(),))
                    clientPropertyData = cur.fetchall()

                    for data in clientPropertyData:
                        # print(type(clientPropertyData))
                        if self.propertyID.get() == data[0]:
                            self.propertyData = clientPropertyData[0]
                            # print(self.propertyData)

                    line_height = self.pdf.font_size * 1.5
                    col_width = self.pdf.epw / 4
                    self.pdf.set_font('Times', '', 10)

                    self.pdf.line(10, 75, 200, 75)
                    self.pdf.line(10, 75, 10, 113)
                    self.pdf.line(200, 75, 200, 113)
                    self.pdf.line(10, 113, 200, 113)

                    #Row1
                    self.pdf.multi_cell(35, line_height, 'Client Name:', border=0,
                                   new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, clientData[1], border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(40, line_height, 'Property ID:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.propertyData[0]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    #Row2
                    self.pdf.multi_cell(35, line_height, 'Client CNIC:', border=0,
                                   new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(clientData[0]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(40, line_height, 'Property Price:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.propertyData[4]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    #Row3
                    self.pdf.multi_cell(35, line_height, 'Client Contact:', border=0,
                                   new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(clientData[2]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(40, line_height, 'Down Payment:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.propertyData[5]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    #Row4
                    self.pdf.multi_cell(35, line_height, 'Client Address:', border=0,
                                   new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(150, line_height, str(clientData[3]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    self.pdf.multi_cell(35, line_height, 'Property Location:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.propertyData[10]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(15)

                    # Data Table
                    cur.execute("select billID,receiveDate,dueDate,installementNo,installmentAmount,receiveAmount,paymentType,balance,status from bill where propertyID=?", (self.propertyID.get(),))
                    billData = cur.fetchall()
                    billHeading = ("Bill ID", "Receive Date", "Due Date", "Installment NO", "Installment Amount", "Receive Amount", "Payment Type", "Balance", "Status")
                    billData.insert(0,billHeading)
                    # print(billData)

                    self.pdf.set_font("Times", size=10)
                    billline_height = self.pdf.font_size * 2
                    billcol_width = self.pdf.epw / 9

                    for row in billData:
                        for data in row:
                            pdf.multi_cell(billcol_width, billline_height, str(data), border=1,
                                           new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
                        pdf.ln(billline_height)

                    self.pdf.ln(5)
                    self.pdf.set_font('Times', 'B', 14)
                    pdf.cell(0, 6, f'Payment Details', 0, 1, 'L')
                    self.pdf.set_font("Times", size=10)

                    # Row5
                    self.pdf.multi_cell(35, line_height, 'Received Amount:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.receive), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    # Row6
                    self.pdf.multi_cell(35, line_height, 'Balance:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.balance), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    # Row7
                    self.pdf.multi_cell(35, line_height, 'Discount:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.propertyData[8]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(line_height)

                    # Row8
                    self.pdf.multi_cell(35, line_height, 'Possession:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.propertyData[13]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
                except Exception as ex:
                    print(ex)

                self.fileName = clientData[1]
                self.pdf.output('ClientReport/'+f'{(self.fileName).replace(" ", "")}.pdf', 'F')
                self.flag = 1

        def openPDF():
            os.system(f'ClientReport\\{(self.fileName).replace(" ", "")}.pdf')


        # ===========================================================================#

if __name__=="__main__":

    root=Tk()
    pdf = FPDF()
    obj=ClientReport(root, pdf)
    root.mainloop()