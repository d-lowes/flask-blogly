"""Blogly application."""

import os

from flask import Flask, request, redirect, render_template
from models import connect_db, db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get("/")
def home_page():
   """redirect to /users"""

   return redirect("/users")

@app.get("/users")
def show_users():
   """render users.html w/ list of all users"""

   # get the user from the table and add to users
   users = [
      {"first_name": "jane", "last_name": "smith"},
      {"first_name": "jane", "last_name": "smith"}
      ]

   return render_template("users.html", users = users)

@app.get("/users/new")
def new_user():
   """Display an add form ; submit the form data and return back to users page"""




