

from PyQt5 import QtCore, QtGui, QtWidgets
import email_handler
import sys
import re
import main_page.data_modules.verifier
# import main_page.main_page_file
import mysql_db


db = mysql_db.SQL()
table = 'user_info'


def setup_info():
    file_info = email_handler.get_file_info()
    a_email_handler = email_handler.EmailHandler(file_info)
    a_remember_me = a_email_handler.get_remember_me_state()
    a_password = ""
    a_nickname = ""
    a_send_mail_state = True
    a_notifications_state = True
    a_email = a_email_handler.get_address()

    for value in file_info:
        if len(re.findall('User nickname: (.*)', value)) > 0:
            a_nickname = re.findall('User nickname: (.*)', value)[0]

        if len(re.findall('Send email state: (.*)', value)) > 0:
            a_send_mail_state = re.findall('Send email state: (.*)', value)[0]
            if a_send_mail_state == '0':
                a_send_mail_state = False
            else:
                a_send_mail_state = True

        if len(re.findall('Notifications state: (.*)', value)) > 0:
            a_notifications_state = re.findall('Notifications state: (.*)', value)[0]
            if a_notifications_state == '0':
                a_notifications_state = False
            else:
                a_notifications_state = True
    return a_email, a_remember_me, a_password, a_nickname, a_send_mail_state, a_notifications_state


email, remember_me, password, nickname, send_mail_state, notifications_state = setup_info()
# print('real email: ', email)


class Ui_settings_window(object):

    def setupUi(self, settings_window):
        settings_window.setObjectName("settings_window")
        settings_window.resize(788, 485)
        self.centralwidget = QtWidgets.QWidget(settings_window)
        self.centralwidget.setObjectName("centralwidget")

        self.settings_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.settings_checkBox.setGeometry(QtCore.QRect(290, 350, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.settings_checkBox.setFont(font)
        self.settings_checkBox.setObjectName("settings_checkBox")

        self.settings_email_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.settings_email_checkBox.setGeometry(QtCore.QRect(290, 390, 425, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.settings_email_checkBox.setFont(font)
        self.settings_email_checkBox.setObjectName("settings_email_checkBox")

        self.settings_notification_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.settings_notification_checkBox.setGeometry(QtCore.QRect(290, 430, 425, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.settings_notification_checkBox.setFont(font)
        self.settings_notification_checkBox.setObjectName("settings_notification_checkBox")

        self.settings_submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.settings_submit_btn.setGeometry(QtCore.QRect(30, 350, 231, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.settings_submit_btn.setFont(font)
        self.settings_submit_btn.setObjectName("settings_submit_btn")

        self.settings_email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.settings_email_input.setGeometry(QtCore.QRect(290, 110, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.settings_email_input.setFont(font)
        self.settings_email_input.setText("")
        self.settings_email_input.setObjectName("settings_email_input")

        self.settings_nickname_input = QtWidgets.QLineEdit(self.centralwidget)
        self.settings_nickname_input.setGeometry(QtCore.QRect(290, 170, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.settings_nickname_input.setFont(font)
        self.settings_nickname_input.setText("")
        self.settings_nickname_input.setObjectName("settings_nickname_input")

        self.settings_password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.settings_password_input.setGeometry(QtCore.QRect(290, 230, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.settings_password_input.setFont(font)
        self.settings_password_input.setText("")
        self.settings_password_input.setObjectName("settings_password_input")

        self.settings_email_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_email_label.setGeometry(QtCore.QRect(20, 100, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(15)
        self.settings_email_label.setFont(font)
        self.settings_email_label.setObjectName("settings_email_label")

        self.settings_nickname_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_nickname_label.setGeometry(QtCore.QRect(20, 160, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(15)
        self.settings_nickname_label.setFont(font)
        self.settings_nickname_label.setObjectName("settings_nickname_label")

        self.settings_password_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_password_label.setGeometry(QtCore.QRect(20, 220, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(15)
        self.settings_password_label.setFont(font)
        self.settings_password_label.setObjectName("settings_password_label")

        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(290, 20, 151, 51))

        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(26)
        font.setWeight(50)
        font.setKerning(True)
        self.settings_label.setFont(font)
        self.settings_label.setObjectName("settings_label")

        settings_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settings_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 23))
        self.menubar.setObjectName("menubar")
        settings_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(settings_window)
        self.statusbar.setObjectName("statusbar")
        settings_window.setStatusBar(self.statusbar)

        self.settings_submit_btn.pressed.connect(self.submit_btn_pressed)

        self.retranslateUi(settings_window)
        QtCore.QMetaObject.connectSlotsByName(settings_window)

    def retranslateUi(self, settings_window):
        _translate = QtCore.QCoreApplication.translate
        settings_window.setWindowTitle(_translate("settings_window", "Settings"))
        self.settings_checkBox.setText(_translate("settings_window", "Remember me"))
        self.settings_submit_btn.setText(_translate("settings_window", "Confirm changes"))
        self.settings_email_label.setText(_translate("settings_window", "Change email address"))
        self.settings_label.setText(_translate("settings_window", "Settings"))
        self.settings_email_input.setText(_translate("settings_window", email))
        self.settings_email_checkBox.setText(_translate("settings_window", "Receive email letters, when a new protest opens"))
        self.settings_notification_checkBox.setText(_translate("settings_window", "Turn on notifications"))
        self.settings_nickname_label.setText(_translate("settings_window", "Change nickname"))
        self.settings_password_label.setText(_translate("settings_window", "Change password"))

        self.settings_nickname_input.setText(_translate("settings_window", nickname))
        self.settings_password_input.setText(_translate("settings_window", password))
        self.settings_checkBox.setChecked(remember_me)
        self.settings_email_checkBox.setChecked(send_mail_state)
        self.settings_notification_checkBox.setChecked(notifications_state)

    def get_user_email(self):
        new_email = self.settings_email_input.text()
        if new_email != "":
            if re.search('[^@]+@[^@]+\.[^@]+', new_email):
                return new_email
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect email address",
                                              "Please, enter an email address in a correct format!")

    def get_user_nickname(self):
        new_nickname = self.settings_nickname_input.text()
        if new_nickname != "":
            if re.search('^[a-zA-Z0-9]+$', new_nickname):
                return new_nickname
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect nickname",
                                              "Please, enter nickname in a correct format.")

    def get_user_password(self):
        new_password = self.settings_password_input.text()
        if new_password != "":
            if re.search('^[a-zA-Z0-9]+$', new_password):
                return new_password
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect password",
                                              "Please, enter password in a correct format.")

    def submit_btn_pressed(self):
        email = email_handler.get_email_from_file(email_handler.get_file_info())
        user_email = self.get_user_email()
        new_password = self.get_user_password()
        new_nickname = self.get_user_nickname()

        # main_page_ui = main_page.main_page_file.ui

        # TEST DATA
        # file = open("setup_info.txt", 'r')
        # data = file.read()
        # print('Settings: ', data)
        # print()

        # new_email = re.sub('(User email: .*)', 'User email: %s' % user_email, data)
        # file = open('setup_info.txt', 'w')
        # file.write(data.replace(data, new_email))
        # file.close()

        if user_email is not None and new_nickname is not None:

            # print("Settings: ", email, user_email)
            # print("Settings: ", db.change_email(table, email, user_email))

            if db.change_email(table, email, user_email):
                file = open('setup_info.txt', 'r')
                data = file.read()
                file.close()

                new_data = re.sub('(User email: .*)', 'User email: %s' % user_email, data)
                new_data = re.sub('(\'Remember me\' status: .*)', "'Remember me' status: %s" % self.settings_checkBox.checkState(), new_data)
                new_data = re.sub('(User nickname: .*)', "User nickname: %s" % new_nickname, new_data)
                new_data = re.sub('(Send email state: .*)', "Send email state: %s" % self.settings_email_checkBox.checkState(), new_data)
                new_data = re.sub('(Notifications state: .*)', "Notifications state: %s" % self.settings_notification_checkBox.checkState(), new_data)

                file = open('setup_info.txt', 'w')
                file.write(data.replace(data, new_data))
                file.close()

                if new_password is not None:
                    db.change_password(table, user_email, new_password)
                settings_page.hide()
            else:
                QtWidgets.QMessageBox.warning(None, "Wrong email",
                                              "There is an account with such email.")
        else:
            QtWidgets.QMessageBox.warning(None, "Incorrect input data",
                                          "Please, fill in all fields.")


settings_app = QtWidgets.QApplication(sys.argv)
settings_page = QtWidgets.QMainWindow()
ui = Ui_settings_window()
ui.setupUi(settings_page)


def main():
    app = QtWidgets.QApplication(sys.argv)
    global settings_window
    settings_window = QtWidgets.QMainWindow()
    ui = Ui_settings_window()
    ui.setupUi(settings_window)
    settings_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

