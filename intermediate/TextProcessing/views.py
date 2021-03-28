from flask import Blueprint, render_template
TextProcessor = Blueprint("text_views", __name__)

@TextProcessor.route("/text/")
def TextHome():
    return "hi from text"

@TextProcessor.route("/text/caps/<string:text>", methods=["GET", "POST"])
def Capitalize(text):
    return text.upper()

@TextProcessor.route("/text/lower/<string:text>", methods=["GET", "POST"])
def LowerCase(text):
    return text.lower()