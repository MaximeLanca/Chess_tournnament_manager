from controllers.tournament_controller import TournamentController
from views.menu import Menu


# TODO : refaire la couleur des objets
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

            elif user_answer == 4:
                print("You have stopped the tournament manager.\nGood bye")
                exit()

            elif user_answer == 5:
                tournament = TournamentController()
                tournament.speed_run()

            else:
                print("We didn't detect any entry input.\n")

        except ValueError:
            print("Error input")


if __name__ == "__main__":
    main()

main()

# TODO[Projet 4] Bug : seul le message d'erreur doit être affiché en rouge
# TODO[Projet 4] "Stop the tournament" ne devrait pas quitter le programme mais revenir au menu initial
# TODO[Projet 4] Commencer la génération de rapports
