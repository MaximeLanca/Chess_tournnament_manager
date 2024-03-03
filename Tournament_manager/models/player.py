from tinydb import TinyDB


class Player:

    def __init__(self, number_of_player, name, birthday, chess_national_id, score=None):
        self.number_of_player = number_of_player
        self.name = name
        self.birthday = birthday
        self.chess_national_id = chess_national_id
        self.score = score or 0

        db = TinyDB("../data/tournament/db.json")
        db.insert(number_of_player)
        db.insert(name)
        db.insert(birthday)
        db.insert(chess_national_id)
        db.insert(score)

    def __str__(self):
        return f"Player {self.number_of_player}"
