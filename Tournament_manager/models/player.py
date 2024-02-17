class Player:

    def __init__(self, number_of_player, name, birthday, chess_national_id, ):
        self.number_of_player = number_of_player
        self.name = name
        self.birthday = birthday
        self.chess_national_id = chess_national_id
        self.score = 0

    def __str__(self):
        return f"Player {self.number_of_player}"
