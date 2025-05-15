from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def Loginpage(current_window=None):
    if current_window:
        current_window.destroy()
    screen1 = Tk()
    screen1.geometry("500x400")
    screen1.title("Login Page")
    screen1.resizable(False, False)
    screen1.iconbitmap()
    screen1.config(bg="#0d6a11")
    Photo = PhotoImage(file="verified_10829089.png").subsample(5, 5)
    icon1 = PhotoImage(file="user_3626461.png").subsample(25, 25)
    icon2 = PhotoImage(file="lock_3624873.png").subsample(25, 25)

    def verf_Login():
        username = entry_username.get()
        password = entry_password.get()
        if username == "SAID" and password == "0000":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    style = ttk.Style()
    style.configure("Valid.TButton",font=('Arial', 10, 'bold'),bg="#7ed957")
    # Create All Frame For Work
    Fram = Frame(screen1,bg="#7ed957")
    Fram.pack(padx=20, pady=20, expand=True, fill="both")
    Label(Fram, image=Photo,bg="#7ed957").pack(pady=20)
    Fram1 = Frame(Fram,bg="#7ed957")
    Fram1.pack(padx=20, pady=10, fill="x")
    Label(Fram1, image=icon1,bg="#7ed957").pack(side="left", padx=5, pady=2)
    Label(Fram1, text="Username : ",bg="#7ed957").pack(side="left", padx=5, pady=2)
    entry_username = Entry(Fram1, width=50)
    entry_username.pack(fill="x", padx=5, pady=2, side="left")

    Fram2 = Frame(Fram,bg="#7ed957")
    Fram2.pack(padx=20, pady=10, fill="x")
    Label(Fram2, image=icon2,bg="#7ed957").pack(side="left", padx=5, pady=2)
    Label(Fram2, text="Password : ",bg="#7ed957").pack(side="left", padx=5, pady=2)
    entry_password = Entry(Fram2, width=50, show="*")
    entry_password.pack(fill="x", padx=5, pady=2, side="left")
    BUT1 = ttk.Button(Fram, text="Inscription", command=lambda: Inscription(screen1),style="Valid.TButton")
    BUT1.pack(side="left", padx=100)
    BUT2 = ttk.Button(Fram, text="Login", command=verf_Login,style="Valid.TButton").pack(side="left", padx=2)
    screen1.mainloop()

def Inscription(current_window=None):
    if current_window:
        current_window.destroy()
    screen = Tk()
    screen.title('Inscription')
    screen.geometry('500x400')
    screen.resizable(False, False)
    screen.config(bg="#7ed957")

    def affich():
        print('\n--- Form Submission ---')
        print('Name :', name.get())
        print('Prenom :', prenom.get())
        print('Email :', Email.get())
        print('Indentifient :', Indentifient.get())
        print('Password :', Password.get())
        print('-' * 23)

    # Title
    Label(screen, text='Inscription Page', font='Georgia 20 bold', fg='white' ,bg="#7ed957").pack(pady=20)
    # Name
    Label(screen, text='Name :', font='Georgia 10 bold', fg='black',bg="#7ed957").place(x=40, y=100)
    name = Entry(screen, width=30, font=('Arial', 12))
    name.place(x=150, y=100)
    # Prenom
    Label(screen, text='Prenom :', font='Georgia 10 bold', fg='black',bg="#7ed957").place(x=40, y=140)
    prenom = Entry(screen, width=30, font=('Arial', 12))
    prenom.place(x=150, y=140)
    # Email
    Label(screen, text='Email :', font='Georgia 10 bold', fg='black',bg="#7ed957").place(x=40, y=180)
    Email = Entry(screen, width=30, font=('Arial', 12))
    Email.place(x=150, y=180)
    # Indentifient
    Label(screen, text='Indentifient :', font='Georgia 10 bold', fg='black' ,bg="#7ed957").place(x=40, y=220)
    Indentifient = Entry(screen, width=30, font=('Arial', 12))
    Indentifient.place(x=150, y=220)
    # Password
    Label(screen, text='Password :', font='Georgia 10 bold', fg='black',bg="#7ed957").place(x=40, y=260)
    Password = Entry(screen, width=30, font=('Arial', 12),show="*")
    Password.place(x=150, y=260)

    # Submit button
    Button(screen, text='Envoyer', fg='black', bg='green', font='Georgia 10 bold', command=affich).place(x=160,y=310)
    Button(screen, text='Login Page', fg='black', bg='green', font='Georgia 10 bold', command=lambda: Loginpage(screen)).place(x=290,y=310)
    screen.mainloop()

Loginpage()
