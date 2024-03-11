from tinydb import TinyDB


class Match:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None

    def define_match_winner(self, winner):
        self.winner = winner
        if self.winner == 1:
            self.player_1.score += 1
        elif self.winner == 2:
            self.player_2.score += 1
        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5

    def save_match_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/match.json")
        db.truncate()
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Chess national ID Player 1": self.player_1.chess_national_id,
                "Chess national ID Player 2": self.player_2.chess_national_id}

    @classmethod
    def from_dict(cls, data):
        return cls(data["Chess national ID Player 1"], data["Chess national ID Player 2"])
