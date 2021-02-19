'''def atencao(name='Brasilia amarela', greeting=None):
    if greeting == None:
        print(f'Atenção {name}!')
    else:
        print(f'Hello {name}!')


atencao()
atencao('Creuzebeck!')
atencao(greeting='Ao top')
atencao('Brasilia', 'Creuzebeck')
'''
'''
def addTwoNumbers(x, y):
    return x + y

addTwoNumbers(4, 6)
result = addTwoNumbers(5, 7)
print(result)
'''
'''
def createDeck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')

    return deck

myDeck = createDeck()
print(len(myDeck))
'''
'''
value = 1

def someFunction():
    value = 10

print(value)
someFunction()
print(value)
'''

