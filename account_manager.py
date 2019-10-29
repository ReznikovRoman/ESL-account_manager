import requests
import json
from datetime import datetime
import ast, time, random
import os


'''
29.10.19


'''




class Match:
    def __init__(self, match_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.match_id = str(match_id)

    def get_match_info(self):#all match info
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        return response

    def get_contestants_profile(self):#2 teams' profiles
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
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

    def get_match_results(self):
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        test_match = Match(self.match_id)
        result = response['result']['points']
        return result

    def get_match_media(self):
        r = requests.get(self.base_url + "/matches/" + self.match_id + "/media")
        response = json.loads(r.text)
        files = []
        for i in range(len(response)):
            files.append(response[i]['filename'])
        return files



class Team:
    def __init__(self, team_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.team_id = str(team_id)

    def get_team_info(self):
        r = requests.get(self.base_url + "/teams/" + self.team_id)
        response = json.loads(r.text)
        return response

    def get_team_members_info(self):
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        members_info = []
        for player in response:
            member = User(player)
            members_info.append(member.get_profile())
        return members_info

    def get_team_members_accounts(self):
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        members_accounts = []
        for player in response:
            member = User(player)
            members_accounts.append(member.get_accounts())
        return members_accounts



class User:
    def __init__(self, id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.id = str(id)


    def get_profile(self): #user profile info
        r = requests.get(self.base_url + "/users/" + self.id + "/basicprofile")
        response = json.loads(r.text)
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
            #account_count = ''
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

    def get_useful_info(self):# useful parameters are: 'id', 'nickname', 'gameaccount', 'region', 'isBarred'
        r = requests.get(self.base_url + "/users/" + self.id + "/basicprofile")
        response = json.loads(r.text)
        new_user = User(self.id)
        new_values = []
        user_accounts = new_user.get_accounts()
        response["gameaccounts"] = user_accounts
        new_keys = ['id', 'nickname', 'region','isBarred','gameaccounts']
        isBarred = False
        for key in response:
            if key == "id":
                new_values.append(response.get(key))
            elif key == "nickname":
                new_values.append(response.get(key))
            elif key == "region":
                new_values.append(response.get(key))
            elif key == "isBarred":
                new_values.append(response.get(key))
                if response.get(key):
                    isBarred = True
                    new_values.append(str(response.get('barredUntil'))[:10])
                    new_values.append(get_duration_period(response.get('barredUntil')))
                    new_keys = ['id', 'nickname', 'region', 'isBarred', 'barredUntil', 'banDuration', 'gameaccounts']
            elif key == "gameaccounts":
                new_values.append(response.get(key))


        useful_parameters = dict(zip(new_keys, new_values))
        return useful_parameters

    def get_special_account(self, option):#special account --> e.g "psn_online_id"
        r = requests.get(self.base_url + "/users/" + self.id + "/gameaccounts")
        response = json.loads(r.text)
        error = 0
        for i in range(len(response)):
            dict = response[i]
            if dict['type'] == option:
                return dict['value']



#FUCNTIONS
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

def check_date(date):#
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




#MAIN
def show_options():
    print("\nType 's' to start\n OR type 'q' to quit")

while True:
    show_options()
    choice = input('Enter your choice: ').lower()
    print()

    if choice == "s":
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        print("User Guide\n     USERS_FUNCTIONS\nType '1' if you want to see a player's accounts\nType '2' : DOESN'T WORK PROPERLY NOW; if you want to check players' accounts in case they can be fakes or multiple accs"
              "\nType '3' if you want to see user's profile\nType '4' if you want to see only some parameters in user's profile."
              "\n     TEAMS_FUNCTIONS\nType '5' if you want to see team's info\nType '6' if you want to see all team members info\nType '7' if you want to see only some info in team_members' profiles"
              "\nType '8' if you want to see team_members' ID, NICKNAME, GAMEACCOUNT and REGION\n     MATCH_FUNCTIONS\nType '9' if you want  to see general mach info"
              "\nType '10' if you want to see contestants'(2 teams) profiles\nType '11' if you want to see contestants members('n' players) info"
              "\nType '12' if you want to see date of the match and its duration\nType '13' if you want to see match result\nType '14' if you want to see match media")
        case = int(input("Type your case's number: "))
        print()

        #USERS FUNCTIONS
        if case == 1:#get user's game_accounts by ID
            id = input("Enter player's ID: ")  #11807411 or 12769661 <-- ID
            test_user = User(id)
            print(test_user.get_accounts())

        elif case == 2:#DOESN'T WORK PROPERLY NOW; check 'n' accounts - whether they have similar game_accounts or not
            n = int(input("Write how many accounts you want to check: "))
            account_types = ["uplay_nick", "psn_online_id", "xbox_account"]
            temp = False

            #might be changed --> you can create a function, which will check admin's input
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

        elif case == 3:# get everything from user's profile
            id = input("Enter player's ID: ")
            test_user = User(id)
            for key, value in test_user.get_profile().items():
                print("{0}: {1}".format(key, value))

        elif case == 4:# get only specific parameters from profile
            id = input("Enter player's ID: ")
            temp = False
            parameters = ["id", "nickname", "region", "homepage", "penaltyPoints", "photo", "premium","trustLevel", "level", "awards", "isBarred", "barredUntil", "wins"]
            parameters_amount = int(input("Write here how many parameters do you want to see: "))
            chosen_parameters = []#parameters, which will be shown

            #might be changed --> you can create a function, which will check admin's input
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

        #TEAMS FUNCTIONS
        elif case == 5:# get team info
            team_id = input("Enter team's ID: ")
            test_team = Team(team_id)
            for key, value in test_team.get_team_info().items():
                print("{0}: {1}".format(key, value))

        elif case == 6:# get everything from members' profiles
            team_id = input("Enter team's ID: ")  #13429171 OR 11995366 <-- team_id
            test_team = Team(team_id)
            members_info = test_team.get_team_members_info()

            for i in range(len(members_info)):
                for key, value in members_info[i].items():
                    print("{0}: {1}".format(key, value))
                print()

        elif case == 7:# get only some parameters from members' profiles
            team_id = input("Enter team's ID: ")
            test_team = Team(team_id)
            members_info = test_team.get_team_members_info()
            temp = False
            parameters = ["id", "nickname", "region", "homepage", "penaltyPoints", "photo", "premium","trustLevel", "level", "awards", "isBarred", "barredUntil", "wins"]
            parameters_amount = int(input("Write here how many parameters do you want to see: "))
            chosen_parameters = []

            #might be changed --> you can create a function, which will check admin's input
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

        elif case == 8:# get useful info from team_members' profiles <-- id, nickname, gameaccount, region
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


        #MATCH FUNCTIONS
        elif case == 9:# get match info
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            for key, value in test_match.get_match_info().items():
                if key == "contestants":
                    contestants = value
                    #print(value[0]['team']['id']) #TEAM ID
                print("{0}: {1}".format(key, value))

        elif case == 10:# get contestants porfiles
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            teams_profiles = test_match.get_contestants_profile()

            for i in range(len(teams_profiles)):
                for key, value in teams_profiles[i].items():
                    print("{0}: {1}".format(key, value))
                print()

        elif case == 11:# get contestants members info
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            contestants_info = test_match.get_contestants_members_info()
            for i in range(len(contestants_info)):
                for key, value in contestants_info[i].items():
                    print("{0}: {1}".format(key, value))
                print()

        elif case == 12:# get date and duration of the match
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            for key, value in test_match.get_match_date_time().items():
                print("{0}: {1}".format(key, value))

        elif case == 13:# get match result
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            results = test_match.get_match_results()
            teams = list(results.keys())
            scores = list(results.values())
            winners = teams[0]
            losers = teams[1]

            #only for 2 teams
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
            team_win_id = "id: " + winners
            team_win_name = "'" + team_win.get_team_info()['name'] + "'"
            team_lose = Team(losers)
            team_lose_id = "id: " + losers
            team_lose_name = "'" + team_lose.get_team_info()['name'] + "'"
            if result != "draw":
                print("{0} has won! {1}".format(team_win_name, team_win_id))
                print("{0} has lost. {1}".format(team_lose_name, team_lose_id))
            else:
                print("The result is draw")
                print("{0}: {1}".format(team_win_name, team_win_id))
                print("{0}: {1}".format(team_lose_name, team_lose_id))

        elif case == 14:# get match media
            match_id = input("Enter match ID: ")
            test_match = Match(match_id)
            match_results = test_match.get_match_media()
            tournament_condition = False
            if len(match_results) == 10:
                tournament_condition = True
            for i in range(len(match_results)):
                print("file №{0}: {1}".format(i+1, match_results[i]))

        else:#only for TESTS
            new_user = User(11807411)
            new_team = Team(13797385)
            new_match = Match(37275772)
            print("TEST: ")
        #input()

    elif choice == "q":
        exit()
    else:
        print('Not a correct format - use only answers, which are given: {}'.format(choice))


