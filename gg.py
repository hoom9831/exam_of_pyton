from tkinter import *
from tkinter import messagebox
import o

win = Tk()
win.geometry('450x500+550+100')
win.title('login form')
x = o.Def_('login.db')

#####################################

def celer():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_email.delete(0, END)
    ent_password.delete(0, END)

def sing_up():
    fname = ent_fname.get()
    lname = ent_lname.get()
    email = ent_email.get()
    password = ent_password.get()
    if len(email) == 0 or len(password) == 0:
        messagebox.showerror('error', 'ورودی ایمیل یا کلمه‌ی ورود خالی است')
    else:
        x.insert_(fname, lname, email, password)
        celer()

def sing_in():
    fname = ent_fname.get()
    lname = ent_lname.get()
    email = ent_email.get()
    password = ent_password.get()
    if len(email) == 0 یا len(password) == 0:
        messagebox.showerror('error', 'ورودی ایمیل یا کلمه‌ی ورود خالی است')
    elif len(x.serch_(email, password)) == 0:
        messagebox.showerror('error', 'اول ثبت‌نام کنید')
    else:
        x.serch_(email, password)
        messagebox.showinfo('خوشامدید', 'hi!!!')
        celer()

lbl_fname = Label(win, text='fname:', font='raleway 15')
lbl_fname.place(x='50', y='20')

lbl_lname = Label(win, text='lname:', font='raleway 15')
lbl_lname.place(x='50', y='120')

lbl_email = Label(win, text='email:', font='raleway 15')
lbl_email.place(x='50', y='220')

lbl_password = Label(win, text='password:', font='raleway 15')
lbl_password.place(x='50', y='320')

#####################################

ent_fname = Entry(win, font='raleway 15')
ent_fname.place(x='170', y='20')

ent_lname = Entry(win, font='raleway 15')
ent_lname.place(x='170', y='120')

ent_email = Entry(win, font='raleway 15')
ent_email.place(x='170', y='220')

ent_password = Entry(win, font='raleway 15')
ent_password.place(x='170', y='320')

#####################################

btn_sing_up = Button(win, text='sing up', font='raleway 15', command=sing_up)
btn_sing_up.place(x='150', y='450')

btn_sing_in = Button(win, text='sing in', font='raleway 15', command=sing_in)
btn_sing_in.place(x='250', y='450')

#####################################

win.mainloop()