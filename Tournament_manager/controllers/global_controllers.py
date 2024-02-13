from Tournament_manager.controllers.players_controller import PlayersController
from Tournament_manager.views.interface import Interface
from Tournament_manager.controllers.tournament_controller import TournamentController


class GlobalController:
    def launch():
        Interface.introduction()
        tournament_name = Interface.ask_tournament_name()
        player_infos = Interface.ask_player_infos()
        round_number = Interface.ask_round()

        players_list = PlayersController(player_infos)
        TournamentController.start_tournament(tournament_name, round_number, players_list)
