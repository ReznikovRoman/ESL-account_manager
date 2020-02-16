
from PyQt5 import QtCore, QtGui, QtWidgets
import login_page.loginPage
import re
import main_page.data_modules.verifier
import settings_page.settings_page
import main_page.main_page_file
import registration_page

import mysql_db



db = mysql_db.SQL()
table = 'user_info'


class Ui_signUp_window(object):

    def get_user_email(self):
        regex = '[^@]+@[^@]+\.[^@]+'
        user_email = self.signUp_email_input.text()
        if user_email != "":
            if re.search(regex, user_email):
                return user_email
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect email address",
                                              "Please, enter an email address in a correct format!")

    def get_user_password(self, user_password):
        # user_password = self.signUp_password_input.text()
        if user_password != "":
            if main_page.data_modules.verifier.Verifier(user_password).check_password():
                return user_password
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect password",
                                              "Please, enter password in a correct format!\n"
                                              "Password can only contain digits or letters")

    def get_user_nickname(self):
        user_nickname = self.signUp_nickname_input.text()
        if user_nickname != "":
            if main_page.data_modules.verifier.Verifier(user_nickname).check_password():
                return user_nickname
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect nickname",
                                              "Please, enter nickname in a correct format!\n"
                                              "Nickname can only contain digits or letters")

    def setupUi(self, signUp_window):
        signUp_window.setObjectName("signUp_window")
        signUp_window.resize(755, 541)
        font = QtGui.QFont()
        font.setPointSize(8)
        signUp_window.setFont(font)

        self.centralwidget = QtWidgets.QWidget(signUp_window)
        self.centralwidget.setObjectName("centralwidget")

        self.signUp_label = QtWidgets.QLabel(self.centralwidget)
        self.signUp_label.setGeometry(QtCore.QRect(210, 20, 331, 81))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(32)
        self.signUp_label.setFont(font)
        self.signUp_label.setObjectName("signUp_label")

        self.signUp_email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.signUp_email_input.setGeometry(QtCore.QRect(330, 160, 341, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.signUp_email_input.setFont(font)
        self.signUp_email_input.setText("")
        self.signUp_email_input.setObjectName("signUp_email_input")

        self.signUp_email_label = QtWidgets.QLabel(self.centralwidget)
        self.signUp_email_label.setGeometry(QtCore.QRect(30, 160, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.signUp_email_label.setFont(font)
        self.signUp_email_label.setObjectName("signUp_email_label")

        self.signUp_password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.signUp_password_input.setGeometry(QtCore.QRect(330, 260, 341, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.signUp_password_input.setFont(font)
        self.signUp_password_input.setObjectName("signUp_password_input")

        self.signUp_password_label = QtWidgets.QLabel(self.centralwidget)
        self.signUp_password_label.setGeometry(QtCore.QRect(30, 250, 171, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.signUp_password_label.setFont(font)
        self.signUp_password_label.setObjectName("signUp_password_label")

        self.signUp_password_2_label = QtWidgets.QLabel(self.centralwidget)
        self.signUp_password_2_label.setGeometry(QtCore.QRect(30, 300, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.signUp_password_2_label.setFont(font)
        self.signUp_password_2_label.setObjectName("signUp_password_2_label")

        self.signUp_password_2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.signUp_password_2_input.setGeometry(QtCore.QRect(330, 310, 341, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.signUp_password_2_input.setFont(font)
        self.signUp_password_2_input.setObjectName("signUp_password_2_input")

        self.signUp_nickname_label = QtWidgets.QLabel(self.centralwidget)
        self.signUp_nickname_label.setGeometry(QtCore.QRect(30, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.signUp_nickname_label.setFont(font)
        self.signUp_nickname_label.setObjectName("signUp_nickname_label")

        self.signUp_nickname_input = QtWidgets.QLineEdit(self.centralwidget)
        self.signUp_nickname_input.setGeometry(QtCore.QRect(330, 210, 341, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.signUp_nickname_input.setFont(font)
        self.signUp_nickname_input.setObjectName("signUp_nickname_input")

        self.signUp_button = QtWidgets.QPushButton(self.centralwidget)
        self.signUp_button.setGeometry(QtCore.QRect(330, 430, 171, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        self.signUp_button.setFont(font)
        self.signUp_button.setObjectName("signUp_button")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(30, 430, 190, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(20)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")

        self.send_mail_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.send_mail_checkBox.setGeometry(QtCore.QRect(30, 390, 391, 18))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.send_mail_checkBox.setFont(font)
        self.send_mail_checkBox.setChecked(True)
        self.send_mail_checkBox.setObjectName("send_mail_checkBox")

        signUp_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(signUp_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        signUp_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(signUp_window)
        self.statusbar.setObjectName("statusbar")
        signUp_window.setStatusBar(self.statusbar)

        self.signUp_button.pressed.connect(self.signup_btn_pressed)
        self.exit_button.pressed.connect(self.exit_btn_pressed)

        self.retranslateUi(signUp_window)
        QtCore.QMetaObject.connectSlotsByName(signUp_window)

    def retranslateUi(self, signUp_window):
        _translate = QtCore.QCoreApplication.translate
        signUp_window.setWindowTitle(_translate("signUp_window", "Sign up Form"))
        self.signUp_label.setText(_translate("signUp_window", "Sign up Form"))
        self.signUp_email_label.setText(_translate("signUp_window", "Enter email address"))
        self.signUp_password_label.setText(_translate("signUp_window", "Enter password"))
        self.signUp_password_2_label.setText(_translate("signUp_window", "Enter your password again"))
        self.signUp_nickname_label.setText(_translate("signUp_window", "Enter your nickname"))
        self.signUp_button.setText(_translate("signUp_window", "Sign Up!"))
        self.exit_button.setText(_translate("signUp_window", "Return back"))
        self.send_mail_checkBox.setText(_translate("signUp_window", "Receive email letters, when a new protest opens"))

    def check_user_info(self):
        user_email = self.get_user_email()
        user_nickname = self.get_user_nickname()
        user_password_1 = self.get_user_password(self.signUp_password_input.text())
        user_password_2 = self.get_user_password(self.signUp_password_2_input.text())
        send_email_state = self.send_mail_checkBox.checkState()
        if self.signUp_email_input.text() == "" or self.signUp_nickname_input.text() == "" or \
                self.signUp_password_input.text() == "" or self.signUp_password_2_input.text() == "":
            QtWidgets.QMessageBox.warning(None, "Enter your info",
                                          "Fill in the all fields.")
            return False
        else:
            if user_email is not None and user_nickname is not None and user_password_1 is not None and \
                    user_password_2 is not None and user_password_1 == user_password_2 and \
                    not db.check_existence(table, user_email):
                return True
            elif user_password_1 is not None and user_password_2 is not None and user_password_1 != user_password_2:
                QtWidgets.QMessageBox.warning(None, "Incorrect passwords!",
                                              "Passwords are not same - check your spelling.")
                return False
            elif db.check_existence(table, user_email):
                QtWidgets.QMessageBox.warning(None, "Wrong email",
                                              "Account with such email already exists.")

    def exit_btn_pressed(self):
        _login_page = login_page.loginPage.loginPage
        _login_page.show()
        signUp_window.hide()

    def signup_btn_pressed(self):
        _login_page = login_page.loginPage.loginPage
        login_page_ui = login_page.loginPage.ui
        settings_ui = settings_page.settings_page.ui
        main_page_ui = main_page.main_page_file.ui

        if self.check_user_info():
            email = self.get_user_email()
            nickname = self.get_user_nickname()
            password = self.get_user_password(self.signUp_password_input.text())
            send_email_state = self.send_mail_checkBox.checkState()

            login_page_ui.email_input.setText(email)

            settings_ui.settings_password_input.setText(password)
            settings_ui.settings_nickname_input.setText(nickname)
            settings_ui.settings_email_checkBox.setChecked(bool(int(send_email_state)))

            main_page_ui.label_greeting.setText("Welcome back, %s!" % nickname)

            setup_info = open("setup_info.txt", "w")
            setup_info.write("User email: {0}\nUser nickname: {1}\n"
                             "Send email state: {2}\n'Remember me' status: 0\n"
                             "Notifications state: {3}".format(email, nickname, send_email_state, 2))
            setup_info.close()

            # TEST DATA
            # file = open("setup_info.txt", 'r')
            # data = file.read()
            # print('SignUp: ', data)
            # print()

            db.add_value(table, (email, password))

            # print("Sign Up: ", email)

            _login_page.show()

            signUp_window.hide()


signUp_window = QtWidgets.QMainWindow()
ui = Ui_signUp_window()
ui.setupUi(signUp_window)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global signUp_window
    signUp_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

