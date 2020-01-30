import requests
import json
import main_page.data_modules.functions
import main_page.data_modules.user


class Team:

    def __init__(self, team_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.team_id = str(team_id)

    def get_team_info(self):
        """Returns all team's info."""
        r = requests.get(self.base_url + "/teams/" + self.team_id)
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            response['Link'] = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(self.team_id,
                                                                                                response['name'])
            return response

    def get_team_members_info(self):
        """Returns all team members' info."""
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            members_info = []
            for player in response:
                member = main_page.data_modules.user.User(player)
                members_info.append(member.get_profile())
            return members_info

    def get_team_members_accounts(self):
        """Return gameaccounts of team members."""
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            members_accounts = []
            for player in response:
                member = main_page.data_modules.user.User(player)
                members_accounts.append(member.get_accounts())
            return members_accounts

    def get_useful_members_info(self):
        """Returns useful info in team members' profiles."""
        r = requests.get(self.base_url + "/teams/" + self.team_id + "/members")
        response = json.loads(r.text)
        members_useful_info = []
        for player in response:
            member = main_page.data_modules.user.User(player)
            members_useful_info.append(member.get_useful_info())
        return members_useful_info
