import pandas as pd
import sqlite3
from tkinter import messagebox

df = pd.read_excel("g1f.xlsx")

print(df)
lists = df.values.tolist()
print(lists)

id = 38

for data in lists:
    print(data)
    con = sqlite3.connect(database=r'marketing.db')
    cur = con.cursor()

    cur.execute("Insert into property(propertyID,projectID,propertySize,propertyPrice"
                ",status,propertyLocation,propertyDescription)values(?,?,?,?,?,?,?)",
                (id,1,data[1],data[2], "Available", f"Ground & 1st Floor {data[0]}", f"Property {data[0]} on Ground & 1st Floor"))
    con.commit()
    id = id+1
messagebox.showinfo("Sucess", "Record submitted sucessfully")

con = sqlite3.connect(database=r'marketing.db')
cur = con.cursor()

cur.execute("select * from property")
propertyData = cur.fetchall()

print(propertyData)
#
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# # create root window
# root = tk.Tk()
# root.title('Treeview Demo - Hierarchical Data')
# root.geometry('400x200')
#
# # configure the grid layout
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)
#
#
# # create a treeview
# tree = ttk.Treeview(root)
# tree.heading('#0', text='Departments', anchor=tk.W)
#
#
# # adding data
# addd=tree.insert('', tk.END, text='Administration', iid=0, open=False)
# tree.insert('', tk.END, text='Logistics', iid=1, open=False)
# tree.insert('', tk.END, text='Sales', iid=2, open=False)
# tree.insert('', tk.END, text='Finance', iid=3, open=False)
# tree.insert('', tk.END, text='IT', iid=4, open=False)
#
# # adding children of first node
# tree.insert(addd, tk.END, text='John Doe', iid=5, open=False)
# tree.insert(addd, tk.END, text='Jane Doe', iid=6, open=False)
# # tree.move(5, 0, 0)
# # tree.move(6, 0, 1)
#
# # place the Treeview widget on the root window
# tree.grid(row=0, column=0, sticky=tk.NSEW)
#
# # run the app
# root.mainloop()
#



#
# import tkinter as tk
# from tkinter import ttk
#
#
# def add():
#     value = add_entry.get()
#     values.append(value)
#     tree.insert("", tk.END, values=(f'#{len(values)}', value, 'more', 'moar'))
#
#
# def search():
#     query = search_entry.get()
#     selections = []
#     for child in tree.get_children():
#         if query.lower() in (tree.item(child)['values']):   # compare strings in  lower cases.
#             print(tree.item(child)['values'])
#             selections.append(child)
#     print('search completed')
#     tree.selection_set(selections)
#
#
# values = []
#
# root = tk.Tk()
# root.title("Medicine database")
#
# lb1 = tk.Label(root, text="Search:")
# lb1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
# search_entry = tk.Entry(root, width=15)
# search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E, rowspan=1)
# btn = tk.Button(root, text="search", width=10, command=search)
# btn.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
#
# add_lb = tk.Label(root, text="add:")
# add_lb.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
# add_entry = tk.Entry(root, width=15)
# add_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E, rowspan=1)
# btn1 = tk.Button(root, text="add", width=10, command=add)
# btn1.grid(row=1, column=0, padx=10, pady=10, rowspan=2)
#
# # treeview
# tree = ttk.Treeview(root, height=25)
# tree["columns"] = ("one", "two", "three", "four")
# tree.column("one", width=120)
# tree.column("two", width=160)
# tree.column("three", width=130)
# tree.column("four", width=160)
# tree.heading("one", text="Numer seryjny leku")
# tree.heading("two", text="Nazwa Leku")
# tree.heading("three", text="Ampułki/Tabletki")
# tree.heading("four", text="Data ważności")
# tree["show"]="headings"
# tree.grid(row=0, column=2, rowspan=6, pady=20)
#
# root.geometry("840x580")
#
#
# if __name__ == '__main__':
#
#     root.mainloop()



# #Import tkinter library
# from tkinter import *
# from tkinter import ttk
# #Create an instance of tkinter frame
# win = Tk()
# #Set the geometry and title of tkinter Main window
# win.geometry("750x250")
# win.title("Main Window")
# #Create a child window using Toplevel method
# child_w= Toplevel(win)
# child_w.geometry("750x250")
# child_w.title("New Child Window")
# #Create Label in Mainwindow and Childwindow
# label_main= Label(win, text="Hi, this is Main window", font=('Helvetica 15'))
# label_main.pack(pady=20)
# label_child= Label(child_w, text= "Hi, this is Child Window", font=('Helvetica 15'))
# label_child.pack()
# win.mainloop()