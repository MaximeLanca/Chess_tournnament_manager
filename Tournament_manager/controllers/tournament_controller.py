import copy
import itertools
from re import M
from typing import List
from Tournament_manager.controllers.players_controller import PlayersController
from Tournament_manager.models.tournament import Tournament
from Tournament_manager.models.round import Round
from Tournament_manager.models.match import Match
from Tournament_manager.views.interface import Interface
from Tournament_manager.models.database import Database


class TournamentController:

    def __init__(self):
        self.tournament = None
        self.round_ = None
        self.match = None

    def run(self):
        Interface.introduction()
        tournament_name = Interface.ask_tournament_name()
        number_of_round = Interface.ask_round()

        players_controller = PlayersController(Interface.ask_number_of_players())
        players_controller.do_players_list()
        self.tournament = Tournament(tournament_name,
                                     number_of_round,
                                     players_controller.players_list,
                                     )

        Interface.started_tournament(self.tournament.tournament_name)
        self.start_tournament()

    def speed_run(self):
        Interface.second_introduction()
        tournament_name = "Quick tournament"
        number_of_round = 2
        number_of_players = 4
        players_controller = PlayersController(number_of_players)
        players_controller.quick_do_players_list()
        self.tournament = Tournament(tournament_name,
                                     number_of_round,
                                     players_controller.players_list,
                                     )

        Interface.started_tournament(self.tournament.tournament_name)
        self.start_tournament()

    def start_tournament(self):
        for i in range(1, self.tournament.number_of_round):
            round_ = Round(round_number=i, matches=self.specify_players())
            self.tournament.add_round(round_)
            Interface.display_round(round_.round_number)
            self.specify_winner(round_)
        self.define_tournament_winner()

    def specify_winner(self, round_):
        for match in round_.matches:
            Interface.display_match(match)
            match.define_match_winner(Interface().ask_winner())
            # self.tournament.save

    def specify_players(self):
        players_list_copy = copy.deepcopy(self.tournament.players_list)

        while players_list_copy:
            copied_player_1 = players_list_copy[0]
            index = 1
            copied_player_2 = players_list_copy[index]

            pairs_list = self.save_history_pairs((copied_player_1, copied_player_2))
            pairs_of_players = self.map_players(copied_player_1, copied_player_2)

            while (copied_player_1, copied_player_2) in pairs_list and index < len(players_list_copy):
                copied_player_2 = players_list_copy[index]
                index += 1

            players_list_copy.remove(players_list_copy[0])
            return pairs_of_players

    def map_players(self, copied_player_1, copied_player_2) -> list:
        matches = []
        player_1 = None
        player_2 = None
        match = None
        # preliminary_list = [player_1, player_2]
        for player in self.tournament.players_list:
            if player.chess_national_id == copied_player_1.chess_national_id:
                player_1 = player
            if player.chess_national_id == copied_player_2.chess_national_id:
                player_2 = player

        if player_1 is not None and player_2 is not None:
            match = Match(player_1, player_2)
            matches.append(match)
        else:
            print("Impossible de trouver un des joueurs.")
        matches.append(match)
        return matches

    @staticmethod
    def save_history_pairs(pairs):
        pairs_list = []
        pairs_list.append(pairs)
        return pairs_list

        # matches = []
        # player_2_index = 0
        # items = list(range(len(self.tournament.players_list)))
        # history_pairs = []
        # while items:
        #    player_1 = self.tournament.players_list[items[0]]
        #    j = 1
        #    player_2 = self.tournament.players_list[items[j]]
        #
        #    while (player_1, player_2) in history_pairs and j < len(items):
        #        player_2 = self.tournament.players_list[items[j]]
        #        player_2_index = items[j]
        #        j += 1
        #
        #    match = Match(player_1, player_2)
        #    matches.append(match)
        #    history_pairs.append((player_1, player_2))
        #
        #    items.remove(player_2_index)
        #    items.remove(items[0])
        # print(items)

    def define_tournament_winner(self):
        self.tournament.players_list.sort(key=lambda x: x.score, reverse=True)
        print(f"The tournament winner is: {self.tournament.players_list[0]} with"
              f"{self.tournament.players_list[0].score} points")
