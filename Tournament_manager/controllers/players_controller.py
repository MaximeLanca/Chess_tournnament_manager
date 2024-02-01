from Tournament_manager.views.menu import Menu
from Tournament_manager.models.players import Player


class PlayersController:

    @staticmethod
    def do_players_list(number_of_players: int) -> dict:
        """Players creation """

        players_list = {}
        for number in range(0, number_of_players):
            player_infos = Menu.ask_player_infos()
            players_list[number] = Player.get_information_players(player_infos[0],
                                                                  player_infos[1],
                                                                  player_infos[2],
                                                                  0)
            print(f"The player {number + 1} has been created.")
        print(players_list)
        return players_list

    @staticmethod
    def get_number_of_players() -> int:
        return Menu.ask_number_of_players()
