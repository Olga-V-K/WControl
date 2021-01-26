import Authorization
import Database


class Main:
    if __name__ == '__main__':
        db = Database.Database()
        auth = Authorization.Authorization(db)
