class Player:

    def __init__(self, name, birthday, chess_national_id, score, number_of_player):
        self.name = name
        self.birthday = birthday
        self.chess_national_id = chess_national_id
        self.score = score
        self.number_of_player = number_of_player

    def __str__(self):
        return f"Player {self.number_of_player}"

        # @staticmethod
    # def get_information_players(name, birthday, chess_national_id, player_score) -> dict:
    #    player = {"Name": name, "Birthday": birthday, "Chess National ID ": chess_national_id,
    #              "Score": player_score}
    #    return player
