from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from ..models.orm import Player


bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    return render_template("home.html")
