from Tournament_manager.models.player import Player
from Tournament_manager.views.interface import Interface


class PlayersController:

    def __init__(self, number_of_players=None, player=None):
        self.number_of_players = number_of_players or None
        self.players_list = []
        self.player = player or None
        self.saved_data_players = []

    def get_players_information(self):
        """Players and lists creation """
        for number in range(1, (self.number_of_players + 1)):
            player_infos = Interface.ask_player_infos()
            replayed_player = self.check_chess_national_id_db(player_infos['chess_national_id'])
            if replayed_player:
                self.player = Player(
                    chess_national_id=replayed_player["Chess national ID"],
                    number_of_player=replayed_player["Number of player"],
                    name=replayed_player["Name"],
                    birthday=replayed_player["Birthday"],
                )

            else:
                self.player = Player(
                    number_of_player=number,
                    name=player_infos['name'],
                    birthday=player_infos['birthday'],
                    chess_national_id=player_infos['chess_national_id'],
                )
                self.player.save_players_db()

            Interface.display_created_player(number)
            self.players_list.append(self.player)

    def get_players_data_db(self, players_id: list) -> list:
        """Load players for a loaded tournament.
            :param: players_id: Chess national id of players
            :return:players_list: players list
        """
        for id_ in players_id:
            self.player = Player.from_db(id_)
            self.players_list.append(self.player)
        return self.players_list

    def check_chess_national_id_db(self, player_chess_national_id) -> dict:
        searched_player = Player.search_player_db(player_chess_national_id)
        if searched_player:
            answer = Interface.ask_to_load_player()

            if answer == "y":
                return searched_player

            else:
                print("The player has not been loaded in this tournament.Enter another ID")

    def quick_do_players_list(self):
        player_1 = Player(
            number_of_player=1,
            name="Maxime",
            birthday="1987-02-08",
            chess_national_id="JH345",
        )
        self.check_chess_national_id_db(player_1.chess_national_id)

        player_2 = Player(
            number_of_player=2,
            name="Damien",
            birthday="1989-05-02",
            chess_national_id="OI321",
        )
        self.check_chess_national_id_db(player_2.chess_national_id)

        player_3 = Player(
            number_of_player=3,
            name="Marc",
            birthday="1980-09-01",
            chess_national_id="DR789",
        )
        self.check_chess_national_id_db(player_3.chess_national_id)

        player_4 = Player(
            number_of_player=4,
            name="Augustin",
            birthday="1995-09-27",
            chess_national_id="TR765",
        )
        self.check_chess_national_id_db(player_4.chess_national_id)
        list_ = [player_1, player_2, player_3, player_4]
        for player in list_:
            self.player = player
            self.player.save_players_db()
            self.players_list.append(self.player)
        return self.players_list
