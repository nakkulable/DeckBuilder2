import datetime
from mongokit import Document
from app.DAO import mongo, cardinfo, card

__author__ = 'Obee'


def infos_old2new(old, new):
    new["artist"] = old["artist"]
    new["converted_mana_cost"] = int(old["convertedManaCost"])
    new["image_url"] = old["downloadLink"]
    new["edition"] = old["edition"]
    try:
        new["exist"] = old["exist"]
    except:
        new["exist"] = False
    new["id"] = old["id"]
    new["is_two_sided"] = old["isTwoSided"]
    new["mana_cost"] = old["manaCost"]
    new["name"] = old["name"]
    new["rarity"] = old["rarity"]
    new["text"] = old["text"]
    new["type"] = old["type"]
    new["love"] =[]
    new["hate"] = []
    new["name_lower_case"] = unicode(old["name"]).lower()
    new.save()
    print "saved id "+str(new.id)


def migrate_card_infos():
    cur = mongo.Magic.cardInfo.find()
    for oldInfo in cur:
        info = mongo.CardInfoDocument()
        infos_old2new(oldInfo,info)

# migrate_card_infos()

def cards_old2new(old, new):
    new.id = old["id"]
    new.name = old['name']
    new.owner = old["owner"]
    new.creation_date = old["creationDate"]
    new.in_proposal = False
    new.card_info_id  = old["cardInfoId"]
    if old['status'] == "trading":
        new.decks = ['trade']
    elif old['status'] == "removing":
        new.decks = ['recycle']
    else:
        new.decks = []
    new.sidedecks=[]
    new.history = [
        {
            "date" : datetime.datetime.utcnow(),
            "action" : "transfered on new page",
            "new_owner": new["owner"]
        }
    ]
    new.save()
    print "saved id "+str(new.id)


def migrate_some_cards():
    cur = mongo.Magic.cards.find()
    for oldCard in cur:
        oldInfo = cardinfo.get_by_id(oldCard["cardInfoId"])
        oldCard['name'] = oldInfo['name']
        if unicode(oldInfo['name']).lower() not in ["swamp","island","mountain","plains","forest"]:
            card = mongo.CardDocument()
            cards_old2new(oldCard,card)


# migrate_some_cards()

@mongo.register
class OldCard(Document):
    __database__ = "Magic"
    __collection__ = "cards"


