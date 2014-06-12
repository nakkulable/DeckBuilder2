from app.DAO.card import Card

__author__ = 'Davor Obilinovic'


class CardList:
    def __init__(self, name):
        self.name = name
        self.cards = {}
        self.count = {}

    def add_card(self, card):
        assert (isinstance(card,Card))
        card_name = card.get_name()
        if card_name in self.cards:
            self.count[card_name] = self.count[card_name]+1
        else:
            self.count[card_name] = 1
            self.cards[card_name] = card

    def get_cards(self):
        return self.cards

    def get_count(self, card_name):
        return self.count[card_name]

    def get_view_size(self):
        l =  len(self.cards)
        if l == 0:
            return l
        return l+3

    def get_name(self):
        return self.name

    def __repr__(self):
        return  str(self.get_view_size())

class ViewColumn:
    def __init__(self):
        self.list = []

    def get_view_size(self):
        ret = 0
        for cl in self.list:
            ret = ret + cl.get_view_size()
        return ret

    def add_CardList(self,cl):
        assert (isinstance(cl,CardList))
        self.list.append(cl)

    def get_deck_card_lists(self):
        l = []
        for e in self.list:
            if e.get_name().lower() != "sideboard":
                l.append(e)
        return l

class Deck:
    def __init__(self,name,cardsList):
        self.name = name
        self.columns = [ViewColumn(), ViewColumn(), ViewColumn()]
        self.cardLists = {
            'instant' : CardList('Instant'),
            'sorcery' : CardList('Sorcery'),
            'creature' : CardList('Creature'),
            'planeswalker' : CardList('Planeswalker'),
            'artifact' : CardList('Artifact'),
            'enchantment' : CardList('Enchantment'),
            'land' : CardList('Land'),
            'sideboard': CardList('Sideboard')
        }
        for card in cardsList:
            category = card.get_card_info()['type']
            if self.name in card['sidedecks']:
                category = 'sideboard'
            self.cardLists[category].add_card(card)

    def get_longest_list(self, exceptions):
        longest = None
        for key in self.cardLists.keys():
            if key not in exceptions and (not longest or self.cardLists[key].get_view_size()>longest.get_view_size()):
                longest = self.cardLists[key]
        return longest

    def get_shortest_column(self):
        shortest = self.columns[0]
        for column in self.columns:
            if column.get_view_size()<shortest.get_view_size():
                shortest = column
        return shortest

    def get_view(self):
        doneKeys = []
        while len(doneKeys) < len(self.cardLists.keys()):
            longestCardList = self.get_longest_list(doneKeys)
            shortestColumn = self.get_shortest_column()
            shortestColumn.add_CardList(longestCardList)
            doneKeys.append(longestCardList.get_name().lower())
        return self.columns

    def get_sideboard(self):
        return self.cardLists['sideboard']

    def get_name(self):
        return self.name


