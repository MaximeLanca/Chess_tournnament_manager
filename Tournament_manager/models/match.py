from tinydb import TinyDB


class Match:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None

        db = TinyDB("../data/tournament/db.json")
        db.insert(player_1)
        db.insert(player_2)

    def define_match_winner(self, winner):
        self.winner = winner
        if self.winner == 1:
            self.player_1.score += 1
        elif self.winner == 2:
            self.player_2.score += 1
        else:
            self.player_1.score += 0.5
            self.player_2.score += 0.5
