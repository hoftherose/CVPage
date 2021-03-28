from flask import Blueprint, render_template
TextProcessor = Blueprint("views", __name__)

@TextProcessor.route("/text/")
def TextHome():
    return "hi"