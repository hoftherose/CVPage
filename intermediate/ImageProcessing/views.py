from flask import Blueprint, request, render_template, url_for
ImageProcessor = Blueprint("image_views", __name__)

@ImageProcessor.route("/image/")
def ImageHome():
    return "hi from image"

@ImageProcessor.route("/image/upload", methods=["GET", "POST"])
def UploadImage():
    if request.method == "POST":
        if 'input_image' in request.files:
            print(request.files['input_image'])
    return render_template("images/upload.html")

@ImageProcessor.route("/image/view")
def ViewImage():
    return render_template("images/view.html")