from flask import Flask, request, jsonify
from mongo_connection import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
server_port = config['ports']['server']
api_port = config['ports']['api']

app = Flask(__name__)


@app.route('/api_add_one', methods=['POST'])
def addOne():
    newUser = request.json
    # advancing by 1 the ID in the support table in mongo
    newID = m.updateID()
    # Add the number_id(int) to the new employee data received
    newUser.update({'id_number': newID})
    # insert new validated data to Database
    m.add(newUser)
    return jsonify(newUser)


@app.route('/api_list', methods=['POST'])
def list():
    data_list = []
    recs = m.find()
    for rec in recs:
        first = rec["first"]
        last = rec["last"]
        id = rec["id_number"]
        data_list.append({'id': id, 'first': first, 'last': last})
    return jsonify({'Results:': data_list})


if __name__ == '__main__':
    m = MongoDB(cs, db, tbl)
    app.run(host='localhost', port=api_port)