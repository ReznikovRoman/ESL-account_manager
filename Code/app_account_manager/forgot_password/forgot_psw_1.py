import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import forgot_password.forgot_psw_2
import login_page.loginPage
import email_handler
import mysql.connector

import random
import re
import mysql_db


db = mysql_db.SQL()
table = 'user_info'

setup_info = email_handler.get_file_info()

NICKNAME = email_handler.get_nickname(setup_info)

# print("1st: ", forgot_password.CODE)


class Ui_forgot_password_1(object):

    def get_user_email(self):
        regex = '[^@]+@[^@]+\.[^@]+'
        user_input = self.known_email_input.text()
        if user_input != "":
            if re.search(regex, user_input):
                return user_input
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect email address",
                                              "Please, enter an email address in a correct format!")

    def setupUi(self, forgotWindow_1):

        forgotWindow_1.setObjectName("forgotWindow_1")
        forgotWindow_1.resize(715, 467)
        self.centralwidget = QtWidgets.QWidget(forgotWindow_1)
        self.centralwidget.setObjectName("centralwidget")

        self.forgot_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.forgot_label_1.setGeometry(QtCore.QRect(210, 30, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(22)
        self.forgot_label_1.setFont(font)
        self.forgot_label_1.setObjectName("forgot_label_1")

        self.known_email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.known_email_input.setGeometry(QtCore.QRect(240, 200, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.known_email_input.setFont(font)
        self.known_email_input.setInputMask("")
        self.known_email_input.setObjectName("known_email_input")

        self.email_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.email_label_1.setGeometry(QtCore.QRect(60, 190, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.email_label_1.setFont(font)
        self.email_label_1.setObjectName("email_label_1")

        self.forgot_btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.forgot_btn_1.setGeometry(QtCore.QRect(240, 260, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.forgot_btn_1.setFont(font)
        self.forgot_btn_1.setFlat(False)
        self.forgot_btn_1.setObjectName("forgot_btn_1")

        self.back_btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn_1.setGeometry(QtCore.QRect(240, 320, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.back_btn_1.setFont(font)
        self.back_btn_1.setFlat(False)
        self.back_btn_1.setObjectName("back_btn_1")

        forgotWindow_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(forgotWindow_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 23))
        self.menubar.setObjectName("menubar")
        forgotWindow_1.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(forgotWindow_1)
        self.statusbar.setObjectName("statusbar")
        forgotWindow_1.setStatusBar(self.statusbar)

        self.retranslateUi(forgotWindow_1)
        QtCore.QMetaObject.connectSlotsByName(forgotWindow_1)

        self.forgot_btn_1.pressed.connect(self.forgot_btn1_pressed)
        self.back_btn_1.pressed.connect(self.return_btn_pressed)

    def retranslateUi(self, forgotWindow_1):
        _translate = QtCore.QCoreApplication.translate
        forgotWindow_1.setWindowTitle(_translate("forgotWindow_1", "forgot password"))
        self.forgot_label_1.setText(_translate("forgotWindow_1", "Forgot Password?"))
        self.email_label_1.setText(_translate("forgotWindow_1", "Enter your email: "))
        self.forgot_btn_1.setText(_translate("forgotWindow_1", "Next"))
        self.back_btn_1.setText(_translate("forgotWindow_1", "Return back"))

    def set_change_email(self, email, code):
        table_name = 'email_to_change'
        esl_db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mypassword',
            database='esl_app'
        )
        cursor = esl_db.cursor()
        sql_add_email = f"INSERT IGNORE INTO {table_name} (email, code) VALUE (%s, %s)"
        cursor.execute(sql_add_email, (email, code))
        esl_db.commit()

    def forgot_btn1_pressed(self):
        email = self.get_user_email()
        if email is not None:
            if db.check_existence(table, email):
                self.set_change_email(email, forgot_password.CODE)
                QtWidgets.QMessageBox.information(None, "Resetting password",
                                                  "The verification code was sent to your email address.")

                _email_handler = email_handler.EmailHandler(setup_info)
                subject = "Password reset"
                msg = "Hi {0}!\n\n" \
                      "Seems like you forgot your 'ESL Account Manager' password. To reset it, enter the verification code.\n\n" \
                      "Your verification code: {1}\n\n" \
                      "Thanks,\n" \
                      "ESL Account Manager".format(NICKNAME, forgot_password.CODE)
                _email_handler.send_email(msg, email, subject)

                code_page = forgot_password.forgot_psw_2.forgot_page_2
                forgot_page_1.hide()
                code_page.show()
            else:
                QtWidgets.QMessageBox.warning(None, "Wrong email",
                                              "There is no account with such email.")
        else:
            QtWidgets.QMessageBox.warning(None, "Enter email address",
                                          "Please, fill in email address field.")

    def return_btn_pressed(self):
        reset_db = mysql_db.SQL()
        reset_table = "email_to_change"
        reset_db.delete_user_by_code(reset_table, forgot_password.CODE)

        _login_page = login_page.loginPage.loginPage
        forgot_page_1.hide()
        _login_page.show()

    # TODO: add 'Return back' button in forgot_2
    # TODO: add 'Send email again' button in forgot_2

    # TODO: (optional) send HTML text in letters, instead of base text



settings_app = QtWidgets.QApplication(sys.argv)

forgot_page_1 = QtWidgets.QMainWindow()
ui = Ui_forgot_password_1()
ui.setupUi(forgot_page_1)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global forgot_page_1

    forgot_page_1.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

