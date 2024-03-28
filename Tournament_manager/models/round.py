from tinydb import TinyDB, Query


class Round:

    def __init__(self, round_number):
        self.round_number = round_number
        self.matches = None
        self.matches_list = []
        self.round_list = None

    def save_round_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        registration_round = db.insert(self.to_dict())
        self.round_list = [registration_round]

    def to_dict(self):
        return {"Round": self.round_number,
                "Matches": self.matches_list
                }

    @classmethod
    def from_dict(cls, id):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        loaded_round = db.get(doc_id=id)
        return cls(loaded_round["Round"],
                   loaded_round["Matches"]
                   )

    @classmethod
    def get_data_round_db(cls):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        last_round = db.all()[-1]
        round_id = [last_round.doc_id]
        return round_id
