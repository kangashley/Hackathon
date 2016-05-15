import datetime
import json
import pymongo
from pymongo import MongoClient
from flask import Flask, jsonify, request
from bson import json_util

app = Flask(__name__)

client = MongoClient('localhost',27017)
db = client.users

def toJson(data):
    return json.dumps(data, default=json_util.default)
users = db.users

def add_act_to_db(act):
    user_id = users.insert_one(act).inserted_id

def open_json():
    with open("users.json") as json_file:
        json_data = json.load(json_file)
    return json_data



##get all users
@app.route('/charity/api/users', methods=['GET'])
def get_users():
    loaded = open_json()

    users = db.users
    user_id = users.insert(loaded).inserted_id
    results = []
    for user in db.users.find():
        results.append(user)
    # json_results = []
    # for result in results:
    #     json_results.append(results)
    return toJson(results)

##get all acts for a given user
@app.route('/charity/api/users/<string:user_id>/acts', methods=['GET'])
def get_acts_for_user(user_id):

    open_json()

    return jsonify({'acts': users[user_id]})

##add new act to user's list
@app.route('/charity/api/users/<string:user_id>/acts', methods=['POST'])
def post_act(user_id):

    # validate_new_post(request.json)

    act = {
        'title': request.json['title'],
        'description': request.json['description'],
        'create_date': "2016-5-3", ##datetime.date.today(),
        'elapsed_time': request.json['elapsed_time'],
        'completed': True
    }

    users = db.users
    user_id = users.insert(act).inserted_id


    return jsonify({'act': act}), 201



##add new user
@app.route('/charity/api/users', methods=['POST'])
def post_user():

    # validate_new_post(request.json)


    users[request.json['username']] = []
    return jsonify(), 201


def validate_new_post(json):
    return None

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)