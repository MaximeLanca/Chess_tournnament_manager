class Player:

    def __init__(self, number_of_player, player_infos, score):
        self.number_of_player = number_of_player
        self.player_infos = player_infos
        self.score = score

    def __str__(self):
        return f"Player {self.number_of_player}"

    def do_players_list(self) -> list:
        """Players creation """
        for number in range(1, self.number_of_players + 1):
            player = Player(name=self.player_infos[0],
                            birthday=self.player_infos[1],
                            chess_national_id=self.player_infos[2],
                            score=0,
                            number_of_player=number)

            self.players_list.append(player)

        return self.players_list
