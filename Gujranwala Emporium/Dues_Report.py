from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from datetime import date, timedelta
import mysql.connector

class duesReport:
    def __init__(self,root):
        self.root = root
        self.root.title("Dues Report")
        self.root.configure(bg='#ffffff')
        self.root.minsize(900, 550)

        # ================================Variables==================================#

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

        #===============================Title Frame=================================#

        self.titleFrame = Frame(self.root, bg="#00479c")
        self.titleFrame.pack(side=TOP, anchor="nw", pady=10, padx=5, fill="x")

        self.titleLabel = Label(self.titleFrame, text="Dues Report", bg="#00479c", fg="white", font="Arial 14")
        self.titleLabel.pack()

        #============================================================================#

        # ===============================Due Label Frame=================================#

        self.dueLabelFrame = Frame(self.root, bg="#ffffff")
        self.dueLabelFrame.pack(side=TOP, anchor="nw", pady=5, padx=90, fill="x")

        self.dueLabel = Label(self.dueLabelFrame, text="Due Report", bg="#ffffff", fg="black", font="Times 12 bold")
        self.dueLabel.pack(side=LEFT, anchor="w", pady=0, padx=0)

        self.refreshButton = Button(self.dueLabelFrame, text="Refresh", width=20, height=1,
                                      bg='#00479c', fg="White", font="Arial 9", relief="flat",
                                      command=lambda: [getRecord()])
        self.refreshButton.pack(side=RIGHT, anchor="e", ipady=5, padx=0)

        # ============================================================================#

        # ===============================Data Table Frame============================#

        self.duedataTableFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.duedataTableFrame.pack(side=TOP, anchor="nw", padx=90, fill="x")

        scrolly = Scrollbar(self.duedataTableFrame, orient=VERTICAL)
        scrollx = Scrollbar(self.duedataTableFrame, orient=HORIZONTAL)
        self.dueProductTable = ttk.Treeview(self.duedataTableFrame, columns=(
            "clientCnic", "clientName", "clientContact", "propertyID", "billID", "dueDate"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, height=15)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.dueProductTable.xview)
        scrolly.config(command=self.dueProductTable.yview)
        self.dueProductTable.heading("#0", text="", anchor=CENTER)
        self.dueProductTable.heading("clientCnic", text="Client Cnic")
        self.dueProductTable.heading("clientName", text="Client Name")
        self.dueProductTable.heading("clientContact", text="Client Contact")
        self.dueProductTable.heading("propertyID", text="Property ID")
        self.dueProductTable.heading("billID", text="Bill ID")
        self.dueProductTable.heading("dueDate", text="Due Date")
        self.dueProductTable.pack(fill=BOTH, expand=1)

        self.dueProductTable.column("#0", width=0, stretch=NO)
        self.dueProductTable.column("clientCnic", width=100)
        self.dueProductTable.column("clientName", width=100)
        self.dueProductTable.column("clientContact", width=100)
        self.dueProductTable.column("propertyID", width=100)
        self.dueProductTable.column("billID", width=100)
        self.dueProductTable.column("dueDate", width=100)

        # ===========================================================================#

        # ===============================Over Due Label Frame=================================#

        self.overDueLabelFrame = Frame(self.root, bg="#ffffff")
        self.overDueLabelFrame.pack(side=TOP, anchor="nw", pady=5, padx=90, fill="x")

        self.overDueLabel = Label(self.overDueLabelFrame, text="Over Due Report", bg="#ffffff", fg="black", font="Times 12 bold")
        self.overDueLabel.pack(side=LEFT, anchor="w", pady=0, padx=0)

        # ============================================================================#

        # ===============================Data Table Frame============================#

        self.dataTableFrame = Frame(self.root, highlightbackground="#00479c", highlightthickness=1, bg='#ffffff')
        self.dataTableFrame.pack(side=TOP, anchor="nw", padx=90, fill="x")

        scrolly = Scrollbar(self.dataTableFrame, orient=VERTICAL)
        scrollx = Scrollbar(self.dataTableFrame, orient=HORIZONTAL)
        self.ProductTable = ttk.Treeview(self.dataTableFrame, columns=(
            "clientCnic", "clientName", "clientContact", "propertyID", "billID", "dueDate"),
                                         yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, height=15)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.heading("#0", text="", anchor=CENTER)
        self.ProductTable.heading("clientCnic", text="Client Cnic")
        self.ProductTable.heading("clientName", text="Client Name")
        self.ProductTable.heading("clientContact", text="Client Contact")
        self.ProductTable.heading("propertyID", text="Property ID")
        self.ProductTable.heading("billID", text="Bill ID")
        self.ProductTable.heading("dueDate", text="Due Date")
        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.column("#0", width=0, stretch=NO)
        self.ProductTable.column("clientCnic", width=100)
        self.ProductTable.column("clientName", width=100)
        self.ProductTable.column("clientContact", width=100)
        self.ProductTable.column("propertyID", width=100)
        self.ProductTable.column("billID", width=100)
        self.ProductTable.column("dueDate", width=100)

        # ===========================================================================#

        def getRecord():
            self.dueList = []
            self.overDueList = []
            con = sqlite3.connect(database=r'marketing.db')
            cur = con.cursor()
            # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
            #                                      database="gujranwalaemporium")
            # cursor = connection.cursor(prepared=True)
            try:
                cur.execute("select propertyID,billID,dueDate from bill where status='Unpaid'")
                billData = cur.fetchall()
                for data in billData:
                    dueDate = data[2]
                    dueDate = date.fromisoformat(dueDate.replace("/","-"))
                    days = dueDate-date.today()
                    if days <= timedelta(days=10) and days >= timedelta(days=0):
                        print(data)
                        cur.execute("select client_cnic from property where propertyID=?", (data[0],))
                        clientCNIC = cur.fetchall()
                        for clientcnic in clientCNIC:
                            cur.execute("select client_cnic,client_name,client_contact from client where client_cnic=?", (clientcnic[0],))
                            clientData = cur.fetchall()
                            for client in clientData:
                                print(client)
                                self.dueList.append(client+data)
                        print('Due List')
                        print(self.dueList)

                        self.dueProductTable.delete(*self.dueProductTable.get_children())
                        for row in self.dueList:
                            self.dueProductTable.insert('', END, values=row)
                    elif days < timedelta(days=0):
                        print(data)
                        cur.execute("select client_cnic from property where propertyID=?", (data[0],))
                        clientCNIC = cur.fetchall()
                        for clientcnic in clientCNIC:
                            cur.execute("select client_cnic,client_name,client_contact from client where client_cnic=?",
                                        (clientcnic[0],))
                            clientData = cur.fetchall()
                            for client in clientData:
                                print(client)
                                self.overDueList.append(client + data)
                        print('Due List')
                        print(self.overDueList)

                        self.ProductTable.delete(*self.ProductTable.get_children())
                        for row in self.overDueList:
                            self.ProductTable.insert('', END, values=row)

            except EXCEPTION as ex:
                messagebox.showerror("Error", f"due to : {str(ex)}")

        getRecord()


if __name__=="__main__":

    root=Tk()
    obj=duesReport(root)
    root.mainloop()