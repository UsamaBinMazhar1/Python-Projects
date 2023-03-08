from tkinter import *
import sqlite3
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta
import tkcalendar as tkc

class Assign_property:
    def __init__(self,root):
        self.root = root
        self.root.title("Assign Property")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        # ================================Variables==================================#

        self.propertyID = IntVar()
        self.propertySize = StringVar()
        self.propertyPrice = IntVar()
        self.downPayment = IntVar()
        self.totalInstallments = StringVar()
        self.pricePerInstallment = IntVar()
        self.discount = IntVar()
        self.status = StringVar()
        self.propertyLocation = StringVar()
        self.propertyDescription = StringVar()

        self.clientCnic = IntVar()
        self.clientName = StringVar()
        self.clientContact = StringVar()
        self.clientAddress = StringVar()
        self.installmentPlan = StringVar()
        self.installmentPlanList = ["Monthly", "Quarterly", "Six Month", "Annually"]
        self.result = IntVar()
        self.prevlaue = ''
        self.billID = IntVar()
        self.clientTag = 0
        self.propertyTag = 0
        self.dp = IntVar()
        self.pa = IntVar()
        self.possessionAmount = IntVar()
        self.discountedAmount = IntVar()

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

        self.titleLabel = Label(self.titleFrame, text="Assign Property", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        #===========================================================================#

        # =============================Client Info Frame============================#

        self.clientInfoFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg="#ffffff")
        self.clientInfoFrame.pack(side=TOP, anchor="nw", pady=10, padx=50, fill="x")
        self.clientInfoFrame.grid_columnconfigure(2, weight=1)

        # Search Client CNIC
        self.clientCnicLabel = Label(self.clientInfoFrame, text="Client CNIC:", bg='#ffffff')
        self.clientCnicLabel.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.clientCnicEntry = Entry(self.clientInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0)
        self.clientCnicEntry.grid(row=1, column=0, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        self.searchClientbutton = Button(self.clientInfoFrame, text="Search", bg='#00479c', fg="White",
                                   font="Arial 9", relief="flat", command=lambda: [showClient()])
        self.searchClientbutton.grid(row=1, column=1, sticky=W, padx=5, pady=5, ipadx=50, ipady=2)

        # Client Name
        self.clientname_label = Label(self.clientInfoFrame, text="Client Name:", bg='#ffffff', font="Arial 10 bold")
        self.clientname_label.grid(row=0, column=3, sticky=W, padx=5, pady=5)

        self.clientnameLabel = Label(self.clientInfoFrame, text="Client Name Here", bg='#ffffff')
        self.clientnameLabel.grid(row=0, column=4, sticky=W, padx=5, pady=5)

        # Client Contact
        self.clientcontact_label = Label(self.clientInfoFrame, text="Client Contact:", bg='#ffffff', font="Arial 10 bold")
        self.clientcontact_label.grid(row=1, column=3, sticky=W, padx=5, pady=5)

        self.clientContactLabel = Label(self.clientInfoFrame, text="Client Contact Here", bg='#ffffff')
        self.clientContactLabel.grid(row=1, column=4, sticky=W, padx=5, pady=5)

        # Client Address
        self.clientaddress_label = Label(self.clientInfoFrame, text="Client Address:", bg='#ffffff', font="Arial 10 bold")
        self.clientaddress_label.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        self.clientAddressLabel = Label(self.clientInfoFrame, text="Client Address Here", bg='#ffffff')
        self.clientAddressLabel.grid(row=2, column=4, sticky=W, padx=5, pady=5)

        # ===========================================================================#

        # =============================Property Info Frame===========================#

        self.PropertyInfoFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg="#ffffff")
        self.PropertyInfoFrame.pack(side=TOP, anchor="nw", pady=0, padx=50, fill="x")
        self.PropertyInfoFrame.grid_columnconfigure(2, weight=1)

        # Search Property ID
        self.propertyIDLabel = Label(self.PropertyInfoFrame, text="Property ID:", bg='#ffffff')
        self.propertyIDLabel.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.propertyIDEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0)
        self.propertyIDEntry.grid(row=1, column=0, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        self.searchPropertybutton = Button(self.PropertyInfoFrame, text="Search", bg='#00479c', fg="White",
                                   font="Arial 9", relief="flat", command=lambda: [showProperty()])
        self.searchPropertybutton.grid(row=1, column=1, sticky=W, padx=5, pady=5, ipadx=50, ipady=2)

        # Property Size
        self.propertysize_label = Label(self.PropertyInfoFrame, text="Property Size:", bg='#ffffff',
                                         font="Arial 10 bold")
        self.propertysize_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.propertySizeLabel = Label(self.PropertyInfoFrame, text="Property Size Here", bg='#ffffff')
        self.propertySizeLabel.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # Property Price
        self.propertyprice_label = Label(self.PropertyInfoFrame, text="Property Price:", bg='#ffffff',
                                        font="Arial 10 bold")
        self.propertyprice_label.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        self.propertyPriceLabel = Label(self.PropertyInfoFrame, text="Property Price Here", bg='#ffffff')
        self.propertyPriceLabel.grid(row=2, column=4, sticky=W, padx=5, pady=5)

        # Property Price Per Feet
        self.propertypriceperfeet_label = Label(self.PropertyInfoFrame, text="Property Price Per Feet:", bg='#ffffff',
                                         font="Arial 10 bold")
        self.propertypriceperfeet_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.propertyPricePerFeetLabel = Label(self.PropertyInfoFrame, text="Property Price Per Feet Here", bg='#ffffff')
        self.propertyPricePerFeetLabel.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # Discount
        self.discount_label = Label(self.PropertyInfoFrame, text="Discount:", bg='#ffffff',
                                         font="Arial 10 bold")
        self.discount_label.grid(row=3, column=3, sticky=W, padx=5, pady=5)

        self.discountEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.discount)
        self.discountEntry.grid(row=3, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)
        self.discountEntry.bind("<KeyRelease>", self.paymentCalculation)

        # Down Payment
        self.downpayment_label = Label(self.PropertyInfoFrame, text="Down Payment:", bg='#ffffff',
                                       font="Arial 10 bold")
        self.downpayment_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.downPaymentEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                      textvariable=self.downPayment)
        self.downPaymentEntry.grid(row=4, column=1, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)
        self.downPaymentEntry.bind("<KeyRelease>", self.paymentCalculation)

        # Possession
        self.possession_label = Label(self.PropertyInfoFrame, text="Possession:", bg='#ffffff',
                                       font="Arial 10 bold")
        self.possession_label.grid(row=4, column=3, sticky=W, padx=5, pady=5)

        self.possessionEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                      textvariable=self.possessionAmount)
        self.possessionEntry.grid(row=4, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)
        self.possessionEntry.bind("<KeyRelease>", self.paymentCalculation)

        # Price Per Installment
        self.priceperinstallment_label = Label(self.PropertyInfoFrame, text="Price Per Installment:", bg='#ffffff',
                                             font="Arial 10 bold")
        self.priceperinstallment_label.grid(row=5, column=3, sticky=W, padx=5, pady=5)

        self.pricePerInstallmentEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.pricePerInstallment)
        self.pricePerInstallmentEntry.grid(row=5, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Total Installments
        self.totalinstallments_label = Label(self.PropertyInfoFrame, text="Total Installments:", bg='#ffffff',
                                             font="Arial 10 bold")
        self.totalinstallments_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.totalInstallmentsEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid",
                                            highlightbackground="#00479c",
                                            highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                            textvariable=self.totalInstallments)
        self.totalInstallmentsEntry.grid(row=5, column=1, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)
        self.totalInstallmentsEntry.bind("<KeyRelease>", self.installmentCalculation)

        # Property Location
        self.propertyLocationLabel = Label(self.PropertyInfoFrame, text="Property Location:", bg='#ffffff',
                                         font="Arial 10 bold")
        self.propertyLocationLabel.grid(row=6, column=3, sticky=W, padx=5, pady=5)

        self.propertyLocationEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.propertyLocation)
        self.propertyLocationEntry.grid(row=6, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Property Description
        self.propertyDescriptionLabel = Label(self.PropertyInfoFrame, text="Property Description:", bg='#ffffff',
                                         font="Arial 10 bold")
        self.propertyDescriptionLabel.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.propertyDescriptionText = Text(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                     highlightcolor="#00479c", highlightthickness=1, borderwidth=0, height=1, width=21)
        self.propertyDescriptionText.grid(row=6, column=1, sticky=W, padx=5, pady=5, ipadx=6, ipady=5, columnspan=2)

        # Select Installment Plan
        self.installmentPlanLabel = Label(self.PropertyInfoFrame, text="Installment Plan:", bg='#ffffff', font="Arial 10 bold")
        self.installmentPlanLabel.grid(row=7, column=3, sticky=W, padx=5, pady=5)

        self.installmentPlanCombobox = ttk.Combobox(self.PropertyInfoFrame, textvariable=self.installmentPlan, values=self.installmentPlanList)
        self.installmentPlanCombobox.grid(row=7, column=4, sticky=W, padx=5, pady=5, ipady=4, ipadx=21)

        # Due Date
        self.dueDateLabel = Label(self.PropertyInfoFrame, text="Due Date:", bg='#ffffff', font="Arial 10 bold")
        self.dueDateLabel.grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.dueDateEntry = tkc.DateEntry(self.PropertyInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                      date_pattern="yyyy/mm/dd")
        self.dueDateEntry.grid(row=7, column=1, sticky=W, padx=5, pady=5, ipady=4, ipadx=44)

        # Payment Calculation
        self.paymentCalculationEntry = Entry(self.PropertyInfoFrame, border=1, relief="solid",
                                           highlightbackground="#00479c",
                                           highlightcolor="#00479c", highlightthickness=1, borderwidth=0,
                                           textvariable=self.result)
        self.paymentCalculationEntry.grid(row=8, column=4, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Status
        self.status_label = Label(self.PropertyInfoFrame, text="Status:", bg='#ffffff',
                                  font="Arial 10 bold")
        self.status_label.grid(row=8, column=0, sticky=W, padx=5, pady=5)

        self.statusLabel = Label(self.PropertyInfoFrame, text="Status Here", bg='#ffffff')
        self.statusLabel.grid(row=8, column=1, sticky=W, padx=5, pady=5)

        # Assign Property
        self.assignPropertybutton = Button(self.PropertyInfoFrame, text="Assign", bg='#00479c', fg="White",
                                           font="Arial 9", relief="flat", command=lambda: [assignProperty()])
        self.assignPropertybutton.grid(row=9, column=4, sticky=W, padx=5, pady=15, ipadx=67, ipady=5)

        # ===========================================================================#

        # ================================Functions==================================#

        def assignProperty():
            if IsValid():
                if self.clientTag == 1 and self.propertyTag == 1:
                    con = sqlite3.connect(database=r'marketing.db')
                    cur = con.cursor()
                    # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
                    #                                      database="gujranwalaemporium")
                    # cursor = connection.cursor(prepared=True)
                    try:
                        if self.propertyIDEntry.get() == "":
                            messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
                        elif self.clientCnicEntry.get() == "":
                            messagebox.showerror("Error", "Client ID Must Required", parent=self.root)
                        else:
                            cur.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
                            propertyData = cur.fetchone()
                            cur.execute("select * from client where client_cnic=?", (self.clientCnicEntry.get(),))
                            clientData = cur.fetchone()
                            if propertyData == None and clientData == None:
                                messagebox.showerror("Error", "Property or Client not Exist", parent=self.root)
                            else:
                                cur.execute("Update property set client_cnic=?,downPayment=?,totalInstallments=?,pricePerInstallment=?"
                                            ",discount=?,status=?,installmentPlan=?,possession=? where propertyID=?",
                                            (
                                                self.clientCnicEntry.get(),
                                                self.dp.get(),
                                                self.totalInstallmentsEntry.get(),
                                                self.pricePerInstallmentEntry.get(),
                                                float(self.discountEntry.get())*float(propertyData[3]),
                                                "Sold",
                                                self.installmentPlan.get(),
                                                self.pa.get(),

                                                self.propertyIDEntry.get()
                                            ))
                                con.commit()
                                self.statusLabel.config(text="Sold")
                                generateBill()
                                messagebox.showinfo("Sucess", "Property Assigned Sucessfully", parent=self.root)
                                self.clientTag = 0
                                self.propertyTag = 0
                    except EXCEPTION as ex:
                        messagebox.showerror("Error", f"due to : {str(ex)}")
                else:
                    messagebox.showinfo("Sucess", "CLient or Property Record is not searched Properly", parent=self.root)

        def showClient():
            self.clientTag = 1
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                if self.clientCnicEntry.get() == "":
                    messagebox.showerror("Error", "Client CNIC Must Required", parent=self.root)
                else:
                    cur.execute("select * from client where client_cnic=?", (self.clientCnicEntry.get(),))
                    clientData = cur.fetchone()
                    if clientData != None:
                        self.clientnameLabel.config(text=clientData[1])
                        self.clientContactLabel.config(text=clientData[2])
                        self.clientAddressLabel.config(text=clientData[3])
                    else:
                        messagebox.showerror("Error", "This Client does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def showProperty():
            self.propertyTag = 1
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                if self.propertyIDEntry.get() == "":
                    messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
                else:
                    cur.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
                    propertyData = cur.fetchone()
                    print(propertyData)
                    if propertyData != None:
                        self.propertySizeLabel.config(text=propertyData[3])
                        self.propertySize = propertyData[3]
                        self.propertyPriceLabel.config(text=propertyData[4])
                        self.propertyPricePerFeetLabel.config(text=float(propertyData[4])/float(propertyData[3]))
                        self.statusLabel.config(text=propertyData[9])
                        self.propertyLocation.set(propertyData[10])
                        self.propertyDescriptionText.insert(END,propertyData[11])
                        self.result.set(propertyData[4])
                    else:
                        messagebox.showerror("Error", "This Property does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def generateBill():
            dueDate = self.dueDateEntry.get()
            dueDate = datetime.date.fromisoformat(dueDate.replace("/","-"))
            print(type(dueDate))
            print(dueDate)
            for installment in range(1,int(self.totalInstallmentsEntry.get())+2):
                billId()
                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
                #                                      database="gujranwalaemporium")
                # cursor = connection.cursor(prepared=True)
                try:
                    if installment != int(self.totalInstallmentsEntry.get())+1:
                        cur.execute(
                            "Insert into bill(billID,propertyID,dueDate,installementNo,installmentAmount,balance,status)values(?,?,?,?,?,?,?)",
                            (self.billID.get(),
                             self.propertyIDEntry.get(),
                             dueDate.strftime("%Y/%m/%d"),
                             installment,
                             self.pricePerInstallmentEntry.get(),
                             self.pricePerInstallmentEntry.get(),
                             "Unpaid"
                             ))
                        con.commit()
                    else:
                        cur.execute(
                            "Insert into bill(billID,propertyID,dueDate,installementNo,installmentAmount,balance,status)values(?,?,?,?,?,?,?)",
                            (self.billID.get(),
                             self.propertyIDEntry.get(),
                             " ",
                             installment,
                             self.pa.get(),
                             self.pa.get(),
                             "Unpaid"
                             ))
                        con.commit()
                    if self.installmentPlan.get() == "Monthly":
                        dueDate = dueDate + relativedelta(months=+1)

                    if self.installmentPlan.get() == "Quarterly":
                        dueDate = dueDate + relativedelta(months=+3)

                    if self.installmentPlan.get() == "Six Month":
                        dueDate = dueDate + relativedelta(months=+6)

                    if self.installmentPlan.get() == "Annually":
                        dueDate = dueDate + relativedelta(months=+12)
                except EXCEPTION as ex:
                    messagebox.showerror("Error", f"due to : {str(ex)}")


        def billId():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select MAX(billID) from bill")
                maxID = cur.fetchone()
                print(maxID)
                if maxID[0] == None:
                    self.billID.set(1)
                else:
                    self.billID.set(int(maxID[0]) + 1)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

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

            if self.propertyIDEntry.get() == '':
                messagebox.showerror("Error", "Property ID is Required", parent=self.root)
                return False

            if self.propertyIDEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Property ID", parent=self.root)
                return False

            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            cur.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
            propertyData = cur.fetchone()

            if propertyData == None:
                messagebox.showerror("Error", "This Property does not Exist", parent=self.root)
                return False

            if propertyData[9] =='Sold':
                messagebox.showerror("Error", "This Property is Already Sold", parent=self.root)
                return False

            if self.downPaymentEntry.get() == '' or self.downPaymentEntry.get() == '0' or self.downPaymentEntry.get() == 0:
                messagebox.showerror("Error", "Down Payment is Required", parent=self.root)
                return False

            if self.downPaymentEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Down Payment", parent=self.root)
                return False

            if self.discountEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Discount", parent=self.root)
                return False

            if self.totalInstallmentsEntry.get() == '':
                messagebox.showerror("Error", "Number of Installments are Required", parent=self.root)
                return False

            if self.totalInstallmentsEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Installment Number", parent=self.root)
                return False

            if self.pricePerInstallmentEntry.get() == '':
                messagebox.showerror("Error", "Installment Amount is Required", parent=self.root)
                return False

            if self.propertyLocationEntry.get() == '':
                messagebox.showerror("Error", "Property Location is Required", parent=self.root)
                return False

            if self.installmentPlan.get() == '' or self.installmentPlan.get() == 'None' or self.installmentPlan.get() == None:
                messagebox.showerror("Error", "Select Installments Plan", parent=self.root)
                return False

            return True

    def paymentCalculation(self, event):
        con = sqlite3.connect(database=r'marketing.db')
        cur = con.cursor()
        # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                      database="gujranwalaemporium")
        # cursor = connection.cursor(prepared=True)
        try:
            cur.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
            propertyData = cur.fetchone()
            da = int(propertyData[4]) - (self.discount.get()*float(propertyData[3]))
            self.discountedAmount.set(da)
            value = int(propertyData[4]) - (((self.downPayment.get()/100)*int(self.discountedAmount.get())) + (self.discount.get()*float(propertyData[3])) + ((self.possessionAmount.get()/100)*int(self.discountedAmount.get())))
            self.result.set(value)
            self.dp.set((self.downPayment.get() / 100) * int(self.discountedAmount.get()))
            self.pa.set((self.possessionAmount.get() / 100) * int(self.discountedAmount.get()))
        except Exception as ex:
            pass

    def installmentCalculation(self, event):
        try:
            pricePerInstallment = int(self.result.get())/int(self.totalInstallments.get())
            self.pricePerInstallment.set(pricePerInstallment)
        except Exception as ex:
            pass


        # ===========================================================================#

if __name__=="__main__":

    root=Tk()
    obj=Assign_property(root)
    root.mainloop()