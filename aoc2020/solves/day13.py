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
        primes = [1 if x == 'x' else int(x) for x in self.buses]
        lcm_me = [i + 1 if x == 'x' else int(x) + i for i,x in enumerate(self.buses)]
        print(lcm_me)
        stride = max(buses)
        time = -buses.index(stride)
        time = 99999999999869
        print(list(enumerate(buses)))
        
        found = False
        while not found:
            time += stride
            #print(f'check {time}')
            ok = 0
            for i, bus in enumerate(buses):
                if (time + i) % bus != 0: break
                ok += 1
            found = ok == len(buses)
        return time


    def checktime(self, time):
        #print(f'check {time}')
        for i, bus in enumerate(self.buses):
            if bus == 'x': continue
            if (time + i) % int(bus) + i != int(bus): return False
        return True

    def tick(self, stops, time):
        #advance each schedule up to desired time and return array of times
        times = []
        for i, stop in enumerate(stops):
            checktime = time + i
            nextstop = next(stop)
            while nextstop < checktime:
                nextstop = next(stop)
            if nextstop > checktime:
                stop.send(nextstop)
            times.append(nextstop)
        return times

    def hasstop(self, bus, t):
        if bus == 'x': return True
        stop = self.gentimes(int(bus))
        nextstop = 0
        while nextstop < t:
            nextstop = next(stop)
            if nextstop == t: return True
        return False



day = day13(13)
day.solve()