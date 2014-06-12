from os import abort
from flask import request, flash, jsonify
from flask.ext.login import current_user,redirect, login_required
import simplejson
from app import app
from app.DAO import card, mongo

__author__ = 'Davor Obilinovic'

@login_required
@app.route('/callback/createDeck', methods=['POST'])
def create_deck():
    data = request.form
    deck_name = data["deckName"]
    if not current_user.add_deck(deck_name):
        return redirect('/')
    flash("Deck " + deck_name+" created!","info")
    return redirect('/')

@login_required
@app.route('/callback/classifyCard/<card_id>',methods=['POST'])
def classify_card(card_id):
    data = request.form
    tags = simplejson.loads(data["tags"])
    c = card.get_by_id(card_id)
    c.add_to_decks(tags)
    return redirect('/')

@login_required
@app.route('/<user_name>/deck/<deck_name>/removeCard/<card_id>',methods=['POST'])
def remove_card_from_deck(user_name,deck_name,card_id):
    if current_user.get_id() != user_name:
        abort(500)
    c = card.get_by_id(card_id)
    c.remove_from_deck(deck_name)
    c.remove_from_sidedeck(deck_name)
    return redirect('/'+user_name+'/deck/'+deck_name)

@login_required
@app.route('/<user_name>/deck/<deck_name>/moveToSidedeck/<card_id>',methods=['POST'])
def move_to_sidedeck(user_name,deck_name,card_id):
    if current_user.get_id() != user_name:
        abort(500)
    c = card.get_by_id(card_id)
    c.add_to_sidedeck(deck_name)
    return redirect('/'+user_name+'/deck/'+deck_name)

@login_required
@app.route('/<user_name>/deck/<deck_name>/removeFromSidedeck/<card_id>',methods=['POST'])
def remove_from_sidedeck(user_name,deck_name,card_id):
    if current_user.get_id() != user_name:
        abort(500)
    c = card.get_by_id(card_id)
    c.remove_from_sidedeck(deck_name)
    return redirect('/'+user_name+'/deck/'+deck_name)

@login_required
@app.route('/<user_name>/deck/<deck_name>/addToDeck/<card_id>',methods=['POST'])
def add_to_deck(user_name,deck_name,card_id):
    if current_user.get_id() != user_name:
        abort(500)
    c = card.get_by_id(card_id)
    c.add_to_deck(deck_name)
    return redirect('/'+user_name+'/deck/'+deck_name)

@app.route("/<user_name>/tradeJSON", methods=["GET"])
def get_trade_json(user_name):
    cur = mongo.CardDocument.find({"owner":user_name,"decks":"trade"},{"name":1,"id":1,"_id":0})
    arr = []
    for obj in cur:
        arr.append({"name":obj["name"],"id":obj["id"]})
    return jsonify({"result":arr})