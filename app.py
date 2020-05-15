from flask import Flask, request
from flask_cors import CORS
import os
import requests
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def test():
    return 'ACTIVE'

@app.route('/cocktail')
def cocktail():
    cocktailAPI = os.environ.get('cocktailAPI')
    url = 'https://the-cocktail-db.p.rapidapi.com/random.php'
    headers = {
        "x-rapidapi-host": 'the-cocktail-db.p.rapidapi.com',
        "x-rapidapi-key": cocktailAPI
    }

    r = requests.get(url, headers=headers)
    return r.json()

@app.route('/weather', methods=['GET'])
def weather():
    if request.method == 'GET':
        weatherAPI = os.environ.get('weatherAPI')
        url = 'https://api.darksky.net/forecast/' + weatherAPI + '/40.7829,73.9654'
    
        r = requests.get(url)
        return r.json()

@app.route('/nasa')
def nasa():
    nasaAPI = os.environ.get('nasaAPI')
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + nasaAPI

    r = requests.get(url)
    return r.json()

@app.route('/gif', methods=['POST'])
def gif():
    if request.method == 'POST':
        query = json.loads(request.data.decode('UTF-8'))

        params = {
            'api_key': os.environ.get('gifAPI'),
            'q': query['query'],
            'limit': '1'
        }

        r = requests.get('https://api.giphy.com/v1/gifs/search', params=params)
        return r.json()
        

if __name__ == '__main__':
    app.debug = True
    app.run()