from flask import Flask
from Blueprints import HomePage, TextProcessor, ImageProcessor

STATIC_FOLDER = "Frontend"
TEMPLATE_FOLDER = "Frontend/templates"

def create_app():
    app = Flask(__name__,
        static_folder=STATIC_FOLDER,
        template_folder=TEMPLATE_FOLDER
    )
    
    app.register_blueprint(HomePage)
    app.register_blueprint(TextProcessor)
    app.register_blueprint(ImageProcessor)

    app.config["CACHE_TYPE"] = "null"
    return app

if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)