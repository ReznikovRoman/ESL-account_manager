
from PyQt5 import QtCore, QtGui, QtWidgets
import main_page.main_page_file
import re
import settings_page.settings_page
import registration_page.signup_page
import email_handler
import forgot_password.forgot_psw_2
import registration_page

import mysql_db


db = mysql_db.SQL()
table = 'user_info'


class Ui_loginPage(object):

    def get_user_email(self):
        regex = '[^@]+@[^@]+\.[^@]+'
        user_input = self.email_input.text()
        if user_input != "":
            if re.search(regex, user_input):
                return user_input
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect email address",
                                              "Please, enter an email address in a correct format!")

    def get_user_password(self):
        regex = '^[a-zA-Z1-9]*$'
        user_password = self.password_input.text()
        if user_password != "":
            if re.search(regex, user_password):
                return user_password
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect password",
                                              "Please, enter password in a correct format!\nPassword can only contain letters or digits.")
        else:
            QtWidgets.QMessageBox.warning(None, "Incorrect password",
                                          "Please, enter your password.")

    def setupUi(self, loginPage):
        loginPage.setObjectName("loginPage")
        loginPage.resize(899, 517)
        self.centralwidget = QtWidgets.QWidget(loginPage)
        self.centralwidget.setObjectName("centralwidget")

        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(310, 170, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email_input.setFont(font)
        self.email_input.setObjectName("email_input")

        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(310, 260, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_input.setFont(font)
        self.password_input.setObjectName("password_input")

        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(30, 160, 271, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.email_label.setFont(font)
        self.email_label.setTextFormat(QtCore.Qt.RichText)
        self.email_label.setObjectName("email_label")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(30, 250, 271, 71))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setTextFormat(QtCore.Qt.RichText)
        self.password_label.setObjectName("password_label")

        self.remember_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.remember_checkBox.setGeometry(QtCore.QRect(340, 410, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.remember_checkBox.setFont(font)
        self.remember_checkBox.setObjectName("remember_checkBox")

        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(120, 400, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")

        self.signUp_button = QtWidgets.QPushButton(self.centralwidget)
        self.signUp_button.setGeometry(QtCore.QRect(550, 400, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signUp_button.setFont(font)
        self.signUp_button.setObjectName("signUp_button")

        self.forgot_button = QtWidgets.QPushButton(self.centralwidget)
        self.forgot_button.setGeometry(QtCore.QRect(700, 40, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.forgot_button.setFont(font)
        self.forgot_button.setObjectName("forgot_button")

        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(270, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")

        loginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 23))
        self.menubar.setObjectName("menubar")
        loginPage.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(loginPage)
        self.statusbar.setObjectName("statusbar")
        loginPage.setStatusBar(self.statusbar)

        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)

        self.login_button.pressed.connect(self.login_btn_pressed)
        self.signUp_button.pressed.connect(self.signup_btn_pressed)
        # self.forgot_button.pressed.connect(self.forgot_btn_pressed) # TODO: first option
        self.forgot_button.pressed.connect(self.forgot_btn_pressed_2)  # TODO: second option

    def retranslateUi(self, loginPage):
        _translate = QtCore.QCoreApplication.translate
        loginPage.setWindowTitle(_translate("loginPage", "Login"))
        self.email_label.setText(_translate("loginPage", "Enter your ESL admin e-mail"))
        self.remember_checkBox.setText(_translate("loginPage", "Remember me"))
        self.login_button.setText(_translate("loginPage", "Login"))
        self.signUp_button.setText(_translate("loginPage", "Sign Up"))
        self.forgot_button.setText(_translate("loginPage", "Forgot Password?"))
        self.login_label.setText(_translate("loginPage", "Login"))
        self.password_label.setText(_translate("loginPage", "Enter your password"))

    def login_btn_pressed(self):
        user_email = self.get_user_email()
        user_password = self.get_user_password()

        file = open('setup_info.txt', 'r')
        data = file.read()
        file.close()

        if len(data) == 0:
            setup_info = open("setup_info.txt", "w")
            setup_info.write("User email: {0}\nUser nickname: {1}\n"
                             "Send email state: {2}\n'Remember me' status: 0\n"
                             "Notifications state: {3}".format(' ', 'User', 0, 2))
            setup_info.close()

            settings_ui = settings_page.settings_page.ui
            main_page_ui = main_page.main_page_file.ui

            settings_ui.settings_password_input.setText(" ")
            settings_ui.settings_nickname_input.setText('User')
            settings_ui.settings_email_checkBox.setChecked(False)

            main_page_ui.label_greeting.setText("Welcome back, %s!" % 'User')

        else:

            if user_email is not None and user_password is not None and (db.check_existence(table, user_email) or registration_page.check_existence(user_email)):
                mainPage = main_page.main_page_file.MainWindow

                new_data = re.sub('\'Remember me\' status: .*', "'Remember me' status: %s" % self.remember_checkBox.checkState(), data)
                file = open('setup_info.txt', 'w')
                file.write(data.replace(data, new_data))
                file.close()

                file = open("setup_info.txt", 'r')
                data = file.read()
                file.close()

                file = open("setup_info.txt", 'w')
                email_from_login = re.sub("User email: .*", "User email: %s" % user_email, data)
                file.write(data.replace(data, email_from_login))
                file.close()

                settings_page.settings_page.ui.settings_email_input.setText(user_email)
                settings_page.settings_page.ui.settings_checkBox.setChecked(self.remember_checkBox.checkState())

                # TEST DATA
                # file = open("setup_info.txt", 'r')
                # data = file.read()
                # file.close()
                # print('Login: ', data)
                # print()

                # print("Login: ", user_email, user_password)

                if db.check_existence(table, user_email):
                    if db.check_input(table, user_email, user_password):
                        mainPage.show()
                        loginPage.hide()
                    else:
                        QtWidgets.QMessageBox.warning(None, "Incorrect account details",
                                                      "Incorrect account info - email or password are wrong.")
                # else:
                #     QtWidgets.QMessageBox.warning(None, "Incorrect account details",
                #                                   "There is no account with such email.")

            elif user_email is None and self.email_input.text() == "":
                QtWidgets.QMessageBox.warning(None, "Incorrect email address",
                                              "Enter email address")
            elif not db.check_existence(table, user_email) and not registration_page.check_existence(user_email):
                QtWidgets.QMessageBox.warning(None, "Incorrect account details",
                                              "There is no account with such email.")

    def signup_btn_pressed(self):
        sign_up_page = registration_page.signup_page.signUp_window
        sign_up_page.show()

        # self.signUp_button.setDisabled(True)
        loginPage.hide()

    def forgot_btn_pressed_2(self):
        forgot_psw_page = forgot_password.forgot_psw_1.forgot_page_1
        loginPage.hide()
        forgot_psw_page.show()


loginPage = QtWidgets.QMainWindow()
ui = Ui_loginPage()
ui.setupUi(loginPage)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global loginPage
    loginPage.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()



