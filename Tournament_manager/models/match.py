from tinydb import TinyDB, Query


class Match:

    def __init__(self, player_1, player_2, winner):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = winner or None

    def define_match_winner(self, result):
        if result == 1:
            self.player_1.score += 1
            self.winner = self.player_1.chess_national_id
            self.update_result_match()

        elif result == 2:
            self.player_2.score += 1
            self.winner = self.player_2.chess_national_id
            self.update_result_match()

        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5
            self.winner = "Equality"

    def save_match_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Chess_national_ID_Player_1": self.player_1.chess_national_id,
                "Chess_national_ID_Player_2": self.player_2.chess_national_id,
                "Winner": self.winner
                }

    @classmethod
    def from_dict(cls, id_):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        loaded_match = db.get(doc_id=id_)
        return cls(loaded_match["Chess_national_ID_Player_1"],
                   loaded_match["Chess_national_ID_Player_2"],
                   loaded_match["Winner"] or None)

    def update_result_match(self):
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        db.update({"Winner": self.winner})

    @classmethod
    def get_data_matches_db(cls) -> list:
        loaded_history_matches = []
        db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
        last_match = db.all()[-1]
        match_id = last_match.doc_id
        loaded_history_matches.append(match_id)
        return loaded_history_matches
