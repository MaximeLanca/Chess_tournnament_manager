import copyfrom Tournament_manager.controllers.players_controller import PlayersControllerfrom Tournament_manager.models.tournament import Tournamentfrom Tournament_manager.models.round import Roundfrom Tournament_manager.models.match import Matchfrom Tournament_manager.views.interface import Interfaceclass TournamentController:    def __init__(self):        self.tournament = None        self.round_ = None        self.match = None        self.matches_id_list = []        self.players_controller = None        self.players_list = []        self.loaded_history_matches = []        self.loaded_current_match = []    def run(self):        """Star the program for prepare tournament. """        Interface.introduction()        tournament_name = Interface.ask_tournament_name()        tournament_location = Interface.ask_tournament_location()        tournament_start_date = str(Interface.ask_tournament_start_date())        tournament_end_date = str(Interface.ask_tournament_end_date())        number_of_round = Interface.ask_round()        self.players_controller = PlayersController(Interface.ask_number_of_players())        self.players_controller.get_data_players()        self.players_list = self.players_controller.players_list        players_id = []        for player in self.players_list:            players_id = [player.chess_national_id]        self.tournament = Tournament(tournament_name,                                     tournament_location,                                     tournament_start_date,                                     tournament_end_date,                                     number_of_round,                                     players_id,                                     )        current_match = False        Interface.started_tournament(self.tournament.tournament_name)        self.start_tournament(current_match)    def speed_run(self):        Interface.second_introduction()        tournament_name = "Quick tournament1"        tournament_location = "Paris"        number_of_round = 2        number_of_players = 4        tournament_start_date = "00-00-0000"        tournament_end_date = "00-00-0001"        self.players_controller = PlayersController(number_of_players)        self.players_list = self.players_controller.quick_do_players_list()        players_id = []        for player in self.players_list:            players_id.append(player.chess_national_id)        self.tournament = Tournament(tournament_name,                                     tournament_location,                                     tournament_start_date,                                     tournament_end_date,                                     number_of_round,                                     players_id,                                     )        Interface.started_tournament(self.tournament.tournament_name)        self.start_tournament(current_match=False)    def start_tournament(self, current_match: bool):        """Star tournament with the new matches or loaded matches according to argument 'current_match'.        :param current_match: Determine if a match has been loaded.        """        self.tournament.round_history = []        if current_match:            round_number = self.round_.round_number        else:            round_number = 1            self.tournament.save_tournament_db()        for nb_round in range(round_number, self.tournament.number_of_round + 1):            if current_match is False:                self.round_ = Round(nb_round)            self.round_.save_round_db()            self.round_.get_data_round_db()            self.tournament.round_history.append(self.round_.last_round_id)            self.define_players_for_match(nb_round, current_match)            self.round_.update_round()            self.tournament.update_tournament()            current_match = False        self.tournament.update_tournament()        self.define_tournament_winner()    def define_players_for_match(self, nb_round: int, current_match: bool):        """Define players for matches.            Save history pairs to avoid duplication of matches and save the tournament        :param nb_round : Round number in tournament        :param current_match : determine if a match has been loaded        """        history_pairs = self.tournament.matches_history        Interface.display_round(nb_round)        players_list_copy = copy.deepcopy(self.players_list)        if current_match:            players_list_copy = self.remove_played_players_of_list(players_list_copy)        while players_list_copy:            copied_player_1 = None            copied_player_2 = None            if players_list_copy:                copied_player_1 = players_list_copy.pop(0)                for player in players_list_copy:                    if (copied_player_1.chess_national_id, player.chess_national_id) not in history_pairs and (                            player.chess_national_id, copied_player_1.chess_national_id) not in history_pairs:                        copied_player_2 = player                        break                chess_national_id_players_pair = (copied_player_1.chess_national_id, copied_player_2.chess_national_id)            else:                players_list_copy = copy.deepcopy(self.players_list)                chess_national_id_players_pair = self.loaded_current_match[0]                for player in players_list_copy:                    if player.chess_national_id == self.loaded_current_match[0][0]:                        index = players_list_copy.index(player)                        copied_player_1 = players_list_copy.pop(index)                    if player.chess_national_id == self.loaded_current_match[0][1]:                        index = players_list_copy.index(player)                        copied_player_2 = players_list_copy[index]            self.tournament.matches_history.append(chess_national_id_players_pair)            pairs_of_players = self.map_players(copied_player_1, copied_player_2)            players_list_copy.remove(copied_player_2)            if current_match is False:                self.match = Match(pairs_of_players[0], pairs_of_players[1], winner=None)            self.start_match()            self.round_.matches = [self.loaded_history_matches]            self.round_.update_round()            current_match = False    def start_match(self):        Interface.display_match(self.match)        answer = Interface().ask_match_winner()        self.match.save_match_db()        self.round_.id_matches_list.append(self.match.id_)        self.round_.update_round()        self.tournament.update_tournament()        if answer == 4:            print("You have stopped the tournament.")            exit()        else:            self.match.define_match_winner(answer)            self.match.update_result_match()            self.match.player_1.update_players_score()            self.match.player_2.update_players_score()    def remove_played_players_of_list(self, players_list_copy):        removed_players = []        for player in players_list_copy:            for match in self.tournament.matches_history:                if player.chess_national_id == match[0]:                    removed_players.append(player)                if player.chess_national_id == match[1]:                    removed_players.append(player)        for player in removed_players:            players_list_copy.remove(player)        return players_list_copy    def map_players(self, copied_player_1: object, copied_player_2: object) -> object:        """map players between original list and copied list with chess national ID data        :param:            copied_player_1: Copied player 1            copied_player_2: Copied player 2        :return:            List of original players ( Object)        """        player_1 = None        player_2 = None        while player_1 is None and player_2 is None:            for player in self.players_list:                if player.chess_national_id == copied_player_1.chess_national_id:                    player_1 = player                elif player.chess_national_id == copied_player_2.chess_national_id:                    player_2 = player                    break                else:                    continue        return [player_1, player_2]    def define_tournament_winner(self):        """Define the winner with the highest score """        self.players_list.sort(key=lambda x: x.score, reverse=True)        print(f"The tournament winner is: {self.players_list[0]} with "              f"{self.players_list[0].score} points")        Interface.players_ranking(self.tournament.tournament_name, self.players_list)    def load_tournament(self):        """Load a tournament in db with all datas players"""        requested_tournament = Interface.ask_tournament_for_to_load()        self.check_loaded_tournament_name(requested_tournament)        self.tournament = Tournament.from_db(requested_tournament)        loaded_players = PlayersController()        self.players_list = loaded_players.get_db_data_players(self.tournament.players_id)        # loaded_id_rounds = self.tournament.round_history        round_list = []        for id_round in self.tournament.round_history:            rd_ = Round.from_db(id_round[0])            round_list.append(rd_)            for match_id in rd_.id_matches_list:                loaded_match = Match.from_db(match_id)                players_pairs = (loaded_match.player_1, loaded_match.player_2)                if loaded_match.winner is None:                    self.loaded_current_match.append(players_pairs)                else:                    self.tournament.matches_history.append(players_pairs)        self.round_ = round_list[-1]        self.prepare_round_for_load_tournament()        current_match = True        Interface.started_tournament(self.tournament.tournament_name)        self.start_tournament(current_match)    def prepare_round_for_load_tournament(self):        """Check if a tournament has been played """        matches_list = []        for match in self.loaded_current_match[0]:            matches_list.append(match)        players_current_match = []        for player in self.players_list:            if player.chess_national_id in matches_list:                players_current_match.append(player)        self.match = Match(players_current_match[0], players_current_match[1], None)        self.round_.matches = self.match    def check_loaded_tournament_name(self, tournament_name: str):        """Check if a tournament has been played        :param            tournament_name: tournament name        """        requested_tournament = Tournament.search_tournament(tournament_name)        while True:            if requested_tournament:                return requested_tournament            else:                answer = Interface.report_tournament_error(tournament_name)                if answer == "t":                    self.load_tournament()                elif answer == "e":                    exit()                else:                    print("Not valid answer ")