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

    def save_players_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Number_of_player": self.number_of_player,
                "Name": self.name,
                "Birthday": self.birthday,
                "Chess_national_ID": self.chess_national_id,
                "Score": self.score
                }

    @classmethod
    def from_dict(cls, data):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        loaded_players = db.search((Query().Chess_national_ID == data["Chess_national_ID"]))
        return cls(loaded_players[0]["Number_of_player"],
                   loaded_players[1]["Name"],
                   loaded_players[3]["Chess_national_ID"],
                   loaded_players[4]["Score"]
                   )

    def update_players_score(self):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        db.update({"Score": self.score})
