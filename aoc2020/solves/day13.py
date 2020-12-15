from aoc import AocDay
from functools import reduce
import math


class day13(AocDay):   

    def __init__(self, day):
        AocDay.__init__(self, day)
        self.process_input()

    def process_input(self):
        self.depart = int(self.input[0])
        self.buses =  [bus for bus in self.input[1].split(',')]

    challenge1 = 'id * mins wait'
    def solve1(self):
        stops = { int(k):self.gentimes(k) for k in self.buses if not k == 'x'}
        mystops = {int(k):0 for k in self.buses if not k == 'x'}
        last = {}
        while last != mystops:
            last = mystops.copy()
            for bus, stop in stops.items():
                nextstop = next(stop)
                if mystops[bus] < self.depart:
                    mystops[bus] = nextstop
            

        best = [-1, self.depart]
        for (bus, time) in mystops.items():
            delta = time - self.depart
            if delta < best[1]:
                best = [bus, delta]
        print(best)
        return math.prod(best)

    def gentimes(self, id):
        time = 0
        while True:
            if id == 'x':
                time += 1
            else:                
                time += int(id)
            yield time

    challenge2 = 'when do all buses leave in order at 1 min interval, min is like a trillion'
    def solve2(self):
        input = '23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,829,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,677,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
        input = [(i,int(x)) for i,x in enumerate(input.split(',')) if x != 'x']

        time = 0
        product = 1
        for bus in input:
            while (time + bus[0]) % bus[1] != 0:
                time += product
            product *= bus[1]
        return time

day = day13(13)
day.solve()