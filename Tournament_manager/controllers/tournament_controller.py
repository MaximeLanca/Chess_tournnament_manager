from Tournament_manager.models.tournament import Tournament
from Tournament_manager.models.match import Match
from Tournament_manager.models.rounds import Round


class TournamentController:

    @staticmethod
    def start_tournament():
        tournament = Tournament(name='abc')
        return tournament

    @staticmethod
    def initializing_round(nb, matches):
        return Round(nb, matches)

    @staticmethod
    def start_round(nb):
        return Round.display_round(nb)

    @staticmethod
    def create_matches(players_list) -> list:
        matches = []
        for i in range(0, len(players_list) - 1, 2):
            matches.append(Match(player_1=players_list[i], player_2=players_list[i + 1]))
        return matches
