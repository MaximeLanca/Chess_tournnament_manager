from tinydb import TinyDB, Query


class Player:

    def __init__(self, number_of_player, name, birthday, chess_national_id, score=None):
        self.number_of_player = number_of_player
        self.name = name
        self.birthday = birthday
        self.chess_national_id = chess_national_id
        self.score = score or 0

    def __str__(self):
        return f"Player {self.number_of_player}"

    def save_player_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Number of player": self.number_of_player,
                "Name": self.name,
                "Birthday": self.birthday,
                "Chess national ID": self.chess_national_id,
                "Score": self.score}

    @classmethod
    def from_dict(cls, data):
        return cls(data["Number of player"],
                   data["Name"],
                   data["Birthday"],
                   data["Chess national ID"],
                   data["Score"])

    @classmethod
    def remove_players(cls):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        db.truncate()
