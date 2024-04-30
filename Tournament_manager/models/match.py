from tinydb import TinyDB, Query


class Match:

    def __init__(self, player_1, player_2, winner=None, id_=None):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = winner
        self.id_ = id_

    def define_match_winner(self, result):
        if result == 1:
            self.player_1.score += 1
            self.winner = self.player_1.chess_national_id

        elif result == 2:
            self.player_2.score += 1
            self.winner = self.player_2.chess_national_id

        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5
            self.winner = "Equality"

    def save_match_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        self.id_ = db.insert(self.to_dict())

    def to_dict(self):
        return {"Chess_national_ID_Player_1": self.player_1.chess_national_id,
                "Chess_national_ID_Player_2": self.player_2.chess_national_id,
                "Winner": self.winner
                }

    @classmethod
    def from_db(cls, id_):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        loaded_match = db.get(doc_id=id_)
        return cls(loaded_match["Chess_national_ID_Player_1"],
                   loaded_match["Chess_national_ID_Player_2"],
                   loaded_match["Winner"] or None,
                   id_
                   )

    def update_result_match(self):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        db.update({"Winner": self.winner}, doc_ids=[self.id_])
