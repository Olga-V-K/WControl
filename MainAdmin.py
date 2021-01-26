from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from datetime import datetime

import AdminMenu


def find_days_and_count(db, sdate, edate, w_id):
    try:
        que = db.query(f"select aDate, sumHours, dayPay from workday where idUser={w_id}")
        sum_hours = 0
        sum_payment = 0

        for i in que:
            if sdate <= i[0] <= edate:
                sum_hours += float(i[1])
                sum_payment += float(i[2])
        return sum_hours, sum_payment
    except:
        messagebox.showerror(title=None, message='Wrong data format!')


def new_day(db, login, a_date, email, hours):
    try:
        worker_inf = db.query("select idUser, hourPay, dayHours from worker where email= '%s'" % email)
        admin_info = db.query("select idAdmin from admin where login= '%s'" % login)

        admin_id = int(admin_info[0][0])
        day_hours = float(worker_inf[0][2])
        hour_pay = int(worker_inf[0][1])
        worker_id = int(worker_inf[0][0])

        if day_hours < hours:
            dif = hours - day_hours
        else:
            dif = 0

        day_pay = hour_pay * (hours + dif * 1.3)
        sql = "insert into workday (idUser, idAdmin, aDate, sumHours, dayPay) values (%s, %s, %s, %s, %s)"
        val = (worker_id, admin_id, a_date, hours, day_pay)
        db.action_db_sql_val(sql, val)
        messagebox.showinfo("Sucess", "Dzien zostal dodany")
    except:
        messagebox.showerror("Error", "Cos poszlo nie tak sprubuj ponownie pozniej")


def report_to_file(db, w_email, s_date, e_date):
    def save():
        files = [('All Files', '*.*'),
                 ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        file.write(text)
        messagebox.showinfo('Succes', 'Raport zostal poprawnie wygenerowany i zapisany')

    worker_info = db.query("select * from worker where email= '%s'" % w_email)[0]
    name = worker_info[1]
    sname = worker_info[2]
    w_id = worker_info[0]

    sum_que = find_days_and_count(db, s_date, e_date, w_id)
    sum_hours = sum_que[0]
    sum_payment = sum_que[1]

    text = f"Pracownik: {name} {sname}\nRaport od dnia {str(s_date)} do {str(e_date)}\n\n\nPrzeprocowanych godzin:" \
           f" {str(sum_hours)}\nWyplata: {str(sum_payment)} "
    save()


class MainAdmin:

    def __init__(self, db, login):
        self.db = db
        self.login = login

        self.root = Tk()
        self.root.geometry('800x500')
        self.root.title('WControl')

        menu = AdminMenu.AdminMenu(self.root, db, login)

        frame1 = Frame(self.root)
        frame1.pack(side='top', padx=0, pady=5)

        frame2 = Frame(self.root)
        frame2.pack(side='top', padx=0, pady=5)

        frame3 = Frame(self.root)
        frame3.pack(side='top', padx=0, pady=5)

        frame4 = Frame(self.root)
        frame4.pack(side='top', padx=0, pady=5)

        frame5 = Frame(self.root)
        frame5.pack(side='top', padx=0, pady=5)

        self.wEmInp = StringVar()
        worker_email_input = Entry(frame1, textvariable=self.wEmInp, width=32).grid(row=0, column=1)
        w_lbl = Label(frame1, text='Worker email').grid(row=0, column=0, padx=10)
        self.whourInp = StringVar()
        workerhour_input = Entry(frame1, textvariable=self.whourInp, width=32).grid(row=1, column=1)
        wh_lbl = Label(frame1, text='Hours').grid(row=1, column=0, padx=10, pady=7)

        self.sDDInp = StringVar()
        start_dd_input = Entry(frame2, textvariable=self.sDDInp, width=10).grid(row=0, column=1, padx=2)
        self.sMMInp = StringVar()
        start_mm_input = Entry(frame2, textvariable=self.sMMInp, width=10).grid(row=0, column=2, padx=2)
        self.sRRInp = StringVar()
        start_rr_input = Entry(frame2, textvariable=self.sRRInp, width=10).grid(row=0, column=3, padx=2)

        self.eDDInp = StringVar()
        end_dd_input = Entry(frame3, textvariable=self.eDDInp, width=10).grid(row=0, column=1, padx=2)
        self.eMMInp = StringVar()
        end_mm_input = Entry(frame3, textvariable=self.eMMInp, width=10).grid(row=0, column=2, padx=2)
        self.eRRInp = StringVar()
        end_rr_input = Entry(frame3, textvariable=self.eRRInp, width=10).grid(row=0, column=3, padx=2)

        s_lbl = Label(frame2, text='OD   dd/mm/rrrr').grid(row=0, column=0)
        e_lbl = Label(frame3, text='DO   dd/mm/rrrr').grid(row=0, column=0)
        btn_enter_day = Button(frame4, text='Dodaj dzien', command=self.enter_day, width=8).grid(row=0, column=0, pady=7,
                                                                                            padx=7)
        btn_show_days = Button(frame4, text='Pokaz dni', command=self.show_days, width=8).grid(row=0, column=1, pady=7,
                                                                                          padx=7)
        btn_gen_payment = Button(frame4, text='Raport', command=self.report, width=8).grid(row=0, column=2, pady=7, padx=7)

        scrollText = Scrollbar(frame5)
        scrollText.pack(side='right', fill='y')
        self.text = Text(frame5, width=500, height=500)
        self.text.focus_set()
        self.text.pack(side='left', fill='y')
        scrollText.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollText.set)

        self.root.mainloop()

    def enter_day(self):
        try:
            date = datetime(int(self.sRRInp.get()), int(self.sMMInp.get()), int(self.sDDInp.get())).date()
            email = self.wEmInp.get()
            hours = float(self.whourInp.get())
            if date and email and hours:
                new_day(self.db, self.login, date, email, hours)
        except:
            messagebox.showerror("", 'Wrong data')

    def show_days(self):
        email = self.wEmInp.get()
        if email:
            try:
                sdate = datetime(int(self.sRRInp.get()), int(self.sMMInp.get()), int(self.sDDInp.get())).date()
                edate = datetime(int(self.eRRInp.get()), int(self.eMMInp.get()), int(self.eDDInp.get())).date()
                que = self.db.get_workdays(email, sdate, edate)
                self.text.delete('1.0', END)
                for i in que:
                    self.text.insert(INSERT, str(i))
            except:
                self.text.delete('1.0', END)
                messagebox.showerror(title=None, message='Wrong data format!')
        else:
            messagebox.showerror("", "Wprowadz wszystkie dane")

    def report(self):
        try:
            email = self.wEmInp.get()
            sdate = datetime(int(self.sRRInp.get()), int(self.sMMInp.get()), int(self.sDDInp.get())).date()
            edate = datetime(int(self.eRRInp.get()), int(self.eMMInp.get()), int(self.eDDInp.get())).date()
            if email and sdate and edate:
                try:
                    report_to_file(self.db, email, sdate, edate)
                except:
                    return 0
            else:
                messagebox.showwarning('', 'Wprowadz wszystkie dane')
        except:
            messagebox.showerror('', 'Wrong data format')