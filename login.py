from customtkinter import *
from PIL import Image
from customtkinter import CTkImage, CTkLabel
from tkinter import messagebox
def login():
 if username.get() == "" or password.get() == "":
  messagebox.showerror("ERROR", " ALL FIELDS ARE REQUIRED")
 elif username.get() == "sai" and password.get() == "9398":
  messagebox.showerror("SUCCESS ", "LOGIN SUCCESSFULLy")
  login_window.destroy()
 else:
  messagebox.showerror("Error", "wrong credntials")


login_window=CTk()
login_window.title("LOGIN PAGE")
login_window.geometry("930x478")
login_window.resizable(0,0)
image=CTkImage(Image.open("LOGIN.jpg"),size=(930,478))
imageLabel=CTkLabel(login_window,image=image,text="")
imageLabel.place(x=0,y=0)

headinglabel=CTkLabel(login_window,text="Employee Management System",bg_color="#FFFFFF",font=("Goudy Old Style",20,"bold"),text_color="dark blue")
headinglabel.place(x=350,y=10)
username=CTkEntry(login_window,placeholder_text="enter the user name ",width=180,fg_color="#275996")
username.place(x=50,y=150)
password=CTkEntry(login_window,placeholder_text="enter the password ",width=180,show="*",fg_color="#275996")
password.place(x=50,y=200)

login_button=CTkButton(login_window,text="Login",cursor="hand2",command=login)
login_button.place(x=70,y=250)

login_window.mainloop()



