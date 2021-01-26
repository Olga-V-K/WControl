from tkinter import *
from tkinter import messagebox
from datetime import datetime


def check_ent_data(db, worker_inf, w_id, email_from_db, new_email, passw_from_db, old_passw, new_passw,
                   new_passw_rep,
                   namei, snamei, dateBi, hpi, dhi):
    if new_email and old_passw and namei and snamei and dateBi and hpi and dhi:
        try:
            email = email_from_db
            password = passw_from_db
            name = worker_inf[1]
            sname = worker_inf[2]
            dateB = worker_inf[3]
            hp = worker_inf[4]
            dh = worker_inf[5]
            changes = FALSE

            cdh = float(dhi)
            chp = int(hpi)
            cdate_b = datetime.strptime(dateBi, '%Y-%m-%d').date()

            if passw_from_db == old_passw:
                if new_email != email_from_db:
                    res = db.query("select idUser from worker where email= '%s'" % new_email)
                    if not res:
                        changes = TRUE
                        email = new_email
                    else:
                        messagebox.showwarning('', 'Pracownik o takim loginie juz istnieje')

                if new_passw != passw_from_db and new_passw:
                    if new_passw == new_passw_rep:
                        changes = TRUE
                        password = new_passw
                    else:
                        messagebox.showwarning('', 'Hasla nie sa jednakowe')

                if name != namei:
                    changes = TRUE
                    name = namei
                if sname != snamei:
                    changes = TRUE
                    sname = snamei
                if dateB != cdate_b:
                    changes = TRUE
                    dateB = cdate_b
                if hp != chp:
                    changes = TRUE
                    hp = chp
                if dh != cdh:
                    changes = TRUE
                    dh = cdh

                if changes:
                    sql = "update worker set name= %s, sName= %s, dateB= %s, hourPay= %s, dayHours= %s, email= %s, " \
                          "password= %s where idUser= %s "
                    val = (name, sname, dateB, hp, dh, email, password, w_id)
                    db.action_db_sql_val(sql, val)
                    messagebox.showinfo('Success', 'Dane pracownika zostaly zmodyfikowane pooprawnie, odnow strone')
            else:
                messagebox.showwarning('', 'Niepoprawne haslo')
        except:
            messagebox.showerror('', 'Wrong data format')
    else:
        messagebox.showwarning('', 'Wypelnij wszystkie obowiazkowe pola')


class FormModifyWorker:

    def __init__(self, db, worker_id):
        self.db = db
        self.w_id = worker_id
        self.worker_inf = db.get_worker_data_id(self.w_id)

        self.win = Toplevel()
        self.win.title('Worker modification')
        self.win.geometry('420x450')

        frame1 = Frame(self.win)
        frame1.pack(side='top', padx=0, pady=5)

        lbl_info = Label(frame1, text='Pola odznaczone * sa obowiazkowe').grid(row=0, columnspan=2, column=0,
                                                                               padx=15, pady=5)
        lbl_email = Label(frame1, text='Email*').grid(row=1, column=0, padx=15, pady=5)
        lbl_old_passw = Label(frame1, text='Stare haslo*').grid(row=2, column=0, padx=15, pady=5)
        lbl_name = Label(frame1, text='Imie*').grid(row=3, column=0, padx=15, pady=5)
        lbl_sname = Label(frame1, text='Nazwisko*').grid(row=4, column=0, padx=15, pady=5)
        lbl_date = Label(frame1, text='Data ur.*').grid(row=5, column=0, padx=15, pady=5)
        lbl_hp = Label(frame1, text='zl/h*').grid(row=6, column=0, padx=15, pady=5)
        lbl_dh = Label(frame1, text='h/day*').grid(row=7, column=0, padx=15, pady=5)
        lbl_new_password = Label(frame1, text='Nowe haslo').grid(row=8, column=0, padx=15, pady=5)
        lbl_new_password_rep = Label(frame1, text='Powtorz nowe haslo').grid(row=9, column=0, padx=15, pady=5)

        self.nEInp = StringVar()
        new_email_input = Entry(frame1, textvariable=self.nEInp, width=32).grid(row=1, column=1, padx=0, pady=5)
        self.nEInp.set(self.worker_inf[6])
        self.oPInp = StringVar()
        old_passw_input = Entry(frame1, textvariable=self.oPInp, width=32, show='*').grid(row=2, column=1, padx=0,
                                                                                          pady=5)
        self.nNInp = StringVar()
        new_name_input = Entry(frame1, textvariable=self.nNInp, width=32).grid(row=3, column=1, padx=0, pady=5)
        self.nNInp.set(self.worker_inf[1])
        self.nSNInp = StringVar()
        new_sname_input = Entry(frame1, textvariable=self.nSNInp, width=32).grid(row=4, column=1, padx=0, pady=5)
        self.nSNInp.set(self.worker_inf[2])
        self.nDInp = StringVar()
        new_date_input = Entry(frame1, textvariable=self.nDInp, width=32).grid(row=5, column=1, padx=0, pady=5)
        self.nDInp.set(self.worker_inf[3])
        self.nHPInp = StringVar()
        new_hp_input = Entry(frame1, textvariable=self.nHPInp, width=32).grid(row=6, column=1, padx=0, pady=5)
        self.nHPInp.set(self.worker_inf[4])
        self.nDHInp = StringVar()
        new_hp_input = Entry(frame1, textvariable=self.nDHInp, width=32).grid(row=7, column=1, padx=0, pady=5)
        self.nDHInp.set(self.worker_inf[5])
        self.nPInp = StringVar()
        new_passw_input = Entry(frame1, textvariable=self.nPInp, width=32, show='*').grid(row=8, column=1, padx=0,
                                                                                          pady=5)
        self.nPRInp = StringVar()
        new_passw_rep_input = Entry(frame1, textvariable=self.nPRInp, width=32, show='*').grid(row=9, column=1,
                                                                                               padx=0, pady=5)
        btn_mod = Button(frame1, text='Zapisz', command=self.submit_changes, width=20).grid(row=10, column=1, padx=0,
                                                                                            pady=25)

    def submit_changes(self):
        check_ent_data(self.db, self.worker_inf, self.w_id, self.worker_inf[6], self.nEInp.get(),
                            self.worker_inf[7], self.oPInp.get(), self.nPInp.get(),
                            self.nPRInp.get(), self.nNInp.get(), self.nSNInp.get(), self.nDInp.get(), self.nHPInp.get(),
                            self.nDHInp.get())
