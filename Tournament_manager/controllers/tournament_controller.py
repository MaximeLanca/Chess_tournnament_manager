import itertools
from Tournament_manager.controllers.players_controller import PlayersController
from Tournament_manager.models.tournament import Tournament
from Tournament_manager.models.round import Round
from Tournament_manager.models.match import Match
from Tournament_manager.views.interface import Interface


class TournamentController:

    def __init__(self):
        self.tournament = None
        self.round_ = None
        self.match = None

    def run(self):
        Interface.introduction()
        tournament_name = Interface.ask_tournament_name()
        number_of_round = Interface.ask_round()

        players_controller = PlayersController(Interface.ask_number_of_players())
        players_controller.do_players_list()
        self.tournament = Tournament(tournament_name,
                                     number_of_round,
                                     self.round_,
                                     players_controller.players_list,
                                     self.match
                                     )

        Interface.started_tournament(self.tournament.tournament_name)
        self.start_tournament()

    def start_tournament(self):
        for i in range(1, self.tournament.number_of_round + 1):
            self.tournament.round_ = Round(round_number=i, matches=self.start_matches())
            Interface.display_round(self.tournament.round_.round_number)
            self.specify_winner()
        self.define_tournament_winner()

    def specify_winner(self):
        for match in self.tournament.round_.matches:
            Interface.display_match(match)
            match.define_match_winner(Interface().ask_winner())

    def start_matches(self) -> list:
        matches = []
        # player_layout = zip(self.tournament.players_list)

        # for players in self.tournament.players_list:
        #    self.tournament.match = Match(player_1=players[0], player_2=players[1])
        #    matches.append(self.tournament.match)
        for i in itertools.combinations(self.tournament.players_list, 2):
            self.tournament.match = Match(player_1=i[0], player_2=i[1])
            matches.append(self.tournament.match)
        return matches
        # if self.tournament.number_of_round > 1:
        #    for i in self.tournament.number_of_round:
        #        self.tournament.match = Match(player_1=player_layout[i], player_2=i[1])
        # return matches

    # for i in itertools.combinations(self.tournament.players_list, 2):
    #     self.tournament.match = Match(player_1=i[0], player_2=i[1])
    #     matches.append(self.tournament.match)
    # return matches
    # nouvelle_liste = [(x[0], y[0], y[1]) for x, y in zip(liste[:-1], liste[1:])]
    def define_tournament_winner(self):
        self.tournament.players_list.sort(key=lambda x: x.score)
        print(f"The tournament winner is: {self.tournament.players_list[0]}")
