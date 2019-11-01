import requests
import json
from datetime import datetime
import time
import random
import os
import winsound
import sys


'''
2) Доделать 22 пункт - можно выбирать платформу, на которой проходит турнир(у игрока с ПСН'ом может не быть ЮПЛЕЯ, но его не покажет все равно)
'''


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


#MAIN
def show_options():
    print("\nType 's' to start\n OR type 'q' to quit")

while True:
    show_options()
    choice = input('Enter your choice: ').lower()
    print()

    if choice == "s":
        #\nType '2' : DOESN'T WORK PROPERLY NOW; if you want to check players' accounts in case they can be fakes or multiple accs
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        print("User Guide\n     USERS_FUNCTIONS\nType '1' if you want to see player's accounts"
              "\nType '3' if you want to see user's profile\nType '4' if you want to see only some parameters in user's profile."
              "\n     TEAMS_FUNCTIONS\nType '5' if you want to see team's info\nType '6' if you want to see all team members info\nType '7' if you want to see only some info in team_members' profiles"
              "\nType '8' if you want to see team_members' ID, NICKNAME, GAMEACCOUNT and REGION\n     MATCH_FUNCTIONS\nType '9' if you want  to see general match info"
              "\nType '10' if you want to see contestants'(2 teams) profiles\nType '11' if you want to see contestants members ('n' players) info"
              "\nType '12' if you want to see date of the match and its duration\nType '13' if you want to see match status and result if it's closed\nType '14' if you want to see match media"
              "\n     LEAGUE_FUNCTIONS\nType '15' if you want to see full league info\nType '16' if you want to see league results\nType '17' if you want to see all contestants, participating tournament"
              "\nType '18' if you want to see info about all users, participating in the tournament (I'm not sure, that you really want it, because process takes a lot, A LOT of time)"
              "\nType '19' if you want to see all matches ID and all gameaccounts there\nType '20' if you want to check open protests\nType '21' OR Type 'auto_admin' if you want to"
              " let the program check new tickets in a certain period of time\nType '22' if you want to see members without 'uplay', 'psn' or xbox accounts', or members who have barrage")
        case = input("\nType your case's number: ")
        print()

        # USERS FUNCTIONS
        if case == "1":  # get user's game_accounts by ID
            id = input("Enter player's ID: ")  # 11807411 or 12769661 <-- ID
            test_user = User(id)
            print(test_user.get_accounts())

        elif case == "2":  # DOESN'T WORK PROPERLY NOW; check 'n' accounts - whether they have similar game_accounts or not
            n = int(input("Write how many accounts you want to check: "))
            account_types = ["uplay_nick", "psn_online_id", "xbox_account"]
            temp = False

            # might be changed --> you can create a function, which will check admin's input
            while temp == False:
                account_type_input = input("Write here the account type - USE ONLY: 'uplay_nick', 'psn_online_id' or 'xbox_account': ")
                if check_input(account_type_input, account_types):
                    temp = True
                    continue
                else:
                    print("Please, use only types, which are already given")
            users = []
            for i in range(n):
                id = input("Enter player's ID: ")
                users.append(User(id))
                if check_accounts(users, account_type_input) == None:
                    print("Calm down, these accounts don't have similar " + account_type_input + 's')
                else:
                    print("Their accounts are similar - you'd better think about their ban\nHere are their accounts", check_accounts(users, account_type_input))

        elif case == "3":  # get everything from user's profile
            id = input("Enter player's ID: ")
            test_user = User(id)
            for key, value in test_user.get_profile().items():
                print("{0}: {1}".format(key, value))

        elif case == "4":  # get only specific parameters from profile
            id = input("Enter player's ID: ")
            temp = False
            parameters = ["id", "nickname", "region", "homepage", "penaltyPoints", "photo", "premium","trustLevel", "level", "awards", "isBarred", "barredUntil", "wins"]
            parameters_amount = int(input("Write here how many parameters do you want to see: "))
            chosen_parameters = []#parameters, which will be shown

            # might be changed --> you can create a function, which will check admin's input
            while temp == False:
                for i in range(parameters_amount):
                    profile_parameter_input = input("Write here an account parameter, those are ONLY: 'id', 'nickname', "
                    "'region', 'homepage', 'penaltyPoints', 'photo', 'premium', 'trustLevel', 'level', 'awards', 'isBarred', 'barredUntil', 'wins': ")
                    if check_input(profile_parameter_input, parameters):
                        temp = True
                        chosen_parameters.append(profile_parameter_input)
                        continue
                    else:
                        print("Please, use only parameters, which are already given")
            test_user = User(id)
            for key, value in test_user.get_profile().items():
                if check_input(key, chosen_parameters):
                    print("{0}: {1}".format(key, value))
                else:
                    continue

        # TEAMS FUNCTIONS
        elif case == "5":  # get team info
            team_id = input("Enter team's ID: ")
            test_team = Team(team_id)
            for key, value in test_team.get_team_info().items():
                print("{0}: {1}".format(key, value))

        elif case == "6":  # get everything from members' profiles
            team_id = input("Enter team's ID: ")  # 13429171 OR 11995366 <-- team_id
            test_team = Team(team_id)
            members_info = test_team.get_team_members_info()

            for i in range(len(members_info)):
                for key, value in members_info[i].items():
                    print("{0}: {1}".format(key, value))
                print()

        elif case == "7":  # get only some parameters from members' profiles
            team_id = input("Enter team's ID: ")
            test_team = Team(team_id)
            members_info = test_team.get_team_members_info()
            temp = False
            parameters = ["id", "nickname", "region", "homepage", "penaltyPoints", "photo", "premium","trustLevel", "level", "awards", "isBarred", "barredUntil", "wins"]
            parameters_amount = int(input("Write here how many parameters do you want to see: "))
            chosen_parameters = []

            # might be changed --> you can create a function, which will check admin's input
            while temp == False:
                for i in range(parameters_amount):
                    profile_parameter_input = input("Write here an account parameter, those are ONLY: 'id', 'nickname', "
                    "'region', 'homepage', 'penaltyPoints', 'photo', 'premium', 'trustLevel', 'level', 'awards', 'isBarred', 'barredUntil', 'wins': ")
                    if check_input(profile_parameter_input, parameters):
                        temp = True
                        chosen_parameters.append(profile_parameter_input)
                        continue
                    else:
                        print("Please, use only parameters, which are already given")

            for i in range(len(members_info)):
                for key, value in members_info[i].items():
                    if check_input(key, chosen_parameters):
                        print("{0}: {1}".format(key, value))
                    else:
                        continue
                print()

        elif case == "8":  # get useful info from team_members' profiles <-- id, nickname, gameaccount, region
            team_id = input("Enter team's ID: ")
            test_team = Team(team_id)
            members_info = test_team.get_team_members_info()
            options = ["id", "nickname", "region"]
            i = 0
            members_accounts = test_team.get_team_members_accounts()
            for member in members_info:
                member_id = member['id']
                team_member = User(member_id)
                print(members_accounts[i])
                for key, value in team_member.get_profile().items():
                    if check_input(key, options):
                        print("{0}: {1}".format(key, value))
                    else:
                        continue
                i += 1
                print()


        # MATCH FUNCTIONS
        elif case == "9":  # get match info
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            for key, value in test_match.get_match_info().items():
                if key == "contestants":
                    contestants = value
                    # print(value[0]['team']['id']) #TEAM ID
                print("{0}: {1}".format(key, value))

        elif case == "10":  # get contestants porfiles
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            teams_profiles = test_match.get_contestants_profile()

            for i in range(len(teams_profiles)):
                for key, value in teams_profiles[i].items():
                    print("{0}: {1}".format(key, value))
                print()

        elif case == "11":  # get contestants members info
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            contestants_info = test_match.get_contestants_members_info()

            for i in range(len(contestants_info)):
                print(contestants_info[i])
                for key, value in contestants_info[i].items():
                    print("{0}: {1}".format(key, value))
                print()

        elif case == "12":  # get date and duration of the match
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            date = test_match.get_match_date_time()
            if date == "open":
                print("Match isn't closed yet")
            else:
                for key, value in date.items():
                    print("{0}: {1}".format(key, value))

        elif case == "13":  # get match status and result
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            match_status = test_match.get_match_status()
            print("match_status: {0}".format(match_status))

            if match_status == "closed":
                print(test_match.get_match_results())

        elif case == "14":  # get match media
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            match_results = test_match.get_match_media()
            if match_results == "open":
                print("Match is still open, there is no match media yet")
            else:
                tournament_condition = False
                if len(match_results) == 10:
                    tournament_condition = True
                for i in range(len(match_results)):
                    print("file №{0}: {1}".format(i+1, match_results[i]))


        # LEAGUE FUNCTIONS

        # league_link = "https://play.eslgaming.com/ + test_league.get_league_description['uri']"  #<-- tournament link
        elif case == "15":  # get full league info
            league_id = input("Enter league ID: ")
            test_league = League(league_id)
            league_description = test_league.get_league_description()
            for key, value in league_description.items():
                print("{0}: {1}".format(key, value))

        elif case == "16":  # get league results
            league_id = input("Enter league ID: ")
            test_league = League(league_id)
            league_results = test_league.get_league_results()
            for result in league_results:
                print("\n{0}".format(result))

        elif case == "17":  # get league contestants
            league_id = input("Enter league ID: ")
            test_league = League(league_id)
            league_contestants = test_league.get_league_contestants()
            for contestant in league_contestants:
                for key, value in contestant.items():
                    if key != "alias" and key != "status":
                        print("{0}: {1}".format(key, value))
                print()

        elif case == "18":  # get all league members info
            league_id = input("Enter league ID: ")
            print()
            test_league = League(league_id)
            for team in test_league.get_league_members_info():
                for player in team:
                    if player == "error":
                        print("Account is deleted")
                    else:
                        for key, value in player.items():
                            print("{0}: {1}".format(key, value))
                        print()
                    #print()

        elif case == "19":  # get gameaccounts in match and match id
            league_id = input("Enter league ID: ")
            test_league = League(league_id)
            matches = test_league.get_matches_and_players()
            for match in matches:
                for key, value in match.items():
                    print("{0}: {1}".format(key, value))
                print()

        elif case == "20":  # get matches, where was opened a protest
            league_id = input("Enter league ID: ")
            test_league = League(league_id)
            protests = test_league.check_tickets()[0]
            total_protests_amount = test_league.check_tickets()[1]
            print("Total amount of opened tickets: {0}".format(total_protests_amount))
            for protest in protests:
                for key, value in protest.items():
                    print("{0}: {1}".format(key, value))
                beep()
                print()

        elif case == "21" or case == "auto_admin":  # loop, which checks new protests
            league_id = input("Enter league ID: ")
            refresh_time = float(input("Enter here, in how many minutes you want program to refresh, e.g 5 means, data will refresh each 5 minutes: "))
            print()
            refresh_time_seconds = refresh_time * 60
            my_file = open("matches_ids.txt", "w")
            my_file.write("")
            my_file.close()
            while True:
                test_league = League(league_id)
                protests = test_league.check_tickets()[0]
                total_protests_amount = test_league.check_tickets()[1]
                print("Total amount of opened tickets: {0}".format(total_protests_amount))
                for protest in protests:
                    for key, value in protest.items():
                        print("{0}: {1}".format(key, value))
                    print()

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




        elif case == "22":  # get members without specific account and members who have barrage
            league_id = input("Enter league ID: ")
            account_types = ["Uplay:", "PSN account:", "Xbox nickname:"]
            temp = False
            while temp == False:
                platform_type = input("Enter what type of nickname is used, e.g. 'Uplay:', 'PSN account:' or 'Xbox nickname:' : ")
                if check_input(platform_type, account_types):
                    temp = True
                    continue
                else:
                    print("Please, use only parameters, which are already given")

            print()
            test_league = League(league_id)
            for team in test_league.get_league_members_info():
                for player in team:
                    if player == "error":
                        print("Account is deleted")
                        print()
                    else:
                        for key, value in player.items():
                            key_temp = key
                            value_temp = value
                            if (key_temp == "gameaccounts" and (value_temp == "User doesn't have any accounts in his profile" or platform_type not in value_temp)) or (key_temp == "isBarred" and  value_temp == True):
                                for key_new, value_new in player.items():
                                    if len(player) > 0:
                                        print("{0}: {1}".format(key_new, value_new))
                                    else:
                                        print("All users have gameaccounts in their profiles and nobody has barrage")
                                print()




        else:  # only for TESTS
            new_user = User(11807411)
            new_team = Team(13797385)
            new_match = Match(37534224)  # 37480050 - technical win; 37480064 - usual match; 	37275772 - draw
            new_league = League(200341)
            '''
            #sound
            for i in range(5):
                beep()
            '''
            print("Incorrect input")
            #print("TEST: ")  # list(new_match.get_contestants_profile()[1].keys())[0]


    elif choice == "q":
        exit()
    else:
        print('Not a correct format - use only answers, which are given: {}'.format(choice))


