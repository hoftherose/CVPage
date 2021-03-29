from flask import Blueprint, request, render_template, url_for
ImageProcessor = Blueprint("image_views", __name__)

@ImageProcessor.route("/image/")
def ImageHome():
    return "hi from image"

@ImageProcessor.route("/image/upload", methods=["GET", "POST"])
def UploadImage():
    if request.method == "POST":
        file = request.files['input_image']
        if file.filename != "":
            file.save(f'static/assets/temp/{file.filename}')
            return render_template("images/upload.html", file=file)
    return render_template("images/upload.html")

@ImageProcessor.route("/image/view")
def ViewImage():
    return render_template("images/view.html")