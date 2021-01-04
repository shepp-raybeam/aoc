from collections import deque

class Solution():
    def __init__(self, input):
        self.input = input

    def process_input(self):
        deck = []
        decks = []
        with open(self.input) as f:
            for line in f:
                line = line.strip()
                if line == '':
                    decks.append(deck)
                    deck = []
                    continue
                if line.startswith('Player'):
                    continue
                deck.append(int(line))
        self.deck1 = deque(reversed(decks[0]))
        self.deck2 = deque(reversed(decks[1]))
    
    def combat(self):
        while self.deck1 and self.deck2:
            c1, c2 = self.deck1.pop(), self.deck2.pop()
            if c1 > c2: 
                self.deck1.extendleft([c1, c2])
            else:
                self.deck2.extendleft([c2, c1])
    
        
    def _newdeck(self, deck, count):
        d1 = deck.copy()
        result = deque()
        for _ in range(count):
            result.appendleft(d1.pop())
        return result

    def rcombat(self, deck1, deck2, hashlist):
        print(deck1, deck2)
        while deck1 and deck2:
            hash = ''.join(map(str,deck1)) + 'x' + ''.join(map(str, deck2))
            if hash in hashlist:  return 0
            hashlist[hash] = True
            c1, c2 = deck1.pop(), deck2.pop()
            winner = None
            if (c1 <= len(deck1)) and (c2 <= len(deck2)):
                rdeck1 = self._newdeck(deck1, c1)
                rdeck2 = self._newdeck(deck2, c2)
                winner = self.rcombat(rdeck1, rdeck2, hashlist)
            else:
                winner = 0 if c1 > c2 else 1
            
            if winner == 0: self.deck1.extendleft([c1, c2])
            else:           self.deck2.extendleft([c2, c1])
        return winner
    
    def solve1(self):
        self.process_input()
        self.combat()
        winner = self.deck1 if self.deck1 else self.deck2
        result = 0
        for i in range(len(winner)):
            result+=winner[i]*(i+1)
        print(result)

    def solve2(self):
        self.process_input()
        self.rcombat(self.deck1, self.deck2, {})
        winner = self.deck1 if len(self.deck2) == 0  else self.deck2
        print(f'1: {list(self.deck1)} 2: {list(self.deck2)}')
        result = 0
        for i in range(len(winner)):
            result+=winner[i]*(i+1)
        print(result)


input = 'inputs/day22_input.txt'
input = 'inputs/day22_small_input.txt'
sol = Solution(input)
sol.solve1()
sol.solve2()