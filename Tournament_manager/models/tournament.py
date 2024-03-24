from tinydb import TinyDB, Query


class Tournament:

    def __init__(self, tournament_name, tournament_location, start_date, end_date, number_of_round, players_id,
                 rounds=None):
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.players_id = players_id
        self.rounds = rounds or None
        self.round_history = []
        self.match_history = []

    def save_tournament_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Tournament_name": self.tournament_name,
                "Tournament_location": self.tournament_location,
                "Start_date": self.start_date,
                "End_date": self.end_date,
                "Number_of_round": self.number_of_round,
                "Players_ID": self.players_id,
                "Round_history": self.round_history,
                "Match_history": self.match_history
                }

    @classmethod
    def from_dict(cls, data):
        return cls(data["Tournament_name"],
                   data["Tournament_location"],
                   data["Start"],
                   data["End"],
                   data["Number_of_round"],
                   data["Players_ID"],
                   data["Round_history"],
                   data["Match_history"]
                   )
