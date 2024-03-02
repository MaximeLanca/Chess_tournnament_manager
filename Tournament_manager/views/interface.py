import re


class Interface:
    @staticmethod
    def menu():
        """Menu tournament manager"""
        try:
            while True:
                ask_information = int(input("What do you want to do ?\n"
                                            "Enter ( 1 ) for to create tournament and players\n"
                                            "Enter ( 2 ) for to load tournament\n"
                                            "Enter ( 3 ) for to create report\n"
                                            "Enter ( 4 ) for to stop application\n"
                                            "\n"
                                            "\n"
                                            ))
                return ask_information
        except ValueError:
            print("You are trying to enter an invalid value.\nTap ( 1 ) or ( 2 ) or (3).")

    @staticmethod
    def introduction():
        """Game introduction"""
        print("Welcome to the local chess tournament !\nThe tournament will feature a minimum of four players and a "
              "maximum of ten.\nEach game will be played with a maximum of 100 moves.\nThe winner of one match will "
              "play with the winner of another match"
              "\n"
              "\n")

    @staticmethod
    def second_introduction():
        """Game introduction"""
        print("Speed run")

    @staticmethod
    def ask_number_of_players() -> int:
        """parameters tournament"""
        while True:
            try:
                number_of_players = int(input("Enter a number of player between 4 and 10 and an evan number:"
                                              "\n"
                                              "\n"))
                if number_of_players % 2 == 0 and 4 <= number_of_players:
                    print(f"{number_of_players} players take part in the tournament."
                          "\n"
                          "\n")
                    return number_of_players
                else:
                    print("Your entry does not meet the requirements."
                          "\n"
                          "\n")
            except ValueError:
                print("Please, enter valid number."
                      "\n"
                      "\n")

    @staticmethod
    def ask_player_infos() -> list:
        player_info = []
        while True:
            try:
                name = input("Enter player name :"
                             "\n"
                             "\n").lower()
                player_info.append(name)
                break
            except NameError:
                print("Entry is not valid"
                      "\n"
                      "\n")

        while True:
            try:
                birthday = input("Enter player birthday (xxxx-yy-zz):")
                birthday_input_format = r'\d{4}-\d{2}-\d{2}'
                birthday_result = re.findall(birthday_input_format, birthday)
                if birthday_result:
                    player_info.append(birthday)
                    break
                else:
                    print('No date specified'
                          "\n"
                          "\n")

            except TypeError:
                print(
                    "Entry is not valid. Please, enter player birthday with the format: (aa/bb/cc) and digital"
                    "entry for the player national_id")

        while True:
            try:
                national_id = input("Enter player national_id (yyyyy):")
                national_id_input_format = r'\d{5}'
                national_id_result = re.findall(national_id_input_format, national_id)
                if national_id_result:
                    player_info.append(national_id)
                    break
                else:
                    print('No id specified'
                          "\n"
                          "\n")
            except ValueError:
                print(
                    "Entry is not valid. Please enter digital entry for the player national_id")
        return player_info

    @staticmethod
    def display_match(match):
        print(f"Player {match.player_1.number_of_player} VS Player {match.player_2.number_of_player}")

    @staticmethod
    def ask_winner():
        return int(input("Who is the Winner:\n"
                         "For Player 1: Tape 1\n"
                         "For Player 2: Tape two 2\n"
                         "Equality: Tape 3\n"
                         "Entry:"
                         "\n"
                         "\n"))

    @staticmethod
    def ask_round():
        return int(input("How many rounds you want to apply ?"
                         "\n"
                         "\n"))

    @staticmethod
    def ask_tournament_name():
        return str(input("What is tournament name?"))

    @staticmethod
    def display_round(nb):
        print(f"Round #{nb} start !")

    @staticmethod
    def display_created_player(number):
        print(f"The player {number} has been created.")

    @staticmethod
    def started_tournament(tournament_name):
        print(f"The {tournament_name} starts now ! ")
