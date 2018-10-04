import json
import os
import psycopg2 as dbapi2
import re
import flask

from flask import Flask
from flask import redirect,render_template, flash
from flask.helpers import url_for
from flask import Blueprint, redirect, render_template, url_for
from flask import current_app, request
from flask_login import LoginManager
from flask_login.utils import login_required, login_user, current_user, logout_user
from passlib.apps import custom_app_context as pwd_context

def create_app():
    app = Flask(__name__)
    return app
app =create_app()

@app.route('/', methods=['GET', 'POST'])
def mainPage():
    return render_template('mainPage.html')

@app.route('/topicOne', methods=['GET', 'POST'])
def topicOne():
    return render_template('topicOne.html')

@app.route('/topicTwo', methods=['GET', 'POST'])
def topicTwo():
    return render_template('topicTwo.html')

@app.route('/topicThree', methods=['GET', 'POST'])
def topicThree():
    return render_template('topicThree.html')

@app.route('/lol', methods=['GET', 'POST'])
def lol():
    return render_template('practice.html')

if __name__ == '__main__':
    app.secret_key = 'secret key'
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 2000, True
        app.config['dsn'] = """user='vagrant' password='vagrant'
                               host='localhost' port=5432 dbname='database'"""

    app.run(host='0.0.0.0', port=port, debug=debug)