from Tournament_manager.controllers import tournament_controller
from Tournament_manager.models.tournament import Tournament
from controllers.players_controller import PlayersController
from views.menu import Menu
from models.rounds import Round
from models.match import Match
from controllers.tournament_controller import TournamentController


def main():
    Menu.introduction()

    player_list = PlayersController.get_number_of_players()
    # TournamentController().start_tournament(player_list)
    # for player in player_list:
    #    tournament = TournamentController().start_tournament(player)

    round_number = Menu.ask_round()
    for i in range(round_number):
        round_ = Round(nb =i, matches = TournamentController.create_matches(player_list ))
            display_round(round_)
            for match in round_.matches:
            display_match(match)

main()