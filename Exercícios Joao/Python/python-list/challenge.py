import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
  for rank in ranks:
      card = rank + " of " + suit
      deck.append(card)

print(f'There are {len(deck)} cards in the deck.')
#print(deck)
print('Dealing ...')

playerDeck = []
for i in range(5):
    card = random.randint(0,len(deck)-1)
    playerDeck.append(deck[card])
    del(deck[card])

print(f'There are {len(deck)} cards in the deck.')
#print(deck)
print('Player has the following cards in their hand:')
print(playerDeck)
