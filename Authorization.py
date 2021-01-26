from tkinter import *
from tkinter import messagebox

import MainWorker
import MainAdmin


class Authorization:

    def __init__(self, datab):
        self.db = datab

        self.root = Tk()
        self.root.geometry('400x250')
        self.root.title('WControl')

        error_lbl = Label(self.root, text="").pack()
        login_lbl = Label(self.root, text="Login").place(x=50, y=60)
        password_lbl = Label(self.root, text="Haslo").place(x=50, y=100)

        submit_button = Button(self.root, text="Zatwierdz", command=self.auth).place(x=240, y=150)
        self.logInp = StringVar()
        self.passwInp = StringVar()
        login_input = Entry(self.root, textvariable=self.logInp, width=30).place(x=120, y=60)
        password_input = Entry(self.root, show='*', textvariable=self.passwInp, width=30).place(x=120, y=100)

        self.root.mainloop()

    def auth(self):
        login = self.logInp.get()
        password = self.passwInp.get()
        admin = True

        if login and password:
            getPassw = self.db.query("select password from admin where login= '%s'" % login)

            if not getPassw:
                getPassw = self.db.query("select password from worker where email= '%s'" % login)
                admin = False
                if not getPassw:
                    messagebox.showinfo(title='Error', message='Brak użytkownika o padanym loginie!')

            if getPassw:
                if getPassw[0][0] == password:
                    if admin:
                        self.root.destroy()
                        MainAdmin.MainAdmin(self.db, login)
                    else:
                        self.root.destroy()
                        MainWorker.MainWorker(self.db, login)
                else:
                    messagebox.showerror(title='Error', message='Niepoprawne haslo!')
        else:
            messagebox.showinfo(title='Error', message='Wprowadz wszystkie dane!')
