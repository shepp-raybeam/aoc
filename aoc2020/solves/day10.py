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
        device = max(self.values)+3
        current = 0
        ones = 0
        threes = 0
        result = self.rec(self.values, ones, threes, current)
        return result[0]*(result[1]+1)

    def rec(self, vals, ones, threes, current):
        if len(vals) == 0:
            return [ones, threes]
        
        for i in range(min(3, len(vals))):
            val = vals[i]
            diff = val - current
            if not (diff == 3 or diff ==1):
                continue
            newvals = vals[0:i] + vals[i+1:]            
            current = val
            if diff == 1:
                ones += 1
            if diff == 3:
                threes += 1 
            return self.rec(newvals, ones, threes, current)
        pass
            
    challenge2 = "not all adapters required, how many ways can you step to max+3"
    def solve2(self):
        mem = {max(self.values)+3:1}
        while len(self.values) > 0:
            val = self.values.pop()
            if val not in mem:
                mem[val] = sum([v for k,v in mem.items() if val < k <= val+3])
        return sum([v for k,v in mem.items() if 0 < k <= 3])
        



day = day10(10)
day.solve()