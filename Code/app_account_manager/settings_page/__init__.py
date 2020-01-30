# from PyQt5 import QtCore, QtGui, QtWidgets
# import email_handler
# import sys
# import re
# # import main_page.main_page_file
#
#
# def setup_info():
#     file_info = email_handler.get_file_info()
#     a_email_handler = email_handler.EmailHandler(file_info)
#     a_email = a_email_handler.get_address()
#     a_remember_me = a_email_handler.get_remember_me_state()
#     return a_email, a_remember_me
#
#
# email, remember_me = setup_info()
#
#
# class Ui_settings_window(object):
#
#     def setupUi(self, settings_window):
#         settings_window.setObjectName("settings_window")
#         settings_window.resize(788, 485)
#         self.centralwidget = QtWidgets.QWidget(settings_window)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.settings_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.settings_checkBox.setGeometry(QtCore.QRect(290, 200, 151, 21))
#         font = QtGui.QFont()
#         font.setFamily("MS Reference Sans Serif")
#         font.setPointSize(11)
#         self.settings_checkBox.setFont(font)
#         self.settings_checkBox.setObjectName("settings_checkBox")
#
#         self.settings_submit_btn = QtWidgets.QPushButton(self.centralwidget)
#         self.settings_submit_btn.setGeometry(QtCore.QRect(30, 270, 231, 61))
#         font = QtGui.QFont()
#         font.setFamily("MS Reference Sans Serif")
#         font.setPointSize(16)
#         self.settings_submit_btn.setFont(font)
#         self.settings_submit_btn.setObjectName("settings_submit_btn")
#
#         self.settings_email_input = QtWidgets.QLineEdit(self.centralwidget)
#         self.settings_email_input.setGeometry(QtCore.QRect(290, 140, 341, 31))
#         font = QtGui.QFont()
#         font.setFamily("Microsoft YaHei")
#         font.setPointSize(12)
#         self.settings_email_input.setFont(font)
#         self.settings_email_input.setText("")
#         self.settings_email_input.setObjectName("settings_email_input")
#
#         self.settings_email_label = QtWidgets.QLabel(self.centralwidget)
#         self.settings_email_label.setGeometry(QtCore.QRect(20, 130, 251, 51))
#         font = QtGui.QFont()
#         font.setFamily("MS Reference Sans Serif")
#         font.setPointSize(15)
#         self.settings_email_label.setFont(font)
#         self.settings_email_label.setObjectName("settings_email_label")
#
#         self.settings_label = QtWidgets.QLabel(self.centralwidget)
#         self.settings_label.setGeometry(QtCore.QRect(290, 20, 151, 51))
#
#         font = QtGui.QFont()
#         font.setFamily("HoloLens MDL2 Assets")
#         font.setPointSize(26)
#         font.setWeight(50)
#         font.setKerning(True)
#         self.settings_label.setFont(font)
#         self.settings_label.setObjectName("settings_label")
#
#         settings_window.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(settings_window)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 23))
#         self.menubar.setObjectName("menubar")
#         settings_window.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(settings_window)
#         self.statusbar.setObjectName("statusbar")
#         settings_window.setStatusBar(self.statusbar)
#
#         self.settings_submit_btn.clicked.connect(self.submit_btn_pressed)
#
#         self.retranslateUi(settings_window)
#         QtCore.QMetaObject.connectSlotsByName(settings_window)
#
#     def retranslateUi(self, settings_window):
#         _translate = QtCore.QCoreApplication.translate
#         settings_window.setWindowTitle(_translate("settings_window", "Settings"))
#         self.settings_checkBox.setText(_translate("settings_window", "Remember me"))
#         self.settings_submit_btn.setText(_translate("settings_window", "Confirm changes"))
#         self.settings_email_label.setText(_translate("settings_window", "Change email address"))
#         self.settings_label.setText(_translate("settings_window", "Settings"))
#         self.settings_email_input.setText(_translate("settings_window", email))
#         self.settings_checkBox.setChecked(remember_me)
#
#     def get_user_email(self):
#         regex = '[^@]+@[^@]+\.[^@]+'
#         user_input = self.settings_email_input.text()
#         if user_input != "":
#             if re.search(regex, user_input):
#                 return user_input
#             else:
#                 QtWidgets.QMessageBox.warning(None, "Incorrect email address",
#                                               "Please, enter an email address in a correct format!")
#
#     def submit_btn_pressed(self):
#         user_email = self.get_user_email()
#         if user_email is not None:
#             start_setup_info = open("setup_info.txt", "w")
#             start_setup_info.write("User email: {0}\n'Remember me' status: {1}".format(user_email,
#                                                                                        self.settings_checkBox.checkState()))
#             start_setup_info.close()
#             # mainPage = main_page.main_page_file.get_main_page()
#             # mainPage.show()
#             settingsPage.hide()
#
#         elif user_email is None and self.settings_email_input.text() == "":
#             QtWidgets.QMessageBox.warning(None, "Incorrect email address",
#                                           "Enter email address")
#
#
# # settings_app = QtWidgets.QApplication(sys.argv)
# # settingsPage = QtWidgets.QMainWindow()
# # ui = Ui_settings_window()
# # ui.setupUi(settingsPage)
