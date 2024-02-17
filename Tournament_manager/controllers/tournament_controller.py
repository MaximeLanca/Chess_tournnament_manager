from itertools import combinations

from Tournament_manager.controllers.players_controller import PlayersController
from Tournament_manager.models.tournament import Tournament
from Tournament_manager.models.round import Round
from Tournament_manager.models.match import Match
from Tournament_manager.views.interface import Interface


class TournamentController:

    def __init__(self):
        self.tournament = None
        self.round_ = None

    def launch(self):
        Interface.introduction()
        tournament_name = Interface.ask_tournament_name()
        round_number = Interface.ask_round()

        players_list = PlayersController(Interface.ask_number_of_players())
        self.tournament = Tournament(tournament_name, round_number, self.round_, players_list, )

    def start_tournament(self):
        for i in range(1, self.tournament.round_number + 1):
            self.tournament.round_ = Round(nb=i, matches=self.start_matches(self.tournament.players_list))
            Interface.display_round(self.tournament.round_.nb)
            self.specify_winner()
        self.define_tournament_winner(self.tournament.players_list)

    def specify_winner(self):
        for match in self.tournament.round_:
            Interface.display_match(match)
            match.define_match_winner(Interface().ask_winner())

    def start_matches(self) -> list:
        matches = []
        for i in combinations(self.tournament.players_list, 2):
            matches.append(Match(player_1=i[0], player_2=i[1]))
        return matches

    def define_tournament_winner(self) -> list:
        self.players_list.sort(key=lambda x: x.score)
        print(f"The tournament winner is: {self.players_list[0]}")
        return self.players_list
