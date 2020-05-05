from flask import Flask
import requests

app = Flask(__name__)

@app.route('/ping')
def test():
    weatherAPI = ''
    url = 'https://api.darksky.net/forecast/' + weatherAPI + '/40.7829,73.9654'
    
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    app.debug = True
    app.run()