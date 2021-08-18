from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call in parent
        for joker_num in '1', '2':
            joker = Card(joker_num, "JOKER")
            self._cards.append(joker)

class MyDeck(JokerDeck):
    def _make_deck(self):
        # print(type(self))
        # print(type(self).__bases__)
        # parent = type(self).__bases__[0]
        # print(type(parent).__bases__)
        # print("parent:", parent)
        # grandparent = type(parent).__bases__[0]
        # print(grandparent)
        super()._make_deck() # will call JokerDeck._make_deck()

