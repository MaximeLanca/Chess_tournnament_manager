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
        self.rounds = rounds or None

    def save_tournament_db(self, matches=None):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        db.insert(self.to_dict(matches))

    def to_dict(self, matches=None):
        return {"Tournament_name": self.tournament_name,
                "Tournament_location": self.tournament_location,
                "Start_date": self.start_date,
                "End_date": self.end_date,
                "Number_of_round": self.number_of_round,
                "Round_number": None,
                "Matches": matches or None
                }

    @classmethod
    def from_dict(cls, data):
        return cls(data["Tournament_name"],
                   data["Tournament_location"],
                   data["Start"],
                   data["End"],
                   data["Number_of_round"],
                   data["Data_players"],
                   data["Round_number"],
                   data["Matches"]
                   )
