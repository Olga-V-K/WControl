from tkinter import messagebox
import mysql.connector


class Database:

    def __init__(self):
        self.__conn = mysql.connector.connect(user="root", password="root", host="127.0.0.1", database="wcontrol")
        self.__cursor = self.__conn.cursor()

    def query(self, ql):
        try:
            self.__cursor.execute(ql)
            return self.__cursor.fetchall()
        except:
            messagebox.showerror('Error', 'Problem with db connection')


    def get_workdays(self, login, sdate, edate):
        worker_inf = self.query("select idUser, name, sName from worker where email= '%s'" % login)
        worker_id = worker_inf[0][0]

        que = self.query(
            f"select aDate, sumHours, dayPay from workday where idUser= '%s' order by aDate desc" % worker_id)
        res = [f"Worker: {worker_inf[0][1]} {worker_inf[0][2]}\n", "DATE\t\t\tHOURS\t\t\tDAY_PAY\n",
               '______________________________________________________________________\n\n']

        for i in que:
            if sdate <= i[0] <= edate:
                res.append(str(i[0]) + '\t\t\t' + str(i[1]) + '\t\t\t' + str(i[2]) + '\n')
        return res

    def get_admins(self):
        worker_inf = self.query("select idAdmin, login from admin")
        res = []

        for i in worker_inf:
            res.append('{0:<20} {1:<25}'.format(*i) + '\n')
        return res

    def del_admin_from_db(self, a_id, login):
        try:
            adm_info = self.query("select idAdmin from admin where login= '%s'" % login)

            if adm_info[0][0] != a_id:
                ql = "delete from admin where idAdmin= '%s'" % a_id
                self.__cursor.execute(ql)
                self.__conn.commit()
                messagebox.showinfo("", "Admin was deleted")
            else:
                messagebox.showerror("Error", "Nie mozesz usunac swojego rekordu!")
        except:
            messagebox.showerror('Error', 'Problem with db connection')

    def del_worker_from_db(self, w_id):
        try:
            ql = "delete from worker where idUser= '%s'" % w_id
            self.__cursor.execute(ql)
            self.__conn.commit()
            messagebox.showinfo("", "Worker was deleted")
        except:
            messagebox.showerror('Error', 'Problem with db connection')

    def get_admin_data(self, a_id):
        admin_info = self.query("select * from admin where idAdmin= '%s'" % a_id)
        login = admin_info[0][1]
        password = admin_info[0][2]
        return login, password

    def get_workers(self):
        worker_inf = self.query("select idUser, name, sName, dateB, hourPay, dayHours, email from worker")
        res = []

        for i in worker_inf:
            res.append(
                '{0:<20} {1:<25} {2:<25} {3:<25} {4:<20} {5:<20} {6:<30}'.format(i[0], i[1], i[2], str(i[3]), i[4],
                                                                                 i[5], i[6]) + '\n')
        return res

    def get_worker_data_id(self, w_id):
        worker_info = self.query("select * from worker where idUser= '%s'" % w_id)
        return worker_info[0]

    def action_db_sql_val(self, sql, val):
        try:
            self.__cursor.execute(sql, val)
            self.__conn.commit()
        except:
            messagebox.showerror('Error', 'Problem with db connection')


