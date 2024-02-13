from Tournament_manager.controllers.global_controllers import GlobalController
from views.interface import Interface


class Main:
    def main(self):
        while True:
            try:
                user_answer = Interface.menu()
                if user_answer == 1:
                    GlobalController.launch()
                    break
                elif user_answer == 2:
                    pass
                elif user_answer == 3:
                    pass
                elif user_answer == 4:
                    print("You have stopped the tournament manager.\nGood bye")
                    exit()
                else:
                    print("We didn't detect any entry input.\n")

            except ValueError:
                print("Error input")


main = Main()
main.main()
