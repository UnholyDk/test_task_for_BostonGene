import os

import requests

SERVER_HOST = os.environ.get('HTTP_TESTS_SERVER_HOST', 'server')
SERVER_PORT = int(os.environ.get('HTTP_FLASK_PORT', 80))
URL = 'http://' + SERVER_HOST
if SERVER_PORT != 80:
    URL += ':{}'.format(SERVER_PORT)


def test_hello_world():
    response = requests.get(URL + '/')
    assert response.text == 'Hello, World!'
    assert response.status_code == 200


def test_1():
    responce = requests.post(URL + '/create_calc',
                            json={'expression': 'x*t**y',
                                'variables': {'x': 10, 'y': 1, 't': 11}})
                                
    assert responce.status_code == 200
    expression_id = responce.json()['expression_id']
    assert expression_id >= 0
    
    responce = requests.get(URL + f'/get_result/{expression_id}')

    assert responce.status_code == 200
    assert responce.json()['result'] == 110


def test_2():
    responce = requests.post(URL + '/create_calc',
                            json={'expression': 'x+y+z+t',
                                'variables': {'x': 10, 'y': 1, 't': 11}})
                                
    assert responce.status_code == 400


def test_3():
    responce = requests.post(URL + '/create_calc',
                            json={'expression': 'x+y / t',
                                'variables': {'x': 10, 'y': 1, 't': 0}})
                                
    assert responce.status_code == 400

def test_4():
    responce = requests.post(URL + '/create_calc',
                            json={'expression': '(x*x + y*y) ** 0.5',
                                'variables': {'x': 8, 'y': 6}})
                                
    assert responce.status_code == 200
    expression_id = responce.json()['expression_id']
    assert expression_id >= 0
    
    responce = requests.get(URL + f'/get_result/{expression_id}')

    assert responce.status_code == 200
    assert responce.json()['result'] == 10

def test_5():
    responce = requests.post(URL + '/create_calc',
                            json={'expression': '(x*x + y*y) ** 0.5',
                                'variables': {'x': 8, 'y': 6}})
                                
    assert responce.status_code == 200
    expression_id = responce.json()['expression_id']
    assert expression_id >= 0
    
    responce = requests.get(URL + f'/get_result/{expression_id + 1}')
    assert responce.status_code == 404