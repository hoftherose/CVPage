# import os
from flask import Flask, render_template, request#, redirect, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from data.parsers import mfields, data_parser

app = Flask(__name__)
api = Api(app)
db_uri = 'sqlite:///data/database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

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

db.create_all()

class DataBaseController(Resource):
    @marshal_with(mfields)
    def get(self, id):
        result = EmployeeModel.query.filter_by(usr_id=id).first()
        return result, 201
    
    @marshal_with(mfields)
    def put(self, id):
        form = data_parser.parse_args()
        entry = EmployeeModel(**form)
        db.session.add(entry)
        db.session.commit()
        return entry, 201
    
    # @marshal_with(mfields)
    # def post(self, id):
    #     form = data_parser.parse_args()
    #     entry = EmployeeModel(**form)
    #     db.session.add(entry)
    #     db.session.commit()
    #     return entry, 201

    def delete(self, id):
        pass

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/form/<int:usr_id>')
# def form(usr_id):
#     return render_template("form.html")

api.add_resource(DataBaseController, '/form/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)