class Menu:
    @staticmethod
    def menu():
        """Menu tournament manager"""
        try:
            while True:
                ask_information = int(input("What do you want to do ?\n"
                                            "Press ( 1 ) for to create tournament and players\n"
                                            "Press ( 2 ) for to load tournament\n"
                                            "Press ( 3 ) for to create report\n"
                                            "Press ( 4 ) for to stop application\n"
                                            "Press ( 5 ) for to Speed Run\n"
                                            "\n"
                                            "\n"
                                            ))
                return ask_information
        except ValueError:
            print("You are trying to enter an invalid value.\nPress ( 1 ) or ( 2 ) or (3).")
