from tinydb import TinyDB, Query


class Tournament:

    def __init__(self, tournament_name, tournament_location, start_date, end_date, number_of_round, players_id=None,
                 rounds=None, round_history=None):
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.players_id = players_id or None
        self.rounds = rounds or None
        self.round_history = round_history or []

    def save_tournament_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        db.insert(self.to_dict())

    def to_dict(self):
        return {"Tournament_name": self.tournament_name,
                "Tournament_location": self.tournament_location,
                "Start_date": self.start_date,
                "End_date": self.end_date,
                "Number_of_round": self.number_of_round,
                "Players_ID": self.players_id,
                "Round_history": self.round_history
                }

    @classmethod
    def from_dict(cls, tournament_name: str):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        loaded_tournament = db.search((Query().Tournament_name == tournament_name))
        return cls(loaded_tournament[0]["Tournament_name"],
                   loaded_tournament[0]["Tournament_location"],
                   loaded_tournament[0]["Start_date"],
                   loaded_tournament[0]["End_date"],
                   loaded_tournament[0]["Number_of_round"],
                   loaded_tournament[0]["Players_ID"],
                   loaded_tournament[0]["Round_history"],
                   )

    def update_tournament(self):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        last_tournament = db.all()[-1]
        id_tournament = [last_tournament.doc_id]
        db.update({"Number_of_round": self.number_of_round}, doc_ids=id_tournament)
        db.update({"Round_history": self.round_history}, doc_ids=id_tournament)

    @classmethod
    def search_tournament(cls, tournament_name: str) -> bool:
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        searched_tournament = db.search(Query().Tournament_name == tournament_name)
        if searched_tournament:
            return True
        else:
            return False
