# import os
from flask import Flask, render_template, request#, redirect, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db_uri = 'sqlite:///data/database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)
db.create_all()

class EmployeeModel(db.Model):
    usr_id      = db.Column(db.Integer(), primary_key=True)
    job_title   = db.Column(db.String(100), nullable=False)
    fname       = db.Column(db.String(100), nullable=False)
    lname       = db.Column(db.String(100), nullable=False)
    empl_code   = db.Column(db.String(2), nullable=False)
    region      = db.Column(db.String(2), nullable=False)
    phone_num   = db.Column(db.String(7), nullable=False)
    email       = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'{self.job_title} {self.usr_id}-{self.empl_code}: {self.lname} {self.fname}'

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