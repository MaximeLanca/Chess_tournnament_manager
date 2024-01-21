from views.menu import Menu


class PlayersController:

    @staticmethod
    def do_players_list(number_of_players: int) -> dict:
        """Players creation """

        players_list = {}
        for number in range(0, number_of_players):
            player_infos = Menu.ask_player_infos()
            player = {"Player Number: ": (number + 1), "Name": player_infos[0], "Birthday": player_infos[1],
                      "Chess National ID ": player_infos[2]}
            players_list[number] = player
            print(f"The player {number + 1} has been created.")

        # print(players_list)

        return players_list
