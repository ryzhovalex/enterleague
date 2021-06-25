import os
import csv
import click

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_migrate import Migrate

from ..models import orm


db = SQLAlchemy()


def create_app():
    # proper init sequence from here: https://stackoverflow.com/a/20749534/14748231
    app = Flask(__name__)

    # TODO: separate different flask modes with more smarter enabling (maybe via click.command)
    # source: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Config.from_object
    from ..models import config
    app.config.from_object(config.DevelopmentConfig())

    db.init_app(app)

    # source: https://github.com/miguelgrinberg/flask-migrate
    migrate = Migrate(app, db)
    # if first time initialization:
    # -- $ flask db init
    # after each change at models:
    # -- $ flask db migrate
    # -- $ flask db upgrade

    # add commands for testing and db manipulations
    from ..tests import commands # needs to be inside function, not outside, or we get circular import (because of "db = SQLAlchemy()")
    commands.init_app(app, db)


    # chain to blueprints
    from ..views import home, factory
    app.register_blueprint(home.bp)
    app.register_blueprint(factory.bp)

    app.cli.add_command(migrate_initial_instances)

    return app
   

@click.command("mii")
@with_appcontext
def migrate_initial_instances():
    # TODO: add check if initial migration has been performed already with checking appropriate database info
    click.echo("Migration of initial instances has been started... it may took some time...")
    click.echo("<>" * 10)

    click.echo("Migration of countries...")
    _migrate_countries()
    click.echo("...Done!")

    click.echo("-" * 20)
    click.echo("Migration of something...")
    # template
    click.echo("...Done!")

    click.echo("=" * 20)
    click.echo("Migration completed!")
    db.session.commit()


def _migrate_countries():
    with open(_make_rel_path("data/countries.csv"), "r") as file:
        csv_file = csv.DictReader(file, delimiter=";")	
        countries = []
        for row in csv_file:
            assert row["prototype"]
            country = orm.Country(name=row["name"], prototype=row["prototype"])
            db.session.add(country)
            print("Country %s with prototype %s added!" % (country["name"], country["prototype"]))


def _make_rel_path(path: str) -> str:
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, path)
    