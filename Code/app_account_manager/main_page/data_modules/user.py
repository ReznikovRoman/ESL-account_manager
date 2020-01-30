import requests
import json
import main_page.data_modules.functions


class User:
    def __init__(self, id):
        self.base_url = 'http://api.eslgaming.com/play/v1/'
        self.id = str(id)

    def get_profile(self):
        """Returns user profile."""
        r = requests.get(self.base_url + "/users/" + self.id + "/basicprofile")
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            link = main_page.data_modules.functions.Functions.get_user_link(self.id)
            response['Link'] = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(self.id, response['nickname'])
            return response

    def get_accounts(self):
        """Returns gameaccounts of a user."""
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

    def get_useful_info(self):
        """Returns Useful Info in user profile: 'id', 'nickname', 'gameaccount', 'region', 'isBarred'"""
        r = requests.get(self.base_url + "/users/" + self.id + "/basicprofile")
        response = json.loads(r.text)
        if main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            new_user = User(self.id)
            user_accounts = new_user.get_accounts()
            new_dict = {"gameaccounts": user_accounts, "id": response.get("id"), "nickname": response.get("nickname"),
                        "region": response.get("region")}
            isBarred = response.get("isBarred")
            if isBarred == False:
                new_dict['isBarred'] = False
            else:
                new_dict['isBarred'] = True
                new_dict['barredUntil'] = response.get('barredUntil')
            new_dict['Link'] = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(self.id,
                                                                                                  response['nickname'])
            return new_dict

    def get_special_account(self, option):  # special account --> e.g "psn_online_id"
        """Returns special (e.g. 'Uplay') gameaccount."""
        r = requests.get(self.base_url + "/users/" + self.id + "/gameaccounts")
        response = json.loads(r.text)
        for i in range(len(response)):
            dict = response[i]
            if dict['type'] == option:
                return dict['value']

