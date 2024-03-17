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

    def save_tournament_db(self, data_players, round_number, matches):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        db.insert(self.to_dict(data_players, round_number, matches))

    def to_dict(self, data_players, round_number, matches):
        return {"Tournament Name": self.tournament_name,
                "Tournament location": self.tournament_location,
                "Start date": self.start_date,
                "End date": self.end_date,
                "Number of round": self.number_of_round,
                "Data players": data_players,
                "Round Number": round_number,
                "Matches": matches
                }

    @classmethod
    def from_dict(cls, data):
        return cls(data["Tournament Name"],
                   data["Tournament location"],
                   data["Start"],
                   data["End"],
                   data["Number of round"],
                   data["Data players"],
                   data["Round Number"],
                   data["Matches"]
                   )

    def add_round(self, round_):
        # self.rounds.append(round_)
        list_ = []
        list_.append(round_)
        self.rounds = list_
