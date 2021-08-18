import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):  # used for repr(obj)
        return(f"Card('{self._rank}','{self._suit}')")

    def __str__(self):
        return f"{self._rank}-{self._suit}"

class CardDeck:  # inherits from 'object'
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    DECK_COUNT = 0
    #           new obj, args ...
    def __init__(self, dealer):
        CardDeck.DECK_COUNT += 1
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return tuple(self._cards)

    def get_dealer(self):  # getter method
        return self._dealer

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")
    @property
    def udealer(self):
        return self._dealer.upper()

    # @thing
    # def my_function(self):
    #     pass
    #
    # my_function = thing(my_function)

    @property
    def spam(self):
        return self._whatever_you_want_dudette

    @classmethod
    def get_deck_count(cls):
        return cls.DECK_COUNT

