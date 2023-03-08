import os
from tkinter import*
from PIL import  Image,ImageTk
from tkinter import messagebox


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.root.configure(bg='#ffffff')
        #======== BG Image ===========


        title = Label(self.root,bd=2, bg="#00479c").place(x=0, y=0, relwidth=1, height=10)
        bottomFrame = Frame(root, bg="#00479c", border=3)
        bottomFrame.pack(side=BOTTOM, anchor="nw", pady=0, padx=5, fill="x")

        bottomLabel = Label(bottomFrame, text="Developed By: Digi Inn", bg="#00479c", fg="white", font="Arial 9")
        bottomLabel.pack()

        self.Logo = Image.open(r"img/Logo.png")
        self.Logo = self.Logo.resize((500, 400), Image.ANTIALIAS)
        self.Logo = ImageTk.PhotoImage(self.Logo)

        logoLabel = Label(self.root, image=self.Logo, bg="white", relief="flat")
        logoLabel.pack(side=RIGHT,padx=35, pady=70)

        #======= Login Page ============

        Frame_login=Frame(self.root,bg="#00479c",bd=2)
        Frame_login.place(x=100,y=50,height=485,width=350)
        title=Label(Frame_login,text="Login Here",font=("Comic Sans MS",35,"bold"),fg="White",bg="#00479c").place(x=50,y=40)


        lbl_user=Label(Frame_login,text="Username",font=("Comic Sans MS",15,"bold"),fg="white",bg="#00479c").place(x=70,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="light gray")
        self.txt_user.place(x=70,y=170,width=200,height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Comic Sans MS", 15, "bold"), fg="white",bg="#00479c").place(x=70, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="light gray", show="*")
        self.txt_pass.place(x=70, y=240, width=200, height=35)

        login_btn=Button(self.root,command=self.login_function,text="Login",bg="white",fg="#00479c",bd=0, font=("Comic Sans MS", 20)).place(x=200, y=440,width=150,height=45)
        root.bind('<Return>', login_btn)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("error","All Fields required",parent=self.root)
        elif self.txt_user.get()!="admin" or self.txt_pass.get()!="admin":
            messagebox.showerror("error", "Invalid Username/Password", parent=self.root)
        else:
            self.root.destroy()
            os.system("python DashBoard.py")
            #os.system("DashBoard")



    #================= Dashboard Link ===========================================



if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()


