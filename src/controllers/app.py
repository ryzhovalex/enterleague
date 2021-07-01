import click

from flask import Flask, g
from flask.cli import with_appcontext

from ..models.db import Database
from ..models.migrator import Migrator
from ..models import config
from ..views import home, factory


def create_app():
    # proper init sequence from here: https://stackoverflow.com/a/20749534/14748231
    app = Flask(__name__)
    db = Database()

    # TODO: separate different flask modes with more smarter enabling (maybe via click.command)
    # source: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Config.from_object
    app.config.from_object(config.DevelopmentConfig())

    db.init_app(app)
    db.migrate(app)

    # chain to blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(factory.bp)

    app.cli.add_command(migrate_initial_instances)

    from ..models.orm import Player

    return app


@click.command("mii")
@with_appcontext
def migrate_initial_instances():
    migrator = Migrator()
    migrator.perform_initial_migration()

