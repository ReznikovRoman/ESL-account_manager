# from PyQt5 import QtCore, QtGui, QtWidgets
# import main_page.main_page_file
# import re
#
#
# class Ui_loginPage(object):
#
#     def get_user_email(self):
#         regex = '[^@]+@[^@]+\.[^@]+'
#         user_input = self.email_input.text()
#         if user_input != "":
#             if re.search(regex, user_input):
#                 return user_input
#             else:
#                 QtWidgets.QMessageBox.warning(None, "Incorrect email address",
#                                               "Please, enter an email address in a correct format!")
#
#     def setupUi(self, loginPage):
#         loginPage.setObjectName("loginPage")
#         loginPage.resize(899, 517)
#         self.centralwidget = QtWidgets.QWidget(loginPage)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.email_input = QtWidgets.QLineEdit(self.centralwidget)
#         self.email_input.setGeometry(QtCore.QRect(310, 170, 571, 51))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.email_input.setFont(font)
#         #self.email_input.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
#         #self.email_input.setAcceptDrops(True)
#         self.email_input.setObjectName("email_input")
#
#         self.email_label = QtWidgets.QLabel(self.centralwidget)
#         self.email_label.setGeometry(QtCore.QRect(30, 160, 271, 71))
#         font = QtGui.QFont()
#         font.setFamily("MS Reference Sans Serif")
#         font.setPointSize(12)
#         self.email_label.setFont(font)
#         self.email_label.setTextFormat(QtCore.Qt.RichText)
#         self.email_label.setObjectName("email_label")
#
#         self.remember_checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.remember_checkBox.setGeometry(QtCore.QRect(340, 280, 141, 31))
#         font = QtGui.QFont()
#         font.setFamily("MS Reference Sans Serif")
#         font.setPointSize(10)
#         self.remember_checkBox.setFont(font)
#         self.remember_checkBox.setObjectName("remember_checkBox")
#
#         self.login_button = QtWidgets.QPushButton(self.centralwidget)
#         self.login_button.setGeometry(QtCore.QRect(120, 270, 181, 61))
#         font = QtGui.QFont()
#         font.setFamily("MS Reference Sans Serif")
#         font.setPointSize(10)
#         font.setBold(True)
#         font.setWeight(75)
#         self.login_button.setFont(font)
#         self.login_button.setObjectName("login_button")
#
#         self.login_label = QtWidgets.QLabel(self.centralwidget)
#         self.login_label.setGeometry(QtCore.QRect(270, 40, 171, 51))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI Emoji")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         self.login_label.setFont(font)
#         self.login_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.login_label.setObjectName("login_label")
#
#         loginPage.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(loginPage)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 23))
#         self.menubar.setObjectName("menubar")
#         loginPage.setMenuBar(self.menubar)
#
#         self.statusbar = QtWidgets.QStatusBar(loginPage)
#         self.statusbar.setObjectName("statusbar")
#         loginPage.setStatusBar(self.statusbar)
#
#         self.retranslateUi(loginPage)
#         QtCore.QMetaObject.connectSlotsByName(loginPage)
#
#         self.login_button.pressed.connect(self.login_btn_pressed)
#
#     def retranslateUi(self, loginPage):
#         _translate = QtCore.QCoreApplication.translate
#         loginPage.setWindowTitle(_translate("loginPage", "Login"))
#         self.email_label.setText(_translate("loginPage", "Enter your ESL admin e-mail"))
#         self.remember_checkBox.setText(_translate("loginPage", "Remember me"))
#         self.login_button.setText(_translate("loginPage", "Login"))
#         self.login_label.setText(_translate("loginPage", "Login"))
#
#     def login_btn_pressed(self):
#
#         user_email = self.get_user_email()
#
#         if user_email is not None:
#             mainPage = main_page.MainWindow
#             mainPage.show()
#             setup_info = open("setup_info.txt", "w")
#             setup_info.write("User email: {0}\n'Remember me' status: {1}".format(user_email, self.remember_checkBox.checkState()))
#             login_page_window.hide()
#             setup_info.close()
#
#         elif user_email is None and self.email_input.text() == "":
#             QtWidgets.QMessageBox.warning(None, "Incorrect email address",
#                                           "Enter email address")
#
#
# login_page_window = QtWidgets.QMainWindow()
# ui = Ui_loginPage()
# ui.setupUi(login_page_window)