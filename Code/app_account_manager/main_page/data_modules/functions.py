from datetime import datetime
import winsound
import main_page.data_modules.team
import time

import simpleaudio as sa
# import numpy as np

from playsound import playsound


class Functions:
    # FUNCTIONS
    @staticmethod
    def check_accounts(users, account_type):  # doesn't work properly ATM
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

    @staticmethod
    def check_input(user_input, info):
        """Checks user input info, result - 'True' | 'False'."""
        if user_input not in info:
            return False
        else:
            return True

    @staticmethod
    def check_date(date):  # ?
        if date[0] == "0":
            return date[1]
        else:
            return date

    @staticmethod
    def get_duration_period(date):
        """Returns match duration."""
        now = datetime.now()

        end_date = date[:10]
        end_time = date[11:19]
        end = end_date + ' ' + end_time
        final_date = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")  # !

        delta = final_date - now
        return delta

    @staticmethod
    def is_error(a_dict):
        """Checks whether the is an error in ESL-Api response or not, result - 'True' | 'False'."""
        if "error" in a_dict.keys():
            return True
        else:
            return False

    @staticmethod
    def beep():
        """Creates sound/Beeps; Works only with Windows OS."""
        duration = 1750  # millisecond
        freq = 2500  # Hz OR 2500 Hz
        return winsound.Beep(freq, duration)

    @staticmethod
    def make_sounds(sound):  # 'playsound' library
        """Makes sounds like 'Ehe-Ehe-Hey!!! or 'Ha!' or 'Hey-Hop!!!'."""
        # sound = 'egegey.mp3'\
        audio = playsound(sound)
        return audio

    # -------HYPERLINKS-------
    @staticmethod
    def get_user_link(user_id):
        """Returns User Link."""
        user_link = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(user_id, "User profile link")
        return user_link

    @staticmethod
    def get_team_link(team_id):
        """Returns Team Link."""
        team_name = main_page.data_modules.team.Team(team_id).get_team_info()['name']
        team_link = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(team_id, team_name)
        return team_link

    @staticmethod
    def get_match_link(match_id):
        """Returns Match Link."""
        match_name = 'Match link'
        match_link = '<a href = https://play.eslgaming.com/match/{0}> {1} </a>'.format(match_id, match_name)
        return match_link

    @staticmethod
    def print_dict(dictionary, window, refresh_time):
        """Prints a dictionary, params: dict, output_window, refresh_time."""
        for key, value in dictionary.items():
            window.append("{0}: {1}".format(key, value))
            time.sleep(refresh_time)
        window.append("")


# Functions.make_sounds('1-2_sounds.mp3')



