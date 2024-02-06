class Tournament:

    def __init__(self, name, player, temporary_list):
        self.name = name
        self.player = player
        self.players = []
        self.players_list = []

    def add_player(self, player):
        self.players.append(player)

    @staticmethod
    def define_tournament_winner(players_list):
        players_list.sort(key=lambda x: x.score)
        print(f"The tournament winner is: {players_list[0]}")
