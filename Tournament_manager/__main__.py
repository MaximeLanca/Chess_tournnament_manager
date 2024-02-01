from Tournament_manager.controllers.global_controllers import GlobalController
from Tournament_manager.models.tournament import Tournament
from views.menu import Menu
from controllers.tournament_controller import TournamentController


def main():
    Menu.introduction()
    players_informations = GlobalController.get_list_of_players()
    players_list = []
    for player in players_informations:
        players_list.append(player)

    round_number = Menu.ask_round()
    print(players_list)
    for i in range(round_number):
        round_ = TournamentController.initializing_round(nb=i,
                                                         matches=TournamentController.create_matches(players_list))
        TournamentController.start_round(round_)
        for match in round_.matches:
            Menu.display_match(match)
            match.define_winner(Menu().ask_winner())


main()
