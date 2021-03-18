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

data_parser = reqparse.RequestParser()
data_parser.add_argument('usr_id', type=int, help='No id', required=True)
data_parser.add_argument('job_title', type=str, help='No title', required=True)
data_parser.add_argument('fname', type=str, help='First name missing', required=True)
data_parser.add_argument('lname', type=str, help='Last name missing', required=True)
data_parser.add_argument('empl_code', type=str, help='employee code missing', required=True)
data_parser.add_argument('region', type=str, help='region missing', required=True)
data_parser.add_argument('phone_num', type=str, help='phone number missing', required=True)
data_parser.add_argument('email', type=str, help='email missing', required=True)

mfields = {
    'usr_id':fields.Integer,
    'job_title':fields.String,
    'fname':fields.String,
    'lname':fields.String,
    'empl_code':fields.String,
    'region':fields.String,
    'phone_num':fields.String,
    'email':fields.String
}

class EmployeeModel(db.Model):
    usr_id      = db.Column(db.Integer(), primary_key=True)
    job_title   = db.Column(db.String(100), nullable=False)
    fname       = db.Column(db.String(100), nullable=False)
    lname       = db.Column(db.String(100), nullable=False)
    empl_code   = db.Column(db.String(2), nullable=False)
    region      = db.Column(db.String(2), nullable=False)
    phone_num   = db.Column(db.String(7), nullable=False)
    email       = db.Column(db.String(100), nullable=False)
    # created_at  = db.Column(db.DateTime())

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