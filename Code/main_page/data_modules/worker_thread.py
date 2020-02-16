from PyQt5.QtCore import QThread, pyqtSignal
import time
import main_page.data_modules.refresh_thread as _refresh_thread
import main_page.data_modules.verifier as _verifier
import main_page.data_modules.user as _user
import main_page.data_modules.functions as _functions
import main_page.data_modules.team as _team
import main_page.data_modules.match as _match
import main_page.data_modules.league as _league
import email_handler


class BackendQThread(QThread):
    quit_thread = pyqtSignal(name='close_thread')

    def __init__(self, mainwindow, task):
        super(BackendQThread, self).__init__()
        self.mainwindow = mainwindow
        self.task = task
        self.update_thread = _refresh_thread.RefreshThread(self.mainwindow, "start")

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
        # elif self.task == 14:  # Get: Info about all players, participating in the tournament
            # self.get_league_contestants_info()
        elif self.task == 14:  # Get: All matches IDs and gameaccounts there
            self.get_league_matches_gameaccounts()
        elif self.task == 15:  # Check open protests
            self.check_protests()
        elif self.task == 16:  # AUTO ADMIN
            self.auto_admin()
        # elif self.task == 18:  # Get: All members, who doesn't have specific gameaccounts
            # self.get_suspects()
        else:
            pass

    def get_player_acc(self):  # Player Account
        """Get all user's gameaccounts."""
        id = self.mainwindow.input_player_id.text()
        if id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter player ID' ")
        else:
            if not _verifier.Verifier(id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_user = _user.User(id)
                self.mainwindow.output_info.append(test_user.get_accounts())
                self.mainwindow.output_info.append(_functions.Functions.get_user_link(id))
                self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def get_player_profile(self):  # Player Profile
        """View user's profile."""
        id = self.mainwindow.input_player_id.text()
        if id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter player ID' ")
        else:
            if not _verifier.Verifier(id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_user = _user.User(id)
                user_profile = test_user.get_profile()
                _functions.Functions.print_dict(user_profile, self.mainwindow.output_info, 0.025)
        self.update_thread.terminate_thread()

    def get_team_info(self):  # Team Info
        """View team's info."""
        team_id = self.mainwindow.input_team_id.text()
        if team_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter team ID' ")
        else:
            if not _verifier.Verifier(team_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_team = _team.Team(team_id)
                if test_team.get_team_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Team with that ID doesn't exist")
                else:
                    _functions.Functions.print_dict(test_team.get_team_info(), self.mainwindow.output_info, 0.025)
        self.update_thread.terminate_thread()

    def get_members_info(self):  # Team Members Info
        """Get all team members' info."""
        team_id = self.mainwindow.input_team_id.text()
        if team_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter team ID' ")
        else:
            if not _verifier.Verifier(team_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_team = _team.Team(team_id)
                members_info = test_team.get_team_members_info()
                if members_info == "error":
                    self.mainwindow.output_info.append("\nERROR: Team with that ID doesn't exist")
                else:
                    for i in range(len(members_info)):
                        _functions.Functions.print_dict(members_info[i], self.mainwindow.output_info, 0.015)
                        time.sleep(0.025)
                    self.mainwindow.output_info.append(
                        _functions.Functions.get_team_link(team_id))
                    self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def get_some_members_info(self):  # Specific team members info
        """Prints only 'id', 'nickname', 'region' and 'Link' of all team members."""
        team_id = self.mainwindow.input_team_id.text()
        if team_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter team ID' ")
        else:
            if not _verifier.Verifier(team_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_team = _team.Team(team_id)
                members_info = test_team.get_team_members_info()
                options = ("id", "nickname", "region", "Link")
                i = 0
                members_accounts = test_team.get_team_members_accounts()
                if members_info == "error" or members_accounts == "error":
                    self.mainwindow.output_info.append("\nERROR: Team with that ID doesn't exist")
                else:
                    for member in members_info:
                        member_id = member['id']
                        team_member = _user.User(member_id)
                        self.mainwindow.output_info.append(members_accounts[i])
                        for key, value in team_member.get_profile().items():
                            if _functions.Functions.check_input(key, options):
                                self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                                time.sleep(0.025)
                            else:
                                continue
                            time.sleep(0.1)
                        self.mainwindow.output_info.append("")
                        i += 1
                    self.mainwindow.output_info.append(
                        _functions.Functions.get_team_link(team_id))
                    self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def get_general_match_info(self):  # Match info
        """Get match info - all settings/data."""
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not _verifier.Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_match = _match.Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    _functions.Functions.print_dict(test_match.get_match_info(), self.mainwindow.output_info, 0.015)
        self.update_thread.terminate_thread()

    def get_contestants_profiles(self):
        """View 2 teams profiles."""
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not _verifier.Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_match = _match.Match(match_id)
                teams_profiles = test_match.get_contestants_profile()
                if teams_profiles == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    for i in range(len(teams_profiles)):
                        _functions.Functions.print_dict(teams_profiles[i], self.mainwindow.output_info, 0.015)
                        time.sleep(0.025)
                    self.mainwindow.output_info.append(_functions.Functions.get_match_link(match_id))
                    self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def get_match_members_profiles(self):
        """View all match members' profiles"""
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not _verifier.Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_match = _match.Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    contestants_info = test_match.get_contestants_members_info()
                    for i in range(len(contestants_info)):
                        _functions.Functions.print_dict(contestants_info[i], self.mainwindow.output_info, 0.1)
                        time.sleep(0.2)
                    self.mainwindow.output_info.append(
                        _functions.Functions.get_match_link(match_id))
                    self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def get_match_date(self):
        """Get match date and its duration."""
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not _verifier.Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_match = _match.Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    date = test_match.get_match_date_time()
                    if date == "open":
                        self.mainwindow.output_info.append("Match isn't closed yet")
                        self.mainwindow.output_info.append("")
                    else:
                        _functions.Functions.print_dict(date, self.mainwindow.output_info, 0.015)
        self.update_thread.terminate_thread()

    def get_match_result(self):
        """Get match status and result, if it is closed."""
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not _verifier.Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_match = _match.Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    match_status = test_match.get_match_status()
                    self.mainwindow.output_info.append("Match status: {0}".format(match_status))
                    if match_status == "closed":
                        _functions.Functions.print_dict(test_match.get_match_results(), self.mainwindow.output_info, 0.1)
        self.update_thread.terminate_thread()

    def get_match_media(self):
        """Get match media, if any."""
        match_id = self.mainwindow.input_match_id.text()
        if match_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter match ID' ")
        else:
            if not _verifier.Verifier(match_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_match = _match.Match(match_id)
                if test_match.get_match_info() == "error":
                    self.mainwindow.output_info.append("\nERROR: Match with that ID doesn't exist")
                else:
                    match_status = test_match.get_match_status()
                    if match_status != "closed":
                        self.mainwindow.output_info.append("Match is still open, there is no match media yet")
                    else:
                        match_results = test_match.get_match_media()
                        if match_results == "nothing":
                            self.mainwindow.output_info.append("There is no match media in this match")
                        else:
                            tournament_condition = False
                            if len(match_results) == 10:  # FOR FUTURE
                                tournament_condition = True
                            for i in range(len(match_results)):
                                file_link = '<a href = {0}> file_{1} </a>'.format(match_results[i], i + 1)
                                self.mainwindow.output_info.append("file №{0}: {1}".format(i + 1, file_link))
                                time.sleep(0.2)
                        self.mainwindow.output_info.append(
                            _functions.Functions.get_match_link(match_id))
                        self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def get_league_info(self):
        """View all league settings"""
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_league = _league.League(league_id)
                league_description = test_league.get_league_description()
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    _functions.Functions.print_dict(league_description, self.mainwindow.output_info, 0.015)
        self.update_thread.terminate_thread()

    def get_league_results(self):
        """Get league results - all matches' results."""
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_league = _league.League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    league_results = test_league.get_league_results()
                    for result in league_results:
                        _functions.Functions.print_dict(result, self.mainwindow.output_info, 0.020)
                        time.sleep(0.025)
        self.update_thread.terminate_thread()

    def get_league_contestants(self):
        """Get info about all teams, participating in the tournament."""
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_league = _league.League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    league_contestants = test_league.get_league_contestants()
                    for contestant in league_contestants:
                        contestant['Link'] = '<a href = https://play.eslgaming.com/team/{0}> {1} </a>'.format(
                            contestant['id'], contestant['name'])
                        for key, value in contestant.items():
                            if key != "alias":
                                self.mainwindow.output_info.append("{0}: {1}".format(key, value))
                                time.sleep(0.03)
                        self.mainwindow.output_info.append("")
                        time.sleep(0.2)
                    self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def get_league_contestants_info(self):
        """Get info about all users, participating in the tournament."""
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                self.mainwindow.output_info.append("")
                test_league = _league.League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    if test_league.get_league_mode() == "1on1":
                        for player in test_league.get_league_members_info():
                            if player == "error":
                                self.mainwindow.output_info.append("Account is deleted")
                            else:
                                _functions.Functions.print_dict(player, self.mainwindow.output_info, 0.0002)
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
        self.update_thread.terminate_thread()

    def get_league_matches_gameaccounts(self):
        """Get all matches and gameaccounts there."""
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_league = _league.League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    matches = test_league.get_matches_and_players()
                    for match in matches:
                        _functions.Functions.print_dict(match, self.mainwindow.output_info, 0.025)
                        time.sleep(0.1)
                    self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def check_protests(self):
        """Checks protests; beeps, if a new one opens."""
        league_id = self.mainwindow.input_league_id.text()
        setup_info = email_handler.get_file_info()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                BackendQThread.set_refresh_thread(self)

                test_league = _league.League(league_id)
                if test_league.get_league_description() == "error":
                    self.mainwindow.output_info.append("\nERROR: League with that ID doesn't exist")
                else:
                    protests = test_league.check_tickets()[0]
                    total_protests_amount = test_league.check_tickets()[1]
                    self.mainwindow.output_info.append(
                        "Total amount of opened tickets: {0}".format(total_protests_amount))
                    # =======Make Sounds========

                    if email_handler.get_status(setup_info, 'notification'):
                        if total_protests_amount == 1 or total_protests_amount == 2:
                            _functions.Functions.make_sounds('1-2_sounds.mp3')
                        elif total_protests_amount > 2:
                            _functions.Functions.make_sounds('new_sounds.mp3')
                    # ==========================
                    for protest in protests:
                        _functions.Functions.print_dict(protest, self.mainwindow.output_info, 0.015)
                        # _functions.Functions.beep()
                        time.sleep(0.025)
                    self.mainwindow.output_info.setOpenExternalLinks(True)
        self.update_thread.terminate_thread()

    def auto_admin(self):
        """Automatically checks new protests in a certain (refresh_time) period of time."""
        league_id = self.mainwindow.input_league_id.text()
        refresh_time = self.mainwindow.input_refresh_time.text()

        setup_info = email_handler.get_file_info()
        _email_handler = email_handler.EmailHandler(setup_info)

        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                if refresh_time == "":
                    self.mainwindow.output_info.append(
                        "\nERROR: 'Enter  'refresh time', so in how many minutes you want program to refresh, e.g '5' means, data will refresh each 5 minutes' ")
                else:
                    if not _verifier.Verifier.check_refresh_time(league_id, refresh_time):
                        self.mainwindow.output_info.append("\nERROR: 'Incorrect Time Format - should be: 5 OR 5.5' ")
                    else:
                        BackendQThread.set_refresh_thread(self)

                        if _league.League(league_id).get_league_description() == "error":
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
                                test_league = _league.League(league_id)
                                protests = test_league.check_tickets()[0]
                                total_protests_amount = test_league.check_tickets()[1]
                                email_text = ""  # Text, which will be send to the admin email
                                total_protests_amount_string = 'Total amount of opened tickets'
                                self.mainwindow.output_info.append(
                                    '<span>{0}: {1}<span>'.format(total_protests_amount_string, total_protests_amount))
                                for protest in protests:
                                    for key, value in protest.items():
                                        email_text += '{0}: {1}'.format(key, value) + '\n'
                                        self.mainwindow.output_info.append('<span>{0}: {1}<span>'.format(key, value))
                                        time.sleep(0.015)
                                    email_text += '\n'
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
                                    # =======_SOUNDS_=======
                                    if email_handler.get_status(setup_info, 'notification'):
                                        if sounds_amount > 0:
                                            if sounds_amount == 1 or sounds_amount == 2:
                                                _functions.Functions.make_sounds('1-2_sounds.mp3')
                                            elif sounds_amount > 2:
                                                _functions.Functions.make_sounds('new_sounds.mp3')
                                    # ====_EMAIL_====
                                    if sounds_amount > 0:
                                        if email_handler.get_status(setup_info, 'email'):
                                            _email_handler.send_email(email_text)
                                            # try:
                                                # email_handler.send_email(email_text)
                                                # if email_handler.send_email(email_text) == 'Email not found!':
                                                    # raise Exception
                                            # except Exception:
                                                # self.mainwindow.output_info.append("Email not found!")
                                                # self.mainwindow.output_info.append("")
                                    # ====NEW_PROTESTS====
                                    my_file = open("matches_ids.txt", 'a')
                                    for id in matches_id:
                                        if id not in values_from_file:
                                            my_file.write("{0}\n".format(id))
                                    my_file.close()
                                    # ==========
                                    time.sleep(refresh_time_seconds)

    def get_suspects(self):
        """Get all users, who have barrage or don't have a specific (e.g. 'Uplay') account."""
        league_id = self.mainwindow.input_league_id.text()
        if league_id == "":
            self.mainwindow.output_info.append("\nERROR: 'Enter league ID' ")
        else:
            if not _verifier.Verifier(league_id).check_id():
                self.mainwindow.output_info.append("\nERROR: 'Incorrect ID' ")
            else:
                account_types = ["Uplay:", "PSN account:", "Xbox nickname:"]
                platform_type = self.mainwindow.input_account_type.text()
                if platform_type == "":
                    self.mainwindow.output_info.append("ERROR: 'Enter account type' ")
                else:
                    if platform_type not in account_types:
                        self.mainwindow.output_info.append(
                            "ERROR: 'Please, use only 'Uplay:', 'PSN account:' or 'Xbox nickname:' ")
                    else:
                        BackendQThread.set_refresh_thread(self)

                        if _functions.Functions.check_input(platform_type, account_types):
                            test_league = _league.League(league_id)
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
                                                            self.mainwindow.output_info.append(
                                                                "{0}: {1}".format(key_new, value_new))
                                                            time.sleep(0.015)
                                                        else:
                                                            self.mainwindow.output_info.append(
                                                                "All users have gameaccounts in their profiles and nobody has barrage")
                                                    self.mainwindow.output_info.append("")
                                                    time.sleep(0.025)
                            self.mainwindow.output_info.append("")
        self.update_thread.terminate_thread()

    def terminate_thread(self):
        """Terminates thread."""
        self.terminate()

    def set_refresh_thread(self):
        """Creates a new Refresh Thread."""
        self.update_thread.start()
        self.mainwindow.threads.append(self.update_thread)
