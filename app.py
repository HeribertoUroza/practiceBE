from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def test():
    return 'workinggg'


if __name__ == '__main__':
    app.debug = True
    app.run()