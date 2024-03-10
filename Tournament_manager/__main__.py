from Tournament_manager.models.player import Player
from controllers.tournament_controller import TournamentController
from views.menu import Menu
from tinydb import TinyDB


def main():
    while True:
        try:
            user_answer = Menu.menu()
            if user_answer == 1:
                Player.remove_players()
                tournament = TournamentController()
                tournament.run()

            elif user_answer == 2:
                tournament = TournamentController()
                tournament.load_tournament()
                break

            elif user_answer == 4:
                print("You have stopped the tournament manager.\nGood bye")
                exit()

            elif user_answer == 5:
                Player.remove_players()
                tournament = TournamentController()
                tournament.speed_run()

            else:
                print("We didn't detect any entry input.\n")
                exit()

        except ValueError:
            print("Error input")


__name__ == "__main__"

main()
