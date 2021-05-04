from flask import Blueprint, render_template
import json

HomePage = Blueprint("home_pages", __name__)

@HomePage.route("/")
def Home():
    return render_template("main/main.html")

@HomePage.route("/projects")
def Projects():
    return render_template("main/projects.html")