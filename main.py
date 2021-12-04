from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, Post
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():

    user_id = None

    if current_user.is_anonymous:
        posts = Post.query.filter_by(public=1).all() # We only get public events
    else:
        posts = Post.query.all()
        user_id = int(current_user.get_id())

    print('El id del usuario es:', type(current_user.get_id()))
    print('El id del primer post es:', type(posts[0].user_id))

    return render_template('index.html', posts = posts,
                user_id = user_id)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
    name=current_user.name)