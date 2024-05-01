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
    def from_db(cls, player_id: str):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        loaded_players = db.search((Query().Chess_national_ID == player_id))
        return cls(loaded_players[0]["Number_of_player"],
                   loaded_players[0]["Name"],
                   loaded_players[0]["Birthday"],
                   loaded_players[0]["Chess_national_ID"],
                   loaded_players[0]["Score"]
                   )

    def update_players_score(self):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        db.update({"Score": self.score}, Query().Chess_national_ID == self.chess_national_id)

    @classmethod
    def search_player(cls, chess_national_id: str):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        searched_player = db.search(Query().Chess_national_ID == chess_national_id)
        return searched_player

    @classmethod
    def search_all_players(cls):
        db = TinyDB("../Tournament_manager/data/tournaments/player.json")
        players_in_db = db.all()
        return players_in_db
