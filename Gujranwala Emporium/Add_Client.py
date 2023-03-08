from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class Add_client:
    def __init__(self,root):
        self.root = root
        self.root.title("Add Client")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        # ================================Variables==================================#

        self.clientCnic = IntVar()
        self.clientName = StringVar()
        self.clientContact = StringVar()
        self.clientAddress = StringVar()

        self.kinCnic = IntVar()
        self.kinName = StringVar()
        self.kinContact = StringVar()
        self.kinAddress = StringVar()

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

        self.titleLabel = Label(self.titleFrame, text="Add Client", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        #===========================================================================#

        # ================================Bottom Frame===============================#

        self.bottomFrame = Frame(self.root, bg="#00479c", border=3)
        self.bottomFrame.pack(side=BOTTOM, anchor="nw", pady=0, padx=5, fill="x")

        self.bottomLabel = Label(self.bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white",
                                 font="Arial 9")
        self.bottomLabel.pack()

        # ============================================================================#

        # ===============================Main Frame=================================#

        self.mainFrame = Frame(self.root, bg="#ffffff")
        self.mainFrame.pack(fill=BOTH, pady=0, ipady=300)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(4, weight=1)
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_rowconfigure(4, weight=1)

        # ===========================================================================#

        #==============================CLient Info Frame============================#

        self.clientInfoFrame = Frame(self.mainFrame, highlightbackground="#00479c", highlightthickness=0, bg="#ffffff")
        self.clientInfoFrame.grid(row=1, column=1, pady=0, padx=5)

        self.clientInfoFrame.grid_rowconfigure(0, weight=1)
        self.clientInfoFrame.grid_columnconfigure(0, weight=1)
        self.clientInfoFrame.grid_rowconfigure(5, weight=1)
        self.clientInfoFrame.grid_columnconfigure(5, weight=1)

        # Client CNIC
        self.clientcnic_label = Label(self.clientInfoFrame, text="Client CNIC:", bg='#ffffff')
        self.clientcnic_label.grid(column=1, row=1, sticky=W, padx=5, pady=10)

        self.clientcnic_entry = Entry(self.clientInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.clientCnic)
        self.clientcnic_entry.grid(column=2, row=1, sticky=W, padx=5, pady=10, ipady=5, ipadx=30)

        # Client Name
        self.clientname_label = Label(self.clientInfoFrame, text="Client Name:", bg='#ffffff')
        self.clientname_label.grid(column=3, row=1, sticky=W, padx=5, pady=5)

        self.clientname_entry = Entry(self.clientInfoFrame, border=1, relief="solid", highlightbackground = "#00479c", highlightcolor= "#00479c",
                                      highlightthickness=1, borderwidth=0, textvariable=self.clientName)
        self.clientname_entry.grid(column=4, row=1, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Client Contact
        self.clientcontact_label = Label(self.clientInfoFrame, text="Client Contact:", bg='#ffffff')
        self.clientcontact_label.grid(column=1, row=2, sticky=W, padx=5, pady=5)

        self.clientcontact_entry = Entry(self.clientInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.clientContact)
        self.clientcontact_entry.grid(column=2, row=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Clients Current Address
        self.clientsCurrentAddress_label = Label(self.clientInfoFrame, text="Clients Current Address:", bg='#ffffff')
        self.clientsCurrentAddress_label.grid(column=1, row=3, sticky=W, padx=5, pady=10)

        self.clientsCurrentAddress_entry = Entry(self.clientInfoFrame, border=1, relief="solid", highlightbackground = "#00479c",
                                                 highlightcolor= "#00479c", highlightthickness=1, borderwidth=0, textvariable=self.clientAddress)
        self.clientsCurrentAddress_entry.grid(column=2, row=3, sticky=W, padx=5, pady=10, ipady=5, ipadx=171, columnspan=3)

        #===========================================================================#

        #==============================Kin Info Frame============================#

        self.kinInfoFrame = Frame(self.mainFrame, highlightbackground="#00479c", highlightthickness=0, bg="#ffffff")
        self.kinInfoFrame.grid(row=1, column=3, pady=0, padx=5)

        self.kinInfoFrame.grid_rowconfigure(0, weight=1)
        self.kinInfoFrame.grid_columnconfigure(0, weight=1)
        self.kinInfoFrame.grid_rowconfigure(5, weight=1)
        self.kinInfoFrame.grid_columnconfigure(5, weight=1)

        # Kin CNIC
        self.kincnic_label = Label(self.kinInfoFrame, text="Kin CNIC:", bg='#ffffff')
        self.kincnic_label.grid(column=1, row=1, sticky=W, padx=5, pady=10)

        self.kincnic_entry = Entry(self.kinInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.kinCnic)
        self.kincnic_entry.grid(column=2, row=1, sticky=W, padx=5, pady=10, ipady=5, ipadx=30)

        # Client Name
        self.kinname_label = Label(self.kinInfoFrame, text="Kin Name:", bg='#ffffff')
        self.kinname_label.grid(column=3, row=1, sticky=W, padx=5, pady=5)

        self.kinname_entry = Entry(self.kinInfoFrame, border=1, relief="solid", highlightbackground = "#00479c", highlightcolor= "#00479c",
                                      highlightthickness=1, borderwidth=0, textvariable=self.kinName)
        self.kinname_entry.grid(column=4, row=1, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Client Contact
        self.kincontact_label = Label(self.kinInfoFrame, text="Kin Contact:", bg='#ffffff')
        self.kincontact_label.grid(column=1, row=2, sticky=W, padx=5, pady=5)

        self.kincontact_entry = Entry(self.kinInfoFrame, border=1, relief="solid", highlightbackground="#00479c",
                                      highlightcolor="#00479c", highlightthickness=1, borderwidth=0, textvariable=self.kinContact)
        self.kincontact_entry.grid(column=2, row=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=30)

        # Clients Current Address
        self.kinCurrentAddress_label = Label(self.kinInfoFrame, text="Kin Current Address:", bg='#ffffff')
        self.kinCurrentAddress_label.grid(column=1, row=3, sticky=W, padx=5, pady=10)

        self.kinCurrentAddress_entry = Entry(self.kinInfoFrame, border=1, relief="solid", highlightbackground = "#00479c",
                                                 highlightcolor= "#00479c", highlightthickness=1, borderwidth=0, textvariable=self.kinAddress)
        self.kinCurrentAddress_entry.grid(column=2, row=3, sticky=W, padx=5, pady=10, ipady=5, ipadx=163, columnspan=3)

        #===========================================================================#

        # ===============================Data Table Frame============================#

        self.dataTableFrame = Frame(self.mainFrame, highlightbackground="#00479c", highlightthickness=0, bg='#ffffff')
        self.dataTableFrame.grid(row=2, column=1, pady=15, padx=5, ipady=5, ipadx=200, columnspan=3)

        scrolly = Scrollbar(self.dataTableFrame, orient=VERTICAL)
        scrollx = Scrollbar(self.dataTableFrame, orient=HORIZONTAL)
        self.ProductTable = ttk.Treeview(self.dataTableFrame, columns=(
        "clientCnic", "clientName", "clientContact", "clientAddress", "kinCnic", "kinName", "kinContact", "kinAddress"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, height=15)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("#0", text="", anchor=CENTER)
        self.ProductTable.heading("clientCnic", text="Client Cnic")
        self.ProductTable.heading("clientName", text="Client Name")
        self.ProductTable.heading("clientContact", text="Client Contact")
        self.ProductTable.heading("clientAddress", text="Client Address")
        self.ProductTable.heading("kinCnic", text="Kin Cnic")
        self.ProductTable.heading("kinName", text="Kin Name")
        self.ProductTable.heading("kinContact", text="Kin Contact")
        self.ProductTable.heading("kinAddress", text="Kin Address")
        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.column("#0", width=0, stretch=NO)
        self.ProductTable.column("clientCnic", width=100)
        self.ProductTable.column("clientName", width=100)
        self.ProductTable.column("clientContact", width=100)
        self.ProductTable.column("clientAddress", width=100)
        self.ProductTable.column("kinCnic", width=100)
        self.ProductTable.column("kinName", width=100)
        self.ProductTable.column("kinContact", width=100)
        self.ProductTable.column("kinAddress", width=100)

        # ===========================================================================#

        # ===============================Button Frame================================#

        self.buttonFrame = Frame(self.mainFrame, bg="#ffffff")
        self.buttonFrame.grid(row=3, column=1, pady=0, padx=5, columnspan=3)
        self.buttonFrame.grid_columnconfigure(0, weight=1)

        # Show Button
        self.show_button = Button(self.buttonFrame, text="Show", width=15, height=2, bg='#00479c', fg="White",
                                  font="Arial 9", command=lambda: [showClient()])
        self.show_button.grid(column=1, row=0, sticky=W, padx=5, pady=10, ipady=2, ipadx=12)

        # Save Button
        self.save_button = Button(self.buttonFrame,text="Save", width=15, height=2, bg='#00479c', fg="White", font="Arial 9", command=lambda:[addClient()])
        self.save_button.grid(column=2, row=0, sticky=W, padx=5, pady=10, ipady=2, ipadx=12)

        # Update Button
        self.update_button = Button(self.buttonFrame,text="Update", width=15, height=2, bg='#00479c', fg="White", font="Arial 9", command=lambda:[updateClient()])
        self.update_button.grid(column=3, row=0, sticky=W, padx=5, pady=10, ipady=2, ipadx=13)

        # Clear Button
        self.clear_button = Button(self.buttonFrame, text="Clear", width=15, height=2, bg='#00479c', fg="White",
                                    font="Arial 9", command=lambda: [clearClientFields()])
        self.clear_button.grid(column=4, row=0, sticky=W, padx=5, pady=10, ipady=2, ipadx=13)

        # Delete Button
        self.delete_button = Button(self.buttonFrame, text="Delete", width=15, height=2, bg='#E81123', fg="White",
                                   font="Arial 9", relief="flat", command=lambda: [deleteClientFields()])
        self.delete_button.grid(column=5, row=0, sticky=W, padx=5, pady=10, ipady=2, ipadx=13)

        # ===========================================================================#

        # ================================Bottom Frame===============================#

        self.bottomFrame = Frame(self.root, bg="#00479c", border=3)
        self.bottomFrame.pack(side=BOTTOM, anchor="nw", pady=0, padx=5, fill="x")

        self.bottomLabel = Label(self.bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white", font="Arial 9")
        self.bottomLabel.pack()

        #============================================================================#


        def addClient():
            if IsValid():
                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                try:
                    cur.execute("select * from client where client_cnic=?", (self.clientcnic_entry.get(),))
                    client_cnic = cur.fetchone()
                    if client_cnic != None:
                        messagebox.showerror("Error", "This Client already Exist", parent=self.root)
                    else:
                        cur.execute("Insert into client(client_cnic,client_name,client_contact,client_address,kin_cnic,kin_name,kin_contact,kin_address)values(?,?,?,?,?,?,?,?);",
                                    (self.clientcnic_entry.get(),
                                     self.clientname_entry.get(),
                                     self.clientcontact_entry.get(),
                                     self.clientsCurrentAddress_entry.get(),
                                     self.kincnic_entry.get(),
                                     self.kinname_entry.get(),
                                     self.kincontact_entry.get(),
                                     self.kinCurrentAddress_entry.get()
                                     ))
                        con.commit()
                        con.close()
                        showClientTable()
                        messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)
                        clearClientFields()
                except EXCEPTION as ex:
                    messagebox.showerror("Error", f"due to : {str(ex)}")

        # def addClient_db2():
        #     if IsValid():
        #         connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #         cursor = connection.cursor(prepared=True)
        #         try:
        #             cursor.execute("select * from client where client_cnic=?", (self.clientcnic_entry.get(),))
        #             client_cnic = cursor.fetchone()
        #             print(client_cnic)
        #             if client_cnic != None:
        #                 messagebox.showerror("Error", "This Client already Exist", parent=self.root)
        #             else:
        #                 cursor.execute("Insert into client(client_cnic,client_name,client_contact,client_address,kin_cnic,kin_name,kin_contact,kin_address)values(?,?,?,?,?,?,?,?)",
        #                             (self.clientcnic_entry.get(),
        #                              self.clientname_entry.get(),
        #                              self.clientcontact_entry.get(),
        #                              self.clientsCurrentAddress_entry.get(),
        #                              self.kincnic_entry.get(),
        #                              self.kinname_entry.get(),
        #                              self.kincontact_entry.get(),
        #                              self.kinCurrentAddress_entry.get()
        #                              ))
        #
        #                 messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)
        #
        #                 clearClientFields()
        #             connection.commit()
        #             connection.close()
        #             showClientTable_db2()
        #         except EXCEPTION as ex:
        #             messagebox.showerror("Error", f"due to : {str(ex)}")

        def showClient():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.clientcnic_entry.get() == "":
                    messagebox.showerror("Error", "Client CNIC Must Required", parent=self.root)
                else:
                    cur.execute("select * from client where client_cnic=?", (self.clientcnic_entry.get(),))
                    clientData = cur.fetchone()
                    if clientData != None:
                        self.clientName.set(clientData[1])
                        self.clientContact.set(clientData[2])
                        self.clientAddress.set(clientData[3])
                        self.kinCnic.set(clientData[4])
                        self.kinName.set(clientData[5])
                        self.kinContact.set(clientData[6])
                        self.kinAddress.set(clientData[7])
                    else:
                        messagebox.showerror("Error", "This Client does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        # def showClient_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         if self.clientcnic_entry.get() == "":
        #             messagebox.showerror("Error", "Client CNIC Must Required", parent=self.root)
        #         else:
        #             cursor.execute("select * from client where client_cnic=?", (self.clientcnic_entry.get(),))
        #             clientData = cursor.fetchone()
        #             if clientData != None:
        #                 self.clientName.set(clientData[1])
        #                 self.clientContact.set(clientData[2])
        #                 self.clientAddress.set(clientData[3])
        #                 self.kinCnic.set(clientData[4])
        #                 self.kinName.set(clientData[5])
        #                 self.kinContact.set(clientData[6])
        #                 self.kinAddress.set(clientData[7])
        #             else:
        #                 messagebox.showerror("Error", "This Client does not Exist", parent=self.root)
        #     except EXCEPTION as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}")

        def updateClient():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.clientcnic_entry.get() == "":
                    messagebox.showerror("Error", "Client CNIC Must Required", parent=self.root)
                else:
                    cur.execute("select * from client where client_cnic=?", (self.clientcnic_entry.get(),))
                    client_cnic = cur.fetchone()
                    if client_cnic == None:
                        messagebox.showerror("Error", "This Client Does not Exist", parent=self.root)
                    else:
                        cur.execute("Update client set client_name=?,client_contact=? ,client_address=?,kin_cnic=?,kin_name=?,kin_contact=?,kin_address=? where client_cnic=?",
                                    (
                                     self.clientName.get(),
                                     self.clientContact.get(),
                                     self.clientAddress.get(),
                                     self.kinCnic.get(),
                                     self.kinName.get(),
                                     self.kinContact.get(),
                                     self.kinAddress.get(),

                                     self.clientCnic.get()
                                     ))
                        con.commit()
                        showClientTable()
                        messagebox.showinfo("Sucess", "Record updated sucessfully", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        # def updateClient_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         if self.clientcnic_entry.get() == "":
        #             messagebox.showerror("Error", "Client CNIC Must Required", parent=self.root)
        #         else:
        #             cursor.execute("select * from client where client_cnic=?", (self.clientcnic_entry.get(),))
        #             client_cnic = cursor.fetchone()
        #             if client_cnic == None:
        #                 messagebox.showerror("Error", "This Client Does not Exist", parent=self.root)
        #             else:
        #                 cursor.execute(
        #                     "Update client set client_name=?,client_contact=? ,client_address=?,kin_cnic=?,kin_name=?,kin_contact=?,kin_address=? where client_cnic=?",
        #                     (
        #                         self.clientName.get(),
        #                         self.clientContact.get(),
        #                         self.clientAddress.get(),
        #                         self.kinCnic.get(),
        #                         self.kinName.get(),
        #                         self.kinContact.get(),
        #                         self.kinAddress.get(),
        #
        #                         self.clientCnic.get()
        #                     ))
        #                 connection.commit()
        #                 showClientTable_db2()
        #                 messagebox.showinfo("Sucess", "Record updated sucessfully", parent=self.root)
        #     except EXCEPTION as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}")

        def showClientTable():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                cur.execute("select * from client")
                rows = cur.fetchall()
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in reversed(rows):
                    clientRowList = list(row)
                    row = tuple(clientRowList)
                    self.ProductTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        showClientTable()

        # def showClientTable_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         cursor.execute("select * from client")
        #         rows = cursor.fetchall()
        #         self.ProductTable.delete(*self.ProductTable.get_children())
        #         for row in reversed(rows):
        #             clientRowList = list(row)
        #             row = tuple(clientRowList)
        #             self.ProductTable.insert('', END, values=row)
        #     except Exception as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
        #
        # showClientTable_db2()

        def clearClientFields():
            self.clientcnic_entry.delete(0, 'end')
            self.clientname_entry.delete(0, 'end')
            self.clientcontact_entry.delete(0, 'end')
            self.clientsCurrentAddress_entry.delete(0, 'end')
            self.kincnic_entry.delete(0, 'end')
            self.kinname_entry.delete(0, 'end')
            self.kincontact_entry.delete(0, 'end')
            self.kinCurrentAddress_entry.delete(0, 'end')

        clearClientFields()

        def deleteClientFields():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.clientcnic_entry.get() == "":
                    messagebox.showerror("Error", "Client CNIC Must Required", parent=self.root)
                else:
                    cur.execute("select client_cnic from property where client_cnic=?", (self.clientcnic_entry.get(),))
                    client_cnic = cur.fetchone()
                    print(client_cnic)
                    if client_cnic != None:
                        messagebox.showerror("Error", "This Client Cannot be Delete because it has Property", parent=self.root)
                        clearClientFields()
                    else:
                        cur.execute(
                            "delete from client where client_cnic=?", (self.clientCnic.get(),))
                        con.commit()
                        showClientTable()
                        clearClientFields()
                        messagebox.showinfo("Sucess", "Record Deleted sucessfully", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def IsValid():
            if self.clientcnic_entry.get()=='':
                messagebox.showerror("Error", "Client CNIC is Required", parent=self.root)
                return False

            if self.clientcnic_entry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Client CNIC", parent=self.root)
                return False

            if self.clientname_entry.get()=='':
                messagebox.showerror("Error", "Client Name is Required", parent=self.root)
                return False

            # if self.clientname_entry.get().isalpha() == False and self.clientname_entry.get().isspace() == False:
            #     messagebox.showerror("Error", "Invalid Client Name", parent=self.root)
            #     return False

            if self.clientcontact_entry.get()=='':
                messagebox.showerror("Error", "Client Contact is Required", parent=self.root)
                return

            if self.clientcontact_entry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Client Contact", parent=self.root)
                return False

            if self.clientsCurrentAddress_entry.get()=='':
                messagebox.showerror("Error", "Client Address is Required", parent=self.root)
                return False

            if self.kincnic_entry.get() == '':
                messagebox.showerror("Error", "Kin CNIC is Required", parent=self.root)
                return False

            if self.kincnic_entry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Kin CNIC", parent=self.root)
                return False

            if self.kinname_entry.get() == '':
                messagebox.showerror("Error", "Kin Name is Required", parent=self.root)
                return False

            # if self.kinname_entry.get().isalpha() == False:
            #     messagebox.showerror("Error", "Invalid Kin Name", parent=self.root)
            #     return False

            if self.kincontact_entry.get() == '':
                messagebox.showerror("Error", "Kin Contact is Required", parent=self.root)
                return

            if self.kincontact_entry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Kin Contact", parent=self.root)
                return False

            if self.kinCurrentAddress_entry.get() == '':
                messagebox.showerror("Error", "Kin Address is Required", parent=self.root)
                return False

            return True



if __name__=="__main__":

    root=Tk()
    obj=Add_client(root)
    root.mainloop()