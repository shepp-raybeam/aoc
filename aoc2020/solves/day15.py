from aoc import AocDay

class day15(AocDay):   

    def __init__(self, day):
        AocDay.__init__(self, day)
        #self.process_input()

    def process_input(self, input):
        self.sequence = [int(v.strip()) for v in input.split(',')]
        
    challenge1 = 'what will be the 2020th number spoken'
    def solve1(self):
        input = '15,12,0,14,3,1'
        #input = '0,3,6'
        self.process_input(input)
        sequence = self.sequence                
        mem = {k:i+1 for i,k in enumerate(sequence[:-1])}
        while len(sequence) < 30000000:
            last = sequence[-1]
            round = len(sequence)
            if last in mem.keys():
                next = round - mem[last]
            else:
                next = 0
            mem[last] = round
            last = next            
            sequence.append(next)
        return sequence[-1]



    def solve2(self):
        pass

day = day15(15)
day.solve()