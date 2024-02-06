from Tournament_manager.controllers.global_controllers import GlobalController
from Tournament_manager.models.tournament import Tournament
from views.menu import Menu
from controllers.tournament_controller import TournamentController


def main():
    Menu.introduction()
    players_list = GlobalController.get_list_of_players()
    print(players_list)
    round_number = Menu.ask_round()

    for i in range(1, round_number + 1):
        round_ = TournamentController.initializing_round(nb=i,
                                                         matches=TournamentController.create_matches(players_list))
        TournamentController.start_round(round_)
        for match in round_.matches:
            Menu.display_match(match)
            match.define_match_winner(Menu().ask_winner())

        Tournament.define_tournament_winner(players_list)


main()
