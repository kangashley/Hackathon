import datetime
from flask import Flask, jsonify, request
app = Flask(__name__)


users = {'user1': [
            {
                'id': 1,
                'title': u'help an elderly person cross the street',
                'description': u'hold their hand and guide them',
                'create_date': u'2016-11-4',
                'elapsed_time': 5,
                'completed': True
            },
            {
                'id': 2,
                'title': u'deliver groceries for an impoverished family',
                'description': u'go to the grocery store, buy groceries, deliver them',
                'create_date': u'2016-11-8',
                'elapsed_time': 60,
                'completed': True
            }
    ],
    'user2': [
            {
                'id': 1,
                'title': u'help an elderly person cross the street',
                'description': u'hold their hand and guide them',
                'create_date': u'2016-11-4',
                'elapsed_time': 5,
                'completed': True
            },
            {
                'id': 2,
                'title': u'deliver groceries for an impoverished family',
                'description': u'go to the grocery store, buy groceries, deliver them',
                'create_date': u'2016-11-8',
                'elapsed_time': 60,
                'completed': True
            }
    ]
}


##get all users
@app.route('/charity/api/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})

##get all acts for a given user
@app.route('/charity/api/users/<string:user_id>/acts', methods=['GET'])
def get_acts_for_user(user_id):
    return jsonify({'acts': users[user_id]})

##add new act to user's list
@app.route('/charity/api/users/<string:user_id>/acts', methods=['POST'])
def post_act(user_id):

    # validate_new_post(request.json)

    act = {
        'id': len(users[user_id])+1,
        'title': request.json['title'],
        'description': request.json['description'],
        'create_date': "2016-5-3", ##datetime.date.today(),
        'elapsed_time': request.json['elapsed_time'],
        'completed': True
    }

    users[user_id].append(act)
    return jsonify({'act': act}), 201

##add new user
@app.route('/charity/api/users', methods=['POST'])
def post_user():

    # validate_new_post(request.json)

    user = {
        'id': len(users[user_id])+1,
        'name': request.json['name'],
        'description': request.json['description'],
        'create_date': "2016-5-3", ##datetime.date.today(),
        'completed': True
    }

    users.append(user)
    return jsonify({'user': user}), 201


def validate_new_post(json):
    return None

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)