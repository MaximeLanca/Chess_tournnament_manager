from Tournament_manager.controllers import tools
from Tournament_manager.models.player import Player
from Tournament_manager.views.interface import Interface
from controllers.tournament_controller import TournamentController
from views.menu import Menu


def main():
    while True:
        try:
            user_answer = Menu.menu()
            if user_answer == 1:
                start_tournament = TournamentController()
                start_tournament.run()

            elif user_answer == 2:
                loaded_tournament = TournamentController()
                loaded_tournament.load_tournament()

            elif user_answer == 3:
                answer = Interface.ask_report_type()
                TournamentController.handle_request_for_report(answer)

            elif user_answer == 4:
                print("You have stopped the tournament manager.\nGood bye")
                exit()

            elif user_answer == 5:
                Player.search_all_players()
                tournament = TournamentController()
                tournament.speed_run()

            else:
                print("We didn't detect any entry input.\n")

        except ValueError:
            print("Error input")


if __name__ == "__main__":
    main()

main()
