from flask import Flask, jsonify
app = Flask(__name__)


acts = [
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

@app.route('/charity/api/user/acts/', methods=['GET'])
def get_acts():
    return jsonify({'acts': acts})


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

