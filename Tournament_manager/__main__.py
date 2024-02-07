from Tournament_manager.controllers.global_controllers import GlobalController
from views.menu import Menu


def main():
    user_answer = Menu.menu()
    if user_answer == 1:
        GlobalController.lauching_of_the_program()
    elif user_answer == 2:
        pass
    elif user_answer == 3:
        pass
    elif user_answer == 4:
        print("Good bye")
        exit()
    else:
        print("We didn't detect any entry input.\n")


main()
