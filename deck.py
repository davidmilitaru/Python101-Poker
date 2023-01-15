import random
import card as cd

class Deck (object):
    def __init__ (self):
        self.deck = []
        for suit in cd.Card.suits_list:
            for rank in cd.Card.ranks_list:
                card = cd.Card (rank, suit)
                self.deck.append(card)

    def shuffle (self):
        random.shuffle (self.deck)

    def __len__ (self):
        return len (self.deck)

    def deal (self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop(0)
