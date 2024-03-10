from tinydb import TinyDB


class Round:

    def __init__(self, round_number, matches):
        self.round_number = round_number
        self.matches = matches

    def list_data_for_backup(self):
        return {"Round number": self.round_number, "Matches": self.matches}
