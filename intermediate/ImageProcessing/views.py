from flask import Blueprint, request, redirect, render_template, url_for
from . import processing
import json

ImageProcessor = Blueprint("image_views", __name__)
EMPTY_IMG = {'filename': '','image': ''}

@ImageProcessor.route("/image/")
def ImageHome():
    return "hi from image"

@ImageProcessor.route("/image/upload/<string:func_name>", methods=["GET", "POST"])
def UploadImage(func_name):
    if valid_func(func_name):
        return render_template("images/upload.html", func_name=func_name)
    return redirect(ImageHome)

@ImageProcessor.route("/image/view/<string:func_name>", methods=["GET", "POST"])
def ViewImage(func_name):
    if request.method == "POST":
        img = request.form['image']
        processed_img = process(img, func_name)
        processed = {
            'filename': f'processed_{request.form["filename"]}',
            'image': processed_img
        }
        return render_template("images/view.html", original=request.form, processed=processed)
    return render_template("images/view.html", original=EMPTY_IMG, processed=EMPTY_IMG)

def process(img_data, func_name):
    prefix, img_64 = img_data.split(',')
    img = processing.base64.decode(img_64)
    img_gray = processing.__dict__[func_name](img)
    return prefix+","+processing.base64.encode(img_gray)

def valid_func(func_name):
    if func_name in processing.__dict__ and func_name[:3] == "img":
        return hasattr(processing.__dict__[func_name], "__call__")
    return False