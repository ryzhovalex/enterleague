""" Controller for performing initial data migrations """

import os
import csv
import click

from .db import Database
from .orm import ChampionshipsCollection, Country, Player, Club
from ..tools.data_manipulator import make_rel_path


class Migrator:
    # TODO: add check if initial migration has been performed already with checking appropriate database info
    def __init__(self):
        self.db = Database()

    def perform_initial_migration(self):
        ECHO_NAMES = ["countries", "championships", "clubs"]
        FUNCTIONS = [self._migrate_countries, self._migrate_championships, self._migrate_clubs]

        click.echo("Migration of initial instances has been started... it may took some time...")
        click.echo("<>" * 10)

        for x in range(len(ECHO_NAMES)):
            if x != 0:
                click.echo("-" * 20)
            click.echo(f"Migration of {ECHO_NAMES[x]}...")
            FUNCTIONS[x]()
            click.echo("...Done!")
            if x == len(ECHO_NAMES - 1):
                click.echo("=" * 20)
                click.echo("Migration completed!")


    def _migrate_countries(self):
        with open(make_rel_path("../data/countries.csv"), "r") as file:
            csv_file = csv.DictReader(file, delimiter=";")	
            countries = []
            for row in csv_file:
                assert row["prototype"]
                country = Country(name=row["name"], prototype=row["prototype"])
                self.db.add(country)
                self.db.commit()

    def _migrate_championships(self):
        # create standard 5 home leagues for all countries
        countries = Country.query.all()
        for country in countries:
            for x in range(1, 6):
                championship = ChampionshipsCollection(name=f"{country.name} Division {x}", country_id=country.id)
            self.db.add(championship)
            self.db.commit()

        # add all other championships from a csv file
        # ...

    def _migrate_clubs(self):
        # migrate all clubs from a csv file
        with open(make_rel_path("../data/clubs.csv"), "r") as file:
            csv_file = csv.DictReader(file, delimiter=";")
            clubs = []
            for row in csv_file:
                country = Country.query.filter_by(name=row["country"]).first()
                club = Club(name=row["name"], country_id=country.id)

        