from . import bp as app
from flask import render_template

# Routes that return JSON
user_data = { # Mock database data
    'lucasl': {
        'user_id': 0,
        'name': 'Lucas',
        'favoriteColor': 'blue',
        'posts': [
            {
                'id': 0,
                'title': 'This is post 1',
                'body': 'This is the text for the post'
            },
            {
                'id': 1,
                'title': 'This is post 2',
                'body': 'This is the text for the post'
            },
            {
                'id': 2,
                'title': 'This is post 3',
                'body': 'This is the text for the post'
            }
        ]
    },
    'christophert': {
        'user_id': 1,
        'name': 'Christopher',
        'favoriteColor': 'orange',
        'posts': [
            {
                'id': 3,
                'title': 'This is post 4',
                'body': 'This is the text for the post'
            },
            {
                'id': 4,
                'title': 'This is post 5',
                'body': 'This is the text for the post'
            },
            {
                'id': 5,
                'title': 'This is post 6',
                'body': 'This is the text for the post'
            }
        ]
    },
    'joelc': {
        'user_id': 2,
        'name': 'Joel',
        'favoriteColor': 'red',
        'posts': [
            {
                'id': 6,
                'title': 'This is post 7',
                'body': 'This is the text for the post'
            },
            {
                'id': 7,
                'title': 'This is post 8',
                'body': 'This is the text for the post'
            },
            {
                'id': 8,
                'title': 'This is post 9',
                'body': 'This is the text for the post'
            }
        ]
    }
}

# Create a route to get all user information
@app.route('/users/')
def users():
    return user_data

# Create a route to get user information based on their username
@app.route('/user/username/<username>')
def user(username):
    if username not in user_data:
        return 'User not found'

    return user_data[username]

# Create a route to get user information based on their id
@app.route('/user/id/<id>')
def user_by_id(id):
    for key, user in user_data.items():
        if user['user_id'] == int(id):
            return user

    return 'User not found'


car_data = {
    0: {
        "name": "Maruti Swift Dzire VDI",
        "year": 2014,
        "selling_price": 450000
    },
    1: {
        "name": "Skoda Rapid 1.5 TDI Ambition",
        "year": 2014,
        "selling_price": 370000
    },
    2: {
        "name": "Honda City 2017-2020 EXi",
        "year": 2006,
        "selling_price": 158000
    }
}

# Create a route that lists all of the cars in car_data
@app.route('/cars/')
def cars():
    return car_data

@app.route('/cars/year/<year>')
def car_by_year(year):
    car_result = {}

    for key, car in car_data.items():
        if car['year'] == int(year):
            car_result[key] = car

    return car_result

@app.route('/cars/id/<id>')
def car_by_id(id):
    if int(id) not in car_data:
        return 'Car not found'

    return car_data[int(id)]