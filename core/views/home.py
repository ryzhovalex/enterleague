from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from ..models import Player


bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    players = Player.query.all()
    return render_template("home.html", players=players)
