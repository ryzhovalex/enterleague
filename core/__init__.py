import os
import click
import random
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_migrate import Migrate


db = SQLAlchemy()


def create_app():
    # proper init sequence from here: https://stackoverflow.com/a/20749534/14748231
    app = Flask(__name__)

    # TODO: separate different flask modes with more smarter enabling (maybe via click.command)
    # source: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Config.from_object
    from . import config
    app.config.from_object(config.DevelopmentConfig())

    db.init_app(app)

    # source: https://github.com/miguelgrinberg/flask-migrate
    migrate = Migrate(app, db)
    # if first time initialization:
    # -- $ flask db init
    # after each change at models:
    # -- $ flask db migrate
    # -- $ flask db upgrade

    app.cli.add_command(add_test_player)

    from .views import home
    app.register_blueprint(home.bp)

    from .models import Player

    return app


@click.command("add-test-player")
@with_appcontext
def add_test_player():
    from .models import Player
    player = Player(firstname="Max", surname="Kudr", age=random.randint(6, 60))
    db.session.add(player)
    db.session.commit()
    click.echo("New test player added.")


