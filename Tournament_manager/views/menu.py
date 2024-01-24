class Menu:

    @staticmethod
    def introduction():
        """Game introduction"""
        print("Welcome to the local chess tournament !\nThe tournament will feature a minimum of four players and a "
              "maximum of ten.\nEach game will be played with a maximum of 100 moves.\nThe winner of one match will "
              "play with the winner of another match"
              "\n"
              "\n"
              "\n")

    @staticmethod
    def ask_number_of_players() -> int:
        """parameters tournament"""
        while True:
            try:
                number_of_players = int(input("Enter number of players:"))
                if number_of_players % 2 == 0 and 4 <= number_of_players:
                    print(f"{number_of_players} players take part in the tournament.")
                    return number_of_players
                else:
                    print("Please, enter valid number.")
            except ValueError:
                print("Please, enter valid number.")

    @staticmethod
    def ask_player_infos():
        while True:
            try:
                name = input("Enter player name :").lower()
                birthday = input("Enter player birthday (2000-12-31):")
                national_id = int(input("Enter player national_id :"))
                return name, birthday, national_id
            except:
                print(
                    "Entry is not valid. Please, enter player birthday with the format: (aa/bb/cc) and digital"
                    "entry for the player national_id")

    @staticmethod
    def display_round(round_):
        print(f"Round #{round_.nb} start !")

    @staticmethod
    def display_match(match):
        print(f"{match.player_1} VS {match.player_2}")

    @staticmethod
    def ask_winner():
        return int(input("Winner? 1 / 2 / 3"))

    @staticmethod
    def ask_round():
        return int(input("How many rounds you want to apply ?"))

# creer un tournois -> creer un joueur
# charger un tournois
# charger un/des rapports
# exit
#
#
#
