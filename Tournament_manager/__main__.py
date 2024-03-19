from controllers.tournament_controller import TournamentController
from views.menu import Menu


# TODO:
def main():
    while True:
        try:
            user_answer = Menu.menu()
            if user_answer == 1:
                tournament = TournamentController()
                tournament.run()

            elif user_answer == 2:
                tournament = TournamentController()
                tournament.load_tournament()

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


if __name__ == "__main__":
    main()

main()
