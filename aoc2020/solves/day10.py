from aoc import AocDay

class day10(AocDay):   


    def __init__(self, day):
        AocDay.__init__(self, day)
        self.process_input()

    def process_input(self):
        self.values = []
        for input in self.input:
            self.values.append(int(input))
        self.values.sort()
        if len(self.values) != len(set(self.values)):
            raise ValueError


    challenge1 = "use all adapters, multiply #1diff*#3diff"
    def solve1(self):
        self.process_input()
        mem = {1:1, 3:0}
        x = max(self.values)+3
        while len(self.values) > 0:
            val = self.values.pop()
            if x-val==3: mem[3] += 1
            if x-val==1: mem[1] += 1
            x = val
        return mem[1]*mem[3]
            
            
    challenge2 = "not all adapters required, how many ways can you step to max+3"
    def solve2(self):
        self.process_input()
        mem = {max(self.values)+3:1}
        while len(self.values) > 0:
            val = self.values.pop()
            if val not in mem:
                mem[val] = sum([v for k,v in mem.items() if val < k <= val+3])
        return sum([v for k,v in mem.items() if 0 < k <= 3])
        



day = day10(10)
day.solve()