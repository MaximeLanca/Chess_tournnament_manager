class Menu:
    @staticmethod
    def menu():
        """Menu tournament manager"""
        try:
            while True:
                ask_information = int(input("What do you want to do ?\n"
                                            "Press ( 1 ) to create tournament and players\n"
                                            "Press ( 2 ) to load tournament\n"
                                            "Press ( 3 ) to create report\n"
                                            "Press ( 4 ) to stop application\n"
                                            "Press ( 5 ) to Speed Run\n"
                                            "\n"
                                            "\n"
                                            ))
                return ask_information
        except ValueError:
            print("You are trying to enter an invalid value.\nPress ( 1 ) or ( 2 ) or (3).")
