from flask import Flask
from TextProcessing import TextProcessor

def create_app():
    app = Flask(__name__)
    app.register_blueprint(TextProcessor)
    return app

if __name__ == "__main__":
    create_app().run(debug=True)