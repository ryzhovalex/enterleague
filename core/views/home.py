from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from ..models import User


bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    users = User.query.all()
    return render_template("home.html", users=users)
