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
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


'''
3) Learn how to use multiple pages in a desktop app
4) Start working on a login system (with a database or simply with creating  a '.txt' file)
5) Send e-mail, when a new protest opens
6) 
'''


class Verifier:
    def __init__(self, user_input):
        self.user_input = user_input

    def check_id(self):
        if self.user_input.isdigit():
            return True
        else:
            return False

    def check_refresh_time(self, input_time):
        if input_time == "0":
            return False
        else:
            valid_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
            for letter in input_time:
                if letter not in valid_values:
                    return False
                else:
                    continue
            return True


class BackendQThread(QThread):

    quit_thread = pyqtSignal(name='close_thread')

    def __init__(self, mainwindow, task):
        super(BackendQThread, self).__init__()
        self.mainwindow = mainwindow
        self.task = task

    def run(self):
        if self.task == 0:  # Get: Player's accounts
            self.get_player_acc()
        elif self.task == 1:  # Get: Player's profile
            self.get_player_profile()
        elif self.task == 2:  # Get: Team's info
            self.get_team_info()
        elif self.task == 3:  # Get: All team members' info
            self.get_members_info()
        elif self.task == 4:  # Get: Only ID, nickname, gameaccount and region in team members' profiles
            self.get_some_members_info()
        elif self.task == 5:  # Get General match info
            self.get_general_match_info()
        elif self.task == 6:  # Get: Contestants' (2 teams) profiles
            self.get_contestants_profiles()
        elif self.task == 7:  # Get: Contestants members' profiles
            self.get_match_members_profiles()
        elif self.task == 8:  # Get: Date and duration of the match
            self.get_match_date()
        elif self.task == 9:  # Get: Match status and result if it is closed
            self.get_match_result()
        elif self.task == 10:  # Get: Match media
            self.get_match_media()
        elif self.task == 11:  # Get: Full league info
            self.get_league_info()
        elif self.task == 12:  # Get: League results
            self.get_league_results()
        elif self.task == 13:  # Get: All contestants, participating in the tournament
            self.get_league_contestants()
        elif self.task == 14:  # Get: Info about all players, participating in the tournament
            self.get_league_contestants_info()
        elif self.task == 15:  # Get: All matches IDs and gameaccounts there
            self.get_league_matches_gameaccounts()
        elif self.task == 16:  # Check open protests
            self.check_protests()
        elif self.task == 17:  # AUTO ADMIN
            self.auto_admin()
        elif self.task == 18:  # Get: All members, who doesn't have specific gameaccounts
            self.get_suspects()
        else:
            pass

    '''
    
    '''

    def get_player_acc(self):  # Player Account
        id = self.mainwindow.input_player_id.text()
        if id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter player ID' ")
        else:
            if not Verifier(id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_user = User(id)
                self.mainwindow.output_info.append(test_user.get_accounts())
                self.mainwindow.output_info.append(get_user_link(id))
                self.mainwindow.output_info.append("")

    def get_player_profile(self):  # Player Profile
        id = self.mainwindow.input_player_id.text()
        if id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter player ID' ")
        else:
            if not Verifier(id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_user = User(id)
                user_profile = test_user.get_profile()
                for key, value in user_profile.items():
                    self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                    time.sleep(0.025)
                self.mainwindow.output_info.append("")

    def get_team_info(self):  # Team Info
        team_id = self.mainwindow.input_team_id.text()
        if team_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter team ID' ")
        else:
            if not Verifier(team_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_team = Team(team_id)
                if test_team.get_team_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Team with that ID doesn't exist")
                else:
                    for key, value in test_team.get_team_info().items():
                        self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                        time.sleep(0.025)
                    self.mainwindow.output_info.append("")

    def get_members_info(self):  # Team Members Info
        team_id = self.mainwindow.input_team_id.text()
        if team_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter team ID' ")
        else:
            if not Verifier(team_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_team = Team(team_id)
                members_info = test_team.get_team_members_info()
                if members_info == "error":
                    self.mainwindow.output_info.append("\nERROR: Team with that ID doesn't exist")
                else:
                    for i in range(len(members_info)):
                        for key, value in members_info[i].items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.015)
                        self.mainwindow.output_info.append("")
                        time.sleep(0.025)
                    self.mainwindow.output_info.append(get_team_link(team_id))
                    self.mainwindow.output_info.append("")

    def get_some_members_info(self):  # Specific team members info
        team_id = self.mainwindow.input_team_id.text()
        if team_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter team ID' ")
        else:
            if not Verifier(team_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_team = Team(team_id)
                members_info = test_team.get_team_members_info()
                options = ["id", "nickname", "region", "Link"]
                i = 0
                members_accounts = test_team.get_team_members_accounts()
                if members_info == "error" or members_accounts == "error":
                    self.mainwindow.output_info.append("\nERROR: Team with that ID doesn't exist")
                else:
                    for member in members_info:
                        member_id = member['id']
                        team_member = User(member_id)
                        self.mainwindow.output_info.append(members_accounts[i])
                        for key, value in team_member.get_profile().items():
                            if check_input(key, options):
                                self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                                time.sleep(0.025)
                            else:
                                continue
                            time.sleep(0.1)
                        self.mainwindow.output_info.append("")
                        i += 1
                    self.mainwindow.output_info.append(get_team_link(team_id))
                    self.mainwindow.output_info.append("")

    def get_general_match_info(self):  # Match info
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_match = Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    for key, value in test_match.get_match_info().items():
                        self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                        time.sleep(0.015)
                    self.mainwindow.output_info.append("")

    def get_contestants_profiles(self):
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_match = Match(match_id)
                teams_profiles = test_match.get_contestants_profile()
                if teams_profiles == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    for i in range(len(teams_profiles)):
                        for key, value in teams_profiles[i].items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.015)
                        self.mainwindow.output_info.append("")
                        time.sleep(0.025)
                    self.mainwindow.output_info.append(get_match_link(match_id))
                    self.mainwindow.output_info.append("")

    def get_match_members_profiles(self):
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_match = Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    contestants_info = test_match.get_contestants_members_info()
                    for i in range(len(contestants_info)):
                        for key, value in contestants_info[i].items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.1)
                        self.mainwindow.output_info.append("")
                        time.sleep(0.2)
                    self.mainwindow.output_info.append(get_match_link(match_id))
                    self.mainwindow.output_info.append("")

    def get_match_date(self):
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_match = Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    date = test_match.get_match_date_time()
                    if date == "open":
                        self.mainwindow.output_info.append("Match isn't closed yet")
                        self.mainwindow.output_info.append("")
                    else:
                        for key, value in date.items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.015)
                    self.mainwindow.output_info.append("")

    def get_match_result(self):
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_match = Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    match_status = test_match.get_match_status()
                    self.mainwindow.output_info.append("Match status: {0}".format(match_status))
                    if match_status == "closed":
                        for key, value in test_match.get_match_results().items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.1)
                    self.mainwindow.output_info.append("")

    def get_match_media(self):
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_match = Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    match_results = test_match.get_match_media()
                    if match_results == "open":
                        self.mainwindow.output_info.append("Match is still open, there is no match media yet")
                    elif match_results == "nothing":
                        self.mainwindow.output_info.append("There is no match media in this match")
                    else:
                        tournament_condition = False
                        if len(match_results) == 10:  # FOR FUTURE
                            tournament_condition = True
                        for i in range(len(match_results)):
                            file_link = '<a href = {0}> file_{1} </a>'.format(match_results[i], i + 1)
                            self.mainwindow.output_info.append("file №{0}: {1}".format(i + 1, file_link))
                            time.sleep(0.2)
                    self.mainwindow.output_info.append(get_match_link(match_id))
                    self.mainwindow.output_info.append("")

    def get_league_info(self):
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_league = League(league_id)
                league_description = test_league.get_league_description()
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    for key, value in league_description.items():
                        self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                        time.sleep(0.015)
                    self.mainwindow.output_info.append("")

    def get_league_results(self):
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_league = League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    league_results = test_league.get_league_results()
                    for result in league_results:
                        for key, value in result.items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.020)
                        self.mainwindow.output_info.append("")
                        time.sleep(0.025)

    def get_league_contestants(self):
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_league = League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    league_contestants = test_league.get_league_contestants()
                    for contestant in league_contestants:
                        contestant['Link'] = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(contestant['id'], contestant['name'])
                        for key, value in contestant.items():
                            if key != "alias":
                                self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                                time.sleep(0.03)
                        self.mainwindow.output_info.append("")
                        time.sleep(0.2)
                    self.mainwindow.output_info.append("")

    def get_league_contestants_info(self):
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                self.mainwindow.output_info.append("")
                test_league = League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    if test_league.get_league_mode() == "1on1":
                        for player in test_league.get_league_members_info():
                            if player == "error":
                                self.mainwindow.output_info.append("Account is deleted")
                            else:
                                for key, value in player.items():
                                    self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                                    time.sleep(0.0002)
                                self.mainwindow.output_info.append("")
                            time.sleep(0.1)
                    else:
                        for team in test_league.get_league_members_info():
                            for player in team:
                                if player == "error":
                                    self.mainwindow.output_info.append("Account is deleted")
                                else:
                                    for key, value in player.items():
                                        self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                                        time.sleep(0.05)
                                    self.mainwindow.output_info.append("")
                                time.sleep(0.1)
                    self.mainwindow.output_info.append("")

    def get_league_matches_gameaccounts(self):
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_league = League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    matches = test_league.get_matches_and_players()
                    for match in matches:
                        for key, value in match.items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.025)
                        self.mainwindow.output_info.append("")
                        time.sleep(0.1)
                    self.mainwindow.output_info.append("")

    def check_protests(self):
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                test_league = League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    protests = test_league.check_tickets()[0]
                    total_protests_amount = test_league.check_tickets()[1]
                    self.mainwindow.output_info.append("Total amount of opened tickets: {0}".format(total_protests_amount))
                    for protest in protests:
                        for key, value in protest.items():
                            self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                            time.sleep(0.015)
                        beep()
                        self.mainwindow.output_info.append("")
                        time.sleep(0.025)
                    self.mainwindow.output_info.setOpenExternalLinks(True)

    def auto_admin(self):
        league_id = self.mainwindow.input_league_id.text()
        refresh_time = self.mainwindow.input_refresh_time.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                if refresh_time == "":
                    self.mainwindow.output_info.append(
                        "\nERROR: 'Enter  'refresh time', so in how many minutes you want program to refresh, e.g '5' means, data will refresh each 5 minutes' ")
                else:
                    if not Verifier.check_refresh_time(league_id, refresh_time):
                        self.mainwindow.output_info.append("\nERROR: 'Incorrect Time Format - should be: 5 OR 5.5' ")
                    else:
                        if League(league_id).get_league_description() == "error":
                            self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                        else:
                            refresh_time_seconds = float(refresh_time) * 60
                            text = ""
                            text += "\n"
                            is_similar_protest = False
                            my_file = open("matches_ids.txt", "w")
                            my_file.write("")
                            my_file.close()
                            while True:
                                test_league = League(league_id)
                                protests = test_league.check_tickets()[0]
                                total_protests_amount = test_league.check_tickets()[1]
                                total_protests_amount_string = 'Total amount of opened tickets'
                                self.mainwindow.output_info.append(
                                    '<span>{0}: {1}<span>'.format(total_protests_amount_string, total_protests_amount))
                                for protest in protests:
                                    for key, value in protest.items():
                                        self.mainwindow.output_info.append('<span>{0}: {1}<span>'.format(key, value))
                                        time.sleep(0.015)
                                    self.mainwindow.output_info.append("")
                                    time.sleep(0.025)

                                if text == "Total amount of opened tickets: {0}".format(total_protests_amount) + "\n":
                                    time.sleep(refresh_time_seconds)
                                    continue
                                else:
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

    def get_suspects(self):
            league_id = self.mainwindow.input_league_id.text()
            if league_id == "":
                self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
            else:
                if not Verifier(league_id).check_id():
                    self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
                else:
                    account_types = ["Uplay:", "PSN account:", "Xbox nickname:"]
                    platform_type = self.mainwindow.input_account_type.text()
                    if platform_type == "":
                        self.mainwindow.output_info.append("ERROR: 'Enter account type' ")
                    else:
                        if platform_type not in account_types:
                            self.mainwindow.output_info.append("ERROR: 'Please, use only 'Uplay:', 'PSN account:' or 'Xbox nickname:' ")
                        else:
                            if check_input(platform_type, account_types):
                                test_league = League(league_id)
                                if test_league.get_league_description() == "error":
                                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                                else:
                                    for team in test_league.get_league_members_info():
                                        for player in team:
                                            if player == "error":
                                                self.mainwindow.output_info.append("Account is deleted")
                                                self.mainwindow.output_info.append("")
                                            else:
                                                for key, value in player.items():
                                                    key_temp = key
                                                    value_temp = value
                                                    if (key_temp == "gameaccounts" and (
                                                            value_temp == "User doesn't have any accounts in his profile" or platform_type not in value_temp)) or (
                                                            key_temp == "isBarred" and value_temp == True):
                                                        for key_new, value_new in player.items():
                                                            if len(player) > 0:
                                                                self.mainwindow.output_info.append("{0}: {1}".format(key_new, value_new))
                                                                time.sleep(0.015)
                                                            else:
                                                                self.mainwindow.output_info.append("All users have gameaccounts in their profiles and nobody has barrage")
                                                        self.mainwindow.output_info.append("")
                                                        time.sleep(0.025)
                                self.mainwindow.output_info.append("")

    def terminate_thread(self):
        self.terminate()


  # AutoAdminThread
'''
class AutoAdminThread(QThread):
    def __init__(self, mainwindow, refresh_time, league_id, parent = None):
        super().__init__()
        self.mainwindow = mainwindow
        self.refresh_time = refresh_time
        self.league_id = league_id
        self.runs = True

    def auto_admin(self):
        text = ""
        text += "\n"
        is_similar_protest = False
        my_file = open("matches_ids.txt", "w")
        my_file.write("")
        my_file.close()
        while True:
            test_league = League(self.league_id)
            protests = test_league.check_tickets()[0]
            total_protests_amount = test_league.check_tickets()[1]
            total_protests_amount_string = 'Total amount of opened tickets'
            self.mainwindow.output_info.append('<span>{0}: {1}<span>'.format(total_protests_amount_string, total_protests_amount))
            for protest in protests:
                for key, value in protest.items():
                    self.mainwindow.output_info.append('<span>{0}: {1}<span>'.format(key, value))
                self.mainwindow.output_info.append("")

            if text == "Total amount of opened tickets: {0}".format(total_protests_amount) + "\n":
                time.sleep(self.refresh_time)
                continue
            else:
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
                time.sleep(self.refresh_time)

    def stop_thread(self):  # takes a long time (obviously "refresh time")
        self.runs = False
        self.wait()

    def terminate_thread(self):  # immediately kills a thread
        self.terminate()

    def run(self):
        self.auto_admin()
        #   self.test_function()
'''

class League:
    def __init__(self, league_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/leagues/'
        self.league_id = str(league_id)

    def get_league_mode(self):
        r = requests.get(self.base_url + self.league_id)
        response = json.loads(r.text)
        return response['mode']

    def get_league_description(self):  # full league description
        r = requests.get(self.base_url + self.league_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
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
                #result = {'key': 'value'}
                results.append(result)

            else:
                team_a_id = match.get_match_info()['contestants'][0]['team']['id']
                team_a_name = match.get_match_info()['contestants'][0]['team']['name']
                team_b_id = match.get_match_info()['contestants'][1]['team']['id']
                team_b_name = match.get_match_info()['contestants'][1]['team']['name']
                #result_0 = "Match is still open - match id: {0}\n{1}; team ID: {2}\n{3}; team ID: {4}".format(match_id, team_a_name, team_a_id, team_b_name, team_b_id)
                result = {'Status': 'Match is  still open', 'Match ID': match_id, 'Link': get_match_link(match_id),
                          get_team_link(team_a_id): team_a_id, get_team_link(team_b_id): team_b_id}
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
            match_id_dict = {"match id": match_id, "Match link": get_match_link(match_id)}
            gameaccounts_dict = match['gameaccounts']
            for key, value in gameaccounts_dict.items():
                gameaccounts_dict[key] = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(key, value)
            match_id_dict.update(gameaccounts_dict)
            gameaccounts.append(match_id_dict)
        return gameaccounts

    def check_tickets(self):
            r = requests.get(self.base_url + self.league_id + "/matches")
            response = json.loads(r.text)
            tickets_amount = 0
            protests = []
            matches_id = []
            if "1on1" in League.get_league_mode(self):
                for match in response:
                    match_status = match['status']
                    if match_status == "protest":
                        tickets_amount += 1

                        match_id = match['id']
                        player_a_id = match['contestants'][0]['user']['id']
                        player_a_name = match['contestants'][0]['user']['nickname']
                        player_b_id = match['contestants'][1]['user']['id']
                        player_b_name = match['contestants'][1]['user']['nickname']

                        new_r = requests.get(self.base_url + self.league_id)
                        new_response = json.loads(new_r.text)

                        league_name = new_response['uri']
                        base_link = "https://play.eslgaming.com"
                        match_link = "match/" + str(match_id) + "/"
                        protest_link = "admin_tickets/all"
                        admin_protests_link = base_link + league_name + protest_link
                        admin_protests_link_url = '<a href={0}> {1} </a>'.format(admin_protests_link, "Open protests")
                        match_protest_link = base_link + league_name + match_link
                        match_protest_link_url = '<a href={0}> {1} </a>'.format(match_protest_link[:-1], "Match page")
                        protest_dict = {"ticket number": tickets_amount, "match_id": match_id,
                                        player_a_id: player_a_name, player_b_id: player_b_name,
                                        "Check your tickets": admin_protests_link_url, "Check match": match_protest_link_url}
                        protests.append(protest_dict)
                        matches_id.append(match_id)
            else:
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
                        protest_link = "admin_tickets/all"
                        admin_protests_link = base_link + league_name + protest_link
                        admin_protests_link_url = '<a href={0}> {1} </a>'.format(admin_protests_link, "Open protests")
                        match_protest_link = base_link + league_name + match_link
                        match_protest_link_url = '<a href={0}> {1} </a>'.format(match_protest_link[:-1], "Match page")
                        protest_dict = {"ticket number": tickets_amount, "match_id": match_id, team_a_id: team_a_name,
                                        team_b_id: team_b_name, "Check your tickets": admin_protests_link_url,
                                        "Check match": match_protest_link_url}
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
            match_name = 'Match link'
            match_link = '<a href = https://play.eslgaming.com/match/{0}> {1} </a>'.format(self.match_id, match_name)
            response['Link'] = match_link
            return response

    def get_match_mode(self):
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if is_error(response):
            return "error"
        else:
            return response['type']

    def get_contestants_profile(self):  # 2 teams' profiles
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        test_match = Match(self.match_id)
        contestants_profiles = []
        if test_match.get_match_info() == "error":
            return "error"
        else:
            for key, value in test_match.get_match_info().items():
                if key == "contestants":
                    contestants = value
                    for i in range(len(contestants)):
                        if Match.get_match_mode(self) == "1on1":
                            if contestants[i]['user']['id'] == None:
                                contestants_profiles.append({'User': 'Deleted player account'})
                            else:
                                contestant = User(contestants[i]['user']['id'])
                                contestants_profiles.append(contestant.get_profile())
                        else:
                            if contestants[i]['team']['id'] == None:
                                contestants_profiles.append({'Team': 'Deleted team account'})
                            else:
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
                beginning_date = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")  # !!!

                end_date = end_date_string[:10]
                end_time = end_date_string[11:19]
                end = end_date + ' ' + end_time
                final_date = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") # !!!

                delta = final_date - beginning_date
                match_name = 'Match link'
                match_link = '<a href = https://play.eslgaming.com/match/{0}> {1} </a>'.format(self.match_id, match_name)
                match_time = {"Start time": start, "End time": end, "Duration of the match": delta, 'Link': match_link}
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
            result_argument = response['result']['score']
            results = result_argument

            teams = list(results.keys())
            scores = list(results.values())
            winners = teams[0]
            losers = teams[1]

            match_name = 'Match link'
            match_link = '<a href = https://play.eslgaming.com/match/{0}> {1} </a>'.format(self.match_id, match_name)

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

            if Match.get_match_mode(self) == "1on1":
                user_win = User(winners)
                user_lose = User(losers)
                user_win_id = ""
                user_win_name = ""
                user_lose_id = ""
                user_lose_name = ""
                if "error" in user_win.get_profile() and "error" in user_lose.get_profile():
                    user_win_name = "'" + "Deleted account" + "'"
                    user_win_id = "id: " + winners
                    user_win_link = "ERROR - DELETED ACCOUNT"
                    user_lose_name = "'" + "Deleted account" + "'"
                    user_lose_id = "id: " + losers
                    user_lose_link = "ERROR - DELETED ACCOUNT"
                if "error" in user_win.get_profile() and not("error" in user_lose.get_profile()):
                    user_win_id = "id: " + winners
                    user_win_name = "'" + "Deleted account" + "'"
                    user_win_link = "ERROR - DELETED ACCOUNT"
                    user_lose_id = "id: " + losers
                    user_lose_name = user_lose.get_profile()['nickname']
                    user_lose_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(losers, user_lose_name)
                if "error" in user_lose.get_profile() and not("error" in user_win.get_profile()):
                    user_lose_id = "id: " + losers
                    user_lose_name = "'" + "Deleted account" + "'"
                    user_lose_link = "ERROR - DELETED ACCOUNT"
                    user_win_id = "id: " + winners
                    user_win_name = user_win.get_profile()['nickname']
                    user_win_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(winners, user_win_name)
                elif not("error" in user_lose.get_profile()) and not("error" in user_win.get_profile()):
                    user_win_id = "id: " + winners
                    user_win_name = user_win.get_profile()['nickname']
                    user_win_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(winners, user_win_name)
                    user_lose_id = "id: " + losers
                    user_lose_name = user_lose.get_profile()['nickname']
                    user_lose_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(losers, user_lose_name)
                if result != "draw":
                    dict = {user_win_link: 'has won!', user_lose_link: 'has lost.', 'Link': match_link}
                    return dict
                else:
                    dict = {'Result': 'There result is draw', user_win_link: user_win_id, user_lose_link: user_lose_id, 'Link': match_link}
                    return dict
            else:
                team_win = Team(winners)
                team_lose = Team(losers)
                team_win_id = ""
                team_win_name = ""
                team_lose_id = ""
                team_lose_name = ""
                if "error" in team_lose.get_team_info() and "error" in team_win.get_team_info():
                    team_win_id = "0 - Deleted Account"
                    team_win_name = "Deleted Account - 1"
                    team_win_link = "ERROR - DELETED ACCOUNT"
                    team_lose_id = "0 - Deleted Account"
                    team_lose_name = "Deleted Account - 2"
                    team_lose_link = "ERROR - DELETED ACCOUNT"
                if "error" in team_win.get_team_info() and not("error" in team_lose.get_team_info()):
                    team_win_id = "id: " + winners
                    team_win_name = "'" + "Deleted account" + "'"
                    team_win_link = "ERROR - DELETED ACCOUNT"
                    team_lose_id = "id: " + losers
                    team_lose_name = team_lose.get_team_info()['name']
                    team_lose_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(losers, team_lose_name)
                if "error" in team_lose.get_team_info() and not("error" in team_win.get_team_info()):
                    team_lose_id = "id: " + losers
                    team_lose_name = "'" + "Deleted account" + "'"
                    team_lose_link = "ERROR - DELETED ACCOUNT"
                    team_win_id = "id: " + winners
                    team_win_name = team_win.get_team_info()['name']
                    team_win_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(winners, team_win_name)
                elif not("error" in team_win.get_team_info()) and not("error" in team_lose.get_team_info()):
                    team_win_id = "id: " + winners
                    team_win_name = team_win.get_team_info()['name']
                    team_win_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(winners, team_win_name)
                    team_lose_id = "id: " + losers
                    team_lose_name = team_lose.get_team_info()['name']
                    team_lose_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(losers, team_lose_name)
                if result != "draw":
                    dict = {team_win_link: 'has won!', team_lose_link: 'has lost.', 'Link': match_link}
                    return dict
                else:
                    dict = {'Result': 'There result is draw', team_win_link: team_win_id, team_lose_link: team_lose_id, 'Link': match_link}
                    return dict

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
            if len(files) == 0:
                return "nothing"
            else:
                return files
        elif status == "open":
            return "Open"  # Match is not closed yet

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
            response['Link'] = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(self.team_id, response['name'])
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
            link = get_user_link(self.id)
            response['Link'] = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(self.id, response['nickname'])
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
            new_dict['Link'] = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(self.id, response['nickname'])
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

# -------HYPERLINKS-------
def get_user_link(user_id):
    user_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(user_id, "User profile link")
    return user_link

def get_team_link(team_id):
    team_name = Team(team_id).get_team_info()['name']
    team_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(team_id, team_name)
    return team_link

def get_match_link(match_id):
    match_name = 'Match link'
    match_link = '<a href = https://play.eslgaming.com/match/{0}> {1} </a>'.format(match_id, match_name)
    return match_link




  # USER INTERFACE
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.threads = []

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
        self.output_info.setOpenExternalLinks(True)
        self.output_info.setAcceptRichText(True)
        #self.output_info.setOpenLinks(True)
        #self.output_info.setReadOnly(False)

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

        # ------------BUTTONS-----------------------------
        self.submit_button.clicked.connect(self.pressed)
        self.clearWindow_button.clicked.connect(self.clear)
        self.stop_button.clicked.connect(self.stop_test_thread)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        #self.output_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
#"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
#"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
#"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.15094pt;\"><br /></p></body></html>"))
        self.label_player_id.setText(_translate("MainWindow", "Enter Player ID"))
        self.label_team_id.setText(_translate("MainWindow", "Enter Team ID"))
        self.label_match_id.setText(_translate("MainWindow", "Enter Match ID"))
        self.label_league_id.setText(_translate("MainWindow", "Enter League ID"))
        self.label_refresh_time.setText(_translate("MainWindow", "Enter Refresh time"))
        self.label_account_type.setText(_translate("MainWindow", "Enter Account type"))
        self.clearWindow_button.setText(_translate("MainWindow", "Clear window"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.stop_button.setEnabled(False)


    def clear(self):
        self.output_info.clear()

    def refresh_text_box(self, text):
        self.output_info.append(text)
        QtGui.QGuiApplication.processEvents()


    # ---------------THREAD FUNCTIONS------------------
    '''
    def set_thread_values(self, refresh_time, league_id):
        self.auto_admin_worker = AutoAdminThread(mainwindow=self, refresh_time=refresh_time, league_id=league_id)

    def start_thread(self):
        self.auto_admin_worker.start()

    def destroy_thread(self):
        self.output_info.append("\nTHE SEARCH IS STOPPED")
        self.auto_admin_worker.terminate_thread()
    '''

    def stop_test_thread(self):
        for task in self.threads:
            task.terminate_thread()
        self.output_info.append("<div>Task is finished</div>")


    # ----------MAIN PART-----------

    def pressed(self):

        choice = str(self.admin_Functions.currentText())
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

        self.threads = []
        task = self.admin_Functions.currentIndex()
        backend_thread = BackendQThread(self, task)
        backend_thread.start()
        self.stop_button.setEnabled(True)
        self.threads.append(backend_thread)

        self.output_info.moveCursor(self.output_info.textCursor().Start)


        # ---------TEAM FUNCTIONS--------

        # ---------MATCH FUNCTIONS----------

        # --------LEAGUE FUNCTIONS--------





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    thread_manager = Ui_MainWindow()

    MainWindow.show()
    sys.exit(app.exec_())