#!/usr/bin/python3
""" flask web server - with changes to pass pycodestyle, Derek :P """

from flask import Flask

app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """ this handles calls to /api/hello """
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
