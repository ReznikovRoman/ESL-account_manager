import mysql_db

db = mysql_db.SQL()
table = 'user_info'


def check_existence(email):
    return db.check_existence(table, email)