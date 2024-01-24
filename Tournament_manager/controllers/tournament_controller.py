from Tournament_manager.models.tournament import Tournament
from Tournament_manager.models.match import Match


class TournamentController:

    @staticmethod
    def start_tournament(player) -> list:
        players_of_tournament = Tournament.add_player(player)
        return players_of_tournament

    def start_match(player):
