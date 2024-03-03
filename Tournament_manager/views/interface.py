import re
from datetime import datetime


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
        """players numbers for start tournament"""
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
                    number_of_players = 4
                    print("The standard number of rounds has been defined."
                          "\n"
                          "\n")
                    return number_of_players

            except ValueError:
                print("Please, enter valid number."
                      "\n"
                      "\n")

    @staticmethod
    def ask_player_infos() -> list:
        """players data"""
        player_infos = []
        while True:
            try:
                name = input("Enter player name :"
                             "\n"
                             "\n").lower()
                player_infos.append(name)
                break
            except NameError:
                print("Entry is not valid"
                      "\n"
                      "\n")

        while True:
            try:
                date_str = input("Please enter the player birthday ( format YYYY-MM ) :")
                birthday_date = str(datetime.strptime(date_str, "%Y-%m-%d"))
                player_infos.append(birthday_date)
            except ValueError:
                print("Invalid date format. Please enter date in 'YYYY-MM-DD' format.")

        while True:
            try:
                national_id = str(input("Enter player national_id (yyyyy):"))
                national_id_input_format = r'\d{5}'
                national_id_result = re.findall(national_id_input_format, national_id)

                if national_id_result:
                    player_infos.append(national_id)
                    break
                else:
                    print('No id specified'
                          "\n"
                          "\n")
            except ValueError:
                print(
                    "Entry is not valid. Please enter digital entry for the player national_id")
        return player_infos

    @staticmethod
    def display_match(match):
        """player's match"""
        print(f"Player {match.player_1.number_of_player} VS Player {match.player_2.number_of_player}")

    @staticmethod
    def ask_match_winner():
        """match winner"""
        return int(input("Identify the Winner:\n"
                         "For Player 1: Tape 1\n"
                         "For Player 2: Tape 2\n"
                         "Equality: Tape 3\n"
                         "Stop the tournament: Tape 4"
                         "Entry:"
                         "\n"
                         "\n"))

    @staticmethod
    def ask_round():
        """rounds number"""
        return int(input("How many rounds you want to apply ?"
                         "\n"
                         "\n"))

    @staticmethod
    def ask_tournament_name():
        """Tournament name"""
        return str(input("What is tournament name?"
                         "\n"
                         "\n"))

    @staticmethod
    def ask_tournament_location():
        """tournament location"""
        return str(input("What is tournament location?"
                         "\n"
                         "\n"))

    @staticmethod
    def ask_tournament_start_date():
        """tournament start date"""
        while True:
            try:
                date_str = input("Please enter the tournament start date ( format YYYY-MM-DD) : ")
                start_date = datetime.strptime(date_str, "%Y-%m-%d")
                return start_date
            except ValueError:
                print("Invalid date format. Please enter date in 'YYYY-MM-DD' format.")

    @staticmethod
    def ask_tournament_end_date():
        """tournament end date"""
        while True:
            try:
                date_str = input("Please enter the tournament end date ( format YYYY-MM-DD) : ")
                end_date = datetime.strptime(date_str, "%Y-%m-%d")
                return end_date
            except ValueError:
                print("Invalid date format. Please enter date in 'YYYY-MM-DD' format.")

    @staticmethod
    def display_round(nb):
        """display round number"""
        print(f"Round #{nb} start !")

    @staticmethod
    def display_created_player(number):
        """display new player"""
        print(f"The player {number} has been created.")

    @staticmethod
    def started_tournament(tournament_name):
        """introduces the tournament name"""
        print(f"The {tournament_name} tournament starts now ! ")

    @staticmethod
    def players_ranking(tournament_name, players_list):
        """display players ranking"""
        print(f"Here are the player ranking for the {tournament_name} tournament"
              "\n"
              "\n"
              "\n")
        for player in players_list:
            print("----------------------------------------------------------------")
            print(f"Player {player.number_of_player} | Name:{player.name} | Score: {player.score} points")
            print("----------------------------------------------------------------")
