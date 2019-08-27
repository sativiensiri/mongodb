from bson import json_util
from bson.json_util import dumps
import json
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'comet'
#app.config['MONGO_URI'] = 'mongodb://10.44.128.98:27017/comet'
app.config['MONGO_URI'] = 'mongodb://rabbitmq:password@10.44.94.135:27017/rabbitmq'
mongo = PyMongo(app)


@app.route("/")
def hello():
    return "Welcome to Python Flask and MongoDB!"


@app.route('/rabbitmq', methods=['GET'])
def get_all_rabbit():
    try:
        data = mongo.db.message
        output = []
        for s in data.find():
            output.append(json.loads(json_util.dumps(s)))
        return jsonify(output)
    except Exception as e:
        return dumps({'error': str(e)})


@app.route('/rabbitmq/<name>', methods=['GET'])
def get_one_name(name):
    try:
        data = mongo.db.message
        output = []
        s = data.find({'name' : name})
        if s:
            for lst in s:
                output.append(json.loads(json_util.dumps(lst)))
        else:
            output = "No such name"
        #return json.dumps(output)
        return jsonify(output)
    except Exception as e:
        return dumps({'error': str(e)})


@app.route('/upload', methods=['POST'])
def add_star():
    try:
        post = request.get_json()
        print (post)
        posts = mongo.db.message
        post_id = posts.insert_one(post).inserted_id
        print(post_id)
        return jsonify({'result' : str(post_id)})
    except Exception as e:
        return dumps({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)