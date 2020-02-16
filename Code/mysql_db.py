import mysql.connector


class SQL:

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mypassword',
            database='esl_app'
        )

        self.cursor = self.db.cursor()

    def create_table(self, table_name):
        """
            Creates a table with <table_name name> and <columns> columns

            table_name: string
        """

        sql_create_table = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY,email VARCHAR(255), UNIQUE KEY unique_email (email), password VARCHAR(255))"

        self.cursor.execute(sql_create_table)

    def check_existence(self, table_name, a_email):
        """
            Checks whether there is a User in the <table> with such <email> or not

            table: string,
            email: string
        """

        sql_email_query = f"SELECT email FROM {table_name}"
        self.cursor.execute(sql_email_query)
        emails = self.cursor.fetchall()

        # print("DB - email: ", a_email)
        # print()
        # print("DB - emails: ", emails)

        for tuple_info in emails:
            if a_email.lower() in tuple_info:
                return True
            else:
                continue
        return False

    def add_value(self, table_name, value):
        """
            Adds <value> to the <table>

            columns: tuple
            table: string
            value: tuple (eg.: ("test@email.com", "123") )
        """

        if not (self.check_existence(table_name, value[0])):
            sql_add_user = f"INSERT INTO {table_name} (email, password) VALUES (%s, %s)"

            self.cursor.execute(sql_add_user, value)

            self.db.commit()
        else:
            print(mysql.connector.errors.IntegrityError('Such email already exists!'))

    def check_input(self, table_name, input_email, input_password):
        """
            Checks whether User's input is correct or not

            table_name: string,
            input_email: string,
            input_password: string
        """

        sql_get_user = f"SELECT * FROM {table_name} WHERE email='{input_email.lower()}'"
        self.cursor.execute(sql_get_user)
        user_info = self.cursor.fetchone()

        if user_info is not None:
            if user_info[1] == input_email.lower() and user_info[2] == input_password:
                return True
            else:
                return False
        else:
            return False

    def get_password(self, table_name, user_email):
        """
            Returns User's password

            table_name: string,
            user_email: string
        """

        sql_get_password = f"SELECT password FROM {table_name} WHERE email = '{user_email.lower()}'"
        self.cursor.execute(sql_get_password)
        password = self.cursor.fetchone()
        return password[0]

    def change_email(self, table_name, prev_email, new_email):
        """
            Changes User's email ('Settings page' function)

            table_name: string,
            prev_email: string (Previous email),
            new_email: string
        """

        # print('MySQL: ', prev_email, new_email)

        # print(self.check_existence(table_name, new_email))

        if not self.check_existence(table_name, new_email.lower()):
            sql_change_email = f"UPDATE {table_name} SET email = '{new_email.lower()}' WHERE email = '{prev_email.lower()}'"
            self.cursor.execute(sql_change_email)
            self.db.commit()
            return True  # 'Email has been changed.'
        elif prev_email.lower() == new_email.lower() or prev_email.lower() == '':
            return True
        else:
            return False  # 'There is no account with such email.'

    def change_password(self, table_name, user_email, new_password):
        """
            Changes User's password ('Forgot Password' function)

            table_name: string,
            user_email: string (known email),
            new_password: string (new user's password)
        """
        if self.check_existence(table_name, user_email.lower()):
            sql_set_password = f"UPDATE {table_name} SET password = '{new_password}' WHERE email = '{user_email.lower()}'"
            self.cursor.execute(sql_set_password)
            self.db.commit()
            return 'Password has been changed.'  # return <true>
        else:
            return 'There is no User with such email.'  # return <false>

    def get_email_by_code(self, table_name, code):
        """
            Returns User's email by the given verification code

            table_name: string,
            code: int (verification code, which was sent to email address)
        """

        sql_get_email = f"SELECT email FROM {table_name} WHERE code = '{code}'"
        self.cursor.execute(sql_get_email)
        email = self.cursor.fetchone()
        return email[0]

    def delete_user_by_code(self, table_name, code):
        """
            Deletes User by <code>

            table_name: string,
            code: int (verification code)
        """

        sql_delete_user = f"DELETE FROM {table_name} WHERE code='{code}'"
        self.cursor.execute(sql_delete_user)
        self.db.commit()

    def delete_user(self, table_name, user_email):
        """
            Deletes User by <user_email>

            table_name: string,
            user_email: string
        """

        sql_delete_user = f"DELETE FROM {table_name} WHERE email='{user_email.lower()}'"
        self.cursor.execute(sql_delete_user)
        self.db.commit()

    def clear_table(self, table_name):
        """
            Deletes all Rows in <table_name>

            table_name: string
        """
        sql_count = f"TRUNCATE TABLE {table_name}"
        self.cursor.execute(sql_count)

    def delete_table(self, table_name):
        """
            Deletes <table_name> from DataBase

            table_name: string
        """
        sql_delete_table = f"DROP TABLE IF EXISTS {table_name}"
        self.cursor.execute(sql_delete_table)
        self.db.commit()


# ==============

# test_db = SQL()
# table = 'user_info'
# table_2 = "email_to_change"

# test_db.clear_table(table_2)

# test_db.delete_user_by_code(table_2, 982076)

# user = "abra@email.comas"
# test_db.delete_user(table, user)


# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='mypassword',
#     database='esl_app'
# )
# cursor = db.cursor()

# sql_create_table = f"CREATE TABLE IF NOT EXISTS email_to_change (" \
#                    f"id INT AUTO_INCREMENT PRIMARY KEY," \
#                    f"email VARCHAR(255)," \
#                    f"code INTEGER(10))"
# cursor.execute(sql_create_table)


""" Registration """


# test_db.create_table(table)

# test_db.delete_table('table')


# email_1 = 'test@email.com'
# password_1 = '123'
# test_db.add_value(table, (email_1, password_1))

# user_to_delete = ''
# test_db.delete_user(table, user_to_delete)

# print(test_db.get_password(table, email_1))


# ===================

""" Login """
# correct_email = 'my@mail.com'
# correct_password = 'password'
#
# wrong_email = 'some@mail.eu'
# wrong_password = '312'

# print(test_db.check_input(table, correct_email, correct_password))
# ======================

""" Forgot Password """

# known_email = "start@mail.com"  # password = '123'
# new_password = 'hi'
# print(test_db.change_password(table, known_email, new_password))

# Check, if new password works

# print(test_db.check_input(table, known_email, new_password))
# =====================

"""Change Email"""

# change_email = 'change@email.com'
# change_password = 'change'
#
# new_email = 'new@email.com'
# test_db.add_value(table, (change_email, change_password))

# print(test_db.change_email(table, change_email, new_email))
