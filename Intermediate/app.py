from flask import Flask, render_template
from TextProcessor.processor import processor

app = Flask(__name__, static_folder="static", template_folder="template")
app.register_blueprint(processor, url_prefix="/text/")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)