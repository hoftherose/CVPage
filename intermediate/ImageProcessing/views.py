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
    if request.method == "POST":
        img = request.form['image']
        processed_img = process(img)
        processed = {
            'filename': f'processed_{request.form["filename"]}',
            'file': processed_img
        }
        return render_template("images/view.html", original=request.form, processed=processed)
    return render_template("images/view.html")

def process(img):
    return img