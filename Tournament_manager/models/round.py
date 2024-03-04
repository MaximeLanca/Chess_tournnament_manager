from tinydb import TinyDB


class Round:

    def __init__(self, round_number, matches):
        self.round_number = round_number
        self.matches = matches

    def save_round_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/round.json")
        db.insert({"Round number": self.round_number, "Matches": self.matches})
