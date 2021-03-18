import requests

BASE = 'http://127.0.0.1:5000/'

data = [
   {'usr_id':       '0',
    'job_title':    'Developer',
    'fname':        'Krish',
    'lname':        'Lee',
    'empl_code':    'E1',
    'region':       'CA',
    'phone_num':    '1234567',
    'email':        'krish.lee@learningcontainer.com'
    }
]

response = requests.put(BASE+'form/0', data[0])
print(response)
response = requests.get(BASE+'form/0')
print(response)