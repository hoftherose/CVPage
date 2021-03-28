from flask import Blueprint
ImageProcessor = Blueprint("image_views", __name__)

@ImageProcessor.route("/image/")
def ImageHome():
    return "hi from image"

@ImageProcessor.route("/image/upload")
def UploadImage():
    return "upload here"