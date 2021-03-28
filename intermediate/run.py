from flask import Flask
from TextProcessing import TextProcessor
from ImageProcessing import ImageProcessor

def create_app():
    app = Flask(__name__)
    app.register_blueprint(TextProcessor)
    app.register_blueprint(ImageProcessor)
    return app

if __name__ == "__main__":
    create_app().run(debug=True)