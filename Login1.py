import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from PIL import ImageTk,Image
class LoginSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry('1300x700+0+0')

        #variables
        self.uname=StringVar()
        self.pass_=StringVar()

        ## setting background image##
        self.bg_icon=ImageTk.PhotoImage(file="C:\\Users\\harshada\\Desktop\\images\\back.jpg")
        self.logo_icon=ImageTk.PhotoImage(file="C:\\Users\\harshada\\Desktop\\images\\logo.jpg")
        bg_lbl=tk.Label(self.root,image=self.bg_icon)
        bg_lbl.pack()
        ##giving label to system
        title=tk.Label(self.root,text="Login System",font=("Times New Roman",40,"bold"),bg="yellow",fg="red",bd=10)
        title.place(x=0,y=0,relwidth=1)

        frame=tk.Frame(self.root,bg="white")
        frame.place(x=530,y=150)

        logo_lbl=tk.Label(frame,image=self.logo_icon,bd=0)
        logo_lbl.grid(row=0,columnspan=2,pady=10)    

        user_lbl=tk.Label(frame,text="username",bg="white",font=("Times New Roman",20,"bold"))
        user_lbl.grid(row=1,column=0,padx=0,pady=10)

        uname_entry=tk.Entry(frame,font=("Times New Roman",10,"bold"),textvariable=self.uname)
        uname_entry.grid(row=1,column=1,padx=20)

        pass_lbl=tk.Label(frame,text="password",bg="white",font=("Times New Roman",20,"bold"))
        pass_lbl.grid(row=2,column=0,padx=0,pady=10)

        pass_entry=tk.Entry(frame,font=("Times New Roman",10,"bold"),textvariable=self.pass_)
        pass_entry.grid(row=2,column=1,padx=20)

        btn_login=tk.Button(frame,text="Login",width=20,font=("Times New Roman",10,"bold"),bg="yellow",fg="red",command=self.login)
        btn_login.grid(columnspan=2,pady=20)
        
    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","Fill all the fields")
        elif self.uname.get()=="harshada" and self.pass_.get()=="1234":
            messagebox.showinfo("Successful","Welcome"+" "+self.uname.get())
        else:
            messagebox.showerror("Error","Username or password invalid !!") 
       

       
root=tk.Tk()
obj=LoginSystem(root)  
root.mainloop()      