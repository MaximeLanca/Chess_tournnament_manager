class Player:

    @staticmethod
    def get_information_players(name, birthday, chess_national_id, player_score) -> dict:
        player = {"Name": name, "Birthday": birthday, "Chess National ID ": chess_national_id,
                  "Score": player_score}
        return player
