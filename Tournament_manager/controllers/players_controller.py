from Tournament_manager.views.menu import Menu
from Tournament_manager.models.player import Player


class PlayersController:

    @staticmethod
    def do_players_list(number_of_players: int) -> list:
        """Players creation """

        players_list = []
        for number in range(1, number_of_players + 1):
            player_infos = Menu.ask_player_infos()

            player = Player(player_infos[0], player_infos[1], player_infos[2], 0, number)
            players_list.append(player)

            print(f"The player {number} has been created.")

        print(players_list)
        return players_list

    @staticmethod
    def get_number_of_players() -> int:
        return Menu.ask_number_of_players()
