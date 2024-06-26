from Tournament_manager.models.player import Player
from Tournament_manager.views.interface import Interface
from controllers.tournament_controller import TournamentController
from views.menu import Menu


def main():
    while True:
        user_answer = Menu.menu()
        if user_answer == 1:
            start_tournament = TournamentController()
            start_tournament.run()

        elif user_answer == 2:
            loaded_tournament = TournamentController()
            loaded_tournament.load_tournament()

        elif user_answer == 3:
            answer = Interface.ask_report_type()
            tournament = TournamentController()
            tournament.handle_request_for_report(answer)

        elif user_answer == 4:
            print("You have stopped the tournament manager.\nGood bye")
            exit()

        elif user_answer == 5:
            Player.search_all_players_db()
            tournament = TournamentController()
            tournament.speed_run()

        else:
            print("We didn't detect any entry input.\n")


if __name__ == "__main__":
    main()

main()
