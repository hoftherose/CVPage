from flask import Blueprint, request, redirect, render_template, url_for
from . import processing
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
            'image': processed_img
        }
        return render_template("images/view.html", original=request.form, processed=processed)
    return render_template("images/view.html", original={'filename': '','image': ''}, processed={'filename': '','image': ''})

def process(img_data):
    prefix, img_64 = img_data.split(',')
    img = processing.base64.decode(img_64)
    img_gray = processing.img2gray(img)
    return prefix+","+processing.base64.encode(img_gray)