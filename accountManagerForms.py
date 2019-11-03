# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import requests
import json
from datetime import datetime
import time
import random
import os
import winsound
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit



class League:
    def __init__(self, league_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/leagues/'
        self.league_id = str(league_id)

    def get_league_description(self):  # full league description
        r = requests.get(self.base_url + self.league_id)
        response = json.loads(r.text)
        return response

    def get_league_results(self):  # get league results
        r = requests.get(self.base_url + self.league_id + "/results")
        response = json.loads(r.text)
        results = []
        for match_info in response:
            match_id = match_info['id']
            match = Match(match_id)
            if match.get_match_status() == "closed":
                result = match.get_match_results()
                results.append(result)
            else:
                team_a_id = match.get_match_info()['contestants'][0]['team']['id']
                team_a_name = match.get_match_info()['contestants'][0]['team']['name']
                team_b_id = match.get_match_info()['contestants'][1]['team']['id']
                team_b_name = match.get_match_info()['contestants'][1]['team']['name']
                result = "Match is still open - match id: {0}\n{1}; team ID: {2}\n{3}; team ID: {4}".format(match_id, team_a_name, team_a_id, team_b_name, team_b_id)
                results.append(result)
        return results

    def get_league_contestants(self): # get all contestants in the tournament
        r = requests.get(self.base_url + self.league_id + "/contestants")
        response = json.loads(r.text)
        return response

    # have to think about optimisation
    def get_league_members_info(self):
        r = requests.get(self.base_url + self.league_id + "/contestants")
        response = json.loads(r.text)
        league_members_info = []
        for contestant in response:
            team = Team(contestant['id'])
            league_members_info.append(team.get_useful_members_info())
        return league_members_info

    def get_matches_and_players(self):
        r = requests.get(self.base_url + self.league_id + "/matches")
        response = json.loads(r.text)
        gameaccounts = []
        for match in response:
            match_id = match['id']
            match_id_dict = {"match id": match_id}
            gameaccounts_dict = match['gameaccounts']
            match_id_dict.update(gameaccounts_dict)
            gameaccounts.append(match_id_dict)
        return gameaccounts

    def check_tickets(self):
        r = requests.get(self.base_url + self.league_id + "/matches")
        response = json.loads(r.text)
        tickets_amount = 0
        protests = []
        matches_id = []
        for match in response:
            match_status = match['status']
            if match_status == "protest":
                tickets_amount += 1
                match_id = match['id']
                team_a_id = match['contestants'][0]['team']['id']
                team_a_name = match['contestants'][0]['team']['name']
                team_b_id = match['contestants'][1]['team']['id']
                team_b_name = match['contestants'][1]['team']['name']
                new_r = requests.get(self.base_url + self.league_id)
                new_response = json.loads(new_r.text)
                league_name = new_response['uri']
                base_link = "https://play.eslgaming.com"
                match_link = "match/" + str(match_id) + "/"
                protest_link = "admin_tickets/all/"
                admin_protests_link = base_link + league_name + protest_link
                match_protest_link = base_link + league_name + match_link
                protest_dict = {"ticket number": tickets_amount,"match_id": match_id, team_a_id: team_a_name, team_b_id: team_b_name, "Check your tickets": admin_protests_link, "Check match": match_protest_link}
                protests.append(protest_dict)
                matches_id.append(match_id)
            else:
                continue
        return protests, tickets_amount, matches_id



class Match:
    def __init__(self, match_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.match_id = str(match_id)

    def get_match_info(self):  # all match info
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            return response

    def get_contestants_profile(self):  # 2 teams' profiles
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            test_match = Match(self.match_id)
            contestants_profiles = []
            for key, value in test_match.get_match_info().items():
                if key == "contestants":
                    contestants = value
                    for i in range(len(contestants)):
                        contestant = Team(contestants[i]['team']['id'])
                        contestants_profiles.append(contestant.get_team_info())
            return contestants_profiles

    def get_contestants_members_info(self):#players' useful info
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            test_match = Match(self.match_id)
            members_info = []
            players_id = []
            i = 0
            for key, value in test_match.get_match_info().items():
                if key == "gameaccounts":
                    players = value
                    for key_player, value_player in players.items():
                        new_member = User(key_player)
                        members_info.append(new_member.get_useful_info())
            return members_info

    def get_match_date_time(self):
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        status = response['status']
        if is_error(response):
            return "error"
        else:
            if status == "closed":
                start_date_string = response['beginAt']
                end_date_string = response['calculatedAt']

                start_date = start_date_string[:10]
                start_time = start_date_string[11:19]
                start = start_date + ' ' + start_time
                beginning_date = datetime.strptime(start, "%Y-%m-%d %H:%M:%S") #!!!

                end_date = end_date_string[:10]
                end_time = end_date_string[11:19]
                end = end_date + ' ' + end_time
                final_date = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") # !!!

                delta = final_date - beginning_date
                match_time = {"Start time": start, "End time": end, "Duration of the match": delta}
                return match_time
            else:
                return "open"

    def get_match_results(self):
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            test_match = Match(self.match_id)
            #teams_count = test_match.get_contestants_profile()
            result_argument = response['result']['score']
            results = result_argument

            teams = list(results.keys())
            scores = list(results.values())
            winners = teams[0]
            losers = teams[1]
            result = ""
            for i in range(2):
                if scores[0] > scores[1]:
                    winners = teams[0]
                    losers = teams[1]
                elif scores[1] > scores[0]:
                    winners = teams[1]
                    losers = teams[0]
                else:
                    result = "draw"

            team_win = Team(winners)
            team_lose = Team(losers)
            team_win_id = ""
            team_win_name = ""
            team_lose_id = ""
            team_lose_name = ""
            if team_win.get_team_info() == "error":
                team_win_id = "id: " + winners
                team_win_name = "'" + "Deleted account" + "'"
                team_lose_id = "id: " + losers
                team_lose_name = "'" + team_lose.get_team_info()['name'] + "'"
            if team_lose.get_team_info() == "error":
                team_lose_id = "id: " + losers
                team_lose_name = "'" + "Deleted account" + "'"
                team_win_id = "id: " + winners
                team_win_name = "'" + team_win.get_team_info()['name'] + "'"
            else:
                team_win_id = "id: " + winners
                team_win_name = "'" + team_win.get_team_info()['name'] + "'"
                team_lose_id = "id: " + losers
                team_lose_name = "'" + team_lose.get_team_info()['name'] + "'"
            if result != "draw":
                return "{0} has won! {1}\n{2} has lost. {3}".format(team_win_name, team_win_id, team_lose_name, team_lose_id)
            else:
                return "The result is draw\n{0}: {1}\n{2}: {3}".format(team_win_name, team_win_id, team_lose_name, team_lose_id)

    def get_match_media(self):
        r = requests.get(self.base_url + "/matches/" + self.match_id + "/media")
        response = json.loads(r.text)
        new_r = requests.get(self.base_url + "/matches/" + self.match_id)
        new_response = json.loads(new_r.text)
        status = new_response['status']
        files = []
        if status == "closed":
            for i in range(len(response)):
                files.append(response[i]['filename'])
            return files
        else:
            return "open"

    def get_match_status(self):
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            status = response['status']
            return status



class Team:
    def __init__(self, team_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.team_id = str(team_id)

    def get_team_info(self):
        r = requests.get(self.base_url + "/teams/" + self.team_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            return response

    def get_team_members_info(self):
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            members_info = []
            for player in response:
                member = User(player)
                members_info.append(member.get_profile())
            return members_info

    def get_team_members_accounts(self):
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            members_accounts = []
            for player in response:
                member = User(player)
                members_accounts.append(member.get_accounts())
            return members_accounts

    def get_useful_members_info(self):
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        members_useful_info = []
        for player in response:
            member = User(player)
            members_useful_info.append(member.get_useful_info())
        return members_useful_info



class User:
    def __init__(self, id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.id = str(id)


    def get_profile(self):  # user profile info
        r = requests.get(self.base_url + "/users/" + self.id + "/basicprofile")
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            return response


    def get_accounts(self):#gameaccounts in user's profile
        r = requests.get(self.base_url + "/users/" + self.id + "/gameaccounts")
        response = json.loads(r.text)
        if len(response) == 0:
            return "User doesn't have any accounts in his profile"
        else:
            account_type = ''
            account_nickname = ''
            account = ''
            accounts = ''
            for i in range(len(response)):
                dict = response[i]
                #account_count = str(i+1) + ')'
                if dict['type'] == "psn_online_id":
                    account_type = "PSN account: "
                    account_nickname = dict['value']
                elif dict['type'] == "uplay_nick":
                    account_type = "Uplay: "
                    account_nickname = dict['value']
                elif dict['type'] == "xbox_account":
                    account_type = "Xbox nickname: "
                    account_nickname = dict['value']
                else:
                    account_nickname = "GameAccount in another game"
                if account_nickname == "GameAccount in another game":
                    continue
                else:
                    account += account_type + "'" + account_nickname + "'" + ' '
            accounts += account
            return accounts

    def get_useful_info(self):  # useful parameters are: 'id', 'nickname', 'gameaccount', 'region', 'isBarred'
        r = requests.get(self.base_url + "/users/" + self.id + "/basicprofile")
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            new_user = User(self.id)
            user_accounts = new_user.get_accounts()
            new_dict = {"gameaccounts":  user_accounts, "id": response.get("id"), "nickname": response.get("nickname"), "region": response.get("region")}
            isBarred = response.get("isBarred")
            if isBarred == False:
                new_dict['isBarred'] = False
            else:
                new_dict['isBarred'] = True
                new_dict['barredUntil'] = response.get('barredUntil')
            return new_dict

    def get_special_account(self, option):#special account --> e.g "psn_online_id"
        r = requests.get(self.base_url + "/users/" + self.id + "/gameaccounts")
        response = json.loads(r.text)
        for i in range(len(response)):
            dict = response[i]
            if dict['type'] == option:
                return dict['value']



  # FUCNTIONS
def check_accounts(users, account_type):#doesn't work properly ATM
    similar_accounts_count = 0
    nicknames = []
    same_accounts = []
    for i in range(len(users)):
        nicknames.append(users[i].get_special_account(account_type))
    same_accounts = [i for i, x in enumerate(nicknames) if nicknames.count(x) > 1]
    similar_accounts_count = len(same_accounts)
    if len(same_accounts) > 0:
         for j in range(len(same_accounts)):
             return users[same_accounts[i]].get_special_account("nickname")
    else:
        return None

def check_input(user_input, info):
    if user_input not in info:
        return False
    else:
        return True

def check_date(date):
    if date[0] == "0":
        return date[1]
    else:
        return date

def get_duration_period(date):

    now = datetime.now()

    end_date = date[:10]
    end_time = date[11:19]
    end = end_date + ' ' + end_time
    final_date = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")  # !!!

    delta = final_date - now
    return delta

def is_error(dict):
    if "error" in dict.keys():
        return True
    else:
        return False

def beep():
    duration = 1750  # millisecond
    freq = 2500  # Hz OR 2500 Hz
    return winsound.Beep(freq, duration)



  # USER INTERFACE
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1700, 920)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(160, 580, 141, 31))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(90, 450, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(26)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")

        self.label_appName = QtWidgets.QLabel(self.centralwidget)
        self.label_appName.setGeometry(QtCore.QRect(370, 0, 261, 51))

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
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
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
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
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
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        self.label_appName.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.label_appName.setFont(font)
        self.label_appName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_appName.setObjectName("label_appName")
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
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")
        self.admin_Functions.addItem("")

        self.output_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_info.setGeometry(QtCore.QRect(599, 120, 1050, 750))
        self.output_info.setObjectName("output_info")
        new_font = QtGui.QFont()
        new_font.setFamily("Myanmar Text")
        new_font.setPointSize(11)
        self.output_info.setFont(new_font)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit_button.clicked.connect(self.pressed)
        self.clearWindow_button.clicked.connect(self.clear)
        self.stop_button.clicked.connect(self.stop_loop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.working = True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.label_appName.setText(_translate("MainWindow", "Account Manager 1.0"))
        self.label_userFunctions.setText(_translate("MainWindow", "Functions"))
        self.admin_Functions.setItemText(0, _translate("MainWindow", "Player\'s accounts"))
        self.admin_Functions.setItemText(1, _translate("MainWindow", "Player\'s profile"))
        self.admin_Functions.setItemText(2, _translate("MainWindow", "Team\'s info"))
        self.admin_Functions.setItemText(3, _translate("MainWindow", "All team members\' info"))
        self.admin_Functions.setItemText(4, _translate("MainWindow", "Only ID, nickname, gameaccount and region in team members\' profiles"))
        self.admin_Functions.setItemText(5, _translate("MainWindow", "General match info"))
        self.admin_Functions.setItemText(6, _translate("MainWindow", "Contestants\' (2 teams) profiles"))
        self.admin_Functions.setItemText(7, _translate("MainWindow", "Contestants members\' profiles"))
        self.admin_Functions.setItemText(8, _translate("MainWindow", "Date and duration of the match"))
        self.admin_Functions.setItemText(9, _translate("MainWindow", "Match status and result if it is closed"))
        self.admin_Functions.setItemText(10, _translate("MainWindow", "Match media"))
        self.admin_Functions.setItemText(11, _translate("MainWindow", "Full league info"))
        self.admin_Functions.setItemText(12, _translate("MainWindow", "League results"))
        self.admin_Functions.setItemText(13, _translate("MainWindow", "All contestants, participating in the tournament"))
        self.admin_Functions.setItemText(14, _translate("MainWindow", "Info about all players, participating in the tournament (takes a lot of time)"))
        self.admin_Functions.setItemText(15, _translate("MainWindow", "All matches IDs and players\' gameaccounts there"))
        self.admin_Functions.setItemText(16, _translate("MainWindow", "Check open protests"))
        self.admin_Functions.setItemText(17, _translate("MainWindow", "AUTO_ADMIN - program will check tickets automatically in a certain period of time"))
        self.admin_Functions.setItemText(18, _translate("MainWindow", "All members, who doesn\'t have specific gameaccounts (e.g. \'uplay\', \'psn\' or \'xbox accounts\'), or members who have barrage"))
        self.output_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.15094pt;\"><br /></p></body></html>"))
        self.label_player_id.setText(_translate("MainWindow", "Enter Player ID"))
        self.label_team_id.setText(_translate("MainWindow", "Enter Team ID"))
        self.label_match_id.setText(_translate("MainWindow", "Enter Match ID"))
        self.label_league_id.setText(_translate("MainWindow", "Enter League ID"))
        self.label_refresh_time.setText(_translate("MainWindow", "Enter Refresh time"))
        self.label_account_type.setText(_translate("MainWindow", "Enter Account type"))
        self.clearWindow_button.setText(_translate("MainWindow", "Clear window"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))

    def clear(self):
        self.output_info.clear()
        self.working = True

    def refresh_text_box(self, text):
        self.output_info.append(text)
        QtGui.QGuiApplication.processEvents()

    def stop_loop(self):
        self.working = False

    def pressed(self):
        choice = str(self.admin_Functions.currentText())
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

        # USER FUNCTIONS
        if choice == "Player's accounts":
            id = self.input_player_id.text()
            if id == "":
                self.output_info.append("\nERROR: 'Enter player ID' ")
            else:
                test_user = User(id)
                self.output_info.setText("\n" + test_user.get_accounts())

        elif choice == "Player's profile":
            id = self.input_player_id.text()
            if id == "":
                self.output_info.append("\nERROR: 'Enter player ID' ")
            else:
                test_user = User(id)
                user_profile = test_user.get_profile()
                text = ""
                for key, value in user_profile.items():
                    text += "{0}: {1}".format(key, value) + "\n"
                self.output_info.setText("\n" + text)


        # TEAM FUNCTIONS
        elif choice == "Team's info":
            team_id = self.input_team_id.text()
            if team_id == "":
                self.output_info.append("\nERROR: 'Enter team ID' ")
            else:
                text = ""
                test_team = Team(team_id)
                for key, value in test_team.get_team_info().items():
                    text += "{0}: {1}".format(key, value) + "\n"
                self.output_info.setText("\n" + text)

        elif choice == "All team members' info":
            team_id = self.input_team_id.text()
            if team_id == "":
                self.output_info.append("\nERROR: 'Enter team ID' ")
            else:
                test_team = Team(team_id)
                members_info = test_team.get_team_members_info()
                text = ""
                for i in range(len(members_info)):
                    for key, value in members_info[i].items():
                        text += "{0}: {1}".format(key, value) + "\n"
                    text += "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Only ID, nickname, gameaccount and region in team members' profiles":
            team_id = self.input_team_id.text()
            if team_id == "":
                self.output_info.append("\nERROR: 'Enter team ID' ")
            else:
                test_team = Team(team_id)
                members_info = test_team.get_team_members_info()
                options = ["id", "nickname", "region"]
                i = 0
                members_accounts = test_team.get_team_members_accounts()
                text = ""
                for member in members_info:
                    member_id = member['id']
                    team_member = User(member_id)
                    text += members_accounts[i] + "\n"
                    for key, value in team_member.get_profile().items():
                        if check_input(key, options):
                            text += "{0}: {1}".format(key, value) + "\n"
                        else:
                            continue
                    i += 1
                    text += "\n"
                self.output_info.setText("\n" + text)


        # MATCH FUNCTIONS
        elif choice == "General match info":
            match_id = self.input_match_id.text()
            if match_id == "":
                self.output_info.append("\nERROR: 'Enter match ID' ")
            else:
                test_match = Match(match_id)
                text = ""
                for key, value in test_match.get_match_info().items():
                    if key == "contestants":
                        contestants = value
                    text += "{0}: {1}".format(key, value) + "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Contestants' (2 teams) profiles":
            match_id = self.input_match_id.text()
            if match_id == "":
                self.output_info.append("\nERROR: 'Enter match ID' ")
            else:
                test_match = Match(match_id)
                teams_profiles = test_match.get_contestants_profile()
                text = ""
                for i in range(len(teams_profiles)):
                    for key, value in teams_profiles[i].items():
                        text += "{0}: {1}".format(key, value) + "\n"
                    text += "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Contestants members' profiles":
            match_id = self.input_match_id.text()
            if match_id == "":
                self.output_info.append("\nERROR: 'Enter match ID' ")
            else:
                test_match = Match(match_id)
                contestants_info = test_match.get_contestants_members_info()
                text = ""
                for i in range(len(contestants_info)):
                    for key, value in contestants_info[i].items():
                        text += "{0}: {1}".format(key, value) + "\n"
                    text += "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Date and duration of the match":
            match_id = self.input_match_id.text()
            if match_id == "":
                self.output_info.append("\nERROR: 'Enter match ID' ")
            else:
                test_match = Match(match_id)
                date = test_match.get_match_date_time()
                text = ""
                if date == "open":
                    text += "Match isn't closed yet" + "\n"
                else:
                    for key, value in date.items():
                        text += "{0}: {1}".format(key, value) + "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Match status and result if it is closed":
            match_id = self.input_match_id.text()
            if match_id == "":
                self.output_info.append("\nERROR: 'Enter match ID' ")
            else:
                test_match = Match(match_id)
                match_status = test_match.get_match_status()
                text = ""
                text += "match_status: {0}".format(match_status) + "\n"
                if match_status == "closed":
                    text += test_match.get_match_results() + "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Match media":
            match_id = self.input_match_id.text()
            if match_id == "":
                self.output_info.append("\nERROR: 'Enter match ID' ")
            else:
                test_match = Match(match_id)
                match_results = test_match.get_match_media()
                text = ""
                if match_results == "open":
                    text += "Match is still open, there is no match media yet" + "\n"
                elif match_results == "nothing":
                    text += "There is no match media in this match" + "\n"
                else:
                    tournament_condition = False
                    if len(match_results) == 10:
                        tournament_condition = True
                    for i in range(len(match_results)):
                        text += "file №{0}:\n {1}".format(i + 1, match_results[i]) + "\n"
                self.output_info.setText("\n" + text)


        # LEAGUE FUNCTIONS
        elif choice == "Full league info":
            league_id = self.input_league_id.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                test_league = League(league_id)
                league_description = test_league.get_league_description()
                text = ""
                for key, value in league_description.items():
                    text += "{0}: {1}".format(key, value) + "\n"
                self.output_info.setText("\n" + text)

        elif choice == "League results":
            league_id = self.input_league_id.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                test_league = League(league_id)
                league_results = test_league.get_league_results()
                text = ""
                for result in league_results:
                    text += "\n{0}".format(result) + "\n"
                self.output_info.setText("\n" + text)

        elif choice == "All contestants, participating in the tournament":
            league_id = self.input_league_id.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                test_league = League(league_id)
                league_contestants = test_league.get_league_contestants()
                text = ""
                for contestant in league_contestants:
                    for key, value in contestant.items():
                        if key != "alias" and key != "status":
                            text += "{0}: {1}".format(key, value) + "\n"
                    text += "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Info about all players, participating in the tournament (takes a lot of time)":
            league_id = self.input_league_id.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                text = ""
                text += "\n"
                test_league = League(league_id)
                if test_league.get_league_mode() == "1on1":
                    for player in test_league.get_league_members_info():
                        if player == "error":
                            text +=  "Account is deleted" + "\n"
                        else:
                            for key, value in player.items():
                                text += "{0}: {1}".format(key, value) + "\n"
                            text += "\n"
                else:
                    for team in test_league.get_league_members_info():
                        for player in team:
                            if player == "error":
                                text += "Account is deleted" + "\n"
                            else:
                                for key, value in player.items():
                                    text += "{0}: {1}".format(key, value) + "\n"
                                text += "\n"
                self.output_info.setText("\n" + text)

        elif choice == "All matches IDs and players' gameaccounts there":
            league_id = self.input_league_id.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                test_league = League(league_id)
                matches = test_league.get_matches_and_players()
                text = ""
                for match in matches:
                    for key, value in match.items():
                        text += "{0}: {1}".format(key, value) + "\n"
                    text += "\n"
                self.output_info.setText("\n" + text)

        elif choice == "Check open protests":
            league_id = self.input_league_id.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                test_league = League(league_id)
                protests = test_league.check_tickets()[0]
                total_protests_amount = test_league.check_tickets()[1]
                text = ""
                text += "Total amount of opened tickets: {0}".format(total_protests_amount) + "\n"
                for protest in protests:
                    for key, value in protest.items():
                        text += "{0}: {1}".format(key, value) + "\n"
                    beep()
                    text += "\n"
                self.output_info.setText("\n" + text)

        elif choice == "AUTO_ADMIN - program will check tickets automatically in a certain period of time":
            league_id = self.input_league_id.text()
            refresh_time = self.input_refresh_time.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                if refresh_time == "":
                    self.output_info.append("\nERROR: 'Enter  'refresh time', so in how many minutes you want program to refresh, e.g '5' means, data will refresh each 5 minutes' ")
                else:
                    text = ""
                    text += "\n"
                    refresh_time_seconds = float(refresh_time) * 60
                    my_file = open("matches_ids.txt", "w")
                    my_file.write("")
                    my_file.close()
                    while True:
                        test_league = League(league_id)
                        protests = test_league.check_tickets()[0]
                        total_protests_amount = test_league.check_tickets()[1]
                        text += "Total amount of opened tickets: {0}".format(total_protests_amount) + "\n"
                        for protest in protests:
                            for key, value in protest.items():
                                text += "{0}: {1}".format(key, value) + "\n"
                            text += "\n"
                        Ui_MainWindow.refresh_text_box(self, text)
                        text = ""

                        values_from_file = []
                        matches_id = test_league.check_tickets()[2]
                        same_matches_id = []
                        with open('matches_ids.txt', 'r') as f:
                            values_from_file = f.read().splitlines()
                        values_from_file = [int(item) for item in values_from_file]
                        same_matches_id = list(set(values_from_file) & set(matches_id))
                        sounds_amount = len(matches_id) - len(same_matches_id)
                        if sounds_amount > 0:
                            for i in range(sounds_amount):
                                beep()
                        my_file = open("matches_ids.txt", "a")
                        for id in matches_id:
                            if id not in values_from_file:
                                my_file.write("{0}\n".format(id))
                        my_file.close()
                        time.sleep(refresh_time_seconds)
                        if self.working == False:
                            break

        elif choice == "All members, who doesn't have specific gameaccounts (e.g. 'uplay', 'psn' or 'xbox accounts'), or members who have barrage":
            league_id = self.input_league_id.text()
            if league_id == "":
                self.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                account_types = ["Uplay:", "PSN account:", "Xbox nickname:"]
                platform_type = self.input_account_type.text()
                if platform_type == "":
                    self.output_info.append("ERROR: 'Enter account type' ")
                else:
                    if platform_type not in account_types:
                        self.output_info.append("ERROR: 'Please, use only 'Uplay:', 'PSN account:' or 'Xbox nickname:' ")
                    else:
                        text = ""
                        if check_input(platform_type, account_types):

                            test_league = League(league_id)
                            for team in test_league.get_league_members_info():
                                for player in team:
                                    if player == "error":
                                        text += "Account is deleted" + "\n"
                                        text += "\n"
                                    else:
                                        for key, value in player.items():
                                            key_temp = key
                                            value_temp = value
                                            if (key_temp == "gameaccounts" and (
                                                    value_temp == "User doesn't have any accounts in his profile" or platform_type not in value_temp)) or (
                                                    key_temp == "isBarred" and value_temp == True):
                                                for key_new, value_new in player.items():
                                                    if len(player) > 0:
                                                        text += "{0}: {1}".format(key_new, value_new) + "\n"
                                                    else:
                                                        text += "All users have gameaccounts in their profiles and nobody has barrage" + "\n"
                                                text += "\n"
                        self.output_info.setText("\n" + text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
