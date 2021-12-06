from flask_login import UserMixin
from sqlalchemy.orm import defaultload
from . import db
import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(200))
    admin = db.Column(db.Boolean, default=False)

    # we create the relation between one user and many posts
    posts = db.relationship("Post", backref="user", lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))  # Title of the post
    place = db.Column(db.String(100))  # Place of the event
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow
    )  # Date of creation of the post
    date = db.Column(db.String(100))  # Date the event will take place
    time = db.Column(db.String(100))  # Time the event will take place
    duration = db.Column(db.String(50))  # Duration of the event
    due_date = db.Column(db.DateTime)    # Due date
    expired = db.Column(db.Boolean, default=False) # If event is expired
    description = db.Column(db.String(500))  # Description of the event
    capacity = db.Column(db.String(100))
    contact = db.Column(db.String(100))  # Contact with the post creator
    public = db.Column(db.Boolean)  # Whether is a public event or not

    # we create the relation between one user and many posts
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
