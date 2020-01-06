

from PyQt5 import QtCore, QtGui, QtWidgets
import app_account_manager.email_handler
import sys
import re
import app_account_manager.main_page.data_modules.verifier
# import app_account_manager.main_page.main_page_file


def setup_info():
    file_info = app_account_manager.email_handler.get_file_info()
    a_email_handler = app_account_manager.email_handler.EmailHandler(file_info)
    a_email = a_email_handler.get_address()
    a_remember_me = a_email_handler.get_remember_me_state()
    a_password = ""
    a_nickname = ""
    a_send_mail_state = True
    for value in file_info:
        if len(re.findall('User password: (.*)', value)) > 0:
            a_password = re.findall('User password: (.*)', value)[0]
        if len(re.findall('User nickname: (.*)', value)) > 0:
            a_nickname = re.findall('User nickname: (.*)', value)[0]
        if len(re.findall('Send email state: (.*)', value)) > 0:
            a_send_mail_state = re.findall('Send email state: (.*)', value)[0]
            if a_send_mail_state == '0':
                a_send_mail_state = False
            else:
                a_send_mail_state = True
    return a_email, a_remember_me, a_password, a_nickname, a_send_mail_state


email, remember_me, password, nickname, send_mail_state = setup_info()


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
        self.settings_nickname_label.setText(_translate("settings_window", "Change nickname"))
        self.settings_password_label.setText(_translate("settings_window", "Change password"))

        self.settings_nickname_input.setText(_translate("settings_window", nickname))
        self.settings_password_input.setText(_translate("settings_window", password))
        self.settings_checkBox.setChecked(remember_me)
        self.settings_email_checkBox.setChecked(bool(send_mail_state))

    def get_user_email(self):
        regex = '[^@]+@[^@]+\.[^@]+'
        user_input = self.settings_email_input.text()
        if user_input != "":
            if re.search(regex, user_input):
                return user_input
            else:
                QtWidgets.QMessageBox.warning(None, "Incorrect email address",
                                              "Please, enter an email address in a correct format!")

    def get_user_password(self):
        regex = '[a-zA-Z0-9]+'
        new_password = self.settings_password_input.text()
        if app_account_manager.main_page.data_modules.verifier.Verifier(new_password).check_password():
            return new_password
        else:
            QtWidgets.QMessageBox.warning(None, "Incorrect password",
                                          "Please, enter password in a correct format.")

    def get_user_nickname(self):
        regex = '[a-zA-Z0-9]+'
        new_nickname = self.settings_nickname_input.text()
        if app_account_manager.main_page.data_modules.verifier.Verifier(new_nickname).check_password():
            return new_nickname
        else:
            QtWidgets.QMessageBox.warning(None, "Incorrect nickname",
                                          "Please, enter nickname in a correct format.")

    def submit_btn_pressed(self):
        user_email = self.get_user_email()
        new_password = self.get_user_password()
        new_nickname = self.get_user_nickname()

        # main_page_ui = app_account_manager.main_page.main_page_file.ui

        if user_email is not None:
            file = open('setup_info.txt', 'r')
            data = file.read()
            file.close()

            new_data = re.sub('(User email: .*)', 'User email: %s' % user_email, data)
            new_data = re.sub('(\'Remember me\' status: .*)', "'Remember me' status: %s" % self.settings_checkBox.checkState(), new_data)
            new_data = re.sub('(User nickname: .*)', "User nickname: %s" % new_nickname, new_data)
            new_data = re.sub('(User password: .*)', "User password: %s" % new_password, new_data)
            new_data = re.sub('(Send email state: .*)', "Send email state: %s" % self.settings_email_checkBox.checkState(), new_data)

            file = open('setup_info.txt', 'w')
            file.write(data.replace(data, new_data))
            file.close()

            # main_page_ui.label_greeting.setText(("Welcome back, %s !" % new_nickname))

            settings_page.hide()

        elif user_email is None and self.settings_email_input.text() == "":
            QtWidgets.QMessageBox.warning(None, "Incorrect email address",
                                          "Enter email address")


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

