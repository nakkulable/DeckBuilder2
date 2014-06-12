import datetime
import hashlib
from flask import flash
from mongokit import Document
from app.DAO import mongo, configParser
from app.DAO.card import Card
from app.DAO.deck import Deck
from app.core import Functions

__author__ = 'Davor Obilinovic'


class User:
    def __init__(self, document):
        assert(isinstance(document, UserDocument))
        self.document = document

    def __getitem__(self, item):
        ret = None
        try:
            ret = self.document[str(item)]
        except:
            pass
        return ret

    def save(self):
        self.document.save()

    def is_authenticated(self):
        return self.document!=None

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.document["username"]

    def profilePictureUrl(self):
        try:
            return "http://graph.facebook.com/"+self.document["facebook_name"]+"/picture?type=large"
        except:
            return "http://cdn.wallwuzz.com/uploads/2013/08/Anonymous-wallpaper.jpg"

    def check_password(self, password):
        m = hashlib.sha1()
        m.update(password)
        digest =  m.hexdigest()
        return digest == self.document["password"]

    def get_undetermined_card(self):
        cardDoc =mongo.CardDocument.find_one({'owner':self["username"],'decks':{'$size':{'$lt':1}}})
        if cardDoc:
            return Card(cardDoc)
        return None

    def get_undetermined_cards_count(self):
        return mongo[configParser.get("Mongo","DBname")].cards\
            .find({'owner':self["username"],'decks':{'$size':{'$lt':1}}})\
                .count()

    def has_undetermined_cards(self):
        return self.get_undetermined_cards_count()>0

    def add_deck(self,deck_name):
        if not Functions.is_valid_deck_name(deck_name):
            flash("Invalid deck name!","error")
            flash("Only letters, digits and - , _  , # , & are allowed and it must start with letter!","error")
            flash("Deck not created!", "error")
            return False
        if not deck_name in self.document["decks"]:
            self.document["decks"].append(deck_name)
            self.save()
            return True
        else:
            flash('Deck already exist!','error')
            flash('Deck not added.','error')
            return False

    def get_decks(self):
        return self['decks']

    def get_decks_count(self):
        return len(self.get_decks())

    def get_deck(self, deck_name):
        if deck_name not in self['decks']:
            return None
        return Deck(deck_name,self.get_deck_cards(deck_name))

    def get_deck_cards(self, deck_name):
        cur = mongo.CardDocument.find({'owner':self.get_id(), 'decks':deck_name})
        l = []
        for cardDoc in cur:
            l.append(Card(cardDoc))
        return l

def get_by_username(username):
    doc = mongo.UserDocument.find_one({'username':username})
    if (doc):
        return User(doc)
    return None

def get_by_id(id):
    return get_by_username(id)

@mongo.register
class UserDocument(Document):
    __database__ = configParser.get("Mongo","DBname")
    __collection__ = 'users'
    #__database__ = config.DB

    use_schemaless = True
    use_dot_notation = True

    structure = {
        'username' : basestring,
        'password' : basestring,
        'last_booster_date' : datetime.datetime,
        'jad_balance' : int,
        'wants_proposal_mail' : bool,
        'wants_wishlist_mail' : bool,
        'starter_deck' : basestring,
        'roles' : [ basestring ],
        'email' : basestring,
        'facebook_name' : basestring,
        'decks' : [basestring]
    }
