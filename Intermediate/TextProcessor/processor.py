from flask import Blueprint, render_template

processor = Blueprint("processor", __name__, static_folder="static", template_folder="template")

@processor.route("/")
def processor_home():
    return render_template("text_home.html")