import click

from flask import Flask, g
from flask.cli import with_appcontext
from flask_migrate import Migrate

from ..models.db import Database
from ..models.migrator import Migrator
from ..models import config
from ..views import home, factory


def create_app():
    # proper init sequence from here: https://stackoverflow.com/a/20749534/14748231
    app = Flask(__name__)
    db = Database()
    db.init_app(app)

    # TODO: separate different flask modes with more smarter enabling (maybe via click.command)
    # source: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Config.from_object
    app.config.from_object(config.DevelopmentConfig())

    # source: https://github.com/miguelgrinberg/flask-migrate
    migrate = Migrate(app, db.get())
    # if first time initialization:
    # -- $ flask db init
    # after each change at models:
    # -- $ flask db migrate
    # -- $ flask db upgrade

    # chain to blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(factory.bp)

    app.cli.add_command(migrate_initial_instances)

    return app


@click.command("mii")
@with_appcontext
def migrate_initial_instances():
    migrator = Migrator()

    click.echo("Migration of initial instances has been started... it may took some time...")
    click.echo("<>" * 10)

    click.echo("Migration of countries...")
    migrator.migrate_countries()
    click.echo("...Done!")

    click.echo("-" * 20)
    click.echo("Migration of championships...")
    migrator.migrate_championships()
    click.echo("...Done!")

    click.echo("=" * 20)
    click.echo("Migration completed!")

