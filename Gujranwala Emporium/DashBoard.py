from tkinter import*
from PIL import  Image,ImageTk
from Add_Property import Add_property
from Assign_Property import Assign_property
from Add_Client import Add_client
from Add_Project import Add_project
from Client_Report import ClientReport
from Bill import bill
from Expenses import Add_Expenses
from Dues_Report import duesReport
from Expense_Report import expenseReport
from tkinter import messagebox
from fpdf import FPDF
import sqlite3
import mysql.connector
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class main:
    def __init__(self,root):
        self.root=root
        self.root.title("Main-Dashboard")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 550
        window_width = 900
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.state('zoomed')

        # =================================Menu Frame================================#
        #title = Label(self.root, bd=2, bg="#00479c").place(x=0, y=0, relwidth=1, height=10)

        # ================================Variables==================================#

        self.billingTag = 0
        self.inventoryTag = 0
        self.reportTag = 0
        self.adminTag = 0

    

        # ================================Bottom Frame===============================#

        bottomFrame = Frame(root, bg="#00479c", border=3)
        bottomFrame.pack(side=BOTTOM, anchor="sw", pady=0, padx=0, fill="x")

        bottomLabel = Label(bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white", font="Arial 7")
        bottomLabel.pack()

        # ===========================================================================#

        # ==========================Button Hover Functions===========================#

        def on_enter(e):
            e.widget['background'] = '#ffffff'
            e.widget['foreground'] = '#000000'

        def on_leave(e):
            e.widget['background'] = '#00479c'
            e.widget['foreground'] = '#ffffff'

        # ===========================================================================#

        # ==========================Hide/Show Functions===========================#

        def pagee():
            self.win = Toplevel(self.root)
            self.new_obj = Add_client(self.win)

        def pageee():
            self.win = Toplevel(self.root)
            self.new_obj = Assign_property(self.win)

        def pageeee():
            self.win = Toplevel(self.root)
            self.new_obj = Add_property(self.win)

        def pageeees():
            self.win = Toplevel(self.root)
            self.new_obj = Add_project(self.win)

        def expense():
            self.win = Toplevel(self.root)
            self.new_obj = Add_Expenses(self.win)

        def dueReport():
            self.win = Toplevel(self.root)
            self.new_obj = duesReport(self.win)

        def expensesReport():
            self.win = Toplevel(self.root)
            self.new_obj = expenseReport(self.win, pdf=FPDF())

        def pageeeess():
            self.win = Toplevel(self.root)
            self.new_obj = ClientReport(self.win, pdf=FPDF())

        def pageeeesss():
            self.win = Toplevel(self.root)
            self.new_obj = bill(self.win, pdf=FPDF())

        def billingHide():
            self.clientBillButton.grid_forget()
            self.expenseButton.grid_forget()

            # self.saleInvoiceButton.grid_forget()
            # self.saleReturnButton.grid_forget()
            self.billingTag = 0

        def billingShow():

            if self.billingTag == 0:
                inventoryHide()
                reportHide()
                adminHide()
                self.clientBillButton.grid(column=0, row=6)
                self.expenseButton.grid(column=0, row=7)

                # self.saleInvoiceButton.grid(column=0, row=8)
                # self.saleReturnButton.grid(column=0, row=9)
                self.billingTag = 1
            else:
                billingHide()

        def inventoryHide():
            self.addPropertyButton.grid_forget()
            self.addProjectButton.grid_forget()

            # self.purchaseOrderButton.grid_forget()
            # self.receivingNoteButton.grid_forget()
            self.inventoryTag = 0

        def inventoryShow():

            if self.inventoryTag == 0:
                billingHide()
                reportHide()
                adminHide()
                self.addPropertyButton.grid(column=0, row=11)
                self.addProjectButton.grid(column=0, row=12)

                # self.purchaseOrderButton.grid(column=0, row=13)
                # self.receivingNoteButton.grid(column=0, row=14)
                self.inventoryTag = 1
            else:
                inventoryHide()

        def reportHide():
            self.clientReportButton.grid_forget()
            self.duesReportButton.grid_forget()
            self.expenseReportButton.grid_forget()
            self.reportTag = 0

        def reportShow():

            if self.reportTag == 0:
                billingHide()
                inventoryHide()
                adminHide()
                self.clientReportButton.grid(column=0, row=16)
                self.duesReportButton.grid(column=0, row=17)
                self.expenseReportButton.grid(column=0, row=18)
                self.reportTag = 1
            else:
                reportHide()

        def adminHide():
            self.addClientButton.grid_forget()
            self.assignPropertyButton.grid_forget()
            self.adminTag = 0

        def adminShow():

            if self.adminTag == 0:
                billingHide()
                inventoryHide()
                reportHide()
                self.addClientButton.grid(column=0, row=3)
                self.assignPropertyButton.grid(column=0, row=4)
                self.adminTag = 1
            else:
                adminHide()

        # ===========================================================================#

        # =================================Menu Frame================================#

        menuFrame = Frame(root, bg="#00479c", relief="sunken")
        menuFrame.pack(side=LEFT, anchor="nw", pady=0, padx=0, fill="y")

        # Image
        self.menuImage = Image.open(r"img/menuIcon.png")
        self.menuImage = self.menuImage.resize((180, 180), Image.ANTIALIAS)
        self.menuImage = ImageTk.PhotoImage(self.menuImage)

        menuImageLabel = Label(menuFrame, image=self.menuImage, bg="#00479c", relief="flat")
        menuImageLabel.grid(column=0, row=0)


        # Dashboard
        self.dashboardPhoto = PhotoImage(file=r"img/dashboardW.png")
        self.dashboardButton = Button(menuFrame, text="Dashboard", width=194, height=35, bg='#00479c', fg="White",
                                      font="Arial 9", relief="flat", image=self.dashboardPhoto, compound=LEFT, padx=10, anchor="w",
                                      command=lambda:[billingHide(), inventoryHide(), reportHide(), adminHide(), functionCaller()])
        self.dashboardButton.grid(column=0, row=1)

        self.dashboardButton.bind("<Enter>", on_enter)
        self.dashboardButton.bind("<Leave>", on_leave)

        # Admin
        self.adminPhoto = PhotoImage(file=r"img/profileW.png")
        self.adminButton = Button(menuFrame, text="Admin", width=194, height=35, bg='#00479c', fg="White", font="Arial 9",
                                  relief="flat", image=self.adminPhoto, compound=LEFT, padx=10, anchor="w",
                                      command=adminShow)
        self.adminButton.grid(column=0, row=2)

        self.adminButton.bind("<Enter>", on_enter)
        self.adminButton.bind("<Leave>", on_leave)

        # Admin Sub Menu
        self.addClientButton = Button(menuFrame, text="Add Client", width=30, height=2,
                                      bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                      command=lambda:[pagee(), adminHide()])

        self.addClientButton.bind("<Enter>", on_enter)
        self.addClientButton.bind("<Leave>", on_leave)

        self.assignPropertyButton = Button(menuFrame, text="Assign Property", width=30, height=2,
                                               bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                               command=lambda:[pageee(), adminHide()])

        self.assignPropertyButton.bind("<Enter>", on_enter)
        self.assignPropertyButton.bind("<Leave>", on_leave)

        # Billing
        self.billingPhoto = PhotoImage(file=r"img/invoiceW.png")
        self.billingButton = Button(menuFrame, text="Billing", width=194, height=35, bg='#00479c', fg="White",
                                    font="Arial 9", relief="flat", image=self.billingPhoto, compound=LEFT, padx=10,
                                    anchor="w", command=billingShow)
        self.billingButton.grid(column=0, row=5)

        self.billingButton.bind("<Enter>", on_enter)
        self.billingButton.bind("<Leave>", on_leave)

        # Billing Sub Menu
        self.clientBillButton = Button(menuFrame, text="Client Bill", width=30, height=2,
                                            bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                            command=lambda:[pageeeesss(), billingHide()])

        self.clientBillButton.bind("<Enter>", on_enter)
        self.clientBillButton.bind("<Leave>", on_leave)

        self.expenseButton = Button(menuFrame, text="Expenses", width=30, height=2,
                                           bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                           command=lambda:[billingHide(), expense()])

        self.expenseButton.bind("<Enter>", on_enter)
        self.expenseButton.bind("<Leave>", on_leave)

        # self.saleInvoiceButton = Button(menuFrame, text="Sale Invoice", width=30, height=2,
        #                                     bg='#00479c', fg="White", font="Arial 9", relief="flat",
        #                                     command=billingHide)
        #
        # self.saleInvoiceButton.bind("<Enter>", on_enter)
        # self.saleInvoiceButton.bind("<Leave>", on_leave)
        #
        # self.saleReturnButton = Button(menuFrame, text="Sale Return", width=30, height=2,
        #                                    bg='#00479c', fg="White", font="Arial 9", relief="flat",
        #                                    command=billingHide)
        #
        # self.saleReturnButton.bind("<Enter>", on_enter)
        # self.saleReturnButton.bind("<Leave>", on_leave)

        # Inventory
        self.inventoryPhoto = PhotoImage(file=r"img/listW.png")
        self.inventoryButton = Button(menuFrame, text="Inventory", width=194, height=35, bg='#00479c', fg="White",
                                      font="Arial 9", relief="flat", image=self.inventoryPhoto, compound=LEFT, padx=10,
                                    anchor="w", command=inventoryShow)
        self.inventoryButton.grid(column=0, row=10)

        self.inventoryButton.bind("<Enter>", on_enter)
        self.inventoryButton.bind("<Leave>", on_leave)

        # Inventory Sub Menu
        self.addPropertyButton = Button(menuFrame, text="Add Property", width=30, height=2,
                                            bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                            command=lambda:[pageeee(), inventoryHide()])

        self.addPropertyButton.bind("<Enter>", on_enter)
        self.addPropertyButton.bind("<Leave>", on_leave)

        self.addProjectButton = Button(menuFrame, text="Add Project", width=30, height=2,
                                           bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                           command=lambda:[pageeees(), inventoryHide()])

        self.addProjectButton.bind("<Enter>", on_enter)
        self.addProjectButton.bind("<Leave>", on_leave)

        # self.purchaseOrderButton = Button(menuFrame, text="Purchase Order", width=30, height=2,
        #                                 bg='#00479c', fg="White", font="Arial 9", relief="flat",
        #                                 command=inventoryHide)
        #
        # self.purchaseOrderButton.bind("<Enter>", on_enter)
        # self.purchaseOrderButton.bind("<Leave>", on_leave)
        #
        # self.receivingNoteButton = Button(menuFrame, text="Receiving Note", width=30, height=2,
        #                                bg='#00479c', fg="White", font="Arial 9", relief="flat",
        #                                command=inventoryHide)
        #
        # self.receivingNoteButton.bind("<Enter>", on_enter)
        # self.receivingNoteButton.bind("<Leave>", on_leave)

        # Report
        self.reportPhoto = PhotoImage(file=r"img/reportW.png")
        self.reportButton = Button(menuFrame, text="Report", width=194, height=35, bg='#00479c', fg="White",
                                   font="Arial 9", relief="flat", image=self.reportPhoto, compound=LEFT, padx=10, anchor="w",
                                      command=reportShow)
        self.reportButton.grid(column=0, row=15)

        self.reportButton.bind("<Enter>", on_enter)
        self.reportButton.bind("<Leave>", on_leave)

        # Report Sub Menu
        self.clientReportButton = Button(menuFrame, text="Client Report", width=30, height=2,
                                            bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                            command=lambda:[pageeeess(), reportHide()])

        self.clientReportButton.bind("<Enter>", on_enter)
        self.clientReportButton.bind("<Leave>", on_leave)

        self.duesReportButton = Button(menuFrame, text="Dues Report", width=30, height=2,
                                         bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                         command=lambda: [reportHide(), dueReport()])

        self.duesReportButton.bind("<Enter>", on_enter)
        self.duesReportButton.bind("<Leave>", on_leave)

        self.expenseReportButton = Button(menuFrame, text="Expense Report", width=30, height=2,
                                       bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                       command=lambda: [reportHide(), expensesReport()])

        self.expenseReportButton.bind("<Enter>", on_enter)
        self.expenseReportButton.bind("<Leave>", on_leave)

        # Backup
        self.backupPhoto = PhotoImage(file=r"img/backup.png")
        self.backupButton = Button(menuFrame, text="Backup", width=194, height=35, bg='#00479c', fg="White",
                                   font="Arial 9", relief="flat", image=self.backupPhoto, compound=LEFT, padx=10, anchor="w",
                                      command=lambda:[billingHide(), inventoryHide(), reportHide(), adminHide(), Backup()])
        self.backupButton.grid(column=0, row=19)

        self.backupButton.bind("<Enter>", on_enter)
        self.backupButton.bind("<Leave>", on_leave)

        # Logout
        self.logoutPhoto = PhotoImage(file=r"img/powerW.png")
        self.logoutButton = Button(menuFrame, text="Logout", width=194, height=35, bg='#00479c', fg="White",
                                   font="Arial 9", relief="flat", image=self.logoutPhoto, compound=LEFT, padx=10,
                                   anchor="w",
                                   command=lambda: [billingHide(), inventoryHide(), reportHide(), adminHide()])
        self.logoutButton.grid(column=0, row=20)

        self.logoutButton.bind("<Enter>", on_enter)
        self.logoutButton.bind("<Leave>", on_leave)

        # ===========================================================================#

        # ===============================Dashboard Frame==============================#

        self.dashboardFrame = Frame(self.root, bg="#F3F3F3", relief="sunken")
        self.dashboardFrame.pack(side=LEFT, ipadx=250, ipady=50, fill=BOTH)
        self.dashboardFrame.grid_columnconfigure(0, weight=1)
        self.dashboardFrame.grid_columnconfigure(5, weight=1)

        self.Logo = Image.open(r"img/Logo.png")
        self.Logo = self.Logo.resize((200, 130), Image.ANTIALIAS)
        self.Logo = ImageTk.PhotoImage(self.Logo)

        logoLabel = Label(self.dashboardFrame, image=self.Logo, bg="#F3F3F3", relief="flat")
        logoLabel.grid(row=1, column=1, pady=15, padx=10, columnspan=4)

        # Projects
        def projectCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
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

            return self.projectCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.projectCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200, height=200)
        self.projectCard.grid(row=2, column=1, pady=10, padx=10)

        projectCanvas(0, 0, 200, 200, radius=30)

        self.projectImg = ImageTk.PhotoImage(Image.open(f"img/houseplan.png"))
        self.projectCard.create_image(10, 10, anchor=NW, image=self.projectImg)

        self.projectLabel = Label(self.projectCard, text='Projects', fg='#777777', bg='#ffffff',
                               font="Arial 12 bold")
        self.projectLabel.pack()
        self.projectCard.create_window(100, 60, window=self.projectLabel)
        self.projectCountLabel = Label(self.projectCard, text='0', fg='#777777', bg='#ffffff', font="Arial 18 bold")
        self.projectCountLabel.pack()
        self.projectCard.create_window(100, 100, window=self.projectCountLabel)

        # Total Property
        def totalPropertyCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
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

            return self.totalPropertyCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.totalPropertyCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200, height=200)
        self.totalPropertyCard.grid(row=2, column=2, pady=10, padx=10)

        totalPropertyCanvas(0, 0, 200, 200, radius=30)

        self.totalPropertyImg = ImageTk.PhotoImage(Image.open(f"img/property.png"))
        self.totalPropertyCard.create_image(10, 10, anchor=NW, image=self.totalPropertyImg)

        self.totalPropertyLabel = Label(self.totalPropertyCard, text='Properties', fg='#777777', bg='#ffffff',
                                  font="Arial 12 bold")
        self.totalPropertyLabel.pack()
        self.totalPropertyCard.create_window(100, 60, window=self.totalPropertyLabel)
        self.totalPropertyCountLabel = Label(self.totalPropertyCard, text='000000', fg='#777777', bg='#ffffff',
                                       font="Arial 18 bold")
        self.totalPropertyCountLabel.pack()
        self.totalPropertyCard.create_window(100, 100, window=self.totalPropertyCountLabel)

        # Available Property
        def availablePropertyCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
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

            return self.availablePropertyCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.availablePropertyCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200, height=200)
        self.availablePropertyCard.grid(row=2, column=3, pady=10, padx=10)

        availablePropertyCanvas(0, 0, 200, 200, radius=30)

        self.availablePropertyImg = ImageTk.PhotoImage(Image.open(f"img/avprop.png"))
        self.availablePropertyCard.create_image(10, 10, anchor=NW, image=self.availablePropertyImg)

        self.availablePropertyLabel = Label(self.availablePropertyCard, text='Available Properties', fg='#777777', bg='#ffffff',
                                        font="Arial 12 bold")
        self.availablePropertyLabel.pack()
        self.availablePropertyCard.create_window(100, 60, window=self.availablePropertyLabel)
        self.availablePropertyCountLabel = Label(self.availablePropertyCard, text='000000', fg='#777777', bg='#ffffff',
                                             font="Arial 18 bold")
        self.availablePropertyCountLabel.pack()
        self.availablePropertyCard.create_window(100, 100, window=self.availablePropertyCountLabel)

        # Sold Property
        def soldPropertyCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
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

            return self.soldPropertyCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.soldPropertyCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200,
                                            height=200)
        self.soldPropertyCard.grid(row=2, column=4, pady=10, padx=10)

        soldPropertyCanvas(0, 0, 200, 200, radius=30)

        self.soldPropertyImg = ImageTk.PhotoImage(Image.open(f"img/deal.png"))
        self.soldPropertyCard.create_image(10, 10, anchor=NW, image=self.soldPropertyImg)

        self.soldPropertyLabel = Label(self.soldPropertyCard, text='Sold Properties', fg='#777777',
                                            bg='#ffffff',
                                            font="Arial 12 bold")
        self.soldPropertyLabel.pack()
        self.soldPropertyCard.create_window(100, 60, window=self.soldPropertyLabel)
        self.soldPropertyCountLabel = Label(self.soldPropertyCard, text='000000', fg='#777777', bg='#ffffff',
                                                 font="Arial 18 bold")
        self.soldPropertyCountLabel.pack()
        self.soldPropertyCard.create_window(100, 100, window=self.soldPropertyCountLabel)

        # Clients
        def clientCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
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

            return self.clientCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.clientCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200, height=200)
        self.clientCard.grid(row=3, column=1, pady=10, padx=10)

        clientCanvas(0, 0, 200, 200, radius=30)

        self.clientImg = ImageTk.PhotoImage(Image.open(f"img/people.png"))
        self.clientCard.create_image(10, 10, anchor=NW, image=self.clientImg)

        self.clientLabel = Label(self.clientCard, text='Clients', fg='#777777', bg='#ffffff',
                                  font="Arial 12 bold")
        self.clientLabel.pack()
        self.clientCard.create_window(100, 60, window=self.clientLabel)
        self.clientCountLabel = Label(self.clientCard, text='000000', fg='#777777', bg='#ffffff',
                                       font="Arial 18 bold")
        self.clientCountLabel.pack()
        self.clientCard.create_window(100, 100, window=self.clientCountLabel)

        # Received Payment
        def receivedPaymentCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
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

            return self.receivedPaymentCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.receivedPaymentCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200, height=200)
        self.receivedPaymentCard.grid(row=3, column=2, pady=10, padx=10)

        receivedPaymentCanvas(0, 0, 200, 200, radius=30)

        self.receivedPaymentImg = ImageTk.PhotoImage(Image.open(f"img/payment.png"))
        self.receivedPaymentCard.create_image(10, 10, anchor=NW, image=self.receivedPaymentImg)

        self.receivedPaymentLabel = Label(self.receivedPaymentCard, text='Received Payment', fg='#777777', bg='#ffffff',
                                        font="Arial 12 bold")
        self.receivedPaymentLabel.pack()
        self.receivedPaymentCard.create_window(100, 60, window=self.receivedPaymentLabel)
        self.receivedPaymentCountLabel = Label(self.receivedPaymentCard, text='0', fg='#777777', bg='#ffffff',
                                             font="Arial 18 bold")
        self.receivedPaymentCountLabel.pack()
        self.receivedPaymentCard.create_window(100, 100, window=self.receivedPaymentCountLabel)

        # Balance
        def balanceCanvas(x1, y1, x2, y2, radius, **kwargs):  # Creating a rounded rectangle
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

            return self.balanceCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.balanceCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200,
                                            height=200)
        self.balanceCard.grid(row=3, column=3, pady=10, padx=10)

        balanceCanvas(0, 0, 200, 200, radius=30)

        self.balanceImg = ImageTk.PhotoImage(Image.open(f"img/moneybag.png"))
        self.balanceCard.create_image(10, 10, anchor=NW, image=self.balanceImg)

        self.balanceLabel = Label(self.balanceCard, text='Balance', fg='#777777',
                                            bg='#ffffff',
                                            font="Arial 12 bold")
        self.balanceLabel.pack()
        self.balanceCard.create_window(100, 60, window=self.balanceLabel)
        self.balanceCountLabel = Label(self.balanceCard, text='0', fg='#777777', bg='#ffffff',
                                                 font="Arial 18 bold")
        self.balanceCountLabel.pack()
        self.balanceCard.create_window(100, 100, window=self.balanceCountLabel)

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

            return self.expenseCard.create_polygon(points, **kwargs, smooth=True, fill="#ffffff")

        self.expenseCard = Canvas(self.dashboardFrame, bg="#F3F3F3", highlightthickness=0, width=200,
                                       height=200)
        self.expenseCard.grid(row=3, column=4, pady=10, padx=10)

        expenseCanvas(0, 0, 200, 200, radius=30)

        self.expenseImg = ImageTk.PhotoImage(Image.open(f"img/wallet.png"))
        self.expenseCard.create_image(10, 10, anchor=NW, image=self.expenseImg)

        self.expenseLabel = Label(self.expenseCard, text='Expenses', fg='#777777',
                                       bg='#ffffff',
                                       font="Arial 12 bold")
        self.expenseLabel.pack()
        self.expenseCard.create_window(100, 60, window=self.expenseLabel)
        self.expenseCountLabel = Label(self.expenseCard, text='0', fg='#777777', bg='#ffffff',
                                            font="Arial 18 bold")
        self.expenseCountLabel.pack()
        self.expenseCard.create_window(100, 100, window=self.expenseCountLabel)

        def functionCaller():
            getSoldProperties()
            getAvailableProperties()
            getTotalProperties()
            getTotalProject()
            getTotalClient()
            account()
            getTotalExpense()

        def getSoldProperties():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT COUNT(status) FROM property WHERE status = 'Sold'")
                soldProperty = cur.fetchone()
                self.soldPropertyCountLabel.config(text=soldProperty[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
                print(f"soldProperty : {str(ex)}")

        getSoldProperties()

        def getAvailableProperties():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT COUNT(status) FROM property WHERE status = 'Available'")
                availableProperty = cur.fetchone()
                self.availablePropertyCountLabel.config(text=availableProperty[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
                print(f"availableProperty : {str(ex)}")

        getAvailableProperties()

        def getTotalProperties():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT COUNT(status) FROM property")
                totalProperty = cur.fetchone()
                self.totalPropertyCountLabel.config(text=totalProperty[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
                print(f"totalProperty : {str(ex)}")

        getTotalProperties()

        def getTotalProject():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT COUNT(projectID) FROM project")
                totalProject = cur.fetchone()
                self.projectCountLabel.config(text=totalProject[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
                print(f"totalProject : {str(ex)}")

        getTotalProject()

        def getTotalClient():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT COUNT(client_cnic) FROM client")
                totalClient = cur.fetchone()
                self.clientCountLabel.config(text=totalClient[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
                print(f"totalClient : {str(ex)}")

        getTotalClient()

        def account():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select SUM(receiveAmount), SUM(balance) from bill")
                billData = cur.fetchone()
                cur.execute("select SUM(propertyPrice), SUM(downPayment), SUM(discount), SUM(possession) from property")
                propertyData = cur.fetchone()
                if propertyData[1]==None:
                    dp = 0
                else:
                    dp = propertyData[1]

                if billData[0]==None:
                    ra = 0
                else:
                    ra = billData[0]
                if propertyData[3]==None:
                    p = 0
                else:
                    p = propertyData[3]
                self.receive = (int(ra)+int(dp))
                self.receivedPaymentCountLabel.config(text=self.receive)
                self.balanceCountLabel.config(text=billData[1])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
                print(f"account : {str(ex)}")

        account()

        def getTotalExpense():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT SUM(expenseAmount) FROM expense")
                totalExpense = cur.fetchone()
                self.expenseCountLabel.config(text=totalExpense[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
                print(f"totalExpense : {str(ex)}")

        getTotalExpense()

        def Backup():
            gauth = GoogleAuth()
            drive = GoogleDrive(gauth)

            fileList = drive.ListFile(
                {'q': "'1V-PZE-CSMmvEAlBJGEWcZ94tVRVGYyQV' in parents and trashed=false"}).GetList()
            for file in fileList:
                print('Title: %s, ID: %s' % (file['title'], file['id']))
                if (file['title'] == "marketing.db"):
                    fileID = file['id']
                    file2 = drive.CreateFile({'id': fileID})
                    file2.Delete()

            upload_file_list = ["marketing.db"]
            for upload_file in upload_file_list:
                gfile = drive.CreateFile({'parents': [{'id': '1V-PZE-CSMmvEAlBJGEWcZ94tVRVGYyQV'}]})
                gfile.SetContentFile(upload_file)
                gfile.Upload()

        # ===========================================================================#

        # ===========================================================================#


if __name__=="__main__":

    root=Tk()
    obj=main(root)
    root.mainloop()