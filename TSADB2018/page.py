from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from bson.json_util import dumps
from flask_pymongo import PyMongo
from flask import make_response
import math, sys
import config



app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = config.mongo_url

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def retreive():
    return render_template('index.html')


@app.route("/getGame/", methods=["GET"])
def getMarkers():
    collection = mongo.db.posts
    doc = collection.find({})
    if collection is None:
        return "nada"
    else:
        cosa = []
        for doc in collection.find():
            try:
                float(doc['place']['type'])
            except ValueError as err:
                cosa.append(doc)


    return dumps(cosa)

    if existing_user is None:
        hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
        users.insert({'name' : request.form['username'], 'password' : hashpass})
        session['username'] = request.form['username']
        return redirect(url_for('index'))

        return 'That username already exists!'

        return render_template('register.html')


@app.route("/sendRequest/<string:query>")
def results(query):
    collection = mongo.db.game
    return query
    payload = new_url+"query="+query+"&key="+key
    req = requests.get(payload)
    json = req.json()
    place_id = json["results"][0]["id"]
    return jsonify({'result' : place_id})


if __name__ ==  "__main__":
    app.run(debug=True)
