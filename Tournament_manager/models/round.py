from tinydb import TinyDB


class Round:

    def __init__(self, round_number, matches):
        self.round_number = round_number
        self.matches = matches

    def save_round_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        db.truncate()
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Round number": self.round_number}

    @classmethod
    def from_dict(cls, data):
        return cls(data["Round number"])
