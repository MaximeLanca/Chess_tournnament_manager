class Match:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None

    def define_winner(self, winner):
        self.winner = winner
        if self.winner == self.player_1:
            self.player_1.score += 1
        if self.winner == self.player_2:
            self.player_2.score += 1
        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5
