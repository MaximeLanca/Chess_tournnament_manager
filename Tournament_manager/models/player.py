from tinydb import TinyDB, Query


class Player:

    def __init__(self, number_of_player, name, birthday, chess_national_id, score=None):
        self.number_of_player = number_of_player
        self.name = name
        self.birthday = birthday
        self.chess_national_id = chess_national_id
        self.score = score or 0

    def save_player_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")

    #        db.insert(self.list_data_for_backup())

    def list_data_for_backup(self):
        return {"Number of player": self.number_of_player,
                "Name": self.name,
                "Birthday": self.birthday,
                "Chess national": self.chess_national_id,
                "Score": self.score}

    def __str__(self):
        return f"Player {self.number_of_player}"
