from tinydb import TinyDB, Query


class Database:
    def __init__(self, tournament):
        self.db = TinyDB("../output/db.json")
        self.tournament = tournament

    def load_data(self):
        return self.db.all(self.tournament)

    def save_data(self):
        self.db.insert(self.tournament)
