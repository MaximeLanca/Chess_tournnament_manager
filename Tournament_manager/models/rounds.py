from random import choice


class Round:

    def __init__(self, tournament_parameters, player_list):
        self.tournament_parameters = tournament_parameters
        self.player_list = player_list

    def create_round(self):
        """Round tournament creation with number of players defined"""

        number_of_players = len(self.player_list)
        for n in range(0, number_of_players):
            player_generic_list[self.number_of_players]
