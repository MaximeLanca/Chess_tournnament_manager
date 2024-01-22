from Tournament_manager.models.tournament import Tournament
from controllers.global_controllers import GlobalController
from views.menu import Menu


class Main:
    Menu.introduction()
    tournament = Tournament(name='Tournament n°1')
    player_list = GlobalController.get_number_of_players()

    for player in player_list:
        tournament.add_player(player)

    rounds_number = 2  # question à poser à l'utilisateur
    for i in range(rounds_number):
        for i in range(rounds_number):
            round_ = Round(nb=i, matches=create_matches(tournament.players))
    # players_list = PlayersController.do_players_list()


Main()
