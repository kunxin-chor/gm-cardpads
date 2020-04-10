from flask import Flask, render_template, request, redirect, url_for, Response
from dotenv import load_dotenv
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

import os

# load environment data before everything else
load_dotenv()

# DAO import
import data


app = Flask(__name__)

# function to get a mock user
def get_current_user():
    return {
        "user_id": ObjectId('5e9045f5f9ecf35b2e406070'),
        "user_name":"Ah Kun"
    }

@app.route('/add-card', methods=["POST"])
def add_card():
    current_user = get_current_user()
    newly_inserted_id = data.add_card(current_user['user_id'],request.json.get('title'), request.json.get('content'),request.json.get('tags'))
    return Response(dumps({'status':'ok', 'new_card_id':newly_inserted_id}), status=200, mimetype='application/json')

# "magic code" -- boilerplate
if __name__ == '__main__':
    data.add_card("user", "title", "content", "tags")
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)