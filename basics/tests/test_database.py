import requests

BASE = 'http://127.0.0.1:5000/'

data = [
   {'job_title':    'Developer',
    'fname':        'Krsh',
    'lname':        'Lee',
    'empl_code':    'E1',
    'region':       'CA',
    'phone_num':    '134567',
    'email':        'krish.lee@learningcontainer.com'
    },
   {'job_title':    'Developer',
    'fname':        'Devid',
    'lname':        'Rome',
    'empl_code':    'Ee',
    'region':       'CA',
    'phone_num':    '1111111',
    'email':        'devid.rome@learningcontainer.com'
    },
   {'job_title':    'Developer',
    'fname':        'Krish',
    'lname':        'Lee',
    'empl_code':    'E1',
    'region':       'CA',
    'phone_num':    '1234567',
    'email':        'krish.lee@learningcontainer.com'
    }
]

def test_delete():
    response = requests.delete(f'{BASE}form/0')
    assert response.status_code == 201
    assert response.json() in ["Deleted 1 row(s)", "Deleted 0 row(s)"]

    response = requests.delete(f'{BASE}form/1')
    assert response.status_code == 201
    assert response.json() in ["Deleted 1 row(s)", "Deleted 0 row(s)"]

    return True

def test_post():
    response = requests.post(BASE+'form/0', data[0])
    assert response.status_code == 201
    assert response.json().keys() == data[0].keys()
    assert list(response.json().values()) == list(data[0].values())
    response = requests.post(BASE+'form/1', data[1])
    assert response.status_code == 201
    assert response.json().keys() == data[1].keys()
    assert list(response.json().values()) == list(data[1].values())
    return True

def test_put():
    response = requests.put(BASE+'form/0', data[2])
    assert response.status_code == 201
    assert response.json().keys() == data[2].keys()
    assert list(response.json().values()) == list(data[2].values())

def test_get():
    response = requests.get(BASE+'form/0')
    assert response.status_code == 201
    assert response.json().keys() == data[2].keys()
    assert list(response.json().values()) == list(data[2].values())

    response = requests.get(BASE+'form/1')
    assert response.status_code == 201
    assert response.json().keys() == data[1].keys()
    assert list(response.json().values()) == list(data[1].values())

    return True