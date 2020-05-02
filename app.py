from flask import Flask
import requests

app = Flask(__name__)

@app.route('/ping')
def test():
    url = 'https://the-cocktail-db.p.rapidapi.com/random.php'
    headers = {
        "x-rapidapi-host": 'the-cocktail-db.p.rapidapi.com',
        "x-rapidapi-key": ''
    }
    r = requests.get(url, headers=headers)
    return r.json()


if __name__ == '__main__':
    app.debug = True
    app.run()