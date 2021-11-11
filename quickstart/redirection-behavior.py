from flask import Flask

app = Flask(__name__)

@app.route('/project/')
def project():
    return 'The Project page'

@app.route('/about')
def about():
    return 'The about page'
