from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

class Add_property:
    def __init__(self,root):
        self.root = root
        self.root.title("Add Property")
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
        self.status.set("Available")
        self.propertyLocation = StringVar()
        self.propertyDescription = StringVar()
        self.project = StringVar()
        self.projectList =[]

        # =============================Window Settings===============================#

        #=============================Centered Screen===============================#

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 550
        window_width = 900
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.root.state('zoomed')

        #===========================================================================#

        #===============================Title Frame=================================#

        self.titleFrame = Frame(self.root, bg="#00479c")
        self.titleFrame.pack(side=TOP, anchor="nw", pady=0, padx=5, fill="x")

        self.titleLabel = Label(self.titleFrame, text="Add Property", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        #===========================================================================#

        #================================Bottom Frame===============================#

        self.bottomFrame = Frame(self.root, bg="#00479c", border=3)
        self.bottomFrame.pack(side=BOTTOM, anchor="nw", pady=0, padx=5, fill="x")

        self.bottomLabel = Label(self.bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white", font="Arial 9")
        self.bottomLabel.pack()

        #===========================================================================#

        # ===============================Main Frame=================================#

        self.mainFrame = Frame(self.root, bg="#ffffff")
        self.mainFrame.pack(fill=BOTH, pady=10)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(3, weight=1)

        # ===========================================================================#

        #================================Info Frame=================================#

        self.infoFrame = Frame(self.mainFrame, highlightbackground="#00479c", highlightthickness=0, bg="#ffffff")
        self.infoFrame.grid(row=0, column=1, pady=0, padx=10)

        self.infoFrame.grid_rowconfigure(0, weight=1)
        self.infoFrame.grid_columnconfigure(0, weight=1)
        self.infoFrame.grid_rowconfigure(5, weight=1)
        self.infoFrame.grid_columnconfigure(5, weight=1)

        # Property ID
        self.propertyIDLabel = Label(self.infoFrame, text="Property ID:", bg='#ffffff')
        self.propertyIDLabel.grid(row=1, column=1, sticky=W, padx=5, pady=10)

        self.propertyIDEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.propertyID)
        self.propertyIDEntry.grid(row=1, column=2, sticky=W, padx=5, pady=10, ipady=5, ipadx=30)

        # Select Project
        self.projectLabel = Label(self.infoFrame, text="Project:", bg='#ffffff')
        self.projectLabel.grid(row=1, column=3, sticky=W, padx=5, pady=5)

        self.projectCombobox = ttk.Combobox(self.infoFrame, textvariable=self.project, values=self.projectList)
        self.projectCombobox.grid(row=1, column=4, sticky=W, padx=5, pady=5, ipady=4, ipadx=20)

        # Property Size
        self.propertySizeLabel = Label(self.infoFrame, text="Property Size:", bg='#ffffff')
        self.propertySizeLabel.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        self.propertySizeEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground = "#00479c", highlightcolor= "#00479c",
                                      highlightthickness=1, borderwidth=0, textvariable=self.propertySize)
        self.propertySizeEntry.grid(row=3, column=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Property Price
        self.propertyPriceLabel = Label(self.infoFrame, text="Property Price:", bg='#ffffff')
        self.propertyPriceLabel.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        self.propertyPriceEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.propertyPrice)
        self.propertyPriceEntry.grid(row=2, column=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Status
        self.statusLabel = Label(self.infoFrame, text="Status:", bg='#ffffff')
        self.statusLabel.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        self.statusEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.status)
        self.statusEntry.grid(row=4, column=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Property Location
        self.propertyLocationLabel = Label(self.infoFrame, text="Property Location:", bg='#ffffff')
        self.propertyLocationLabel.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        self.propertyLocationEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground = "#00479c",
                                                 highlightcolor= "#00479c", highlightthickness=1, borderwidth=0, textvariable=self.propertyLocation)
        self.propertyLocationEntry.grid(row=5, column=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=158, columnspan=3)

        # Property Description
        self.propertyDescriptionLabel = Label(self.infoFrame, text="Property Description:", bg='#ffffff')
        self.propertyDescriptionLabel.grid(row=6, column=1, sticky=W, padx=5, pady=10)

        self.propertyDescriptionEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground = "#00479c",
                                                 highlightcolor= "#00479c", highlightthickness=1, borderwidth=0, textvariable=self.propertyDescription)
        self.propertyDescriptionEntry.grid(row=6, column=2, sticky=W, padx=5, pady=10, ipady=5, ipadx=158, columnspan=3)

        #===========================================================================#

        # ===============================Button Frame================================#

        self.buttonFrame = Frame(self.mainFrame, bg="#ffffff")
        self.buttonFrame.grid(row=2, column=1, pady=0, padx=0, columnspan=2, sticky=E)

        # Show Button
        self.show_button = Button(self.buttonFrame, text="Show", width=15, height=2, bg='#00479c', fg="White",
                                  font="Arial 9", command=lambda: [showProperty()], relief="flat")
        self.show_button.grid(row=1, column=0, sticky=W, padx=0, pady=0, ipadx=30)

        # Save Button
        self.save_button = Button(self.buttonFrame, text="Save", width=15, height=2, bg='#00479c', fg="White",
                                  font="Arial 9", command=lambda: [addProperty()], relief="flat")
        self.save_button.grid(row=1, column=1, sticky=W, padx=15, pady=0, ipadx=30)

        # Update Button
        self.update_button = Button(self.buttonFrame, text="Update", width=15, height=2, bg='#00479c', fg="White",
                                    font="Arial 9", command=lambda: [updateProperty()], relief="flat")
        self.update_button.grid(row=1, column=2, sticky=W, padx=0, pady=0, ipadx=30)

        # Clear Button
        self.clear_button = Button(self.buttonFrame, text="Clear", width=15, height=2, bg='#00479c', fg="White",
                                   font="Arial 9", command=lambda: [clearPropertyFields()], relief="flat")
        self.clear_button.grid(row=1, column=3, sticky=W, padx=15, pady=0, ipadx=30)

        # Delete Button
        self.delete_button = Button(self.buttonFrame, text="Delete", width=15, height=2, bg='#E81123', fg="White",
                                   font="Arial 9", command=lambda: [deleteProperty()], relief="flat")
        self.delete_button.grid(row=1, column=4, sticky=W, padx=0, pady=0, ipadx=30)

        # ===========================================================================#

        #===================================Cards Frame=============================#

        self.cardFrame = Frame(self.mainFrame, bg="#ffffff")
        self.cardFrame.grid(row=0, column=2, pady=0, padx=10)

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

            return self.soldPropertyCard.create_polygon(points, **kwargs, smooth=True, fill="#B9F3E7")

        self.soldPropertyCard = Canvas(self.cardFrame, bg="#ffffff", highlightthickness=0, width=200, height=115)
        self.soldPropertyCard.grid(row=0, column=1, pady=5, padx=5)

        soldPropertyCanvas(0, 0, 200, 115, radius=30)

        self.soldPropertyImg = ImageTk.PhotoImage(Image.open(f"img/sold.png"))
        self.soldPropertyCard.create_image(15,10, anchor=NW, image=self.soldPropertyImg)

        self.soldLabel = Label(self.soldPropertyCard, text='Sold Properties', fg='#999999', bg='#B9F3E7', font="Arial 12 bold")
        self.soldLabel.pack()
        self.soldPropertyCard.create_window(100, 55, window=self.soldLabel)
        self.soldCountLabel = Label(self.soldPropertyCard, text='00', fg='#999999', bg='#B9F3E7', font="Arial 28 bold")
        self.soldCountLabel.pack()
        self.soldPropertyCard.create_window(100, 90, window=self.soldCountLabel)

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

            return self.availablePropertyCard.create_polygon(points, **kwargs, smooth=True, fill="#CFE6FE")

        self.availablePropertyCard = Canvas(self.cardFrame, bg="#ffffff", highlightthickness=0, width=200, height=115)
        self.availablePropertyCard.grid(row=0, column=2, pady=5, padx=5)

        availablePropertyCanvas(0, 0, 200, 115, radius=30)

        self.availablePropertyImg = ImageTk.PhotoImage(Image.open(f"img/available.png"))
        self.availablePropertyCard.create_image(15, 10, anchor=NW, image=self.availablePropertyImg)

        self.availableLabel = Label(self.availablePropertyCard, text='Available Properties', fg='#999999', bg='#CFE6FE', font="Arial 12 bold")
        self.availableLabel.pack()
        self.availablePropertyCard.create_window(100, 55, window=self.availableLabel)
        self.availableCountLabel = Label(self.availablePropertyCard, text='00', fg='#999999', bg='#CFE6FE', font="Arial 28 bold")
        self.availableCountLabel.pack()
        self.availablePropertyCard.create_window(100, 90, window=self.availableCountLabel)

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

            return self.totalPropertyCard.create_polygon(points, **kwargs, smooth=True, fill="#89A8D0")

        self.totalPropertyCard = Canvas(self.cardFrame, bg="#ffffff", highlightthickness=0, width=410, height=115)
        self.totalPropertyCard.grid(row=1, column=1, pady=5, padx=0, columnspan=2)

        totalPropertyCanvas(0, 0, 410, 115, radius=30)

        self.totalPropertyImg = ImageTk.PhotoImage(Image.open(f"img/all.png"))
        self.totalPropertyCard.create_image(15, 15, anchor=NW, image=self.totalPropertyImg)

        self.totalLabel = Label(self.totalPropertyCard, text='Total Properties', fg='#ffffff', bg='#89A8D0', font="Arial 16 bold")
        self.totalLabel.pack()
        self.totalPropertyCard.create_window(100, 75, window=self.totalLabel)

        self.totalPropertyCard.create_line(210, 100, 210, 15, fill="#ffffff", width=1)

        self.totalCountLabel = Label(self.totalPropertyCard, text='00', fg='#ffffff', bg='#89A8D0', font="Arial 28 bold")
        self.totalCountLabel.pack()
        self.totalPropertyCard.create_window(320, 70, window=self.totalCountLabel)

        #===========================================================================#

        # ===============================Data Table Frame============================#

        self.dataTableFrame = Frame(self.mainFrame, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.dataTableFrame.grid(row=1, column=1, pady=15, padx=0, columnspan=2, sticky=EW)

        scrolly = Scrollbar(self.dataTableFrame, orient=VERTICAL)
        scrollx = Scrollbar(self.dataTableFrame, orient=HORIZONTAL)
        self.ProductTable = ttk.Treeview(self.dataTableFrame, columns=(
            "propertyID", "projectID", "projectTitle", "propertySize", "propertyPrice", "status", "propertyLocation", "propertyDescription"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, height=10)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("#0", text="", anchor=CENTER)
        self.ProductTable.heading("propertyID", text="Property ID")
        self.ProductTable.heading("projectID", text="Project ID")
        self.ProductTable.heading("projectTitle", text="Project Title")
        self.ProductTable.heading("propertySize", text="Property Size")
        self.ProductTable.heading("propertyPrice", text="Property Price")
        self.ProductTable.heading("status", text="status")
        self.ProductTable.heading("propertyLocation", text="Property Location")
        self.ProductTable.heading("propertyDescription", text="Property Description")
        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.column("#0", width=0, stretch=NO)
        self.ProductTable.column("propertyID", width=30)
        self.ProductTable.column("projectID", width=30)
        self.ProductTable.column("projectTitle", width=30)
        self.ProductTable.column("propertySize", width=30)
        self.ProductTable.column("propertyPrice", width=30)
        self.ProductTable.column("status", width=20)
        self.ProductTable.column("propertyLocation", width=50)
        self.ProductTable.column("propertyDescription", width=100)

        # ===========================================================================#

        # ================================Functions=================================#

        def addProperty():
            if IsValid():
                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                try:
                    if self.propertyIDEntry.get() == "":
                        messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
                    else:
                        cur.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
                        propertyData = cur.fetchone()
                        cur.execute("select * from project")
                        projectData = cur.fetchall()
                        for Data in projectData:
                            if self.project.get() in Data:
                                projectID = Data[0]
                        if propertyData != None:
                            messagebox.showerror("Error", "This Property already Exist", parent=self.root)
                        else:
                            cur.execute("Insert into property(propertyID,projectID,propertySize,propertyPrice"
                                        ",status,propertyLocation,propertyDescription)values(?,?,?,?,?,?,?)",
                                        (self.propertyIDEntry.get(),
                                         projectID,
                                         self.propertySizeEntry.get(),
                                         self.propertyPriceEntry.get(),
                                         self.statusEntry.get(),
                                         self.propertyLocationEntry.get(),
                                         self.propertyDescriptionEntry.get()
                                         ))
                            con.commit()
                            messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)
                            automateID()
                            getProject()
                            getSoldProperties()
                            getAvailableProperties()
                            getTotalProperties()
                            clearPropertyFields()
                            showPropertyTable()
                except EXCEPTION as ex:
                    messagebox.showerror("Error", f"due to : {str(ex)}")

        # def addProperty_db2():
        #     if IsValid():
        #         connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                              database="gujranwalaemporium")
        #         cursor = connection.cursor(prepared=True)
        #         try:
        #             if self.propertyIDEntry.get() == "":
        #                 messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
        #             else:
        #                 cursor.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
        #                 propertyData = cursor.fetchone()
        #                 cursor.execute("select * from project")
        #                 projectData = cursor.fetchall()
        #                 for Data in projectData:
        #                     if self.project.get() in Data:
        #                         projectID = Data[0]
        #                 if propertyData != None:
        #                     messagebox.showerror("Error", "This Property already Exist", parent=self.root)
        #                 else:
        #                     cursor.execute("Insert into property(propertyID,projectID,propertySize,propertyPrice"
        #                                 ",status,propertyLocation,propertyDescription)values(?,?,?,?,?,?,?)",
        #                                 (self.propertyIDEntry.get(),
        #                                  projectID,
        #                                  self.propertySizeEntry.get(),
        #                                  self.propertyPriceEntry.get(),
        #                                  self.statusEntry.get(),
        #                                  self.propertyLocationEntry.get(),
        #                                  self.propertyDescriptionEntry.get()
        #                                  ))
        #                     connection.commit()
        #                     messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)
        #                     automateID_db2()
        #                     getProject_db2()
        #                     getSoldProperties()
        #                     getAvailableProperties()
        #                     getTotalProperties()
        #                     clearPropertyFields()
        #                     showPropertyTable_db2()
        #         except EXCEPTION as ex:
        #             messagebox.showerror("Error", f"due to : {str(ex)}")

        def showProperty():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.propertyIDEntry.get() == "":
                    messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
                else:
                    cur.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
                    propertyData = cur.fetchone()
                    cur.execute("select * from project where projectID=?", (propertyData[2],))
                    projectData = cur.fetchall()
                    if propertyData != None:
                        self.projectList = []
                        for project in projectData:
                            self.projectList.append(project[1])
                            self.projectCombobox['values'] = self.projectList
                        self.propertySize.set(propertyData[3])
                        self.propertyPrice.set(propertyData[4])
                        self.status.set(propertyData[9])
                        self.propertyLocation.set(propertyData[10])
                        self.propertyDescription.set(propertyData[11])
                    else:
                        messagebox.showerror("Error", "This Property does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        # def showProperty_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         if self.propertyIDEntry.get() == "":
        #             messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
        #         else:
        #             cursor.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
        #             propertyData = cursor.fetchone()
        #             cursor.execute("select * from project where projectID=?", (propertyData[2],))
        #             projectData = cursor.fetchall()
        #             if propertyData != None:
        #                 self.projectList = []
        #                 for project in projectData:
        #                     self.projectList.append(project[1])
        #                     self.projectCombobox['values'] = self.projectList
        #                 self.propertySize.set(propertyData[3])
        #                 self.propertyPrice.set(propertyData[4])
        #                 self.status.set(propertyData[9])
        #                 self.propertyLocation.set(propertyData[10])
        #                 self.propertyDescription.set(propertyData[11])
        #             else:
        #                 messagebox.showerror("Error", "This Property does not Exist", parent=self.root)
        #     except EXCEPTION as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}")

        def updateProperty():
            if IsValid():
                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                try:
                    if self.propertyIDEntry.get() == "":
                        messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
                    else:
                        cur.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
                        propertyData = cur.fetchone()
                        cur.execute("select * from project")
                        projectData = cur.fetchall()
                        for Data in projectData:
                            if self.project.get() in Data:
                                projectID = Data[0]
                        if propertyData == None:
                            messagebox.showerror("Error", "This Property not Exist", parent=self.root)
                        else:
                            cur.execute("Update property set projectID=?,propertySize=?,propertyPrice=?"
                                        ",status=?,propertyLocation=?,propertyDescription=? where propertyID=?",
                                        (
                                            projectID,
                                            self.propertySizeEntry.get(),
                                            self.propertyPriceEntry.get(),
                                            self.statusEntry.get(),
                                            self.propertyLocationEntry.get(),
                                            self.propertyDescriptionEntry.get(),

                                            self.propertyIDEntry.get()
                                         ))
                            con.commit()
                            messagebox.showinfo("Sucess", "Record updated sucessfully", parent=self.root)
                            automateID()
                            getProject()
                            getSoldProperties()
                            getAvailableProperties()
                            getTotalProperties()
                            clearPropertyFields()
                            showPropertyTable()
                except EXCEPTION as ex:
                    messagebox.showerror("Error", f"due to : {str(ex)}")

        # def updateProperty_db2():
        #     if IsValid():
        #         connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                              database="gujranwalaemporium")
        #         cursor = connection.cursor(prepared=True)
        #         try:
        #             if self.propertyIDEntry.get() == "":
        #                 messagebox.showerror("Error", "Property ID Must Required", parent=self.root)
        #             else:
        #                 cursor.execute("select * from property where propertyID=?", (self.propertyIDEntry.get(),))
        #                 propertyData = cursor.fetchone()
        #                 cursor.execute("select * from project")
        #                 projectData = cursor.fetchall()
        #                 for Data in projectData:
        #                     if self.project.get() in Data:
        #                         projectID = Data[0]
        #                 if propertyData == None:
        #                     messagebox.showerror("Error", "This Property not Exist", parent=self.root)
        #                 else:
        #                     cursor.execute("Update property set projectID=?,propertySize=?,propertyPrice=?"
        #                                 ",status=?,propertyLocation=?,propertyDescription=? where propertyID=?",
        #                                 (
        #                                     projectID,
        #                                     self.propertySizeEntry.get(),
        #                                     self.propertyPriceEntry.get(),
        #                                     self.statusEntry.get(),
        #                                     self.propertyLocationEntry.get(),
        #                                     self.propertyDescriptionEntry.get(),
        #
        #                                     self.propertyIDEntry.get()
        #                                  ))
        #                     connection.commit()
        #                     messagebox.showinfo("Sucess", "Record updated sucessfully", parent=self.root)
        #                     automateID_db2()
        #                     getProject_db2()
        #                     getSoldProperties()
        #                     getAvailableProperties()
        #                     getTotalProperties()
        #                     clearPropertyFields()
        #                     showPropertyTable_db2()
        #         except EXCEPTION as ex:
        #             messagebox.showerror("Error", f"due to : {str(ex)}")

        def automateID():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                cur.execute("select MAX(propertyID) from property")
                maxID = cur.fetchone()
                if maxID[0]==None:
                    self.propertyID.set(1)
                else:
                    self.propertyID.set(int(maxID[0])+1)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        automateID()

        # def automateID_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         cursor.execute("select MAX(propertyID) from property")
        #         maxID = cursor.fetchone()
        #         if maxID[0]==None:
        #             self.propertyID.set(1)
        #         else:
        #             self.propertyID.set(int(maxID[0])+1)
        #     except Exception as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
        #
        # automateID_db2()

        def getProject():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                cur.execute("select * from project")
                projectData = cur.fetchall()
                for project in projectData:
                    self.projectList.append(project[1])
                    self.projectCombobox['values'] = self.projectList
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        getProject()

        # def getProject_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         cursor.execute("select * from project")
        #         projectData = cursor.fetchall()
        #         for project in projectData:
        #             self.projectList.append(project[1])
        #             self.projectCombobox['values'] = self.projectList
        #     except EXCEPTION as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}")
        #
        # getProject_db2()

        def clearPropertyFields():
            self.projectList = []
            getProject()
            # getProject_db2()
            self.propertySizeEntry.delete(0, 'end')
            self.propertyPriceEntry.delete(0, 'end')
            self.status.set("Available")
            self.propertyLocationEntry.delete(0, 'end')
            self.propertyDescriptionEntry.delete(0, 'end')

        clearPropertyFields()

        def showPropertyTable():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                # cur.execute("select * from property")
                # data=cur.fetchall()
                # print(data)
                cur.execute("select property.propertyID, property.projectID, project.projectTitle, property.propertySize, property.propertyPrice, property.status"
                            ",property.propertyLocation, property.propertyDescription FROM property "
                            "INNER JOIN project ON property.projectID = project.projectID")
                rows = cur.fetchall()
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in reversed(rows):
                    propertyRowList = list(row)
                    row = tuple(propertyRowList)
                    self.ProductTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        showPropertyTable()

        # def showPropertyTable_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         # cur.execute("select * from property")
        #         cursor.execute("select property.propertyID, property.projectID, project.projectTitle, property.propertySize, property.propertyPrice, property.status"
        #                     ",property.propertyLocation, property.propertyDescription FROM property "
        #                     "INNER JOIN project ON property.projectID = project.projectID")
        #         rows = cursor.fetchall()
        #         self.ProductTable.delete(*self.ProductTable.get_children())
        #         for row in reversed(rows):
        #             propertyRowList = list(row)
        #             row = tuple(propertyRowList)
        #             self.ProductTable.insert('', END, values=row)
        #     except Exception as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
        #
        # showPropertyTable_db2()

        def getSoldProperties():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("SELECT COUNT(status) FROM property WHERE status = 'Sold'")
                soldProperty = cur.fetchone()
                self.soldCountLabel.config(text=soldProperty[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

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
                self.availableCountLabel.config(text=availableProperty[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

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
                self.totalCountLabel.config(text=totalProperty[0])
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        getTotalProperties()

        def deleteProperty():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.propertyIDEntry.get() == "":
                    messagebox.showerror("Error", "Project ID Must Required", parent=self.root)
                else:
                    cur.execute("select propertyID from bill where propertyID=?", (self.propertyIDEntry.get(),))
                    propertyData = cur.fetchone()
                    if propertyData != None:
                        messagebox.showerror("Error", "This Property Cannot be Delete because this Property is sold", parent=self.root)
                        clearPropertyFields()
                    else:
                        cur.execute("delete from property where propertyID=?", (self.propertyID.get(),))
                        con.commit()
                        showPropertyTable()
                        messagebox.showinfo("Sucess", "Record deleted sucessfully", parent=self.root)
                        clearPropertyFields()
                        automateID()
                        getSoldProperties()
                        getAvailableProperties()
                        getTotalProperties()
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def IsValid():
            if self.project.get() == '':
                messagebox.showerror("Error", "Project ID is Required", parent=self.root)
                return False

            if self.propertySizeEntry.get()=='':
                messagebox.showerror("Error", "Property Size is Required", parent=self.root)
                return False

            if self.propertyPriceEntry.get()=='':
                messagebox.showerror("Error", "Property Price is Required", parent=self.root)
                return False

            if self.propertyPriceEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Property Price", parent=self.root)
                return False

            if self.propertyLocationEntry.get() == '':
                messagebox.showerror("Error", "Property Location is Required", parent=self.root)
                return False

            if self.propertyDescriptionEntry.get() == '':
                messagebox.showerror("Error", "Property Description is Required", parent=self.root)
                return False

            return True

        # ===========================================================================#

if __name__=="__main__":

    root=Tk()
    obj=Add_property(root)
    root.mainloop()