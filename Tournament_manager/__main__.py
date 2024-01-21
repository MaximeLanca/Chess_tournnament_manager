from controllers.global_controllers import GlobalController
from views.menu import Menu


class Main:
    Menu.introduction()
    GlobalController.get_number_of_players()
    # players_list = PlayersController.do_players_list()


Main()
