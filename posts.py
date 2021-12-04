from datetime import date
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Post
from . import db

posts = Blueprint("posts", __name__)


@posts.route("/create_post")
@login_required
def create_post():
    print("Holi")
    return render_template("create_post.html")


@posts.route("/create_post", methods=["POST"])
@login_required
def create_post_post():

    print(request.form)

    # get data from the form fields
    title = request.form.get("name")
    place = request.form.get("place")
    date = request.form.get("date")
    time = request.form.get("time")
    duration = request.form.get("duration")
    description = request.form.get("description")
    contact = request.form.get("contact")
    capacity = request.form.get("capacity")
    public = False if request.form.get("privateCheck") else True
    user_id = current_user.get_id()

    print("Title:", title)
    print("Place:", place)
    print("Date:", date)
    print("Time:", time)
    print("Duration:", duration)
    print("Description:", description)
    print("Contact:", contact)
    print("Public:", public)
    print("User id:", user_id)

    # create a new event post
    new_post = Post(
        title=title,
        place=place,
        date=date,
        duration=duration,
        time=time,
        description=description,
        capacity=capacity,
        contact=contact,
        public=public,
        user_id=user_id,
    )

    # add the new post to the database
    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for("main.index"))


@posts.route("/delete_post/<id>")
@login_required
def delete_post_post(id):
    post = Post.query.filter_by(id=id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("main.index"))
