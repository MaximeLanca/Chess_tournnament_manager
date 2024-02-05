from itertools import combinations
from Tournament_manager.models.tournament import Tournament
from Tournament_manager.models.match import Match
from Tournament_manager.models.round import Round


class TournamentController:

    @staticmethod
    def start_tournament():
        tournament = Tournament(name='abc')
        return tournament

    @staticmethod
    def initializing_round(nb, matches):
        return Round(nb, matches)

    @staticmethod
    def start_round(nb: int):
        return Round.display_round(nb)

    @staticmethod
    def create_matches(players_list: list) -> list:
        matches = []
        for i in combinations(players_list, 2):
            matches.append(Match(player_1=i[0], player_2=i[1]))
        return matches
