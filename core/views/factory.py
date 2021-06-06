from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from ..models import Player


bp = Blueprint("factory", __name__, url_prefix="/factory")


@bp.route("/")
def factory():
    players = Player.query.all()
    return render_template("factory.html", players=players)
