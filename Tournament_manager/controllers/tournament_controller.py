from Tournament_manager.models.tournament import Tournament
from Tournament_manager.views.interface import Interface


class TournamentController:

    def __init__(self, tournament_name, round_number, players_list, tournament):
        self.tournament_name = tournament_name
        self.round_number = round_number
        self.players_list = players_list
        self.tournament = tournament

    def start_tournament(self):
        Interface.started_tournament(self.tournament_name)
        self.tournament = Tournament(self.tournament_name, self.round_number, self.players_list)
