from tkinter import *
from tkinter import messagebox
import re

import Authorization
import AdminAdmin
import AdminMenu
import MainAdmin
import FormNewWorker
import FormModifyWorker


def get_id_from_string(line):
    que = line.split(" ")
    return int(que[0])


def check_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return 1
    else:
        return 0


class AdminWorker:

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

        btn_new = Button(frame1, text='Nowy', command=self.new_worker, width=8).grid(row=0, column=0, pady=7, padx=7)
        btn_del = Button(frame1, text='Usun', command=self.del_selected, width=8).grid(row=0, column=1, pady=7, padx=7)
        btn_modify = Button(frame1, text='Modyfikuj', command=self.modify_data, width=8).grid(row=0, column=2, pady=7,
                                                                                              padx=7)
        lbl = Label(frame3,
                    text='{0:<10} {1:<10} {2:<10} {3:<10} {4:<10} {5:<10} {6:<10}'.format(
                        "(ID,", "NAME,", "S_NAME,", "B_DATE,", 'zl/h,', 'H/DAY,', 'EMAIL)')
                    ).grid(row=0, column=0, padx=5, pady=5)
        self.workers_box = Listbox(frame2, width=750, heigh=300)
        self.workers_box.grid(row=0, column=0, padx=0, pady=5)
        self.insert_into_box()
        self.root.mainloop()

    def del_selected(self):
        line = ""
        try:
            line = self.workers_box.get(self.workers_box.curselection())
        except:
            messagebox.showinfo("Warning", "Wybierz pracownika, kturego chcesz usunac!")

        if line:
            win = Toplevel()
            win.title('warning')
            win.geometry('300x100')
            Label(win, text="Czu naprawde chcesz usunac tego pracownika?").pack()

            def del_worker():
                win.destroy()
                self.db.del_worker_from_db(get_id_from_string(line))
                self.insert_into_box()

            Button(win, text='Usun', command=del_worker).pack()
            Button(win, text='Anuluj', command=win.destroy).pack()

    def log_out(self):
        self.root.destroy()
        a = Authorization.Authorization(self.db)
        a.auth()

    def new_worker(self):
        FormNewWorker.FormNewWorker(self.db)
        self.insert_into_box()

    def modify_data(self):
        try:
            line = self.workers_box.get(self.workers_box.curselection())
            FormModifyWorker.FormModifyWorker(self.db, get_id_from_string(line))
        except:
            messagebox.showwarning('', 'Wybierz pracownika')

    def insert_into_box(self):
        self.workers_box.delete(0, END)
        res = self.db.get_workers()
        [self.workers_box.insert(i, a) for i, a in enumerate(res)]

    def start_admin_m(self):
        self.root.destroy()
        A = MainAdmin.MainAdmin(self.db, self.login)

    def start_admin_a(self):
        self.root.destroy()
        AdminAdmin.AdminAdmin(self.db, self.login)
