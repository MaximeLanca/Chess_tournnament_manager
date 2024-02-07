from itertools import combinations
from Tournament_manager.models.tournament import Tournament
from Tournament_manager.models.match import Match
from Tournament_manager.models.round import Round
from Tournament_manager.views.menu import Menu


class TournamentController:

    @staticmethod
    def start_tournament():
        tournament = Tournament(name='abc')
        Menu.introduction()
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

    @staticmethod
    def calculate_scores(players_list):
        players_ranking = Tournament.define_tournament_winner(players_list)
        print(f"The tournament winner is: {players_ranking[0]}")
