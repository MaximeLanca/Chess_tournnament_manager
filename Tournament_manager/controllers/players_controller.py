from Tournament_manager.models.player import Player
from Tournament_manager.views.interface import Interface


class PlayersController:

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players

    def do_players_list(self):
        """Players creation """

        for number in range(1, (self.number_of_players + 1)):
            player_infos = Interface.ask_player_infos()
            player = Player(
                number_of_player=number,
                name=player_infos[0],
                birthday=player_infos[1],
                chess_national_id=player_infos[2],
            )
            self.players_list.append(player)
