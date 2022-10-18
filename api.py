import flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import pymongo
import details

app = flask.Flask(__name__)

limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=['50 per hour', '100 per day'],
        storage_uri="memory://"
        )

# TODO authentication token based

# TODO link to database

# TODO link to redis cache

# TODO updates methods for different actions routes are below

@app.route('/', methods=['GET'])
def home():
    return details.resume

@app.route('/bio', methods=['GET'])
@limiter.limit("15/minute;1/second")
def bio():
    return details.resume['basics']

@app.route('/skills', methods=['GET'])
@limiter.limit('5/minute')
def skills():
    return details.resume['skills']

@app.route('/social', methods=['GET'])
def social():
    return details.resume['profiles']

@app.route('/projects', methods=['GET'])
def projects():
    return details.resume['projects']

@app.route('/work', methods=['GET'])
def work_exp():
    return details.resume['work']

@app.route('/awards', methods=['GET'])
def awards():
    return details.resume['awards']

@app.route('/certs', methods=['GET'])
def certs():
    return details.resume['certificates']

if __name__ == '__main__':
    app.run(
            host='127.0.0.1',
            port=43210,
            debug=True
            )
