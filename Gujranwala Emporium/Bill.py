from tkinter import *
import sqlite3
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from tkcalendar import DateEntry
from fpdf import FPDF
import tkcalendar as tkc
import os

class bill:
    def __init__(self,root, pdf):
        self.root = root
        self.pdf = pdf
        self.root.title("Bill")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.ln(50)

        # ================================Variables==================================#

        self.propertyID = IntVar()
        self.propertyIDList = []
        self.propertyLocation = StringVar()
        self.clientPropertyData = []

        self.billID = IntVar()
        self.status = StringVar()
        self.receiveAmount = IntVar()
        self.dueDate = StringVar()
        self.installmentNo = StringVar()
        self.balance = IntVar()
        self.installmentAmount = IntVar()
        self.tempBalance = IntVar()
        self.tempReceiveAmount = StringVar()
        self.clientData = ()
        self.flag = 0


        # ==========================================================================#

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
        self.titleFrame.pack(side=TOP, anchor="nw", pady=0, padx=5, fill="x")

        self.titleLabel = Label(self.titleFrame, text="Client Billing", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        # ===========================================================================#

        # ===============================Space Frame=================================#

        self.spaceFrame = Frame(self.root, bg="#ffffff")
        self.spaceFrame.pack(side=TOP, anchor="nw", pady=20, padx=5, fill="x")

        # ===========================================================================#

        #================================Bottom Frame================================#

        self.bottomFrame = Frame(self.root, bg="#00479c", border=3)
        self.bottomFrame.pack(side=BOTTOM, anchor="nw", pady=0, padx=5, fill="x")

        self.bottomLabel = Label(self.bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white", font="Arial 9")
        self.bottomLabel.pack()

        #============================================================================#

        # =================================Info Frame================================#

        self.infoFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=0,
                               bg="#ffffff")
        self.infoFrame.pack(side=TOP, pady=0, padx=5, ipady=70, ipadx=55, fill="y")
        self.infoFrame.grid_columnconfigure(2, weight=1)

        # Search Client CNIC
        self.clientCnicLabel = Label(self.infoFrame, text="Client CNIC:", bg='#ffffff')
        self.clientCnicLabel.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.clientCnicEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0)
        self.clientCnicEntry.grid(row=1, column=0, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        self.searchClientbutton = Button(self.infoFrame, text="Search", bg='#00479c', fg="White",
                                   font="Arial 9", relief="flat", command=lambda: [showClient()])
        self.searchClientbutton.grid(row=1, column=1, sticky=W, padx=5, pady=5, ipadx=50, ipady=2)

        # Client Name
        self.clientname_label = Label(self.infoFrame, text="Client Name:", bg='#ffffff')
        self.clientname_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.clientnameLabel = Label(self.infoFrame, text="Client Name Here", bg='#ffffff')
        self.clientnameLabel.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # Client Contact
        self.clientcontact_label = Label(self.infoFrame, text="Client Contact:", bg='#ffffff')
        self.clientcontact_label.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        self.clientContactLabel = Label(self.infoFrame, text="Client Contact Here", bg='#ffffff')
        self.clientContactLabel.grid(row=2, column=4, sticky=W, padx=5, pady=5)

        # Search Property ID
        self.propertyIDLabel = Label(self.infoFrame, text="Property ID:", bg='#ffffff')
        self.propertyIDLabel.grid(row=0, column=3, sticky=W, padx=5, pady=5)

        self.propertyIDCombobox = ttk.Combobox(self.infoFrame, textvariable = self.propertyID, values=self.propertyIDList)
        self.propertyIDCombobox.grid(row=1, column=3, sticky=W, padx=5, pady=5, ipady=4, ipadx=25)

        self.selectPropertybutton = Button(self.infoFrame, text="Select", bg='#00479c', fg="White",
                                           font="Arial 9", relief="flat", command=lambda: [showProperty()])
        self.selectPropertybutton.grid(row=1, column=4, sticky=W, padx=5, pady=5, ipadx=50, ipady=2)

        # Property Location
        self.propertyLocationLabel = Label(self.infoFrame, text="Property Location:", bg='#ffffff')
        self.propertyLocationLabel.grid(row=3, column=0, sticky=W, padx=5, pady=10)

        self.propertyLocationEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                           highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                           textvariable=self.propertyLocation)
        self.propertyLocationEntry.grid(row=3, column=1, sticky=W, padx=5, pady=10, ipady=5, ipadx=30, columnspan=4)

        # Bill ID
        self.billIDLabel = Label(self.infoFrame, text="Bill ID:", bg='#ffffff')
        self.billIDLabel.grid(row=4, column=0, sticky=W, padx=5, pady=45)

        self.billIDEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.billID)
        self.billIDEntry.grid(row=4, column=1, sticky=W, padx=5, pady=45, ipady=5, ipadx=30)

        # Receive Date
        self.receiveDateLabel = Label(self.infoFrame, text="Receive Date:", bg='#ffffff')
        self.receiveDateLabel.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.receiveDateEntry = tkc.DateEntry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0, date_pattern="yyyy/mm/dd")
        self.receiveDateEntry.grid(row=5, column=1, sticky=W, padx=5, pady=5, ipady=4, ipadx=44)

        # Due Date
        self.dueDateLabel = Label(self.infoFrame, text="Due Date:", bg='#ffffff')
        self.dueDateLabel.grid(row=5, column=3, sticky=W, padx=5, pady=5)

        self.dueDateEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.dueDate)
        self.dueDateEntry.grid(row=5, column=4, sticky=W, padx=5, pady=5, ipady=4, ipadx=30)

        # Installment No
        self.installmentNoLabel = Label(self.infoFrame, text="Installment No:", bg='#ffffff')
        self.installmentNoLabel.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.installmentNoEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                 highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.installmentNo)
        self.installmentNoEntry.grid(row=6, column=1, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Installment Amount
        self.installmentAmountLabel = Label(self.infoFrame, text="Installment Amount:", bg='#ffffff')
        self.installmentAmountLabel.grid(row=6, column=3, sticky=W, padx=5, pady=5)

        self.installmentAmountEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                 highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.installmentAmount)
        self.installmentAmountEntry.grid(row=6, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Receive Amount
        self.receiveAmountLabel = Label(self.infoFrame, text="Receive Amount:", bg='#ffffff')
        self.receiveAmountLabel.grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.receiveAmountEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                        highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.receiveAmount)
        self.receiveAmountEntry.grid(row=7, column=1, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)
        self.receiveAmountEntry.bind("<KeyRelease>", self.balanceCalculation)

        # Balance
        self.balanceLabel = Label(self.infoFrame, text="Balance:", bg='#ffffff')
        self.balanceLabel.grid(row=7, column=3, sticky=W, padx=5, pady=5)

        self.balanceEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                            highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.balance)
        self.balanceEntry.grid(row=7, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Payment Type
        self.paymentTypeLabel = Label(self.infoFrame, text="Payment Type:", bg='#ffffff')
        self.paymentTypeLabel.grid(row=8, column=0, sticky=W, padx=5, pady=5)

        self.paymentTypeEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                 highlightcolor="#00479c", highlightthickness=1, borderwidth=0)
        self.paymentTypeEntry.grid(row=8, column=1, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Status
        self.statusLabel = Label(self.infoFrame, text="Status:", bg='#ffffff')
        self.statusLabel.grid(row=8, column=3, sticky=W, padx=5, pady=5)

        self.statusEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                 highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.status, state='disabled')
        self.statusEntry.grid(row=8, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Save Bill
        self.saveBillbutton = Button(self.infoFrame, text="Save", bg='#00479c', fg="White",
                                           font="Arial 9", relief="flat", command=lambda: [addBill()])
        self.saveBillbutton.grid(row=9, column=4, sticky=W, padx=5, pady=10, ipadx=73, ipady=5)

        # Clear Fields
        self.clearBillbutton = Button(self.infoFrame, text="Clear", bg='#00479c', fg="White",
                                     font="Arial 9", relief="flat", command=lambda: [clearBillFields()])
        self.clearBillbutton.grid(row=10, column=4, sticky=W, padx=5, pady=0, ipadx=71, ipady=5)

        # ===========================================================================#

        # # =================================Bill Frame================================#
        #
        # self.billFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1,
        #                        bg="#ffffff")
        # self.billFrame.pack(side=RIGHT, pady=0, padx=5, ipady=10, ipadx=30, fill="y")
        #
        # self.Logo = Image.open(r"img/Logo.png")
        # self.Logo = self.Logo.resize((150, 100), Image.ANTIALIAS)
        # self.Logo = ImageTk.PhotoImage(self.Logo)
        #
        # logoLabel = Label(self.billFrame, image=self.Logo, bg="#ffffff", relief="flat")
        # logoLabel.grid(row=0, column=0, sticky=W, padx=250, pady=50, columnspan=5)
        #
        # self.clientnameLabel_Bill = Label(self.billFrame, text="Client Name:", bg='#ffffff', font="Times 10 bold")
        # self.clientnameLabel_Bill.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        #
        # self.clientNameLabel_Bill = Label(self.billFrame, text="Client Name Here", bg='#ffffff', font="Times 10")
        # self.clientNameLabel_Bill.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        #
        # self.clientcnicLabel_Bill = Label(self.billFrame, text="Client CNIC:", bg='#ffffff', font="Times 10 bold")
        # self.clientcnicLabel_Bill.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        #
        # self.clientCNICLabel_Bill = Label(self.billFrame, text="Client CNIC Here", bg='#ffffff', font="Times 10")
        # self.clientCNICLabel_Bill.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        #
        # self.clientcontactLabel_Bill = Label(self.billFrame, text="Client Contact:", bg='#ffffff', font="Times 10 bold")
        # self.clientcontactLabel_Bill.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        #
        # self.clientContactLabel_Bill = Label(self.billFrame, text="Client Contact Here", bg='#ffffff', font="Times 10")
        # self.clientContactLabel_Bill.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        #
        # self.clientaddressLabel_Bill = Label(self.billFrame, text="Client Address:", bg='#ffffff', font="Times 10 bold")
        # self.clientaddressLabel_Bill.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        #
        # self.clientAddressLabel_Bill = Label(self.billFrame, text="Client Address Here", bg='#ffffff', font="Times 10")
        # self.clientAddressLabel_Bill.grid(row=4, column=1, sticky=W, padx=5, pady=5)
        #
        # self.propertyidLabel_Bill = Label(self.billFrame, text="Property ID:", bg='#ffffff', font="Times 10 bold")
        # self.propertyidLabel_Bill.grid(row=1, column=3, sticky=W, padx=5, pady=5)
        #
        # self.propertyIDLabel_Bill = Label(self.billFrame, text="Property ID Here", bg='#ffffff', font="Times 10")
        # self.propertyIDLabel_Bill.grid(row=1, column=4, sticky=W, padx=5, pady=5)
        #
        # self.propertypriceLabel_Bill = Label(self.billFrame, text="Property Price:", bg='#ffffff', font="Times 10 bold")
        # self.propertypriceLabel_Bill.grid(row=2, column=3, sticky=W, padx=5, pady=5)
        #
        # self.propertyPriceLabel_Bill = Label(self.billFrame, text="Property Price Here", bg='#ffffff', font="Times 10")
        # self.propertyPriceLabel_Bill.grid(row=2, column=4, sticky=W, padx=5, pady=5)
        #
        # self.downpaymentLabel_Bill = Label(self.billFrame, text="Down Payment:", bg='#ffffff', font="Times 10 bold")
        # self.downpaymentLabel_Bill.grid(row=3, column=3, sticky=W, padx=5, pady=5)
        #
        # self.downPaymentLabel_Bill = Label(self.billFrame, text="Down Payment Here", bg='#ffffff', font="Times 10")
        # self.downPaymentLabel_Bill.grid(row=3, column=4, sticky=W, padx=5, pady=5)
        #
        # self.propertylocationLabel_Bill = Label(self.billFrame, text="Property Location:", bg='#ffffff', font="Times 10 bold")
        # self.propertylocationLabel_Bill.grid(row=4, column=3, sticky=W, padx=5, pady=5)
        #
        # self.propertyLocationLabel_Bill = Label(self.billFrame, text="Property Location Here", bg='#ffffff', font="Times 10")
        # self.propertyLocationLabel_Bill.grid(row=4, column=4, sticky=W, padx=5, pady=5)
        #
        # self.billidLabel_Bill = Label(self.billFrame, text="Bill ID:", bg='#ffffff', font="Times 10 bold")
        # self.billidLabel_Bill.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        #
        # self.billIDLabel_Bill = Label(self.billFrame, text="Bill ID Here", bg='#ffffff', font="Times 10")
        # self.billIDLabel_Bill.grid(row=5, column=1, sticky=W, padx=5, pady=25)
        #
        # self.receivedateLabel_Bill = Label(self.billFrame, text="Receive Date:", bg='#ffffff', font="Times 10 bold")
        # self.receivedateLabel_Bill.grid(row=6, column=0, sticky=W, padx=5, pady=5)
        #
        # self.receiveDateLabel_Bill = Label(self.billFrame, text="Receive Date Here", bg='#ffffff', font="Times 10")
        # self.receiveDateLabel_Bill.grid(row=6, column=1, sticky=W, padx=5, pady=5)
        #
        # self.duedateLabel_Bill = Label(self.billFrame, text="Due Date:", bg='#ffffff', font="Times 10 bold")
        # self.duedateLabel_Bill.grid(row=6, column=3, sticky=W, padx=5, pady=5)
        #
        # self.dueDateLabel_Bill = Label(self.billFrame, text="Due Date Here", bg='#ffffff', font="Times 10")
        # self.dueDateLabel_Bill.grid(row=6, column=4, sticky=W, padx=5, pady=5)
        #
        # self.installmentnoLabel_Bill = Label(self.billFrame, text="Installment No:", bg='#ffffff', font="Times 10 bold")
        # self.installmentnoLabel_Bill.grid(row=7, column=0, sticky=W, padx=5, pady=5)
        #
        # self.installmentNoLabel_Bill = Label(self.billFrame, text="Installment No Here", bg='#ffffff', font="Times 10")
        # self.installmentNoLabel_Bill.grid(row=7, column=1, sticky=W, padx=5, pady=5)
        #
        # self.installmentamountLabel_Bill = Label(self.billFrame, text="Installment Amount:", bg='#ffffff', font="Times 10 bold")
        # self.installmentamountLabel_Bill.grid(row=7, column=3, sticky=W, padx=5, pady=5)
        #
        # self.installmentAmountLabel_Bill = Label(self.billFrame, text="Installment Amount Here", bg='#ffffff', font="Times 10")
        # self.installmentAmountLabel_Bill.grid(row=7, column=4, sticky=W, padx=5, pady=5)
        #
        # self.receiveamountLabel_Bill = Label(self.billFrame, text="Receive Amount:", bg='#ffffff', font="Times 10 bold")
        # self.receiveamountLabel_Bill.grid(row=8, column=0, sticky=W, padx=5, pady=5)
        #
        # self.receiveAmountLabel_Bill = Label(self.billFrame, text="Receive Amount Here", bg='#ffffff', font="Times 10")
        # self.receiveAmountLabel_Bill.grid(row=8, column=1, sticky=W, padx=5, pady=5)
        #
        # self.balanceamountLabel_Bill = Label(self.billFrame, text="Balance:", bg='#ffffff',
        #                                          font="Times 10 bold")
        # self.balanceamountLabel_Bill.grid(row=8, column=3, sticky=W, padx=5, pady=5)
        #
        # self.balanceAmountLabel_Bill = Label(self.billFrame, text="Balance Here", bg='#ffffff',
        #                                          font="Times 10")
        # self.balanceAmountLabel_Bill.grid(row=8, column=4, sticky=W, padx=5, pady=5)

        # Print Bill
        self.printBillbutton = Button(self.infoFrame, text="Print", bg='#00479c', fg="White",
                                     font="Arial 9", relief="flat", command=lambda: [pdfData(), openPDF()])
        self.printBillbutton.grid(row=11, column=4, sticky=W, padx=5, pady=10, ipadx=73, ipady=5)

        # ===========================================================================#


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
                    self.clientData = cur.fetchone()
                    if self.clientData != None:
                        cur.execute("select * from property where client_cnic=?", (self.clientCnicEntry.get(),))
                        self.clientPropertyData = cur.fetchall()
                        if self.clientPropertyData != None:
                            for data in range(len(self.clientPropertyData)):
                                self.propertyIDList.append(self.clientPropertyData[data][0])
                            self.propertyIDCombobox['values'] = self.propertyIDList
                        else:
                            messagebox.showerror("Error", "No Property Assigned to this Client", parent=self.root)

                        self.clientnameLabel.config(text=self.clientData[1])
                        self.clientContactLabel.config(text=self.clientData[2])
                    else:
                        messagebox.showerror("Error", "This Client does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def showProperty():
            self.flag = 0
            for data in self.clientPropertyData:
                if self.propertyID.get() == data[0]:
                    self.propertyLocation.set(data[10])
            getBill()
            if self.propertyID.get() == 0:
                messagebox.showerror("Error", "Please Select Property ID", parent=self.root)

        def addBill():
            if IsValid():
                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
                #                                      database="gujranwalaemporium")
                # cursor = connection.cursor(prepared=True)
                try:
                    if self.billIDEntry.get() == "":
                        messagebox.showerror("Error", "Bill ID Must Required", parent=self.root)
                    else:
                        cur.execute("select status from bill where billID=?", (self.billIDEntry.get(),))
                        billStatusData = cur.fetchone()
                        if billStatusData[0] != 'Paid':
                            if self.balanceEntry.get() == "0":
                                self.status.set("Paid")
                            if self.tempReceiveAmount.get() != 'None':
                                self.receiveAmount.set(int(self.tempReceiveAmount.get())+int(self.receiveAmountEntry.get()))
                            else:
                                self.receiveAmount.set(self.receiveAmountEntry.get())
                            cur.execute("Update bill set receiveDate=?,receiveAmount=?,paymentType=?,balance=?,status=? where billID=?",
                                        (
                                         self.receiveDateEntry.get(),
                                         self.receiveAmount.get(),
                                         self.paymentTypeEntry.get(),
                                         self.balanceEntry.get(),
                                         self.status.get(),

                                         self.billIDEntry.get()
                                         ))
                            con.commit()
                            # billPreview()
                            messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)

                        else:
                            messagebox.showinfo("Sucess", "This Bill Is Already Paid", parent=self.root)
                except EXCEPTION as ex:
                    messagebox.showerror("Error", f"due to : {str(ex)}")

        def getBill():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select * from bill where propertyID=? and status=?", (self.propertyID.get(),"Unpaid",))
                billData = cur.fetchone()
                self.billID.set(billData[0])
                self.dueDate.set(billData[3])
                self.installmentNo.set(billData[4])
                self.installmentAmount.set(billData[5])
                self.tempReceiveAmount.set(billData[6])
                self.balance.set(billData[8])
                self.tempBalance.set(billData[8])
                self.status.set(billData[9])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        def clearBillFields():
            self.clientCnicEntry.delete(0, 'end')
            self.clientnameLabel.config(text="Client Name Here")
            self.clientContactLabel.config(text="Client Contact Here")
            self.propertyIDList = []
            self.propertyLocationEntry.delete(0, 'end')
            self.billIDEntry.delete(0, 'end')
            self.dueDateEntry.delete(0, 'end')
            self.installmentNoEntry.delete(0, 'end')
            self.installmentAmountEntry.delete(0, 'end')
            self.receiveAmountEntry.delete(0, 'end')
            self.balanceEntry.delete(0, 'end')
            self.paymentTypeEntry.delete(0, 'end')
            self.statusEntry.delete(0, 'end')

        clearBillFields()

        # def billPreview():
        #     self.clientCNICLabel_Bill.config(text=self.clientData[0])
        #     self.clientNameLabel_Bill.config(text=self.clientData[1])
        #     self.clientContactLabel_Bill.config(text=self.clientData[2])
        #     self.clientAddressLabel_Bill.config(text=self.clientData[3])
        #
        #     for data in self.clientPropertyData:
        #         if self.propertyID.get() == data[0]:
        #             self.propertyIDLabel_Bill.config(text=data[0])
        #             self.propertyPriceLabel_Bill.config(text=data[4])
        #             self.downPaymentLabel_Bill.config(text=data[5])
        #             self.propertyLocationLabel_Bill.config(text=data[10])
        #
        #     # con = sqlite3.connect(database=r'marketing.db')
        #     # cur = con.cursor()
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     cursor.execute("select * from bill where billID=?", (self.billID.get(),))
        #     billData = cursor.fetchone()
        #     billList = list(billData)
        #     billList.pop(1)
        #     billData = tuple(billList)
        #
        #     self.billIDLabel_Bill.config(text=billData[0])
        #     self.receiveDateLabel_Bill.config(text=billData[1])
        #     self.dueDateLabel_Bill.config(text=billData[2])
        #     self.installmentNoLabel_Bill.config(text=billData[3])
        #     self.installmentAmountLabel_Bill.config(text=billData[4])
        #     self.receiveAmountLabel_Bill.config(text=billData[5])
        #     self.balanceAmountLabel_Bill.config(text=billData[7])

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
                    self.pdf.cell(0, 6, f'Client Bill', 0, 1, 'C')
                    self.pdf.ln(10)
                    cur.execute("select * from client where client_cnic=?", (self.clientCnicEntry.get(),))
                    clientData = cur.fetchone()

                    cur.execute("select * from property where propertyID=?", (self.propertyID.get(),))
                    clientPropertyData = cur.fetchall()

                    for data in clientPropertyData:
                        print(type(clientPropertyData))
                        if self.propertyID.get() == data[0]:
                            self.propertyData = clientPropertyData[0]
                            print(self.propertyData)

                    line_height = self.pdf.font_size * 1.5
                    col_width = self.pdf.epw / 4
                    self.pdf.set_font('Times', '', 10)

                    self.pdf.line(10, 75, 200, 75)
                    self.pdf.line(10, 75, 10, 105)
                    self.pdf.line(200, 75, 200, 105)
                    self.pdf.line(10, 105, 200, 105)

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

                    self.pdf.multi_cell(col_width, line_height, str(clientData[3]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(40, line_height, 'Property Location:', border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.multi_cell(col_width, line_height, str(self.propertyData[10]), border=0,
                                        new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)

                    self.pdf.ln(10)

                    # Data Table
                    cur.execute("select billID,receiveDate,dueDate,installementNo,installmentAmount,receiveAmount,paymentType,balance,status from bill where billID=?", (self.billID.get(),))
                    billData = cur.fetchall()
                    billHeading = ("Bill ID", "Receive Date", "Due Date", "Installment NO", "Installment Amount", "Receive Amount", "Payment Type", "Balance", "Status")
                    billData.insert(0,billHeading)
                    print(billData)

                    self.pdf.set_font("Times", size=10)
                    billline_height = self.pdf.font_size * 2
                    billcol_width = self.pdf.epw / 9

                    for row in billData:
                        for data in row:
                            pdf.multi_cell(billcol_width, billline_height, str(data), border=1,
                                           new_x="RIGHT", new_y="TOP", max_line_height=self.pdf.font_size)
                        pdf.ln(billline_height)

                except Exception as ex:
                    print(ex)

                self.fileName = f'Bill{billData[1][0]}'
                print(self.fileName)
                self.pdf.output('Bills/'+f'{self.fileName}.pdf', 'F')
                self.flag = 1

        def openPDF():
            os.system(f'Bills\\{self.fileName}.pdf')

        def IsValid():
            if self.clientCnicEntry.get() == '':
                messagebox.showerror("Error", "Client CNIC is Required", parent=self.root)
                return False

            if self.clientCnicEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Client CNIC", parent=self.root)
                return False

            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            cur.execute("select * from client where client_cnic=?", (self.clientCnicEntry.get(),))
            client_cnic = cur.fetchone()

            if client_cnic == None:
                messagebox.showerror("Error", "This Client does not Exist", parent=self.root)
                return False

            if self.propertyID.get() == '':
                messagebox.showerror("Error", "Select Property", parent=self.root)
                return False

            if self.receiveAmountEntry.get() == '' or self.receiveAmountEntry.get() == '0' or self.receiveAmountEntry.get() == 0:
                messagebox.showerror("Error", "Receive Amount is Required", parent=self.root)
                return False

            if self.receiveAmountEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Receive Amount", parent=self.root)
                return False

            if self.paymentTypeEntry.get() == '':
                messagebox.showerror("Error", "Payment Type is Required", parent=self.root)
                return False

            return True

    def balanceCalculation(self, event):
        try:
            balance = int(self.tempBalance.get())-int(self.receiveAmountEntry.get())
            self.balance.set(balance)
        except Exception as ex:
            pass


if __name__=="__main__":

    root=Tk()
    pdf = FPDF()
    obj=bill(root, pdf)
    root.mainloop()