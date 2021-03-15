import json
from flask import Flask, render_template, request#, redirect, url_for
from flask_restful import Api

from forms.forms import modify_data

app = Flask(__name__)
api = Api(app)

fn = 'basics/data/data.json'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        with open(fn, 'r') as f: data = json.load(f)

        ok = modify_data(data, request)
        
        with open(fn, 'w') as f: json.dump(data, f)

        if ok: return render_template("form.html", error=False)
        return render_template("form.html", error=True)
    return render_template("form.html", error=False)

@app.route('/data', methods=['GET'])
def data():
    file = open(fn, 'r')
    data = json.load(file)
    file.close()
    return data

if __name__ == '__main__':
    app.run(debug=True)