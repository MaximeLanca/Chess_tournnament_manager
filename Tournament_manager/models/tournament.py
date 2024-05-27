from tinydb import TinyDB, Query


class Tournament:

    def __init__(self, tournament_name, tournament_location, start_date, end_date, number_of_round, players_id=None,
                 description=None):
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.players_id = players_id or None
        self.rounds_history = []
        self.matches_history = []
        self.description = description

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
                "Round_history": self.rounds_history,
                "Description": self.description
                }

    @classmethod
    def from_db(cls, tournament_name: str):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        loaded_tournament = db.search((Query().Tournament_name == tournament_name))
        if loaded_tournament:
            tournament_data = loaded_tournament[0]
            tournament = cls(tournament_data["Tournament_name"],
                             tournament_data["Tournament_location"],
                             tournament_data["Start_date"],
                             tournament_data["End_date"],
                             tournament_data["Number_of_round"],
                             tournament_data["Players_ID"],
                             tournament_data["Description"]
                             )
            tournament.rounds_history = tournament_data['Round_history']
            return tournament
        else:
            raise ValueError("Tournament not found in database")

    def update_tournament_db(self):
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        last_tournament = db.all()[-1]
        id_tournament = [last_tournament.doc_id]
        db.update({"Number_of_round": self.number_of_round}, doc_ids=id_tournament)
        db.update({"Round_history": self.rounds_history}, doc_ids=id_tournament)

    @classmethod
    def search_tournament_db(cls, tournament_name: str) -> list:
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        searched_tournament = db.search(Query().Tournament_name == tournament_name)
        return searched_tournament

    @classmethod
    def search_all_tournaments_db(cls) -> list:
        db = TinyDB("../Tournament_manager/data/tournaments/tournament.json")
        tournaments_db = db.all()
        return tournaments_db
