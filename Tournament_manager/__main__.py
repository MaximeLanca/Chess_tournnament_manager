from Tournament_manager.controllers.tournament_controller import TournamentController
from Tournament_manager.views.menu import Menu


def main():
    while True:
        try:
            user_answer = Menu.menu()
            if user_answer == 1:
                tournament = TournamentController()
                tournament.run()
                break
            elif user_answer == 2:
                loaded_tournament = TournamentController.load_tournament()
                # db.all()
                pass
            elif user_answer == 3:
                pass
            elif user_answer == 4:
                print("You have stopped the tournament manager.\nGood bye")
                exit()
            elif user_answer == 5:
                tournament = TournamentController()
                tournament.speed_run()

            else:
                print("We didn't detect any entry input.\n")
                exit()

        except ValueError:
            print("Error input")


__name__ == "__main__"

main()
