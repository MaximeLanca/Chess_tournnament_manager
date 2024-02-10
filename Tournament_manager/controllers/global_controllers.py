from Tournament_manager.controllers.players_controller import PlayersController
from Tournament_manager.views.menu import Menu
from Tournament_manager.controllers.tournament_controller import TournamentController


class GlobalController:

    @staticmethod
    def lunch():

        TournamentController.start_tournament()
        players_list = GlobalController.get_list_of_players()
        round_number = Menu.ask_round()

        for i in range(1, round_number + 1):
            round_ = TournamentController.initializing_round(nb=i,
                                                             matches=TournamentController.create_matches(players_list))
            TournamentController.start_round(round_)
            for match in round_.matches:
                Menu.display_match(match)
                match.define_match_winner(Menu().ask_winner())
        TournamentController.calculate_scores(players_list)

    @staticmethod
    def get_list_of_players() -> list:
        number_of_players = Menu.ask_number_of_players()
        players_list = PlayersController.do_players_list(number_of_players)
        return players_list
