""" Controller for performing initial data migrations """

import os
import csv

from .db import Database
from .orm import ChampionshipsCollection, Country, Player, Club
from ..tools.data_manipulator import make_rel_path


class Migrator:
    # TODO: add check if initial migration has been performed already with checking appropriate database info
    def __init__(self):
        self.db = Database()

    def migrate_countries(self):
        with open(make_rel_path("../data/countries.csv"), "r") as file:
            csv_file = csv.DictReader(file, delimiter=";")	
            countries = []
            for row in csv_file:
                assert row["prototype"]
                country = Country(name=row["name"], prototype=row["prototype"])
                self.db.session.add(country)
                print("Country %s with prototype %s added!" % (country["name"], country["prototype"]))

    def migrate_championships(self):
        # create standard 5 home leagues for all countries
        countries = Country.query.all()
        for country in countries:
            for x in range(1, 6):
                championship = ChampionshipsCollection(name=f"{country.name} Division {x}", country_id=country.id)

        # add all other championships from a csv file
        # ...

    def migrate_clubs(self):
        # migrate all clubs from a csv file
        with open(make_rel_path("../data/clubs.csv"), "r") as file:
            csv_file = csv.DictReader(file, delimiter=";")
            clubs = []
            for row in csv_file:
                country = Country.query.filter_by(name=row["country"]).first()
                club = Club(name=row["name"], country_id=country.id)

        