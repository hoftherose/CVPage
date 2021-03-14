import json
from flask import Flask, render_template, request#, redirect, url_for
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return request.form["form"]
    return render_template("form.html")

@app.route('/get', methods=['GET', 'POST'])
def employee_data():
    if request.method == 'POST':
        file = open('basics/data/data.json', 'w')
        data = json.load(file)
        data[len(data)] = request.form["data"]
    file = open('basics/data/data.json', 'r')
    data = json.load(file)
    return data

if __name__ == '__main__':
    app.run(debug=True)