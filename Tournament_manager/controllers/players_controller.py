from tinydb import TinyDB, Query

from Tournament_manager.models.player import Player
from Tournament_manager.views.interface import Interface


class PlayersController:

    def __init__(self, number_of_players=None, player=None):
        self.number_of_players = number_of_players or None
        self.players_list = []
        self.player = player or None

    def do_players_list(self):
        """Players creation """
        for number in range(1, (self.number_of_players + 1)):
            player_infos = Interface.ask_player_infos()
            self.player = Player(
                number_of_player=number,
                name=player_infos[0],
                birthday=player_infos[1],
                chess_national_id=player_infos[2],
            )
            self.player.save_player_db()
            Interface.display_created_player(number)
            self.players_list.append(self.player)

    def get_db_data_players(self):
        db_players = TinyDB("../Tournament_manager/data/tournaments/player.json")
        loaded_players = db_players.all()
        for data in loaded_players:
            self.player = Player(number_of_player=data["Number of player"],
                                 name=data["Name"],
                                 birthday=data["Birthday"],
                                 chess_national_id=data["Chess national ID"],
                                 score=data["Score"])
            self.players_list.append(self.player)
        return self.players_list

    def update_players_score(self, pairs_of_players):
        db_players = TinyDB("../Tournament_manager/data/tournaments/player.json")
        info = Query()
        for player in pairs_of_players:
            db_players.update({"Score": player.score}, info["Chess national ID"] == player.chess_national_id)

    def quick_do_players_list(self):

        player_1 = Player(
            number_of_player=1,
            name="Maxime",
            birthday="1987-02-08",
            chess_national_id=12345,
        )
        player_2 = Player(
            number_of_player=2,
            name="Damien",
            birthday="1989-05-02",
            chess_national_id=54321,
        )

        player_3 = Player(
            number_of_player=3,
            name="Marc",
            birthday="1980-09-01",
            chess_national_id=56789,
        )

        player_4 = Player(
            number_of_player=4,
            name="Augustin",
            birthday="1995-09-27",
            chess_national_id=98765,
        )

        list_ = [player_1, player_2, player_3, player_4]
        for player in list_:
            self.player = player
            self.player.save_player_db()
            self.players_list.append(self.player)
        return self.players_list
