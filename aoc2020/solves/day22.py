decks = []
input = 'inputs/day22_input.txt'
input = 'inputs/day22_small_input.txt'


deck = []
with open(input) as f:
  for line in f:
    line = line.strip()
    if line == '':
        decks.append(deck)
        deck = []
        continue
    if line.startswith('Player'):
        continue
    deck.append(int(line))

"""
deck1 = decks[0]
deck2 = decks[1]

while len(deck1) and len(deck2):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
        deck1 = deck1 + [card1, card2]
    if card2 > card1:
        deck2 = deck2 + [card2, card1]

deck = deck1
if len(deck2):
    deck = deck2


#print(deck)
#print([a*b for a,b in zip(reversed(deck), list(range(1, len(deck)+1)))])
score = sum([a*b for a,b in zip(reversed(deck), list(range(1, len(deck)+1)))])
print(score)
"""
hashlist = []
def game(deck1, deck2):    
    while len(deck1) and len(deck2):
        try:
            winner  = round(deck1[:], deck2[:])
            card1 = deck1.pop(0)
            card2 = deck2.pop(0)
        except ValueError:
            winner = 1
        if winner == 1:
            deck1 = deck1 + [card1, card2]
        else:
            deck2 = deck2 + [card2, card1]
    winner = 1
    if len(deck2):
        winner = 2
    return winner

def round(deck1, deck2):
    #hash check
    roundhash =  str(hash(' '.join([str(c) for c in deck1]))) +str(hash(' '.join([str(c) for c in deck2])))
    if roundhash in hashlist:
        raise ValueError(f'player1 wins')
    hashlist.append(roundhash)

    card1 = deck1.pop(0)
    card2 = deck2.pop(0)

    if len(deck1) > card1 and len(deck2) > card2:        
        winner = game(deck1[:card1], deck2[:card2])
    else:
        winner = 1 if card1 > card2 else 2
    return winner

print(decks)
deck1 = decks[0]
deck2 = decks[1]
print(game(deck1, deck2), deck1, deck2)
