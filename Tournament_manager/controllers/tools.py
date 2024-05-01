import csv
import os

from Tournament_manager.controllers.constants import PLAYERS_FIELDNAMES
from Tournament_manager.models.player import Player


def create_report_folder():
    """folders and csv file creation"""
    try:
        os.mkdir('../output')

    except:
        print('Folders and files already exist. deliverables will be create in existing folder ')

    with open('../output/players_list_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=PLAYERS_FIELDNAMES)
        writer.writeheader()

    create_players_list_report()


def create_players_list_report():
    """save information in csv file"""
    saved_players_db = Player.search_all_players()
    with open('../output/players_list_report.csv', 'a', newline='', encoding='utf-8') as csvfile:
        for info in saved_players_db:
            writer = csv.DictWriter(csvfile, fieldnames=PLAYERS_FIELDNAMES)
            writer.writerow({'number of player': info['Number_of_player'],
                             'Name': info['Name'],
                             'Birthday': info['Birthday'],
                             'Chess national ID': info['Chess_national_ID'],
                             'Score': info['Score'],
                             })
    print('--- Successful extraction of players list ---')
    print("-----------------------------------------------------")

# "Number_of_player": 1,
# "Name": "Maxime",
# "Birthday": "1987-02-08",
# "Chess_national_ID": "JH345",
# "Score": 2
# {'Number_of_player': 1, 'Name': 'Maxime', 'Birthday': '1987-02-08', 'Chess_national_ID': 'JH345', 'Score': 2}
