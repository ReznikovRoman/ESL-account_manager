import requests
import json
import app_account_manager.main_page.data_modules.functions
import app_account_manager.main_page.data_modules.match
import app_account_manager.main_page.data_modules.team


class League:
    def __init__(self, league_id):
        self.base_url = 'http://api.eslgaming.com/play/v1/leagues/'
        self.league_id = str(league_id)

    def get_league_mode(self):
        """Returns a league mode ('1on1', '5on5', etc.)."""
        r = requests.get(self.base_url + self.league_id)
        response = json.loads(r.text)
        if response['mode'] is None:
            return response['name']['full']
        return response['mode']

    def get_league_description(self):
        """Returns full league description."""
        r = requests.get(self.base_url + self.league_id)
        response = json.loads(r.text)
        if app_account_manager.main_page.data_modules.functions.Functions.is_error(response):
            return "error"
        else:
            return response

    def get_league_results(self):
        """Returns league results."""
        r = requests.get(self.base_url + self.league_id + "/results")
        response = json.loads(r.text)
        results = []
        for match_info in response:
            match_id = match_info['id']
            match = app_account_manager.main_page.data_modules.match.Match(match_id)
            if match.get_match_status() == "closed":
                result = match.get_match_results()
                results.append(result)
            else:
                if "1on1" in League.get_league_mode(self) or "Single Elimination" in League.get_league_mode(self):
                    player_a_id = match.get_match_info()['contestants'][0]['user']['id']
                    player_b_id = match.get_match_info()['contestants'][1]['user']['id']
                    if player_a_id is None or player_b_id is None:
                        result = {'Status': 'Match is  still open', 'Match ID': match_id,
                                  'Link': app_account_manager.main_page.data_modules.functions.Functions.get_match_link(match_id),
                                  'Contestants': 'There are no 2 contestants yet'}
                        results.append(result)
                    else:
                        player_a_name = match.get_match_info()['contestants'][0]['user']['nickname']
                        player_b_name = match.get_match_info()['contestants'][1]['user']['nickname']
                        result = {'Status': 'Match is  still open', 'Match ID': match_id,
                                  'Link': app_account_manager.main_page.data_modules.functions.Functions.get_match_link(match_id),
                                  app_account_manager.main_page.data_modules.functions.Functions.get_user_link(player_a_id): player_a_id,
                                  app_account_manager.main_page.data_modules.functions.Functions.get_user_link(player_b_id): player_b_id}
                        results.append(result)
                else:
                    team_a_id = match.get_match_info()['contestants'][0]['team']['id']
                    team_b_id = match.get_match_info()['contestants'][1]['team']['id']
                    if team_a_id is None or team_b_id is None:
                        result = {'Status': 'Match is  still open', 'Match ID': match_id,
                                  'Link': app_account_manager.main_page.data_modules.functions.Functions.get_match_link(match_id),
                                  'Contestants': 'There are no 2 contestants yet'}
                        results.append(result)
                    else:
                        team_a_name = match.get_match_info()['contestants'][0]['team']['name']
                        team_b_name = match.get_match_info()['contestants'][1]['team']['name']
                        result = {'Status': 'Match is  still open', 'Match ID': match_id,
                                  'Link': app_account_manager.main_page.data_modules.functions.Functions.get_match_link(match_id),
                                  app_account_manager.main_page.data_modules.functions.Functions.get_team_link(team_a_id): team_a_id,
                                  app_account_manager.main_page.data_modules.functions.Functions.get_team_link(team_b_id): team_b_id}
                        results.append(result)
        return results

    def get_league_contestants(self):
        """Returns all contestants in the tournament."""
        r = requests.get(self.base_url + self.league_id + "/contestants")
        response = json.loads(r.text)
        return response

    def get_league_members_info(self):  # have to think about optimisation
        """Returns info about users, participating in the tournament."""
        r = requests.get(self.base_url + self.league_id + "/contestants")
        response = json.loads(r.text)
        league_members_info = []
        for contestant in response:
            team = app_account_manager.main_page.data_modules.team.Team(contestant['id'])
            league_members_info.append(team.get_useful_members_info())
        return league_members_info

    def get_matches_and_players(self):
        """Returns Matches IDs and Players Gameaccounts there."""
        r = requests.get(self.base_url + self.league_id + "/matches")
        response = json.loads(r.text)
        gameaccounts = []
        for match in response:
            match_id = match['id']
            match_id_dict = {"match id": match_id,
                             "Match link": app_account_manager.main_page.data_modules.functions.Functions.get_match_link(match_id)}
            gameaccounts_dict = match['gameaccounts']
            for key, value in gameaccounts_dict.items():
                gameaccounts_dict[key] = '<a href = https://play.eslgaming.com/player/{0}> {1} </a>'.format(key, value)
            match_id_dict.update(gameaccounts_dict)
            gameaccounts.append(match_id_dict)
        return gameaccounts

    def check_tickets(self):
        """Returns opened protests, if any."""
        r = requests.get(self.base_url + self.league_id + "/matches")
        response = json.loads(r.text)
        tickets_amount = 0
        protests = []
        matches_id = []
        if "1on1" in League.get_league_mode(self) or "Single Elimination" in League.get_league_mode(self):
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
                                    "Check your tickets": admin_protests_link_url,
                                    "Check match": match_protest_link_url}
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
