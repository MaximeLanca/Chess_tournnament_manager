from tinydb import TinyDB


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
    def from_dict(cls, data):
        return cls(data["Matches"])

# def save_matches_list(self):
#    db = TinyDB("../Tournament_manager/data/tournaments/matches.json")
#    matches = db.all()[-1]
#    matches_list = [matches.doc_id]
#
