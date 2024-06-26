import re
from datetime import datetime
from colorama import Fore, Style


class Interface:
    @staticmethod
    def menu():
        """Menu tournament manager"""
        try:
            while True:
                ask_information = int(input("What do you want to do ?\n"
                                            "Enter ( 1 ) to create tournament and players\n"
                                            "Enter ( 2 ) to load tournament\n"
                                            "Enter ( 3 ) to create report\n"
                                            "Enter ( 4 ) to stop application\n"
                                            "\n"
                                            "\n"
                                            ))
                return ask_information
        except ValueError:
            print(
                f"{Fore.RED} + You are trying to enter an invalid value.\nTap ( 1 ) or ( 2 ) or (3).{Style.RESET_ALL}")

    @staticmethod
    def introduction():
        """Game introduction"""
        print("Welcome to the local chess tournament !")

    @staticmethod
    def second_introduction():
        """Game introduction"""
        print("Speed run")

    @staticmethod
    def ask_number_of_players() -> int:
        """players numbers for start tournament"""
        while True:
            try:
                number_of_players = int(input("Enter a number of player between 4 and 10 and an evan number :"))
                if number_of_players % 2 == 0 and 4 <= number_of_players:
                    print(f"{Fore.BLUE}{number_of_players} players take part in the tournament.{Style.RESET_ALL}")
                    return number_of_players
                else:
                    number_of_players = 4
                    print("The standard number of rounds has been defined.")
                    return number_of_players

            except ValueError:
                print(Fore.RED + "Please, enter valid number.")

    @staticmethod
    def ask_player_infos() -> dict:
        """players data"""
        player_infos = {}
        while True:
            try:
                national_id = str(input("Enter player national_id ( format AB123) :"))
                regex_pattern = r'^[A-Za-z]{2}\d{3}$'
                national_id_result = re.findall(regex_pattern, national_id)

                if national_id_result:
                    player_infos['chess_national_id'] = national_id
                    break
                else:
                    print(f'{Fore.RED} No id specified{Style.RESET_ALL}')
            except ValueError:
                print(f'{Fore.RED}'
                      f'Entry is not valid. Please enter digital entry for the player national_id{Style.RESET_ALL}')

        while True:
            try:
                name = input("Enter player name :").lower()
                player_infos['name'] = name
                break
            except NameError:
                print("Entry is not valid")

        while True:
            try:
                date_str = input("Please enter the player birthday ( format YYYY-MM-DD ) :")
                birthday_date = str(datetime.strptime(date_str, "%Y-%m-%d"))
                if birthday_date:
                    player_infos['birthday'] = birthday_date
                    break
                else:
                    print(f"{Fore.RED}No birthday specified{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid date format. Please enter date in 'YYYY-MM-DD' format.{Style.RESET_ALL}")
        return player_infos

    @staticmethod
    def display_match(match):
        """player's match"""
        print(
            f"Player{Fore.BLUE} {match.player_1.name}{Style.RESET_ALL} VS Player {Fore.BLUE}{match.player_2.name}"
            f"{Style.RESET_ALL}")

    @staticmethod
    def ask_tournament_description():
        """ask description tournament of director"""
        desc = input("What description tournament would you enter? :")
        return desc

    @staticmethod
    def ask_match_winner(match):
        """match winner"""
        return int(input("Identify the Winner:\n"
                         f"For{Fore.BLUE} {match.player_1.name}{Style.RESET_ALL}: Tape 1\n"
                         f"For{Fore.BLUE} {match.player_2.name}{Style.RESET_ALL}: Tape 2\n"
                         "Equality: Tape 3\n"
                         "Stop the tournament: Tape 4\n"
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
                print(f"{Fore.RED} + Invalid date format. Please enter date in 'YYYY-MM-DD' format.{Style.RESET_ALL}")

    @staticmethod
    def ask_tournament_end_date():
        """tournament end date"""
        while True:
            try:
                date_str = input("Please enter the tournament end date ( format YYYY-MM-DD) : ")
                end_date = datetime.strptime(date_str, "%Y-%m-%d")
                return end_date
            except ValueError:
                print(f"{Fore.RED} + Invalid date format. Please enter date in 'YYYY-MM-DD' format.{Style.RESET_ALL}")

    @staticmethod
    def display_round(nb):
        """display round number"""
        print(f"Round{Fore.GREEN} #{nb}{Style.RESET_ALL} start !")

    @staticmethod
    def display_created_player(number):
        """display new player"""
        print(f"The {Fore.BLUE}player {number}{Style.RESET_ALL} has been created.")

    @staticmethod
    def send_message_for_started_tournament(tournament_name):
        """introduces the tournament name"""
        print(f"The {Fore.GREEN}{tournament_name}{Style.RESET_ALL} tournament starts now ! ")

    @staticmethod
    def display_tournament_winner(players_list):
        print(f"The tournament winner is: {Fore.BLUE}{players_list[0].name}{Style.RESET_ALL} with "
              f"{Fore.CYAN}{players_list[0].score}{Style.RESET_ALL} points")

    @staticmethod
    def players_ranking(tournament_name, players_list):
        """display players ranking"""
        print(f"Here are the player ranking for the{Fore.GREEN} {tournament_name}{Style.RESET_ALL} tournament"
              "\n")
        for player in players_list:
            print("----------------------------------------------------------------")
            print(
                f"Player:{Fore.BLUE} {player.number_of_player}{Style.RESET_ALL} | "
                f"Name:{Fore.BLUE}{player.name}{Style.RESET_ALL} | "
                f"Score:{Fore.CYAN} {player.score} points{Style.RESET_ALL}")
            print("----------------------------------------------------------------")

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

    @staticmethod
    def send_error_message_on_tournament(tournament_name):
        return input(f"They're not tournament with the name '{tournament_name}'.\n"
                     "Tape 't' for search an other tournament name or tape 'e' for quit the program) (t/e): ")

    @staticmethod
    def stop_the_game():
        print("All players have met during tournament.\nThe tournament is over.")

    @staticmethod
    def ask_report_type() -> int:
        try:
            while True:
                answer = int(input("What report type you wish ?\n"
                                   "Press ( 1 ) to create players list\n"
                                   "Press ( 2 ) to create tournament list\n"
                                   "Press ( 3 ) to know date and place of a tournament\n"
                                   "Press ( 4 ) to create players list of a requested tournament\n"
                                   "Press ( 5 ) to create all rounds and matches of a tournament list\n"
                                   "\n"
                                   "\n"
                                   ))
                return answer
        except ValueError:
            print("You are trying to enter an invalid value.\nPress ( 1 ) or ( 2 ) or (3).")

    @staticmethod
    def send_message_after_extraction_of_db():
        print('--- Successful extraction of db ---')
        print("-----------------------------------------------------")

    @staticmethod
    def send_message_on_existing_folder_report():
        print('Folders and files already exist. deliverables will be create in existing folder')
