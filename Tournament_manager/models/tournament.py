from tinydb import TinyDB


class Tournament:

    def __init__(self, tournament_name, start_date, end_date, number_of_round, players_list, rounds=None):
        self.tournament_name = tournament_name
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.players_list = players_list
        self.rounds = rounds or []

        db = TinyDB("../data/tournament/db.json")
        db.insert(tournament_name)
        db.insert(start_date)
        db.insert(end_date)
        db.insert(number_of_round)
        db.insert(players_list)
        db.insert(rounds)

    def add_round(self, round_):
        self.rounds.append(round_)
