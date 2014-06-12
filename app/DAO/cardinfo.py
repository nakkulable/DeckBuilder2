from mongokit import Document
from app.DAO import mongo, configParser

__author__ = 'Davor Obilinovic'

class CardInfo:
    def __init__(self, document):
        assert(isinstance(document, CardInfoDocument))
        self.document = document

    def __getitem__(self, item):
        try:
            return self.document[item]
        except:
            return None

    def save(self):
        self.document.save()

    def get_id(self):
        return self["id"]

    def get_image_url(self):
        return self.document['image_url']

    def get_interested(self):
        return self["love"]

    def get_haters(self):
        return self["hate"]


def get_by_id(id):
    doc = mongo.CardInfoDocument.find_one({'id':id})
    if (doc):
        return CardInfo(doc)
    return None

def get_info_docs_by_name(name):
    return mongo.CardInfoDocument.find({'name_lower_case':str(name).lower()})

def get_infos_by_name(name):
    list = []
    for doc in get_info_docs_by_name(name):
        list.append(CardInfo(doc))
    return list

@mongo.register
class CardInfoDocument(Document):
    __database__ = configParser.get("Mongo","DBname")
    __collection__ = 'cardInfo'
    #__database__ = config.DB

    use_schemaless = True
    use_dot_notation = True

    structure = {
        "artist" : basestring,
        "converted_mana_cost" : int,
        "image_url" : basestring,
        "edition" : basestring,
        "exist" : bool,
        "id" : int,
        "is_two_sided" : bool,
        "mana_cost" : basestring,
        "name" : basestring,
        "rarity" : basestring,
        "text" : basestring,
        "type" : basestring,
        "love" :[basestring],
        "hate" : [basestring],
        "name_lower_case":basestring
    }

