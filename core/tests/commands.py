import os
import click
import random
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from ..models import Player


@click.command("add-test-player")
@with_appcontext
def add_test_player():
    player = Player(firstname="Max", surname="Kudr", age=random.randint(6, 60))
    db.session.add(player)
    db.session.commit()
    click.echo("New test player added.")


def init_app(app, database):
    global db # TODO: remove global var and instead of it make class or something different
    app.cli.add_command(add_test_player)
    db = database