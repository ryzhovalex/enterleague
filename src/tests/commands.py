import os
import click
from random import randint

from flask.cli import with_appcontext

from ..models.orm import Player


@click.command("add-test-player")
@with_appcontext
def add_test_player():
    global db
    player = Player(firstname="Max", surname="Kudr", age=randint(6, 60))
    db.session.add(player)
    db.session.commit()
    click.echo("New test player added.")


def init_app(app, database):
    global db
    app.cli.add_command(add_test_player)
    db = database