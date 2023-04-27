"""Blogly application."""

import os

from flask import Flask, request, redirect, render_template
from models import connect_db, db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# debug = DebugToolbarExtension(app)

connect_db(app)


@app.get("/")
def home_page():
    """redirect to /users"""

    return redirect("/users")


@app.get("/users")
def show_users():
    """render users.html w/ list of all users"""

    # TODO: add order by to users
    users = User.query.all()

    return render_template("users.html", users=users)


@app.get("/users/new")
def new_user():
    """Display an add form ; submit the form data and return back to users page"""

    return render_template("new_users.html")


@app.post("/users/new")
def new_user_form():
    """submit new user form to user's class"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"] or None

    user = User(first_name=first_name,
                last_name=last_name,
                image_url=image_url)

    db.session.add(user)
    db.session.commit()
    #TODO: flash message user added

    return redirect("/users")


@app.get("/users/<int:id>")
def show_user(id):
    """Display info about the current user, with edit page and delete user
    options"""

    user = User.query.get_or_404(id)

    return render_template("user_detail.html", user=user)


@app.get("/users/<int:id>/edit")
def edit_user(id):
    """Show edit page for user"""

    user = User.query.get_or_404(id)

    return render_template("edit_user.html", user=user)


@app.post("/users/<int:id>/edit")
def save_user_edit(id):
    """Process the edit form and redirect to the user page"""

    user = User.query.get_or_404(id)

    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.post("/users/<int:id>/delete")
def delete_user(id):
    """Delete the user"""

    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/users")
