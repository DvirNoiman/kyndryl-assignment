from flask import Flask, request, jsonify
from mongo_connection import *
from validation import *
import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
server_port = config['ports']['server']
api_port = config['ports']['api']


app = Flask(__name__)



@app.route('/')
def index():
    return 'Main Page'


@app.route('/add', methods=['POST'])
def add():
    # collect data from form
    first = request.form['fname']
    last = request.form['lname']

    # validate input
    if not validate_string(first):
        return jsonify({'Message': "Validation Error: First Name inserted is not valid."})
    if not validate_string(last):
        return jsonify({'Message': "Validation Error: Last Name inserted is not valid."})
    # call API
    data = {'first': first, 'last': last}
    x = requests.post(f'http://localhost:{api_port}/api_add_one', json=data)
    # Display new Data in Page
    return jsonify({'Message': 'Employee Added'})


@app.route('/list', methods=['POST'])
def list():
    data = requests.post(f'http://localhost:{api_port}/api_list', json={'find': 'all'})
    return jsonify({'data': json.loads(data.text)})


if __name__ == '__main__':
    m = MongoDB(cs, db, tbl)
    app.run(host='localhost', port=server_port)