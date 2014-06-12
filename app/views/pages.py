from os import abort
from flask import render_template, redirect
from flask.ext.login import login_required, current_user
from app import app
from app.DAO import user, cardinfo

__author__ = 'Davor Obilinovic'

@app.route('/')
@login_required
def index():
    if current_user.has_undetermined_cards():
        return render_template('classify.html',
                               page = 'classify',
                               user=current_user)
    return redirect('/'+current_user.get_id())


@app.route('/<user_name>', methods=['GET'])
def profile_page(user_name):
    if current_user.has_undetermined_cards():
        return redirect('/')
    profile_user = user.get_by_id(user_name)
    if not user:
        abort(404)
    return render_template('profile.html',
                           page = 'profile',
                           user = current_user,
                           profile_user = profile_user)

@app.route('/card-info/<card_name>',methods=['GET'])
def card_info_page(card_name):
    infos = cardinfo.get_infos_by_name(card_name)
    return render_template('card-info.html',
                           page='card-info',
                           profile_user = current_user,
                           user=current_user,
                           card_name = card_name,
                           infos = infos)

@app.route('/<user_name>/deck/<deck_name>', methods=['GET'])
def deck_page(user_name, deck_name):
    profile_user = user.get_by_id(user_name)
    return render_template('deck.html',
                           deck = profile_user.get_deck(deck_name),
                           page = 'deck',
                           profile_user = profile_user,
                           user=current_user)

@app.route('/<user_name>/trade', methods=['GET'])
def trade_page(user_name):
    profile_user = user.get_by_id(user_name)
    return render_template('trade.html',
                           page = 'trade',
                           profile_user = profile_user,
                           user = current_user )