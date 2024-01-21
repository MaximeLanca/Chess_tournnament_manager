class Player:

    def __init__(self, name, birthday, chess_national_id, player_score):
        self.name = name
        self.birthday = birthday
        self.chess_national_id = chess_national_id
        self.player_score = player_score

    def get_information_players(self) -> dict:
        player = {"Name": self.name, "Birthday": self.birthday, "Chess National ID ": self.chess_national_id,
                  "Score": self.player_score}
        return player
