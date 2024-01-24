class Tournament:

    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player) -> list:
        self.players.append(player)
        return self.players
