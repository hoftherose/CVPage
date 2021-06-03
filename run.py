from flask import Flask
from Blueprints import HomePage, TextProcessor, ImageProcessor

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(HomePage)
    app.register_blueprint(TextProcessor)
    app.register_blueprint(ImageProcessor)

    app.config["CACHE_TYPE"] = "null"
    return app

if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)