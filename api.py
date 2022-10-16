import flask
import details

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# import resume data from another file

@app.route('/', methods=['GET'])
def home():
    return details.resume

@app.route('/bio', methods=['GET'])
def bio():
    return details.resume['basics']

@app.route('/skills', methods=['GET'])
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

app.run()
