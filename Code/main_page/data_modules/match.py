import requests
import json
from datetime import datetime
import main_page.data_modules.functions
import main_page.data_modules.user
import main_page.data_modules.team


class Match:
    def __init__(self, match_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.match_id = str(match_id)

    def get_match_info(self):
        """Returns all match info."""
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            match_name = 'Match link'
            match_link = '<a href = https://play.eslgaming.com/match/{0}> {1} </a>'.format(self.match_id, match_name)
            response['Link'] = match_link

            del response['contestants']
            del response['maps']
            del response['gameaccounts']
            del response['parameters']

            return response

    def get_match_mode(self):
        """Returns match mode ('1on1', '5on5', etc.)."""
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            return response['type']

    def get_contestants_profile(self):
        """Returns 2 teams profiles."""
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
                                contestant = main_page.data_modules.user.User(contestants[i]['user']['id'])
                                contestants_profiles.append(contestant.get_profile())
                        else:
                            if contestants[i]['team']['id'] == None:
                                contestants_profiles.append({'Team': 'Deleted team account'})
                            else:
                                contestant = main_page.data_modules.team.Team(contestants[i]['team']['id'])
                                contestants_profiles.append(contestant.get_team_info())
            return contestants_profiles

    def get_contestants_members_info(self):
        """Returns useful info of players, participating in that match."""
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
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
                        new_member = main_page.data_modules.user.User(key_player)
                        members_info.append(new_member.get_useful_info())
            return members_info

    def get_match_date_time(self):
        """Returns Match Date and its Duration."""
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        status = response['status']
        if main_page.data_modules.functions.Functions.is_error(response):
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
                final_date = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")  # !!!

                delta = final_date - beginning_date
                match_name = 'Match link'
                match_link = '<a href = https://play.eslgaming.com/match/{0}> {1} </a>'.format(self.match_id,
                                                                                               match_name)
                match_time = {"Start time": start, "End time": end, "Duration of the match": delta, 'Link': match_link}
                return match_time
            else:
                return "open"

    def get_match_results(self):
        """Returns match status and result, if it is closed."""
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
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
                user_win = main_page.data_modules.user.User(winners)
                user_lose = main_page.data_modules.user.User(losers)
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
                if "error" in user_win.get_profile() and not ("error" in user_lose.get_profile()):
                    user_win_id = "id: " + winners
                    user_win_name = "'" + "Deleted account" + "'"
                    user_win_link = "ERROR - DELETED ACCOUNT"
                    user_lose_id = "id: " + losers
                    user_lose_name = user_lose.get_profile()['nickname']
                    user_lose_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(losers,
                                                                                                        user_lose_name)
                if "error" in user_lose.get_profile() and not ("error" in user_win.get_profile()):
                    user_lose_id = "id: " + losers
                    user_lose_name = "'" + "Deleted account" + "'"
                    user_lose_link = "ERROR - DELETED ACCOUNT"
                    user_win_id = "id: " + winners
                    user_win_name = user_win.get_profile()['nickname']
                    user_win_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(winners,
                                                                                                       user_win_name)
                elif not ("error" in user_lose.get_profile()) and not ("error" in user_win.get_profile()):
                    user_win_id = "id: " + winners
                    user_win_name = user_win.get_profile()['nickname']
                    user_win_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(winners,
                                                                                                       user_win_name)
                    user_lose_id = "id: " + losers
                    user_lose_name = user_lose.get_profile()['nickname']
                    user_lose_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(losers,
                                                                                                        user_lose_name)
                if result != "draw":
                    dict = {user_win_link: 'has won!', user_lose_link: 'has lost.', 'Link': match_link}
                    return dict
                else:
                    dict = {'Result': 'There result is draw', user_win_link: user_win_id, user_lose_link: user_lose_id,
                            'Link': match_link}
                    return dict
            else:
                team_win = main_page.data_modules.team.Team(winners)
                team_lose = main_page.data_modules.team.Team(losers)
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
                if "error" in team_win.get_team_info() and not ("error" in team_lose.get_team_info()):
                    team_win_id = "id: " + winners
                    team_win_name = "'" + "Deleted account" + "'"
                    team_win_link = "ERROR - DELETED ACCOUNT"
                    team_lose_id = "id: " + losers
                    team_lose_name = team_lose.get_team_info()['name']
                    team_lose_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(losers,
                                                                                                      team_lose_name)
                if "error" in team_lose.get_team_info() and not ("error" in team_win.get_team_info()):
                    team_lose_id = "id: " + losers
                    team_lose_name = "'" + "Deleted account" + "'"
                    team_lose_link = "ERROR - DELETED ACCOUNT"
                    team_win_id = "id: " + winners
                    team_win_name = team_win.get_team_info()['name']
                    team_win_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(winners,
                                                                                                     team_win_name)
                elif not ("error" in team_win.get_team_info()) and not ("error" in team_lose.get_team_info()):
                    team_win_id = "id: " + winners
                    team_win_name = team_win.get_team_info()['name']
                    team_win_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(winners,
                                                                                                     team_win_name)
                    team_lose_id = "id: " + losers
                    team_lose_name = team_lose.get_team_info()['name']
                    team_lose_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(losers,
                                                                                                      team_lose_name)
                if result != "draw":
                    dict = {team_win_link: 'has won!', team_lose_link: 'has lost.', 'Link': match_link}
                    return dict
                else:
                    dict = {'Result': 'There result is draw', team_win_link: team_win_id, team_lose_link: team_lose_id,
                            'Link': match_link}
                    return dict

    def get_match_media(self):
        """Returns match media, if any."""
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
        """Returns current match status."""
        r = requests.get(self.base_url + "/matches/" + self.match_id)
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            status = response['status']
            return status
