from Tournament_manager.controllers.players_controller import PlayersController
from Tournament_manager.views.menu import Menu


class GlobalController:

    @staticmethod
    def get_list_of_players() -> list:
        number_of_players = Menu.ask_number_of_players()
        players_list = PlayersController.do_players_list(number_of_players)
        return players_list
