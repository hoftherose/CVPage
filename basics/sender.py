import requests

BASE = 'http://127.0.0.1:5000/'

data = [
   {'usr_id':       '0',
    'job_title':    'Developer',
    'fname':        'Krsh',
    'lname':        'Lee',
    'empl_code':    'E1',
    'region':       'CA',
    'phone_num':    '134567',
    'email':        'krish.lee@learningcontainer.com'
    },
   {'usr_id':       '1',
    'job_title':    'Developer',
    'fname':        'Devid',
    'lname':        'Rome',
    'empl_code':    'Ee',
    'region':       'CA',
    'phone_num':    '1111111',
    'email':        'devid.rome@learningcontainer.com'
    },
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

response = requests.delete(BASE+'form/0')
print(response.json())
input()
response = requests.delete(BASE+'form/1')
print(response.json())
input()
response = requests.post(BASE+'form/0', data[0])
print(response.json())
input()
response = requests.post(BASE+'form/1', data[1])
print(response.json())
input()
response = requests.put(BASE+'form/0', data[2])
print(response.json())
input()
response = requests.get(BASE+'form/0')
print(response.json())
input()
response = requests.get(BASE+'form/1')
print(response.json())