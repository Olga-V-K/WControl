from tkinter import *
from tkinter import messagebox

import AdminAdmin
import AdminWorker
import MainAdmin
import Authorization


def show_days_msg():
    msg = "Zeby wyswietlic przeprocowane przez pracownika dni w okreslonym terminie,\n" \
          "nalezy wykonac nastepujace kroki:\n\n\n" \
          "1. Wprowadz email pracownika (mozna znalezc w zakladce <Workers>.\n" \
          "2. Wprowadfz poczatkowa date (pole <OD dddd-mm-dd>).\n" \
          "3. Wprowadz koncowa date (pole <DO dddd-mm-dd>).\n" \
          "4. Zatwierdz przyciskiem <Pokaz dni>."
    messagebox.showinfo("Pokaz dni pracownika", msg)


def new_day_msg():
    msg = "Zeby dodac dzien dla wybranego procownika,\n" \
          "nalezy wykonac nastepujace kroki:\n\n\n" \
          "1. Wprowadz email pracownika (mozna znalezc w zakladce <Workers>.\n" \
          "2. Wprowadz ilosc przepracowanych godzin.\n" \
          "3. Wprowadfz date (pole <OD dddd-mm-dd>).\n" \
          "4. Zatwierdz przyciskiem <Dodaj dzien>."
    messagebox.showinfo("Dodaj dzien", msg)


def raport_msg():
    msg = "Zeby wygenerowac raport dla wybranego pracownika,\n" \
          "nalezy wykonac nastepujace kroki:\n\n\n" \
          "1. Wprowadz email pracownika (mozna znalezc w zakladce <Workers>.\n" \
          "2. Wprowadfz date (pole <OD dddd-mm-dd>).\n" \
          "3. Wprowadz koncowa date (pole <DO dddd-mm-dd>).\n" \
          "4. Zatwierdz przyciskiem <Raport> i postepuj zgodnie z poleceniami."
    messagebox.showinfo("Generowanie raportu", msg)


def modify_data_msg():
    msg = "Zeby zmodyfikowac dane uzytkownika,\n" \
          "nalezy wykonac nastepujace kroki:\n\n\n" \
          "1. Wybierz uzytkownika z listy i nacisnij.\n" \
          "2. Nacisnij przycisk <Modyfikuj>.\n" \
          "3. Zmodyfikuj dane (wypelnij wszystkie obowiazkowe pola).\n" \
          "4. Zatwierdz zmiane przyciskiem."
    messagebox.showinfo("Modyfikacja danych uzytkownika", msg)


def del_user_msg():
    msg = "Zeby usunac uzytkownika,\n" \
          "nalezy wykonac nastepujace kroki:\n\n\n" \
          "1. Wybierz urzytkownika z listy i nacisnij.\n" \
          "2. Nacisnij przycist <Usun>.\n" \
          "3. Postepuj zgodnie z poleceniami."
    messagebox.showinfo("Usuniecie danuch uzytkownika", msg)


class AdminMenu:

    def __init__(self, root, db, login):
        self.db = db
        self.root = root
        self.login = login

        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        menubar.add_command(label='Main', command=self.start_admin_m)
        menubar.add_command(label='Admins', command=self.start_admin_a)
        menubar.add_command(label='Workers', command=self.start_admin_w)

        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=file)
        file.add_command(label='o \"Pokaz dni pracownika\"', command=show_days_msg)
        file.add_command(label='o \"Raport przepracowanych dni\"', command=raport_msg)
        file.add_command(label='o \"Dodaj dzien\"', command=new_day_msg)
        file.add_separator()
        file.add_command(label='o \"Modyfikacja danych uzytkownika\"', command=modify_data_msg)
        file.add_command(label='o \"Usuniecie uzytkownika\"', command=del_user_msg)

        menubar.add_command(label='Logout', command=self.log_out)

    def start_admin_a(self):
        self.root.destroy()
        AdminAdmin.AdminAdmin(self.db, self.login)

    def start_admin_m(self):
        self.root.destroy()
        MainAdmin.MainAdmin(self.db, self.login)

    def start_admin_w(self):
        self.root.destroy()
        AdminWorker.AdminWorker(self.db, self.login)

    def log_out(self):
        self.root.destroy()
        Authorization.Authorization(self.db)
