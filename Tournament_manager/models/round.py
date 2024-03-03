from tinydb import TinyDB


class Round:

    def __init__(self, round_number, matches):
        self.round_number = round_number
        self.matches = matches

        db = TinyDB("../data/tournament/db.json")
        db.insert(round_number)
        db.insert(matches)
