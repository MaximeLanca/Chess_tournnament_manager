from Tournament_manager.models.player import Player
from Tournament_manager.views.interface import Interface


class PlayersController:

    def __init__(self, number_of_players, player_infos):
        self.number_of_players = number_of_players
        self.player_infos = player_infos
        self.players_list = []

    def get_data_players(self) -> list:
        self.number_of_players = Interface.ask_number_of_players()
        self.players_list = Player(self.number_of_players, self.player_info)
        return self.players_list
