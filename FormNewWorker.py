from datetime import datetime
from tkinter import *
from tkinter import messagebox
import re


class FormNewWorker:

    def __init__(self, db):
        self.db = db
        self.win = Toplevel()
        self.win.geometry('370x320')
        self.win.title('New worker')

        frame1 = Frame(self.win)
        frame1.pack(side='top', padx=0, pady=5)

        frame2 = Frame(self.win)
        frame2.pack(side='top', padx=0, pady=5)

        lbl_name = Label(frame1, text="Imie:* ").grid(row=0, column=0, padx=15, pady=5)
        lbl_sname = Label(frame1, text='Nazwisko:* ').grid(row=1, column=0, padx=15, pady=5)
        lbl_d_ur = Label(frame1, text='Data ur. (rrrr/mm/dd):* ').grid(row=2, column=0, padx=15, pady=5)
        lbl_dh = Label(frame1, text='H/day:* ').grid(row=3, column=0, padx=15, pady=5)
        lbl_ph = Label(frame1, text='Zl/h:* ').grid(row=4, column=0, padx=15, pady=5)
        lbl_email = Label(frame1, text='Email:*').grid(row=5, column=0, padx=15, pady=5)
        lbl_passw = Label(frame1, text='Haslo:* ').grid(row=6, column=0, padx=15, pady=5)
        lbl_passw_rep = Label(frame1, text='Powtorz haslo:* ').grid(row=7, column=0, padx=15, pady=5)

        self.nameInp = StringVar()
        name_input = Entry(frame1, textvariable=self.nameInp, width=30).grid(row=0, column=1, padx=2, pady=5)
        self.snameInp = StringVar()
        sname_input = Entry(frame1, textvariable=self.snameInp, width=30).grid(row=1, column=1, padx=2, pady=5)
        self.dUrInp = StringVar()
        d_ur_input = Entry(frame1, textvariable=self.dUrInp, width=30).grid(row=2, column=1, padx=2, pady=5)
        self.dHInp = StringVar()
        d_h__input = Entry(frame1, textvariable=self.dHInp, width=30).grid(row=3, column=1, padx=2, pady=5)
        self.pHInp = StringVar()
        p_h__input = Entry(frame1, textvariable=self.pHInp, width=30).grid(row=4, column=1, padx=2, pady=5)
        self.emailInp = StringVar()
        email_input = Entry(frame1, textvariable=self.emailInp, width=30).grid(row=5, column=1, padx=2, pady=5)
        self.passwInp = StringVar()
        passw_input = Entry(frame1, textvariable=self.passwInp, width=30, show='*').grid(row=6, column=1, padx=2, pady=5)
        self.passwRepInp = StringVar()
        passw_rep_input = Entry(frame1, textvariable=self.passwRepInp, width=30, show='*').grid(row=7, column=1, padx=2,
                                                                                           pady=5)
        btn_submit = Button(frame1, text='Zapisz', command=self.get_formdata_new).grid(row=8, column=1, padx=2, pady=5)

    def get_formdata_new(self):
        try:
            name = self.nameInp.get()
            sname = self.snameInp.get()
            data_ur = self.dUrInp.get()
            day_hour = self.dHInp.get()
            pay_hour = self.pHInp.get()
            email = self.emailInp.get()
            password = self.passwInp.get()
            password_rep = self.passwRepInp.get()

            try:
                data_ur = datetime.strptime(data_ur, '%Y-%m-%d').date()
                day_hour = float(day_hour)
                pay_hour = int(pay_hour)

                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    res = self.db.query("select idUser from worker where email= '%s'" % email)
                    if not res:
                        if password == password_rep:
                            sql = "insert into worker (name, sName, dateB, hourPay, dayHours, email, password) values " \
                                  "(%s, %s, %s, %s, %s, %s, %s) "
                            val = (name, sname, data_ur, pay_hour, day_hour, email, password)
                            self.db.action_db_sql_val(sql, val)
                            messagebox.showinfo('Success', 'Pracownik zostal dodany')
                            self.win.destroy()
                        else:
                            messagebox.showerror('Error', 'Haswa nie sa jednakowe')
                    else:
                        messagebox.showwarning('', 'Pracownik z takie email juz istnieje')
                else:
                    messagebox.showerror('Error', 'Wprowadz poprawny email')
            except:
                messagebox.showwarning('', 'Wrong data format')
        except:
            messagebox.showinfo('', 'Wprowadz wszystkie dane')