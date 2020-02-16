import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import forgot_password
import login_page.loginPage
import main_page.data_modules.verifier
import mysql_db


db = mysql_db.SQL()
table = 'user_info'


class Ui_forgot_password_3(object):

    def setupUi(self, forgot_password_3):
        forgot_password_3.setObjectName("forgot_password_3")
        forgot_password_3.resize(715, 467)
        self.centralwidget = QtWidgets.QWidget(forgot_password_3)
        self.centralwidget.setObjectName("centralwidget")

        self.forgot_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.forgot_label_3.setGeometry(QtCore.QRect(210, 30, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(22)
        self.forgot_label_3.setFont(font)
        self.forgot_label_3.setObjectName("forgot_label_3")

        self.label_psw_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_psw_1.setGeometry(QtCore.QRect(50, 150, 191, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_psw_1.setFont(font)
        self.label_psw_1.setObjectName("label_psw_1")

        self.input_psw_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_psw_1.setGeometry(QtCore.QRect(250, 150, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_psw_1.setFont(font)
        self.input_psw_1.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_psw_1.setObjectName("input_psw_1")

        self.label_psw_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_psw_2.setGeometry(QtCore.QRect(50, 230, 191, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_psw_2.setFont(font)
        self.label_psw_2.setObjectName("label_psw_2")

        self.input_psw_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_psw_2.setGeometry(QtCore.QRect(250, 230, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_psw_2.setFont(font)
        self.input_psw_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_psw_2.setObjectName("input_psw_2")

        self.forgot_btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.forgot_btn_3.setGeometry(QtCore.QRect(250, 300, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.forgot_btn_3.setFont(font)
        self.forgot_btn_3.setObjectName("forgot_btn_3")

        forgot_password_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(forgot_password_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 23))
        self.menubar.setObjectName("menubar")
        forgot_password_3.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(forgot_password_3)
        self.statusbar.setObjectName("statusbar")
        forgot_password_3.setStatusBar(self.statusbar)

        self.retranslateUi(forgot_password_3)
        QtCore.QMetaObject.connectSlotsByName(forgot_password_3)

        self.forgot_btn_3.pressed.connect(self.forgot_btn3_pressed)

    def retranslateUi(self, forgot_password_3):
        _translate = QtCore.QCoreApplication.translate
        forgot_password_3.setWindowTitle(_translate("forgot_password_3", "forgot password"))
        self.forgot_label_3.setText(_translate("forgot_password_3", "Forgot Password?"))
        self.label_psw_1.setText(_translate("forgot_password_3", "Enter new password: "))
        self.label_psw_2.setText(_translate("forgot_password_3", "Re-enter password: "))
        self.forgot_btn_3.setText(_translate("forgot_password_3", "Change Password"))

    def get_user_password(self, user_password):
        if user_password != "":
            if main_page.data_modules.verifier.Verifier(user_password).check_password():
                return user_password
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect password",
                                              "Please, enter password in a correct format!\n"
                                              "Password can only contain digits or letters")

    def check_passwords(self, psw1, psw2):
        if psw1 is not None and psw2 is not None and psw1 == psw2:
            return True
        elif psw1 is not None and psw2 is not None and psw1 != psw2:
            QtWidgets.QMessageBox.warning(None, "Incorrect passwords!",
                                          "Passwords are not same - check your spelling.")
            # return False
        elif self.input_psw_1.text() == "" or self.input_psw_2.text() == "":
            QtWidgets.QMessageBox.warning(None, "Enter your new password",
                                          "Fill in the all fields.")
            # return False

    def forgot_btn3_pressed(self):
        user_psw1 = self.get_user_password(self.input_psw_1.text())
        user_psw2 = self.get_user_password(self.input_psw_2.text())
        if self.check_passwords(user_psw1, user_psw2):
            code = forgot_password.CODE
            table_name = "email_to_change"
            EMAIL = db.get_email_by_code(table_name, code)

            db.change_password(table, EMAIL, self.input_psw_1.text())

            db.delete_user_by_code(table_name, code)

            _login_page = login_page.loginPage.loginPage
            forgot_page_3.hide()
            _login_page.show()


forgot_app3 = QtWidgets.QApplication(sys.argv)

forgot_page_3 = QtWidgets.QMainWindow()
ui = Ui_forgot_password_3()
ui.setupUi(forgot_page_3)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global forgot_page_3

    forgot_page_3.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


