from tinydb import TinyDB, Query


class Tournament:

    def __init__(self, tournament_name, tournament_location, start_date, end_date, number_of_round, players_list,
                 rounds=None):
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.players_list = players_list
        self.rounds = rounds or []

    def save_tournament_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        db.truncate()
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Tournament Name": self.tournament_name,
                "Tournament location": self.tournament_location,
                "Start date": self.start_date,
                "End date": self.end_date,
                "Number of round": self.number_of_round,
                "Rounds": self.rounds
                }

    @classmethod
    def from_dict(cls, data):
        return cls(data["Tournament Name"],
                   data["Tournament location"],
                   data["Start"],
                   data["End"],
                   data["Number of round"],
                   data["Rounds"])

    def add_round(self, round_):
        self.rounds.append(round_)
