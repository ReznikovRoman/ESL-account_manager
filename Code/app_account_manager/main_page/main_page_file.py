# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#
#     def setupUi(self, MainWindow):
#         self.threads = []
#
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.setEnabled(True)
#         MainWindow.resize(1700, 920)
#
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.progressLabel = QtWidgets.QLabel(self.centralwidget)
#         self.progressLabel.setGeometry(QtCore.QRect(160, 580, 141, 31))
#         self.progressLabel.setObjectName("progressLabel")
#
#         self.submit_button = QtWidgets.QPushButton(self.centralwidget)
#         self.submit_button.setGeometry(QtCore.QRect(90, 450, 281, 111))
#         font = QtGui.QFont()
#         font.setFamily("Segoe MDL2 Assets")
#         font.setPointSize(26)
#         self.submit_button.setFont(font)
#         self.submit_button.setObjectName("submit_button")
#
#         self.label_appName = QtWidgets.QLabel(self.centralwidget)
#         self.label_appName.setGeometry(QtCore.QRect(370, 0, 261, 51))
#
#         self.label_refresh_time = QtWidgets.QLabel(self.centralwidget)
#         self.label_refresh_time.setGeometry(QtCore.QRect(410, 468, 131, 20))
#
#         self.label_account_type = QtWidgets.QLabel(self.centralwidget)
#         self.label_account_type.setGeometry(QtCore.QRect(411, 545, 151, 20))
#
#         self.clearWindow_button = QtWidgets.QPushButton(self.centralwidget)
#         self.clearWindow_button.setGeometry(QtCore.QRect(90, 635, 281, 111))
#         font = QtGui.QFont()
#         font.setFamily("Segoe MDL2 Assets")
#         font.setPointSize(26)
#         self.clearWindow_button.setFont(font)
#         self.clearWindow_button.setObjectName("clearWindow_button")
#
#         self.stop_button = QtWidgets.QPushButton(self.centralwidget)
#         self.stop_button.setGeometry(QtCore.QRect(90, 775, 281, 111))
#         font = QtGui.QFont()
#         font.setFamily("Segoe MDL2 Assets")
#         font.setPointSize(26)
#         self.stop_button.setFont(font)
#         self.stop_button.setObjectName("stop_button")
#
#         palette = QtGui.QPalette()
#         brush = QtGui.QBrush(QtGui.QColor(66, 72, 188))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(174, 196, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
#         brush = QtGui.QBrush(QtGui.QColor(119, 154, 247))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
#         brush = QtGui.QBrush(QtGui.QColor(43, 74, 160))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
#         brush = QtGui.QBrush(QtGui.QColor(160, 183, 247))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(66, 72, 188))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(174, 196, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
#         brush = QtGui.QBrush(QtGui.QColor(119, 154, 247))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
#         brush = QtGui.QBrush(QtGui.QColor(43, 74, 160))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
#         brush = QtGui.QBrush(QtGui.QColor(160, 183, 247))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
#         brush = QtGui.QBrush(QtGui.QColor(174, 196, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
#         brush = QtGui.QBrush(QtGui.QColor(119, 154, 247))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
#         brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
#         brush = QtGui.QBrush(QtGui.QColor(43, 74, 160))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
#         brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
#         brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
#
#         self.label_appName.setPalette(palette)
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(18)
#         font.setBold(False)
#         font.setWeight(50)
#
#         self.label_appName.setFont(font)
#         self.label_appName.setLayoutDirection(QtCore.Qt.RightToLeft)
#         self.label_appName.setObjectName("label_appName")
#         self.label_userFunctions = QtWidgets.QLabel(self.centralwidget)
#         self.label_userFunctions.setGeometry(QtCore.QRect(20, 90, 131, 31))
#
#         font = QtGui.QFont()
#         font.setFamily("Bahnschrift SemiBold")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#
#         self.label_userFunctions.setFont(font)
#         self.label_userFunctions.setObjectName("label_userFunctions")
#         self.admin_Functions = QtWidgets.QComboBox(self.centralwidget)
#         self.admin_Functions.setGeometry(QtCore.QRect(10, 130, 491, 140))
#
#         font = QtGui.QFont()
#         font.setFamily("Myanmar Text")
#         font.setPointSize(10)
#
#         self.admin_Functions.setFont(font)
#         self.admin_Functions.setObjectName("admin_Functions")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#         self.admin_Functions.addItem("")
#
#         self.output_info = QtWidgets.QTextBrowser(self.centralwidget)
#         self.output_info.setGeometry(QtCore.QRect(599, 120, 1050, 750))
#         self.output_info.setObjectName("output_info")
#         new_font = QtGui.QFont()
#         new_font.setFamily("Myanmar Text")
#         new_font.setPointSize(11)
#         self.output_info.setFont(new_font)
#         self.output_info.setOpenExternalLinks(True)
#         self.output_info.setAcceptRichText(True)
#         # self.output_info.setOpenLinks(True)
#         # self.output_info.setReadOnly(False)
#
#         self.input_player_id = QtWidgets.QLineEdit(self.centralwidget)
#         self.input_player_id.setGeometry(QtCore.QRect(10, 390, 113, 20))
#         self.input_player_id.setObjectName("input_player_id")
#
#         self.input_team_id = QtWidgets.QLineEdit(self.centralwidget)
#         self.input_team_id.setGeometry(QtCore.QRect(142, 390, 121, 20))
#         self.input_team_id.setObjectName("input_team_id")
#
#         self.input_match_id = QtWidgets.QLineEdit(self.centralwidget)
#         self.input_match_id.setGeometry(QtCore.QRect(280, 390, 113, 20))
#         self.input_match_id.setObjectName("input_match_id")
#
#         self.input_league_id = QtWidgets.QLineEdit(self.centralwidget)
#         self.input_league_id.setGeometry(QtCore.QRect(412, 390, 121, 20))
#         self.input_league_id.setObjectName("input_league_id")
#
#         self.input_refresh_time = QtWidgets.QLineEdit(self.centralwidget)
#         self.input_refresh_time.setGeometry(QtCore.QRect(412, 490, 121, 20))
#         self.input_refresh_time.setObjectName("input_refresh_time")
#
#         self.input_account_type = QtWidgets.QLineEdit(self.centralwidget)
#         self.input_account_type.setGeometry(QtCore.QRect(412, 567, 121, 20))
#         self.input_account_type.setObjectName("input_account_type")
#
#         self.label_player_id = QtWidgets.QLabel(self.centralwidget)
#         self.label_player_id.setGeometry(QtCore.QRect(10, 366, 111, 20))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_player_id.setFont(font)
#         self.label_player_id.setObjectName("label_player_id")
#
#         self.label_team_id = QtWidgets.QLabel(self.centralwidget)
#         self.label_team_id.setGeometry(QtCore.QRect(140, 366, 111, 20))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_team_id.setFont(font)
#         self.label_team_id.setObjectName("label_team_id")
#
#         self.label_match_id = QtWidgets.QLabel(self.centralwidget)
#         self.label_match_id.setGeometry(QtCore.QRect(280, 366, 111, 20))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_match_id.setFont(font)
#         self.label_match_id.setObjectName("label_match_id")
#
#         self.label_league_id = QtWidgets.QLabel(self.centralwidget)
#         self.label_league_id.setGeometry(QtCore.QRect(420, 366, 111, 20))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_league_id.setFont(font)
#         self.label_league_id.setObjectName("label_league_id")
#
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_account_type.setFont(font)
#         self.label_account_type.setObjectName("label_account_type")
#
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.label_refresh_time.setFont(font)
#         self.label_refresh_time.setObjectName("label_refresh_time")
#
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.progressLabel.setFont(font)
#         self.progressLabel.setText("Program status")
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 23))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         # ------------BUTTONS-----------------------------
#         self.submit_button.clicked.connect(self.pressed)
#         self.clearWindow_button.clicked.connect(self.clear)
#         self.stop_button.clicked.connect(self.stop_test_thread)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.submit_button.setText(_translate("MainWindow", "Submit"))
#         self.label_appName.setText(_translate("MainWindow", "Account Manager 1.0"))
#         self.label_userFunctions.setText(_translate("MainWindow", "Functions"))
#         self.admin_Functions.setItemText(0, _translate("MainWindow", "Player\'s accounts"))
#         self.admin_Functions.setItemText(1, _translate("MainWindow", "Player\'s profile"))
#         self.admin_Functions.setItemText(2, _translate("MainWindow", "Team\'s info"))
#         self.admin_Functions.setItemText(3, _translate("MainWindow", "All team members\' info"))
#         self.admin_Functions.setItemText(4, _translate("MainWindow",
#                                                        "Only ID, nickname, gameaccount and region in team members\' profiles"))
#         self.admin_Functions.setItemText(5, _translate("MainWindow", "General match info"))
#         self.admin_Functions.setItemText(6, _translate("MainWindow", "Contestants\' (2 teams) profiles"))
#         self.admin_Functions.setItemText(7, _translate("MainWindow", "Contestants members\' profiles"))
#         self.admin_Functions.setItemText(8, _translate("MainWindow", "Date and duration of the match"))
#         self.admin_Functions.setItemText(9, _translate("MainWindow", "Match status and result if it is closed"))
#         self.admin_Functions.setItemText(10, _translate("MainWindow", "Match media"))
#         self.admin_Functions.setItemText(11, _translate("MainWindow", "Full league info"))
#         self.admin_Functions.setItemText(12, _translate("MainWindow", "League results"))
#         self.admin_Functions.setItemText(13,
#                                          _translate("MainWindow", "All contestants, participating in the tournament"))
#         self.admin_Functions.setItemText(14, _translate("MainWindow",
#                                                         "Info about all players, participating in the tournament (takes a lot of time)"))
#         self.admin_Functions.setItemText(15,
#                                          _translate("MainWindow", "All matches IDs and players\' gameaccounts there"))
#         self.admin_Functions.setItemText(16, _translate("MainWindow", "Check open protests"))
#         self.admin_Functions.setItemText(17, _translate("MainWindow",
#                                                         "AUTO_ADMIN - program will check tickets automatically in a certain period of time"))
#         self.admin_Functions.setItemText(18, _translate("MainWindow",
#                                                         "All members, who doesn\'t have specific gameaccounts (e.g. \'uplay\', \'psn\' or \'xbox accounts\'), or members who have barrage"))
#         # self.output_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#         # "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#         # "p, li { white-space: pre-wrap; }\n"
#         # "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
#         # "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.15094pt;\"><br /></p></body></html>"))
#         self.label_player_id.setText(_translate("MainWindow", "Enter Player ID"))
#         self.label_team_id.setText(_translate("MainWindow", "Enter Team ID"))
#         self.label_match_id.setText(_translate("MainWindow", "Enter Match ID"))
#         self.label_league_id.setText(_translate("MainWindow", "Enter League ID"))
#         self.label_refresh_time.setText(_translate("MainWindow", "Enter Refresh time"))
#         self.label_account_type.setText(_translate("MainWindow", "Enter Account type"))
#         self.clearWindow_button.setText(_translate("MainWindow", "Clear window"))
#         self.stop_button.setText(_translate("MainWindow", "Stop"))
#         self.stop_button.setEnabled(False)
#
#     def clear(self):
#         self.output_info.clear()
#
#     def stop_test_thread(self):
#         """Stops main thread"""
#         for task in self.threads:
#             task.terminate_thread()
#         self.output_info.append("<div>Task is finished</div>")
#
#     # ----------MAIN PART-----------
#
#     def pressed(self):
#         """ 'Key pressed' event """
#         choice = str(self.admin_Functions.currentText())
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#
#         self.threads = []
#         task = self.admin_Functions.currentIndex()
#         backend_thread = main_page.data_modules.worker_thread.BackendQThread(self, task)
#         backend_thread.start()
#         self.stop_button.setEnabled(True)
#         self.threads.append(backend_thread)
#
#         self.output_info.moveCursor(self.output_info.textCursor().Start)
#
#
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
#
# thread_manager = Ui_MainWindow()
#
# import main_page.data_modules.worker_thread

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import settings_page.settings_page
import email_handler


nickname = email_handler.get_nickname(email_handler.get_file_info())


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.threads = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1700, 920)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(160, 580, 141, 31))
        self.progressLabel.setObjectName("progressLabel")

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(90, 450, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(26)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")

        self.change_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_button.setGeometry(QtCore.QRect(1350, 5, 300, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(26)
        self.change_button.setFont(font)
        self.change_button.setObjectName("change_button")

        self.label_appName = QtWidgets.QLabel(self.centralwidget)
        self.label_appName.setGeometry(QtCore.QRect(370, 0, 261, 51))

        self.label_greeting = QtWidgets.QLabel(self.centralwidget)
        self.label_greeting.setGeometry(QtCore.QRect(340, 50, 635, 51))

        self.label_refresh_time = QtWidgets.QLabel(self.centralwidget)
        self.label_refresh_time.setGeometry(QtCore.QRect(410, 468, 131, 20))

        self.label_account_type = QtWidgets.QLabel(self.centralwidget)
        self.label_account_type.setGeometry(QtCore.QRect(411, 545, 151, 20))

        self.clearWindow_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearWindow_button.setGeometry(QtCore.QRect(90, 635, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(26)
        self.clearWindow_button.setFont(font)
        self.clearWindow_button.setObjectName("clearWindow_button")

        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(90, 775, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(26)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(66, 72, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 196, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 154, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 74, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 183, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 72, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 196, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 154, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 74, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 183, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 196, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 154, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 74, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 56, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 112, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        self.label_appName.setPalette(palette)
        self.label_greeting.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.label_appName.setFont(font)
        self.label_appName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_appName.setObjectName("label_appName")

        self.label_greeting.setFont(font)
        self.label_greeting.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_greeting.setObjectName("label_greeting")

        self.label_userFunctions = QtWidgets.QLabel(self.centralwidget)
        self.label_userFunctions.setGeometry(QtCore.QRect(20, 90, 131, 31))

        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_userFunctions.setFont(font)
        self.label_userFunctions.setObjectName("label_userFunctions")
        self.admin_Functions = QtWidgets.QComboBox(self.centralwidget)
        self.admin_Functions.setGeometry(QtCore.QRect(10, 130, 491, 140))

        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)

        self.admin_Functions.setFont(font)
        self.admin_Functions.setObjectName("admin_Functions")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")  # Get info about all players in the league
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        # self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        # self.admin_Functions.addItem("")  # get barraged players

        self.output_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_info.setGeometry(QtCore.QRect(599, 120, 1050, 750))
        self.output_info.setObjectName("output_info")
        new_font = QtGui.QFont()
        new_font.setFamily("Myanmar Text")
        new_font.setPointSize(11)
        self.output_info.setFont(new_font)
        self.output_info.setOpenExternalLinks(True)
        self.output_info.setAcceptRichText(True)

        self.input_player_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_player_id.setGeometry(QtCore.QRect(10, 390, 113, 20))
        self.input_player_id.setObjectName("input_player_id")

        self.input_team_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_team_id.setGeometry(QtCore.QRect(142, 390, 121, 20))
        self.input_team_id.setObjectName("input_team_id")

        self.input_match_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_match_id.setGeometry(QtCore.QRect(280, 390, 113, 20))
        self.input_match_id.setObjectName("input_match_id")

        self.input_league_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_league_id.setGeometry(QtCore.QRect(412, 390, 121, 20))
        self.input_league_id.setObjectName("input_league_id")

        self.input_refresh_time = QtWidgets.QLineEdit(self.centralwidget)
        self.input_refresh_time.setGeometry(QtCore.QRect(412, 490, 121, 20))
        self.input_refresh_time.setObjectName("input_refresh_time")

        self.input_account_type = QtWidgets.QLineEdit(self.centralwidget)
        self.input_account_type.setGeometry(QtCore.QRect(412, 567, 121, 20))
        self.input_account_type.setObjectName("input_account_type")

        self.label_player_id = QtWidgets.QLabel(self.centralwidget)
        self.label_player_id.setGeometry(QtCore.QRect(10, 366, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_player_id.setFont(font)
        self.label_player_id.setObjectName("label_player_id")

        self.label_team_id = QtWidgets.QLabel(self.centralwidget)
        self.label_team_id.setGeometry(QtCore.QRect(140, 366, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_team_id.setFont(font)
        self.label_team_id.setObjectName("label_team_id")

        self.label_match_id = QtWidgets.QLabel(self.centralwidget)
        self.label_match_id.setGeometry(QtCore.QRect(280, 366, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_match_id.setFont(font)
        self.label_match_id.setObjectName("label_match_id")

        self.label_league_id = QtWidgets.QLabel(self.centralwidget)
        self.label_league_id.setGeometry(QtCore.QRect(420, 366, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_league_id.setFont(font)
        self.label_league_id.setObjectName("label_league_id")

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_account_type.setFont(font)
        self.label_account_type.setObjectName("label_account_type")

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_refresh_time.setFont(font)
        self.label_refresh_time.setObjectName("label_refresh_time")

        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressLabel.setFont(font)
        self.progressLabel.setText("Program status")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ------------BUTTONS-----------------------------
        self.submit_button.clicked.connect(self.pressed)
        self.clearWindow_button.clicked.connect(self.clear)
        self.stop_button.clicked.connect(self.stop_thread)
        self.change_button.clicked.connect(self.change_settings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Account Manager"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.label_appName.setText(_translate("MainWindow", "Account Manager"))
        self.label_greeting.setText(_translate("MainWindow", "Welcome back, %s !" % nickname))
        self.label_userFunctions.setText(_translate("MainWindow", "Functions"))
        self.admin_Functions.setItemText(0, _translate("MainWindow", "Get Player\'s accounts"))
        self.admin_Functions.setItemText(1, _translate("MainWindow", "View Player\'s profile"))
        self.admin_Functions.setItemText(2, _translate("MainWindow", "Get Team\'s info"))
        self.admin_Functions.setItemText(3, _translate("MainWindow", "View all team members\' profiles"))
        self.admin_Functions.setItemText(4, _translate("MainWindow",
                                                       "Get team members' ID, nickname, gameaccount and region"))
        self.admin_Functions.setItemText(5, _translate("MainWindow", "View general Match info"))  # TODO: Remove(?) - 1
        self.admin_Functions.setItemText(6, _translate("MainWindow", "Get Contestants\' (2 teams) profiles"))
        self.admin_Functions.setItemText(7, _translate("MainWindow", "Get Contestants members\' profiles"))
        self.admin_Functions.setItemText(8, _translate("MainWindow", "Get Date and duration of the match"))
        self.admin_Functions.setItemText(9, _translate("MainWindow", "Get Match status and result if it is closed"))
        self.admin_Functions.setItemText(10, _translate("MainWindow", "Get Match media"))
        self.admin_Functions.setItemText(11, _translate("MainWindow", "View Full league info"))  # TODO: Remove(?) - 2
        self.admin_Functions.setItemText(12, _translate("MainWindow", "Get League results"))
        self.admin_Functions.setItemText(13,
                                         _translate("MainWindow",
                                                    "View All contestants, participating in the tournament"))
        # 3self.admin_Functions.setItemText(14, _translate("MainWindow",
                                                        # "Get Info about all players, participating in the tournament"))
        self.admin_Functions.setItemText(14,
                                         _translate("MainWindow", "Get All matches IDs and players\' gameaccounts there"))
        self.admin_Functions.setItemText(15, _translate("MainWindow", "Check open protests"))
        self.admin_Functions.setItemText(16, _translate("MainWindow",
                                                        "Auto Admin - program will search for new tickets automatically"))
        # self.admin_Functions.setItemText(18, _translate("MainWindow",
        #                                                 "Get barraged members or members without gameaccount"))
        self.label_player_id.setText(_translate("MainWindow", "Enter Player ID"))
        self.label_team_id.setText(_translate("MainWindow", "Enter Team ID"))
        self.label_match_id.setText(_translate("MainWindow", "Enter Match ID"))
        self.label_league_id.setText(_translate("MainWindow", "Enter League ID"))
        self.label_refresh_time.setText(_translate("MainWindow", "Enter Refresh time"))
        self.label_account_type.setText(_translate("MainWindow", "Enter Account type"))
        self.clearWindow_button.setText(_translate("MainWindow", "Clear window"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.change_button.setText(_translate("MainWindow", "Settings"))
        self.stop_button.setEnabled(False)

    def clear(self):
        self.output_info.clear()

    def stop_thread(self):
        """Stops main thread"""
        for task in self.threads:
            task.terminate_thread()
        self.output_info.append("<div>Task is finished</div>")

    # ----------MAIN PART-----------

    def pressed(self):
        """ 'Key pressed' event """
        choice = str(self.admin_Functions.currentText())
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

        self.threads = []
        task = self.admin_Functions.currentIndex()
        backend_thread = main_page.data_modules.worker_thread.BackendQThread(self, task)
        backend_thread.start()
        self.stop_button.setEnabled(True)
        self.threads.append(backend_thread)

        self.output_info.moveCursor(self.output_info.textCursor().Start)

    def change_settings(self):

        # TEST DATA
        # file = open("setup_info.txt", 'r')
        # data = file.read()
        # print('Main: ', data)
        # print()

        settingsPage = settings_page.settings_page.settings_page
        settingsPage.show()


thread_manager = Ui_MainWindow()


MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


def main():
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow.show()
    sys.exit(app.exec_())


def get_main_page():
    main_page = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_page)
    return main_page


import main_page.data_modules.worker_thread


if __name__ == "__main__":
    main()