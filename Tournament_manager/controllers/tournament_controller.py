import copyfrom tinydb import TinyDB, Queryfrom Tournament_manager.controllers.players_controller import PlayersControllerfrom Tournament_manager.models.tournament import Tournamentfrom Tournament_manager.models.round import Roundfrom Tournament_manager.models.match import Matchfrom Tournament_manager.views.interface import Interfaceclass TournamentController:    def __init__(self):        self.tournament = None        self.round_ = None        self.match = None        self.save_match_list = []        self.players_controller = None    def run(self):        Interface.introduction()        tournament_name = Interface.ask_tournament_name()        tournament_location = Interface.ask_tournament_location()        tournament_start_date = str(Interface.ask_tournament_start_date())        tournament_end_date = str(Interface.ask_tournament_end_date())        number_of_round = Interface.ask_round()        self.players_controller = PlayersController(Interface.ask_number_of_players())        self.players_controller.get_data_players()        players_list = self.players_controller.players_list        self.tournament = Tournament(tournament_name,                                     tournament_location,                                     tournament_start_date,                                     tournament_end_date,                                     number_of_round,                                     players_list,                                     )        current_match = False        Interface.started_tournament(self.tournament.tournament_name)        self.start_tournament(current_match)    def speed_run(self):        Interface.second_introduction()        tournament_name = "Quick tournament"        tournament_location = "Paris"        number_of_round = 2        number_of_players = 4        tournament_start_date = "00-00-0000"        tournament_end_date = "00-00-0001"        self.players_controller = PlayersController(number_of_players)        players_list = self.players_controller.quick_do_players_list()        self.tournament = Tournament(tournament_name,                                     tournament_location,                                     tournament_start_date,                                     tournament_end_date,                                     number_of_round,                                     players_list,                                     )        current_match = False        Interface.started_tournament(self.tournament.tournament_name)        self.start_tournament(current_match)    def start_tournament(self, current_match: bool):        """Star tournament with the new matches or loaded matches according to argument 'current_match'.        Args :            current_match: Type Boolean. Determine if a match has been loaded.        """        if current_match is False:            loaded_round = 0        else:            loaded_round = self.tournament.rounds.round_number        history_pairs = self.save_history_pairs()        self.tournament.save_tournament_db()        if loaded_round == self.tournament.number_of_round:            history_pairs.append(self.tournament.rounds.matches)            self.define_players_for_match(loaded_round, history_pairs, current_match)        else:            for nb_round in range(1, self.tournament.number_of_round + 1):                db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")                db.search(Query().fragment({"Tournament Name": self.tournament.tournament_name}))                db.update({"Round Number": nb_round})                self.define_players_for_match(nb_round, history_pairs, current_match)        self.define_tournament_winner()    def define_players_for_match(self, nb_round: int, history_pairs: list, current_match: bool):        """Define players for matches.            Save history pairs to avoid duplication of matches and save the tournament        Args :            nb_round : Round number in tournament            history_pairs : played marches for history            current_match : determine if a match has been loaded        """        players_list_copy = copy.deepcopy(self.tournament.players_list)        Interface.display_round(nb_round)        while players_list_copy:            copied_player_1 = players_list_copy.pop(0)            copied_player_2 = None            for player in players_list_copy:                if (copied_player_1.chess_national_id, player.chess_national_id) not in history_pairs and (                        player.chess_national_id, copied_player_1.chess_national_id) not in history_pairs:                    copied_player_2 = player                    break            if current_match:                for player in players_list_copy:                    if player.chess_national_id == history_pairs[0]:                        copied_player_1 = player                    if player.chess_national_id == history_pairs[1]:                        copied_player_2 = player            chess_national_id_players = (copied_player_1.chess_national_id, copied_player_2.chess_national_id)            history_pairs = self.save_history_pairs(chess_national_id_players)            pairs_of_players = self.map_players(copied_player_1, copied_player_2)            matches = Match(pairs_of_players[0], pairs_of_players[1])            matches.save_match_db()            round_ = Round(nb_round, matches)            self.tournament.rounds = round_            self.ask_match_situation(round_)            players_list_copy.remove(copied_player_2)            if self.players_controller is None:                self.players_controller = PlayersController()    def map_players(self, copied_player_1: object, copied_player_2: object) -> object:        """map players between original list and copied list with chess national ID data        Arg:            copied_player_1: Copied player 1            copied_player_2: Copied player 2        Returns:            List of original players ( Object)        """        player_1 = None        player_2 = None        while player_1 is None and player_2 is None:            for player in self.tournament.players_list:                if player.chess_national_id == copied_player_1.chess_national_id:                    player_1 = player                elif player.chess_national_id == copied_player_2.chess_national_id:                    player_2 = player                    break                else:                    continue        return [player_1, player_2]    def save_history_pairs(self, pair_of_players=None):        self.save_match_list.append(pair_of_players)        return self.save_match_list    def ask_match_situation(self, round_: object):        match = round_.matches        Interface.display_match(match)        answer = Interface().ask_match_winner()        if answer == 4:            print("You have stopped the tournament.")            exit()        else:            match.define_match_winner(answer)    def define_tournament_winner(self):        self.tournament.players_list.sort(key=lambda x: x.score, reverse=True)        print(f"The tournament winner is: {self.tournament.players_list[0]} with "              f"{self.tournament.players_list[0].score} points")        Interface.players_ranking(self.tournament.tournament_name, self.tournament.players_list)    def load_tournament(self):        loaded_tournament_name = Interface.ask_tournament_for_to_load()        query = Query()        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")        loaded_tournament = db.search(query.Tournament_name == loaded_tournament_name)        # print(loaded_tournament)        self.tournament = Tournament(loaded_tournament['Tournament_name'],                                     loaded_tournament['Tournament_location'],                                     loaded_tournament['Start_date'],                                     loaded_tournament['End_date'],                                     loaded_tournament['Number_of_round'],                                     loaded_tournament['Round_number'],                                     loaded_tournament['Matches']                                     )        # loaded_players = PlayersController()        # players_list = loaded_players.get_db_data_players()## player_1_chess_national_id = dict_match["Chess national ID Player 1"]# player_2_chess_national_id = dict_match["Chess national ID Player 2"]## for player in players_list:#    if (player_1_chess_national_id == player.chess_national_id or#            player_2_chess_national_id == player.chess_national_id):#        players.append(player)#    else:#        continue# loaded_matches = Match(players[0], players[1])# loaded_round_ = Round(round_number, loaded_matches)### Interface.started_tournament(self.tournament.tournament_name)# current_match = True# self.start_tournament(current_match)