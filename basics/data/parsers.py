import flask
from flask_restful import reqparse, fields

data_parser = reqparse.RequestParser()
data_parser.add_argument('job_title', type=str, help='Job title missing', required=False)
data_parser.add_argument('fname', type=str, help='First name missing', required=True)
data_parser.add_argument('lname', type=str, help='Last name missing', required=True)
data_parser.add_argument('empl_code', type=str, help='employee code missing', required=True)
data_parser.add_argument('region', type=str, help='region missing', required=False)
data_parser.add_argument('phone_num', type=str, help='phone number missing', required=False)
data_parser.add_argument('email', type=str, help='email missing', required=True)

mfields = {
    'job_title':fields.String,
    'fname':fields.String,
    'lname':fields.String,
    'empl_code':fields.String,
    'region':fields.String,
    'phone_num':fields.String,
    'email':fields.String
}