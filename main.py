from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, Post
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():

    user = None

    if current_user.is_anonymous:
        posts = Post.query.filter_by(public=1).all()  # We only get public events
    else:
        posts = Post.query.order_by(Post.date_created.desc()).all()
        user = User.query.filter_by(id=int(current_user.get_id())).first()
        print(user)

    return render_template("index.html", posts=posts, user=user)


@main.route("/conocenos")
def conocenos():
    return render_template("conocenos.html")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)
