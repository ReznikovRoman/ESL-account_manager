import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import forgot_password.forgot_psw_3
import forgot_password.forgot_psw_1
import mysql_db
import email_handler


setup_info = email_handler.get_file_info()
# print("2nd: ", forgot_password.CODE)


class Ui_forgot_password_2(object):

    def setupUi(self, forgot_password_2):
        forgot_password_2.setObjectName("forgot_password_2")
        forgot_password_2.resize(715, 467)
        forgot_password_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtWidgets.QWidget(forgot_password_2)

        self.centralwidget.setObjectName("centralwidget")

        self.forgot_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.forgot_label_2.setGeometry(QtCore.QRect(210, 30, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(22)
        self.forgot_label_2.setFont(font)
        self.forgot_label_2.setObjectName("forgot_label_2")

        self.label_code = QtWidgets.QLabel(self.centralwidget)
        self.label_code.setGeometry(QtCore.QRect(50, 200, 261, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.label_code.setFont(font)
        self.label_code.setObjectName("label_code")

        self.input_code = QtWidgets.QLineEdit(self.centralwidget)
        self.input_code.setGeometry(QtCore.QRect(330, 200, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_code.setFont(font)
        self.input_code.setWhatsThis("")
        self.input_code.setAutoFillBackground(False)
        self.input_code.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.input_code.setInputMask("")
        self.input_code.setObjectName("input_code")

        self.forgot_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.forgot_btn_2.setGeometry(QtCore.QRect(330, 250, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.forgot_btn_2.setFont(font)
        self.forgot_btn_2.setFlat(False)
        self.forgot_btn_2.setObjectName("forgot_btn_2")

        self.back_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn_2.setGeometry(QtCore.QRect(330, 315, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.back_btn_2.setFont(font)
        self.back_btn_2.setFlat(False)
        self.back_btn_2.setObjectName("back_btn_2")

        self.email_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.email_btn_2.setGeometry(QtCore.QRect(330, 380, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(14)
        self.email_btn_2.setFont(font)
        self.email_btn_2.setFlat(False)
        self.email_btn_2.setObjectName("email_btn_2")

        forgot_password_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(forgot_password_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 23))
        self.menubar.setObjectName("menubar")
        forgot_password_2.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(forgot_password_2)
        self.statusbar.setObjectName("statusbar")
        forgot_password_2.setStatusBar(self.statusbar)

        self.retranslateUi(forgot_password_2)
        QtCore.QMetaObject.connectSlotsByName(forgot_password_2)

        self.forgot_btn_2.pressed.connect(self.forgot_btn2_pressed)
        self.back_btn_2.pressed.connect(self.back_btn2_pressed)
        self.email_btn_2.pressed.connect(self.email_btn2_pressed)

    def retranslateUi(self, forgot_password_2):
        _translate = QtCore.QCoreApplication.translate
        forgot_password_2.setWindowTitle(_translate("forgot_password_2", "forgot password"))
        self.forgot_label_2.setText(_translate("forgot_password_2", "Forgot Password?"))
        self.label_code.setText(_translate("forgot_password_2", "Enter your verification code: "))
        self.forgot_btn_2.setText(_translate("forgot_password_2", "Next"))
        self.back_btn_2.setText(_translate("forgot_password_2", "Return back"))
        self.email_btn_2.setText(_translate("forgot_password_2", "Send code again"))

    def forgot_btn2_pressed(self):
        user_input = self.input_code.text()
        if user_input != "":
            if int(user_input) == forgot_password.CODE:
                password_page = forgot_password.forgot_psw_3.forgot_page_3
                forgot_page_2.hide()
                password_page.show()
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect verification code",
                                              "Your code is incorrect, try to re-enter it.")
        else:
            QtWidgets.QMessageBox.warning(None, "Incorrect verification code",
                                          "Enter verification code.")

    def back_btn2_pressed(self):
        db = mysql_db.SQL()
        table = "email_to_change"
        db.delete_user_by_code(table, forgot_password.CODE)

        forgot_1 = forgot_password.forgot_psw_1.forgot_page_1
        forgot_page_2.hide()
        forgot_1.show()

    def email_btn2_pressed(self):
        db = mysql_db.SQL()
        table = "email_to_change"
        email = db.get_email_by_code(table, forgot_password.CODE)

        _email_handler = email_handler.EmailHandler(setup_info)
        subject = "Password reset"
        msg = "Hi!\n\n" \
              "Seems like you forgot your 'ESL Account Manager' password. To reset it, enter the verification code.\n\n" \
              "Your verification code: {0}\n\n" \
              "Thanks,\n" \
              "ESL Account Manager".format(forgot_password.CODE)
        _email_handler.send_email(msg, email, subject)

        QtWidgets.QMessageBox.information(None, "Resetting password",
                                          "The verification code was sent again.")



forgot_app2 = QtWidgets.QApplication(sys.argv)

forgot_page_2 = QtWidgets.QMainWindow()
ui = Ui_forgot_password_2()
ui.setupUi(forgot_page_2)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global forgot_page_2

    forgot_page_2.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

