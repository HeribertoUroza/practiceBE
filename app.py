from flask import Flask
import requests

app = Flask(__name__)

@app.route('/cocktail')
def cocktail():
    url = 'https://the-cocktail-db.p.rapidapi.com/random.php'
    headers = {
        "x-rapidapi-host": 'the-cocktail-db.p.rapidapi.com',
        "x-rapidapi-key": ''
    }
    r = requests.get(url, headers=headers)
    return r.json()

@app.route('/weather')
def weather():
    weatherAPI = ''
    url = 'https://api.darksky.net/forecast/' + weatherAPI + '/40.7829,73.9654'
    
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    app.debug = True
    app.run()