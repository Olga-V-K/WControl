from tkinter import *
from tkinter import messagebox
import string
import random

import AdminMenu
from FormModifyAdmin import FormModifyAdmin
from AdminWorker import get_id_from_string


def gen_random_string(length):
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=length))
    return res


def create_admin(db):
    check = TRUE
    adm_login = ''
    adm_passw = ''
    while check:
        adm_login = gen_random_string(random.randint(4, 10))
        if not db.query("select idAdmin from admin where login= '%s'" % adm_login):
            adm_passw = gen_random_string(random.randint(4, 10))
            check = FALSE
    db.action_db_sql_val("insert into admin (login, password) values (%s, %s)", (adm_login, adm_passw))
    text = "Dane nowego administratora: \nLogin: {0} \nHaslo: {1}".format(adm_login, adm_passw)
    messagebox.showinfo("Dane administratora", text)


class AdminAdmin:

    def __init__(self, db, login):
        self.db = db
        self.login = login

        self.root = Tk()
        self.root.geometry('800x500')
        self.root.title('WControl')

        menu = AdminMenu.AdminMenu(self.root, self.db, self.login)

        frame1 = Frame(self.root)
        frame1.pack(side='top', padx=0, pady=5)

        frame3 = Frame(self.root)
        frame3.pack(side='top', padx=0, pady=5)

        frame2 = Frame(self.root)
        frame2.pack(side='top', padx=0, pady=5)

        self.admins_box = Listbox(frame2, width=750, heigh=300)
        btn_new = Button(frame1, text='Nowy', command=self.new_admin, width=8).grid(row=0, column=0, pady=7, padx=7)
        btn_del = Button(frame1, text='Usun', command=self.del_selected, width=8).grid(row=0, column=1, pady=7, padx=7)
        btn_modify = Button(frame1, text='Modyfikuj', command=self.modify_data, width=8).grid(row=0, column=2, pady=7,
                                                                                              padx=7)
        lbl = Label(frame3,
                    text='{0:<10} {1:<10}'.format("(ID,", "LOGIN)")).grid(row=0, column=0, padx=5, pady=5)
        self.admins_box.grid(row=0, column=0, padx=0, pady=5)
        self.insert_into_box()
        self.root.mainloop()

    def insert_into_box(self):
        self.admins_box.delete(0, END)
        res = self.db.get_admins()
        [self.admins_box.insert(i, a) for i, a in enumerate(res)]

    def modify_data(self):
        try:
            line = self.admins_box.get(self.admins_box.curselection())
            FormModifyAdmin(self.db, get_id_from_string(line))
            self.insert_into_box()
        except:
            messagebox.showwarning('', 'Wybierz administratora')

    def del_selected(self):
        line = ""
        try:
            line = self.admins_box.get(self.admins_box.curselection())
        except:
            messagebox.showinfo("Warning", "Wybierz administratora, kturego chcesz usunac!")

        if line:
            win = Toplevel()
            win.title('warning')
            win.geometry('300x100')
            Label(win, text="Czu naprawde chcesz usunac tego administratora?").pack()

            def del_admin():
                win.destroy()
                adm_id = get_id_from_string(line)
                self.db.del_admin_from_db(adm_id, self.login)
                self.insert_into_box()

            Button(win, text='Usun', command=del_admin).pack()
            Button(win, text='Anuluj', command=win.destroy).pack()

    def new_admin(self):
        create_admin(self.db)
        self.insert_into_box()
