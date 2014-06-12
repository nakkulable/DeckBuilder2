from os import abort
from flask import jsonify, Response
from flask.ext.login import login_required, current_user,request
from app import app
from app.DAO import mongo
import re

__author__ = 'Davor Obilinovic'

@login_required
@app.route("/autocomplete/<user_name>/addToDeck/<deck_name>", methods=['GET'])
def autocomplete_add_to_deck(user_name, deck_name):
    if current_user.get_id() != user_name:
        abort(500)
    text = request.args['query']
    regx = re.compile("^"+text, re.IGNORECASE)
    cur = mongo.CardDocument.find({'owner':user_name, 'name': regx, 'decks':{'$ne':deck_name}},{'id':1,'name':1,'_id':0})
    res = []
    for obj in cur:
        e = {'value':obj['name'],'data':obj['id']}
        res.append(e)
    return jsonify(suggestions=res)
