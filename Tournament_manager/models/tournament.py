class Tournament:

    def __init__(self, name, ):
        self.match = None
        self.round = None
        self.name = name

    @staticmethod
    def define_tournament_winner(players_list):
        players_list.sort(key=lambda x: x.score)
        return players_list
