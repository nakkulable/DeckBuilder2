import datetime
import user
from mongokit import Document
from app.DAO import mongo, configParser, cardinfo
from app.DAO.cardinfo import CardInfo

__author__ = 'Davor Obilinovic'

class Card:
    def __init__(self, document):
        assert(isinstance(document, CardDocument))
        self.document = document
        self._info = None

    def __getitem__(self, item):
        try:
            return self.document[item]
        except:
            return None

    def save(self):
        self.document.save()

    def get_id(self):
        return self["id"]

    def get_owner_name(self):
        return self["owner"]

    def get_owner(self):
        return user.get_by_username(self.get_owner_name())

    def get_creation_date(self):
        return self["creation_date"]

    def get_creation_date_string(self):
        date_time =  self["creation_date"]
        return str(date_time.date())

    def is_in_proposal(self):
        return self["in_proposal"]

    def get_card_info_id(self):
        return self["card_info_id"]

    def get_card_info(self):
        if not self._info:
            self._info = cardinfo.get_by_id(self.get_card_info_id())
        return self._info

    def get_name(self):
        return self['name']

    def declare_love(self, username):
        card_infos_cur = cardinfo.get_info_docs_by_name(self.get_name())
        for card_info_doc in card_infos_cur:
            card_info = CardInfo(card_info_doc)
            card_info.document["love"].append(username)
            if username in card_info["hate"]:
                card_info.document["hate"].remove(username)
            card_info.save()

    def declare_hate(self, username):
        card_infos_cur = cardinfo.get_info_docs_by_name(self.get_name())
        for card_info_doc in card_infos_cur:
            card_info = CardInfo(card_info_doc)
            card_info.document["hate"].append(username)
            if username in card_info["love"]:
                card_info.document["love"].remove(username)
            card_info.save()

    def get_rarity(self):
        return self.get_card_info()["rarity"]

    def is_two_sided(self):
        return self.get_card_info()["is_two_sided"]

    def get_interested(self):
        return self._info.get_interested()

    def get_haters(self):
        return self._info.get_haters()

    def get_image_url(self):
        return self.get_card_info()["image_url"]

    def add_to_deck(self, deck):
        if deck not in self.document['decks']:
            self.document['decks'].append(deck)
            self.save()

    def add_to_decks(self, decks):
        for deck in decks:
            self.add_to_deck(deck)

    def remove_from_deck(self,deck_name):
        try:
            self.document['decks'].remove(deck_name)
            self.save()
            return True
        except:
            return False

    def add_to_sidedeck(self, deck_name):
        self.document['sidedecks'].append(deck_name)
        self.save()
        return True

    def remove_from_sidedeck(self, deck_name):
        try:
            self.document['sidedecks'].remove(deck_name)
            self.save()
            return True
        except:
            return False

def get_by_id(id):
    doc = mongo.CardDocument.find_one({'id':int(id)})
    if (doc):
        return Card(doc)
    return None

@mongo.register
class CardDocument(Document):
    __database__ = configParser.get("Mongo","DBname")
    __collection__ = 'cards'
    #__database__ = config.DB

    use_schemaless = True
    use_dot_notation = True

    structure = {
        'id' : int,
        'name' : basestring,
        'owner' : basestring,
        'creation_date' : datetime.datetime,
        'in_proposal' : bool,
        'card_info_id' : int,
        'decks' : [basestring],
        'sidedecks': [basestring],
        'history' : []
    }