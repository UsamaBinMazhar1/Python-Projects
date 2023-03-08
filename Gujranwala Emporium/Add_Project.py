from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

class Add_project:
    def __init__(self,root):
        self.root = root
        self.root.title("Add Property")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)
        self.root.maxsize(900, 550)

        # ================================Variables==================================#

        self.projectID = IntVar()
        self.projectTitle = StringVar()
        self.projectCost = IntVar()
        self.projectDescription = StringVar()

        #=============================Centered Screen===============================#

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 550
        window_width = 900
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #===========================================================================#

        #================================IMAGE Frame================================#

        self.imgFrame = Frame(self.root, bg="#00479c")
        self.imgFrame.pack(side=LEFT, pady=5, padx=0, ipady=0, ipadx=0, fill="y")

        self.Logo = Image.open(r"img/1.jpg")

        self.Logo = self.Logo.resize((400, 900), Image.ANTIALIAS)
        self.Logo = ImageTk.PhotoImage(self.Logo)

        logoLabel = Label(self.imgFrame, image=self.Logo, bg="#ffffff", relief="flat")
        logoLabel.pack(side=LEFT)

        #===========================================================================#

        #================================Info Frame================================#

        self.infoFrame = Frame(self.root, bg="#ffffff")
        self.infoFrame.pack(side=TOP, fill="x")
        self.infoFrame.grid_columnconfigure(0, weight=1)
        self.infoFrame.grid_columnconfigure(4, weight=1)

        # Add Project Label
        self.addProjectLabel = Label(self.infoFrame, text="Add Project", bg='#ffffff', font="Arial 16 bold")
        self.addProjectLabel.grid(row=0, column=1, padx=0, pady=30, sticky=EW, columnspan=3)

        # Project ID
        self.projectIDLabel = Label(self.infoFrame, text="Project ID:", bg='#ffffff')
        self.projectIDLabel.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        self.projectIDEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#000000",
                                     highlightcolor="#000000", highlightthickness=1, borderwidth=0,
                                     textvariable=self.projectID)
        self.projectIDEntry.grid(row=2, column=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=32)

        # Project Title
        self.projectTitleLabel = Label(self.infoFrame, text="Title:", bg='#ffffff')
        self.projectTitleLabel.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        self.projectTitleEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#000000",
                                    highlightcolor="#000000", highlightthickness=1, borderwidth=0,
                                    textvariable=self.projectTitle)
        self.projectTitleEntry.grid(row=3, column=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=32)

        # Project Cost
        self.projectCostLabel = Label(self.infoFrame, text="Project Cost:", bg='#ffffff')
        self.projectCostLabel.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        self.projectCostEntry = Entry(self.infoFrame, border=1, relief="solid", highlightbackground="#000000",
                                    highlightcolor="#000000", highlightthickness=1, borderwidth=0,
                                    textvariable=self.projectCost)
        self.projectCostEntry.grid(row=4, column=2, sticky=W, padx=5, pady=5, ipady=5, ipadx=32)

        # Project Description
        self.projectDescriptionLabel = Label(self.infoFrame, text="Description:", bg='#ffffff')
        self.projectDescriptionLabel.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        self.projectDescriptionEntry = Text(self.infoFrame, border=1, relief="solid", highlightbackground="#000000",
                                    highlightcolor="#000000", highlightthickness=1, borderwidth=0, height=5, width=23)
        self.projectDescriptionEntry.grid(row=5, column=2, sticky=W, padx=5, pady=5)

        # Show Button
        self.show_button = Button(self.infoFrame, text="Show", width=20, height=0, bg='#000000', fg="White",
                                  font="Arial 9", command=lambda: [showProject()], relief="flat")
        self.show_button.grid(row=4, column=3, sticky=W, padx=5, pady=5, ipady=2, ipadx=0)

        # Save Button
        self.save_button = Button(self.infoFrame, text="Save", width=20, height=0, bg='#000000', fg="White",
                                  font="Arial 9", command=lambda: [addProject()], relief="flat")
        self.save_button.grid(row=2, column=3, sticky=W, padx=5, pady=5, ipady=2, ipadx=0)

        # Update Button
        self.update_button = Button(self.infoFrame, text="Update", width=20, height=0, bg='#000000', fg="White",
                                    font="Arial 9", command=lambda: [updateProject()], relief="flat")
        self.update_button.grid(row=3, column=3, sticky=W, padx=5, pady=5, ipady=2, ipadx=0)

        # Clear Button
        self.clear_button = Button(self.infoFrame, text="Clear", width=20, height=0, bg='#000000', fg="White",
                                   font="Arial 9", command=lambda: [clearProjectFields()], relief="flat")
        self.clear_button.grid(row=5, column=3, sticky=N, padx=5, pady=5, ipady=2, ipadx=0)

        # Delete Button
        self.delete_button = Button(self.infoFrame, text="Delete", width=20, height=0, bg='#E81123', fg="White",
                                   font="Arial 9", command=lambda: [deleteProject()], relief="flat")
        self.delete_button.grid(row=5, column=3, sticky=N, padx=5, pady=45, ipady=2, ipadx=0)

        #===========================================================================#

        # ===============================Data Table Frame============================#

        self.dataTableFrame = Frame(self.root, bg='#ffffff')
        self.dataTableFrame.pack(side=TOP, anchor="nw", pady=5, padx=5, fill="x")

        scrolly = Scrollbar(self.dataTableFrame, orient=VERTICAL)
        self.ProductTable = ttk.Treeview(self.dataTableFrame, columns=("projectID", "projectTitle", "projectDescription", "projectCost"), yscrollcommand=scrolly.set, height=11)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("#0", text="", anchor=CENTER)
        self.ProductTable.heading("projectID", text="Project ID")
        self.ProductTable.heading("projectTitle", text="Project Title")
        self.ProductTable.heading("projectDescription", text="Project Description")
        self.ProductTable.heading("projectCost", text="Project Cost")
        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.column("#0", width=0, stretch=NO)
        self.ProductTable.column("projectID", width=100)
        self.ProductTable.column("projectTitle", width=100)
        self.ProductTable.column("projectDescription", width=100)
        self.ProductTable.column("projectCost", width=100)

        # ===========================================================================#

        def addProject():
            if IsValid():
                con = sqlite3.connect(database=r'marketing.db')
                cur = con.cursor()
                try:
                    if self.projectIDEntry.get() == "":
                        messagebox.showerror("Error", "Project ID Must Required", parent=self.root)
                    else:
                        cur.execute("select * from project where projectID=?", (self.projectIDEntry.get(),))
                        projectData = cur.fetchone()
                        if projectData != None:
                            messagebox.showerror("Error", "This Project already Exist", parent=self.root)
                        else:
                            cur.execute("Insert into project(projectID,projectTitle,projectDescription,projectCost)values(?,?,?,?)",
                                        (self.projectIDEntry.get(),
                                         self.projectTitleEntry.get(),
                                         self.projectDescriptionEntry.get("1.0",END),
                                         self.projectCostEntry.get(),
                                         ))
                            con.commit()
                            showProjectTable()
                            messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)
                            clearProjectFields()
                            automateID()
                except EXCEPTION as ex:
                    messagebox.showerror("Error", f"due to : {str(ex)}")

        # def addProject_db2():
        #     if IsValid():
        #         connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                              database="gujranwalaemporium")
        #         cursor = connection.cursor(prepared=True)
        #         try:
        #             if self.projectIDEntry.get() == "":
        #                 messagebox.showerror("Error", "Project ID Must Required", parent=self.root)
        #             else:
        #                 cursor.execute("select * from project where projectID=?", (self.projectIDEntry.get(),))
        #                 projectData = cursor.fetchone()
        #                 if projectData != None:
        #                     messagebox.showerror("Error", "This Project already Exist", parent=self.root)
        #                 else:
        #                     cursor.execute("Insert into project(projectID,projectTitle,projectDescription,projectCost)values(?,?,?,?)",
        #                                 (self.projectIDEntry.get(),
        #                                  self.projectTitleEntry.get(),
        #                                  self.projectDescriptionEntry.get("1.0",END),
        #                                  self.projectCostEntry.get(),
        #                                  ))
        #                     connection.commit()
        #                     showProjectTable_db2()
        #                     messagebox.showinfo("Sucess", "Record submitted sucessfully", parent=self.root)
        #                     clearProjectFields()
        #                     automateID_db2()
        #         except EXCEPTION as ex:
        #             messagebox.showerror("Error", f"due to : {str(ex)}")

        def updateProject():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.projectIDEntry.get() == "":
                    messagebox.showerror("Error", "Project ID Must Required", parent=self.root)
                else:
                    cur.execute("select * from project where projectID=?", (self.projectIDEntry.get(),))
                    projectData = cur.fetchone()
                    if projectData == None:
                        messagebox.showerror("Error", "This project Does not Exist", parent=self.root)
                    else:
                        cur.execute("Update project set projectTitle=?,projectDescription=? ,projectCost=? where projectID=?",
                                    (
                                     self.projectTitle.get(),
                                     self.projectDescriptionEntry.get("1.0",END),
                                     self.projectCost.get(),

                                     self.projectID.get()
                                     ))
                        con.commit()
                        showProjectTable()
                        messagebox.showinfo("Sucess", "Record updated sucessfully", parent=self.root)
                        clearProjectFields()
                        automateID()
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        # def updateProject_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         if self.projectIDEntry.get() == "":
        #             messagebox.showerror("Error", "Project ID Must Required", parent=self.root)
        #         else:
        #             cursor.execute("select * from project where projectID=?", (self.projectIDEntry.get(),))
        #             projectData = cursor.fetchone()
        #             if projectData == None:
        #                 messagebox.showerror("Error", "This project Does not Exist", parent=self.root)
        #             else:
        #                 cursor.execute("Update project set projectTitle=?,projectDescription=? ,projectCost=? where projectID=?",
        #                             (
        #                              self.projectTitle.get(),
        #                              self.projectDescriptionEntry.get("1.0",END),
        #                              self.projectCost.get(),
        #
        #                              self.projectID.get()
        #                              ))
        #                 connection.commit()
        #                 showProjectTable_db2()
        #                 messagebox.showinfo("Sucess", "Record updated sucessfully", parent=self.root)
        #                 clearProjectFields()
        #                 automateID_db2()
        #     except EXCEPTION as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}")

        def showProject():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.projectIDEntry.get() == "":
                    messagebox.showerror("Error", "project ID Must Required", parent=self.root)
                else:
                    cur.execute("select * from project where projectID=?", (self.projectIDEntry.get(),))
                    projectData = cur.fetchone()
                    if projectData != None:
                        clearProjectFields()
                        self.projectTitle.set(projectData[1])
                        self.projectDescriptionEntry.insert(END,projectData[2])
                        self.projectCost.set(projectData[3])
                    else:
                        messagebox.showerror("Error", "This Project does not Exist", parent=self.root)
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        # def showProject_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         if self.projectIDEntry.get() == "":
        #             messagebox.showerror("Error", "project ID Must Required", parent=self.root)
        #         else:
        #             cursor.execute("select * from project where projectID=?", (self.projectIDEntry.get(),))
        #             projectData = cursor.fetchone()
        #             if projectData != None:
        #                 clearProjectFields()
        #                 self.projectTitle.set(projectData[1])
        #                 self.projectDescriptionEntry.insert(END,projectData[2])
        #                 self.projectCost.set(projectData[3])
        #             else:
        #                 messagebox.showerror("Error", "This Project does not Exist", parent=self.root)
        #     except EXCEPTION as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}")

        def clearProjectFields():
            self.projectTitleEntry.delete(0, 'end')
            self.projectDescriptionEntry.delete("1.0","end")
            self.projectCostEntry.delete(0, 'end')

        clearProjectFields()

        def deleteProject():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                if self.projectIDEntry.get() == "":
                    messagebox.showerror("Error", "Project ID Must Required", parent=self.root)
                else:
                    cur.execute("select projectID from property where projectID=?", (self.projectIDEntry.get(),))
                    projectData = cur.fetchone()
                    if projectData != None:
                        messagebox.showerror("Error", "This Project Cannot be Delete because it has Property", parent=self.root)
                        clearProjectFields()
                    else:
                        cur.execute("delete from project where projectID=?", (self.projectID.get(),))
                        con.commit()
                        showProjectTable()
                        messagebox.showinfo("Sucess", "Record deleted sucessfully", parent=self.root)
                        clearProjectFields()
                        automateID()
            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        def showProjectTable():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                cur.execute("select * from project")
                rows = cur.fetchall()
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in reversed(rows):
                    projectRowList = list(row)
                    row = tuple(projectRowList)
                    self.ProductTable.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        showProjectTable()

        # def showProjectTable_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         cursor.execute("select * from project")
        #         rows = cursor.fetchall()
        #         self.ProductTable.delete(*self.ProductTable.get_children())
        #         for row in reversed(rows):
        #             projectRowList = list(row)
        #             row = tuple(projectRowList)
        #             self.ProductTable.insert('', END, values=row)
        #     except Exception as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
        #
        # showProjectTable_db2()

        def automateID():
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            try:
                cur.execute("select MAX(projectID) from project")
                maxID = cur.fetchone()
                if maxID[0]==None:
                    self.projectID.set(1)
                else:
                    self.projectID.set(int(maxID[0])+1)
            except Exception as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)

        automateID()

        # def automateID_db2():
        #     connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
        #                                          database="gujranwalaemporium")
        #     cursor = connection.cursor(prepared=True)
        #     try:
        #         cursor.execute("select MAX(projectID) from project")
        #         maxID = cursor.fetchone()
        #         if maxID[0]==None:
        #             self.projectID.set(1)
        #         else:
        #             self.projectID.set(int(maxID[0])+1)
        #     except Exception as ex:
        #         messagebox.showerror("Error", f"due to : {str(ex)}", parent=self.root)
        #
        # automateID_db2()


        def IsValid():
            if self.projectTitleEntry.get()=='':
                messagebox.showerror("Error", "Project Title is Required", parent=self.root)
                return False

            if self.projectCostEntry.get()=='':
                messagebox.showerror("Error", "Project Cost is Required", parent=self.root)
                return False

            if self.projectCostEntry.get().isdigit() == False:
                messagebox.showerror("Error", "Invalid Project Cost", parent=self.root)
                return False

            if self.projectDescriptionEntry.get("1.0",END)=='':
                messagebox.showerror("Error", "Project Description is Required", parent=self.root)
                return False
            return True


if __name__=="__main__":

    root=Tk()
    obj=Add_project(root)
    root.mainloop()