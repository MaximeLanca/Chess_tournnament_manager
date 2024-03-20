from tinydb import TinyDB, Query


class Match:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None
        self.registration_number_match = None

    def define_match_winner(self, winner):
        self.winner = winner
        if self.winner == 1:
            self.player_1.score += 1
            self.update_result_match(self.player_1.chess_national_id)
        elif self.winner == 2:
            self.player_2.score += 1
            self.update_result_match(self.player_2.chess_national_id)
        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5
            self.update_result_match("Equality")

    def save_match_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        self.registration_number_match = db.insert(self.to_dict())

    def to_dict(self):
        return {"Chess_national_ID_Player_1": self.player_1.chess_national_id,
                "Chess_national_ID_Player_2": self.player_2.chess_national_id,
                "Winner": None
                }

    @classmethod
    def from_dict(cls, data):
        return cls(data["Chess_national_ID_Player_1"],
                   data["Chess_national_ID_Player_2"],
                   data["Winner"]
                   )

    def update_result_match(self, winner):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        db.update({"Winner": winner})
