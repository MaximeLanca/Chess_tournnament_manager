from itertools import combinations
from Tournament_manager.models.match import Match
from Tournament_manager.models.round import Round
from Tournament_manager.views.interface import Interface


class Tournament:

    def __init__(self, tournament_name, round_number, players_list, match, ):
        self.tournament_name = tournament_name
        self.round_number = round_number
        self.players_list = players_list
        self.match = match
        self.round_ = None

    def start_round(self):
        for i in range(1, self.round_number + 1):
            self.round_ = Round(nb=i, matches=self.create_matches(self.players_list))
            Interface.display_round(self.round_.nb)
            self.specify_winner()
        self.define_tournament_winner(self.players_list)

    def specify_winner(self):
        for match in self.round_.matches:
            Interface.display_match(match)
            match.define_match_winner(Interface().ask_winner())

    def create_matches(self) -> list:
        matches = []
        for i in combinations(self.players_list, 2):
            matches.append(Match(player_1=i[0], player_2=i[1]))
        return matches

    def define_tournament_winner(self) -> list:
        self.players_list.sort(key=lambda x: x.score)
        print(f"The tournament winner is: {self.players_list[0]}")
        return self.players_list
