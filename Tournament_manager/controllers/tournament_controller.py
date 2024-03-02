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
        self.save_match_list = []

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
        for i in range(1, self.tournament.number_of_round + 1):
            self.specify_players(i)
        self.define_tournament_winner()

    def specify_match_winner(self, round_):
        for match in round_.matches:
            Interface.display_match(match)
            match.define_match_winner(Interface().ask_winner())
            # self.tournament.save

    def specify_players(self, round_number):
        matches = []
        players_list_copy = copy.deepcopy(self.tournament.players_list)
        Interface.display_round(round_number)

        while players_list_copy:
            index = 1
            copied_player_1 = players_list_copy[0]
            copied_player_2 = players_list_copy[index]

            history_pairs = self.save_history_pairs((copied_player_1, copied_player_2))

            while (copied_player_1, copied_player_2) in history_pairs and index < len(players_list_copy):
                copied_player_2 = players_list_copy[index]
                index += 1
            pairs_of_players = self.map_players(copied_player_1, copied_player_2)

            match = Match(pairs_of_players[0], pairs_of_players[1])
            matches.append(match)
            round_ = Round(round_number, matches)
            self.tournament.add_round(round_)
            self.specify_match_winner(round_)

            players_list_copy.remove(copied_player_1)
            players_list_copy.remove(copied_player_2)

    def map_players(self, copied_player_1, copied_player_2) -> list:
        player_1 = None
        player_2 = None

        while player_1 is None and player_2 is None:
            for player in self.tournament.players_list:
                if player.chess_national_id == copied_player_1.chess_national_id:
                    player_1 = player
                elif player.chess_national_id == copied_player_2.chess_national_id:
                    player_2 = player
                    break
                else:
                    continue
        return [player_1, player_2]

    def save_history_pairs(self, pair_of_players):
        self.save_match_list.append(pair_of_players)
        print(self.save_match_list)
        return self.save_match_list

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
        print(f"The tournament winner is: {self.tournament.players_list[0]} with "
              f"{self.tournament.players_list[0].score} points")
