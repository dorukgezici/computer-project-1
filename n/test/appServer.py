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

def create_app():
    app = Flask(__name__)
    return app
app =create_app()

@app.route('/', methods=['GET', 'POST'])
def mainPage():
    return render_template('mainPage.html')

@app.route('/topicOne', methods=['GET', 'POST'])
def topicOne():
    return render_template('topic_1/topicOne.html')

@app.route('/t1Count', methods=['GET', 'POST'])
def t1Count():
    return render_template('topic_1/t1Count.html')

@app.route('/t1AddSub', methods=['GET', 'POST'])
def t1AddSub():
    return render_template('topic_1/t1AddSub.html')

@app.route('/videoCount', methods=['GET', 'POST'])
def videoCount():
    return render_template('topic_1/videoCount.html')

@app.route('/topicTwo', methods=['GET', 'POST'])
def topicTwo():
    return render_template('topic_2/topicTwo.html')

@app.route('/t2shapes', methods=['GET', 'POST'])
def t2shapes():
    return render_template('topic_2/t2shapes.html')

@app.route('/topicThree', methods=['GET', 'POST'])
def topicThree():
    return render_template('topic_3/topicThree.html')



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