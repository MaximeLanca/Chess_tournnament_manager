from controllers.players_controller import PlayersController
from views.menu import Menu


class GlobalController:

    @staticmethod
    def get_number_of_players() -> dict:
        number_of_players = Menu.ask_number_of_players()
        players_list = PlayersController.do_players_list(number_of_players)
        print(players_list)
        return players_list
