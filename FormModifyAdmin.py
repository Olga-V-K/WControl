from tkinter import *
from tkinter import messagebox


def check_ent_data(db, a_id, login_from_db, new_login, passw_from_db, old_passw, new_passw, new_passw_rep):

    if new_login and old_passw:
        login = login_from_db
        password = passw_from_db
        changes = FALSE

        if passw_from_db == old_passw:
            if new_login != login_from_db:
                res = db.query("select idAdmin from admin where login= '%s'" % new_login)
                if not res:
                    changes = TRUE
                    login = new_login
                else:
                    messagebox.showwarning('', 'Admin o takim loginie juz istnieje')

            if new_passw != passw_from_db and new_passw:
                if new_passw == new_passw_rep:
                    changes = TRUE
                    password = new_passw
                else:
                    messagebox.showwarning('', 'Hasla nie sa jednakowe')

            if changes:
                db.action_db_sql_val("update admin set login= %s, password= %s where idAdmin= %s",
                                     (login, password, a_id))
                messagebox.showinfo('Success', 'Dane administratora zostaly zmodyfikowane pooprawnie, odnow strone')
        else:
            messagebox.showwarning('', 'Niepoprawne haslo')
    else:
        messagebox.showwarning('', 'Wypelnij wszystkie obowiazkowe pola')


class FormModifyAdmin:

    def __init__(self, db, a_id):
        self.db = db
        self.a_id = a_id

        res = self.db.get_admin_data(self.a_id)
        login = res[0]
        password = res[1]

        win = Toplevel()
        win.title('Admin modification')
        win.geometry('420x280')

        frame1 = Frame(win)
        frame1.pack(side='top', padx=0, pady=5)

        lbl_info = Label(frame1, text='Pola odznaczone * sa obowiazkowe').grid(row=0, columnspan=2, column=0,
                                                                               padx=15, pady=5)
        lbl_new_login = Label(frame1, text='Login*').grid(row=1, column=0, padx=15, pady=5)
        lbl_old_passw = Label(frame1, text='Stare haslo*').grid(row=2, column=0, padx=15, pady=5)
        lbl_new_password = Label(frame1, text='Nowe haslo').grid(row=3, column=0, padx=15, pady=5)
        lbl_new_password_rep = Label(frame1, text='Powtorz nowe haslo').grid(row=4, column=0, padx=15, pady=5)

        nLInp = StringVar()
        new_login_input = Entry(frame1, textvariable=nLInp, width=32).grid(row=1, column=1, padx=0, pady=5)
        nLInp.set(login)
        oPInp = StringVar()
        old_passw_input = Entry(frame1, textvariable=oPInp, width=32, show='*').grid(row=2, column=1, padx=0,
                                                                                     pady=5)
        nPInp = StringVar()
        new_passw_input = Entry(frame1, textvariable=nPInp, width=32, show='*').grid(row=3, column=1, padx=0,
                                                                                     pady=5)
        nPRInp = StringVar()
        new_passw_rep_input = Entry(frame1, textvariable=nPRInp, width=32, show='*').grid(row=4, column=1, padx=0,
                                                                                          pady=5)

        def submit_changes():
            check_ent_data(db, a_id, login, nLInp.get(), password, oPInp.get(), nPInp.get(), nPRInp.get())

        btn_mod = Button(frame1, text='Zapisz', command=submit_changes).grid(row=6, column=1, padx=0, pady=5)