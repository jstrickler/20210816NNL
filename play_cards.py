from carddeck import CardDeck
from jokerdeck import JokerDeck, MyDeck

d1 = CardDeck("Fred")
print(d1)
print(type(d1))
d2 = CardDeck("Mary")

# legal, but wrong
print(d1._dealer)



# legal, but not preferred
# and not needed
print(d1.get_dealer())

# legal, and right
print(d1.dealer)
#  internally calls dealer()

print(d1.udealer)

d1.dealer = "Ethel"
print(d1.dealer)
print(d1.udealer)

try:
    d1.dealer = 123
except TypeError as err:
    print(err)
else:
    print(d1.dealer)
    print(d1.udealer)

d1.shuffle()
print(d1.cards)

hand = []
for i in range(5):
    hand.append(d1.draw())
print("Hand:", hand)
print(hand[0])

print(CardDeck.get_deck_count())
print(d1.get_deck_count())

j = JokerDeck("Jimmy")
print(j)
j.shuffle()
print(j.cards)

m = MyDeck("Molly")
