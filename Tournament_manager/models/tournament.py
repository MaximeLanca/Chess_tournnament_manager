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

    #    db.insert(self.list_data_for_backup())

    def list_data_for_backup(self):
        i = 1
        for player in self.players_list:
            dict = {f"Player {i}": player}
            i += 1

        return {"Tournament Name": self.tournament_name,
                "Tournament location": self.tournament_location,
                "Start date": self.start_date,
                "End date": self.end_date,
                "Number of round": self.number_of_round,
                "Players List": self.players_list,
                "Rounds": self.rounds}

    def add_round(self, round_):
        self.rounds.append(round_)
