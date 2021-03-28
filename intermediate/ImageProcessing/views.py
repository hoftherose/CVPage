from flask import Blueprint, render_template, url_for
ImageProcessor = Blueprint("image_views", __name__)

@ImageProcessor.route("/image/")
def ImageHome():
    return "hi from image"

@ImageProcessor.route("/image/upload")
def UploadImage():
    return render_template("images/upload.html")