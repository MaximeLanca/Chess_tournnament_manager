from tinydb import TinyDB, Query


class Round:

    def __init__(self, round_number, matches_list=None, matches=None):
        self.round_number = round_number
        self.id_matches_list = matches_list or []
        self.matches = matches
        self.last_round_id = None

    def save_round_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        db.insert(self.to_dict())
        # self.round_list = [saved_round]

    def to_dict(self):
        return {"Round": self.round_number,
                "ID_matches_list": self.id_matches_list,
                }

    @classmethod
    def from_db(cls, ids_):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        loaded_round = db.get(doc_id=ids_)
        return cls(loaded_round["Round"],
                   loaded_round["ID_matches_list"],
                   None,
                   )

    def get_data_round_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        last_round = db.all()[-1]
        self.last_round_id = last_round.doc_id

    def update_round(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        last_round = db.all()[-1]
        id_round = [last_round.doc_id]
        db.update({"Round": self.round_number}, doc_ids=id_round)
        db.update({"ID_matches_list": self.id_matches_list}, doc_ids=id_round)
