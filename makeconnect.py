from flask import Flask, jsonify, request
import json
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'rabbitmq'
app.config['MONGO_URI'] = 'mongodb://rabbitmq:password@10.44.94.135:27017/rabbitmq'

mongo = PyMongo(app)


@app.route('/rabbitmq', methods=['GET'])
def get_all_rabbit():
    data = mongo.db.message
    output = []
    for s in data.find():
        output.append(json.loads(json_util.dumps(s)))
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)