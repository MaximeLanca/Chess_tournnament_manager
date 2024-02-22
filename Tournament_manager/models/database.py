from tinydb import TinyDB, Query


class Database:
    def __init__(self):
        self.db = TinyDB("../output/db.json")

    def load_data(self):
        return self.db.all()

    def add_data(self, data):
        self.db.insert(data)
