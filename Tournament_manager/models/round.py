from tinydb import TinyDB, Query


class Round:

    def __init__(self, round_number, matches, matches_list, round_list):
        self.round_number = round_number
        self.matches = None or matches
        self.id_matches_list = [] or matches_list
        self.round_list = None or round_list
        self.id_last_round = []

    def save_round_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        saved_round = db.insert(self.to_dict())
        self.round_list = [saved_round]

    def to_dict(self):
        return {"Round": self.round_number,
                "Matches": self.id_matches_list
                }

    @classmethod
    def from_dict(cls, id_):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        loaded_round = db.get(doc_id=id_[0])
        return cls(loaded_round["Round"],
                   loaded_round["Matches"],
                   None,
                   None
                   )

    def get_data_round_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        last_round = db.all()[-1]
        self.id_last_round.append(last_round.doc_id)

    @classmethod
    def delete_round(cls):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        last_round = db.all()[-1]
        db.remove(doc_ids=[last_round.doc_id])
