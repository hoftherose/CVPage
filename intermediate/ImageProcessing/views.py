from flask import Blueprint, request, redirect, render_template, url_for
import json

ImageProcessor = Blueprint("image_views", __name__)

@ImageProcessor.route("/image/")
def ImageHome():
    return "hi from image"

@ImageProcessor.route("/image/upload", methods=["GET", "POST"])
def UploadImage():
    return render_template("images/upload.html")

@ImageProcessor.route("/image/view", methods=["GET", "POST"])
def ViewImage():
    data = json.loads(request.data)
    if request.method == "POST":
        return render_template("images/view.html", data=data)
    return render_template("images/view.html")