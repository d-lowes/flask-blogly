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
def show_homePage():
   """Display Home Page"""

   return render_template("home.html")

# @app.post("/")
# def something():
#    """Fill in later"""