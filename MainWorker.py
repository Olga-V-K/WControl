from tkinter import *
from tkinter import messagebox
from datetime import datetime
import Authorization


def help_msg1():
    messagebox.showinfo("Informacja", "Wprowadz przedzial czasowy, dni z kturego chcesz zobaczyc.")


def help_msg2():
    messagebox.showinfo("Informacja", "Wprowadz dd, mm i rrrr w odpowiednich miejscach.")


class MainWorker:

    def __init__(self, db, login):
        self.db = db
        self.login = login

        root = Tk()
        root.geometry('800x500')
        root.title('WControl')

        menubar = Menu(root)
        root.config(menu=menubar)
        help_ = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_)
        help_.add_command(label="o \"About\"", command=help_msg1)
        help_.add_command(label="o \"Data format\"", command=help_msg2)

        def log_out():
            root.destroy()
            Authorization.Authorization(db)

        menubar.add_command(label='Logout', command=log_out)

        frame1 = Frame(root)
        frame1.pack(side='top', padx=0, pady=5)

        frame2 = Frame(root)
        frame2.pack(side='top', padx=0, pady=5)

        frame3 = Frame(root)
        frame3.pack(side='top', padx=0, pady=10)

        self.sDDInp = StringVar()
        start_dd_input = Entry(frame1, textvariable=self.sDDInp, width=10).grid(row=0, column=1, padx=2)
        self.sMMInp = StringVar()
        start_mm_input = Entry(frame1, textvariable=self.sMMInp, width=10).grid(row=0, column=2, padx=2)
        self.sRRInp = StringVar()
        start_rr_input = Entry(frame1, textvariable=self.sRRInp, width=10).grid(row=0, column=3, padx=2)
        self.eDDInp = StringVar()
        end_dd_input = Entry(frame2, textvariable=self.eDDInp, width=10).grid(row=0, column=1, padx=2)
        self.eMMInp = StringVar()
        end_mm_input = Entry(frame2, textvariable=self.eMMInp, width=10).grid(row=0, column=2, padx=2)
        self.eRRInp = StringVar()
        end_rr_input = Entry(frame2, textvariable=self.eRRInp, width=10).grid(row=0, column=3, padx=2)

        s_lbl = Label(frame1, text='OD   dd/mm/rrrr').grid(row=0, column=0)
        e_lbl = Label(frame2, text='DO   dd/mm/rrrr').grid(row=0, column=0)
        btn_find = Button(frame2, text='Pokaz', command=self.find_days, width=8).grid(row=2, column=3, pady=7, padx=2)

        # Text output area
        scrollText = Scrollbar(frame3)
        scrollText.pack(side='right', fill='y')
        self.text = Text(frame3, width=500, height=500)
        self.text.focus_set()
        self.text.pack(side='left', fill='y')
        scrollText.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollText.set)

        root.mainloop()

    def find_days(self):
        try:
            sdate = datetime(int(self.sRRInp.get()), int(self.sMMInp.get()), int(self.sDDInp.get())).date()
            edate = datetime(int(self.eRRInp.get()), int(self.eMMInp.get()), int(self.eDDInp.get())).date()

            que = self.db.get_workdays(self.login, sdate, edate)
            self.text.delete('1.0', END)
            for i in que:
                self.text.insert(INSERT, str(i))
        except:
            self.text.delete('1.0', END)
            messagebox.showerror(title=None, message='Wrong data format!')