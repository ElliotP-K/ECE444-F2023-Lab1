from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment


app = Flask(__name__)
moment = Moment()
bootstrap = Bootstrap(app)
moment.init_app(app)


@app.route('/')
def index():
    return render_template('index.html', name='Elliot', current_time=datetime.utcnow())
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())
