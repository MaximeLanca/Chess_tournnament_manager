class Tournament:

    def __init__(self, tournament_name, number_of_round, players_list, rounds=None):
        self.tournament_name = tournament_name
        self.number_of_round = number_of_round
        self.players_list = players_list
        self.rounds = rounds or []

    def add_round(self, round_):
        self.rounds.append(round_)
