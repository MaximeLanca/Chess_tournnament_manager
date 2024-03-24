import re
from datetime import datetime
from colorama import Fore, Style, Back


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
            print(Fore.RED + "You are trying to enter an invalid value.\nTap ( 1 ) or ( 2 ) or (3).")

    @staticmethod
    def introduction():
        """Game introduction"""
        print(Fore.BLUE + "Welcome to the local chess tournament !\nThe tournament will feature a minimum of four "
                          "players and a maximum of ten.\nEach game will be played with a maximum of 100 moves.\nThe "
                          "winner of one match will play with the winner of another match"
                          "\n"
                          "\n")

    @staticmethod
    def second_introduction():
        """Game introduction"""
        print(Fore.BLUE + "Speed run")

    @staticmethod
    def ask_number_of_players() -> int:
        """players numbers for start tournament"""
        while True:
            try:
                number_of_players = int(input("Enter a number of player between 4 and 10 and an evan number :"))
                if number_of_players % 2 == 0 and 4 <= number_of_players:
                    print(Fore.BLUE + f"{number_of_players} players take part in the tournament.")
                    return number_of_players
                else:
                    number_of_players = 4
                    print(Fore.BLUE + "The standard number of rounds has been defined.")
                    return number_of_players

            except ValueError:
                print(Fore.RED + "Please, enter valid number.")

    @staticmethod
    def ask_player_infos() -> list:
        """players data"""
        player_infos = []
        while True:
            try:
                national_id = str(input("Enter player national_id ( format AB123) :"))
                regex_pattern = r'^[A-Za-z]{2}\d{3}$'
                national_id_result = re.findall(regex_pattern, national_id)

                if national_id_result:
                    player_infos.append(national_id)
                    break
                else:
                    print(Fore.RED + 'No id specified')
            except ValueError:
                print(Fore.RED + "Entry is not valid. Please enter digital entry for the player national_id")

        while True:
            try:
                name = input("Enter player name :").lower()
                player_infos.append(name)
                break
            except NameError:
                print(Fore.RED + "Entry is not valid")

        while True:
            try:
                date_str = input("Please enter the player birthday ( format YYYY-MM-DD ) :")
                birthday_date = str(datetime.strptime(date_str, "%Y-%m-%d"))
                if birthday_date:
                    player_infos.append(birthday_date)
                    break
                else:
                    print(Fore.RED + 'No birthday specified')
            except ValueError:
                print(Fore.RED + "Invalid date format. Please enter date in 'YYYY-MM-DD' format.")
        # TODO : Vérication d'un players national ID unique
        return player_infos

    @staticmethod
    def display_match(match):
        """player's match"""
        print(Fore.GREEN + f"Player {match.player_1.number_of_player} VS Player {match.player_2.number_of_player}")

    @staticmethod
    def ask_match_winner():
        """match winner"""
        return int(input("Identify the Winner:\n"
                         "For Player 1: Tape 1\n"
                         "For Player 2: Tape 2\n"
                         "Equality: Tape 3\n"
                         "Stop the tournament: Tape 4\n"
                         "Entry:"
                         ))

    @staticmethod
    def ask_round():
        """rounds number"""
        return int(input("How many rounds you want to apply? : "))

    @staticmethod
    def ask_tournament_name():
        """Tournament name"""
        return str(input("What is tournament name? : "))

    @staticmethod
    def ask_tournament_location():
        """tournament location"""
        return str(input("What is tournament location? : "))

    @staticmethod
    def ask_tournament_start_date():
        """tournament start date"""
        while True:
            try:
                date_str = input("Please enter the tournament start date ( format YYYY-MM-DD) : ")
                start_date = datetime.strptime(date_str, "%Y-%m-%d")
                return start_date
            except ValueError:
                print(Fore.RED + "Invalid date format. Please enter date in 'YYYY-MM-DD' format.")

    @staticmethod
    def ask_tournament_end_date():
        """tournament end date"""
        while True:
            try:
                date_str = input("Please enter the tournament end date ( format YYYY-MM-DD) : ")
                end_date = datetime.strptime(date_str, "%Y-%m-%d")
                return end_date
            except ValueError:
                print(Fore.RED + "Invalid date format. Please enter date in 'YYYY-MM-DD' format.")

    @staticmethod
    def display_round(nb):
        """display round number"""
        print(Fore.GREEN + f"Round #{nb} start !")

    @staticmethod
    def display_created_player(number):
        """display new player"""
        print(Fore.BLUE + f"The player {number} has been created.")

    @staticmethod
    def started_tournament(tournament_name):
        """introduces the tournament name"""
        print(Fore.GREEN + f"The {tournament_name} tournament starts now ! ")

    @staticmethod
    def players_ranking(tournament_name, players_list):
        """display players ranking"""
        print(f"Here are the player ranking for the {tournament_name} tournament"
              "\n"
              "\n"
              "\n")
        for player in players_list:
            print(Back.MAGENTA + "----------------------------------------------------------------")
            print(
                Back.MAGENTA + f"Player {player.number_of_player} | Name:{player.name} | Score: {player.score} points")
            print(Back.MAGENTA + "----------------------------------------------------------------")

    @staticmethod
    def ask_tournament_for_to_load():
        """ask tournament to load in DB"""
        answer = input("What is the tournament name for to load ?")
        return answer

    @staticmethod
    def ask_to_load_player():
        while True:
            try:
                answer = input("This player has already been referenced in a tournament\nDo you want use this "
                               "profile? (y/n)")
                return answer
            except TypeError:
                print("Your answer isn't valid. Please try again.")
