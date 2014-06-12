__author__ = 'Davor Obilinovic'


def is_valid_deck_name(deck_name):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    special_characters = "#-_&"
    if deck_name=="" or deck_name[0] not in letters:
        return False
    for c in deck_name:
        if not (c in letters or c in numbers or c in special_characters):
            return False
    return True